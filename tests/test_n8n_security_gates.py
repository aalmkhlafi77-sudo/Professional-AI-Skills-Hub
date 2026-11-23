"""Synthetic security tests: no credentials, network, or third-party execution."""
import importlib.util
import unittest
from pathlib import Path
spec = importlib.util.spec_from_file_location("gate", Path(__file__).resolve().parents[1] / "integration/n8n_security_gates.py")
gate = importlib.util.module_from_spec(spec)
spec.loader.exec_module(gate)

def n(name, kind="n8n-nodes-base.set", **kw):
    return {"name": name, "type": kind, "parameters": {}, **kw}
def w(*nodes, **kw):
    return {"nodes": list(nodes), **kw}

class AdmissionSecurityTests(unittest.TestCase):
    def test_redaction_nested(self):
        data = {"access_token": "fake", "items": [{"password": "fake2"}], "message": "Bearer fake-token"}
        out = gate.redact(data)
        self.assertNotIn("fake", str(out))
        self.assertNotIn("fake2", str(out))
    def test_nonsecret_preserved(self):
        self.assertEqual(gate.redact({"status": "ok"}), {"status": "ok"})
    def test_secret_header_detected(self):
        x = n("HTTP", "n8n-nodes-base.httpRequest")
        x["parameters"] = {"headerParameters": {"Authorization": "Bearer fake"}}
        self.assertIn("POTENTIAL_PLAINTEXT_SECRET:HTTP", gate.assess(w(x)))
    def test_pure_transform(self):
        self.assertEqual(gate.assess(w(n("Set"))), [])
    def test_duplicate_names(self):
        self.assertIn("DUPLICATE_NODE_NAME", gate.assess(w(n("Set"), n("Set"))))
    def test_invalid_workflow(self):
        self.assertEqual(gate.assess({"nodes": "bad"}), ["INVALID_WORKFLOW"])
    def test_invalid_node(self):
        self.assertEqual(gate.assess(w(None)), ["INVALID_NODE"])
    def test_mcp_workflow_denied(self):
        self.assertIn("UNAPPROVED_MCP_EXPOSURE", gate.assess(w(n("Set"), availableInMCP=True)))
    def test_mcp_node_denied(self):
        self.assertIn("UNAPPROVED_NODE_MCP:Set", gate.assess(w(n("Set", availableInMCP=True))))
    def test_mcp_synthetic_approval(self):
        self.assertEqual(gate.assess(w(n("Set"), availableInMCP=True), authenticated_approval=True), [])
    def test_subworkflow_denied(self):
        self.assertIn("UNPINNED_SIDE_EFFECT:Call", gate.assess(w(n("Call", "n8n-nodes-base.executeWorkflow"))))
    def test_data_table_denied(self):
        self.assertIn("UNPINNED_SIDE_EFFECT:Write", gate.assess(w(n("Write", "n8n-nodes-base.dataTable"))))
    def test_command_denied(self):
        self.assertIn("UNPINNED_SIDE_EFFECT:Shell", gate.assess(w(n("Shell", "n8n-nodes-base.executeCommand"))))
    def test_http_denied(self):
        self.assertIn("UNPINNED_NETWORK:Fetch", gate.assess(w(n("Fetch", "n8n-nodes-base.httpRequest"))))
    def test_http_pinned(self):
        self.assertEqual(gate.assess(w(n("Fetch", "n8n-nodes-base.httpRequest"), pinData={"Fetch": []})), [])
    def test_retry_write_requires_proof(self):
        x = n("Insert", "n8n-nodes-base.mySql", retryOnFail=True)
        x["parameters"] = {"operation": "insert", "idempotencyKey": "claimed"}
        self.assertIn("RETRY_WRITE_REQUIRES_EXTERNAL_DEDUP_PROOF:Insert", gate.assess(w(x)))
    def test_retry_read_allowed(self):
        x = n("Read", "n8n-nodes-base.mySql", retryOnFail=True)
        x["parameters"] = {"operation": "select"}
        self.assertEqual(gate.assess(w(x)), [])
    def test_synthetic_dedup(self):
        ledger = gate.SyntheticIdempotencyLedger()
        self.assertTrue(ledger.commit("fake-order", "fake-payload"))
        self.assertFalse(ledger.commit("fake-order", "fake-payload"))
        self.assertEqual(len(ledger.writes), 1)
    def test_dedup_missing_key(self):
        with self.assertRaises(ValueError):
            gate.SyntheticIdempotencyLedger().commit("", "fake")
if __name__ == "__main__":
    unittest.main()
