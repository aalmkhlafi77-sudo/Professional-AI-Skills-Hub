"""No external service access: positive and negative synthetic fixtures."""
import importlib.util
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location("n8n_preflight", ROOT / "integration/n8n_offline_preflight.py")
mod = importlib.util.module_from_spec(spec)
spec.loader.exec_module(mod)


def workflow(*nodes, **extra):
    return {"nodes": list(nodes), **extra}


def node(name, kind, **kw):
    return {"name": name, "type": kind, "parameters": {}, **kw}


class N8nOfflineSafetyTests(unittest.TestCase):
    def test_pure_transform_allowed(self):
        self.assertEqual(mod.preflight(workflow(node("Set", "n8n-nodes-base.set"))), [])

    def test_data_table_write_denied_without_approval(self):
        self.assertIn("UNPINNED_SIDE_EFFECT:Write", mod.preflight(
            workflow(node("Write", "n8n-nodes-base.dataTable"))))

    def test_subworkflow_test_escape_denied(self):
        self.assertIn("UNPINNED_SIDE_EFFECT:Call", mod.preflight(
            workflow(node("Call", "n8n-nodes-base.executeWorkflow"))))

    def test_command_denied(self):
        self.assertIn("UNPINNED_SIDE_EFFECT:Command", mod.preflight(
            workflow(node("Command", "n8n-nodes-base.executeCommand"))))

    def test_network_without_pin_denied(self):
        self.assertIn("UNPINNED_NETWORK:HTTP", mod.preflight(
            workflow(node("HTTP", "n8n-nodes-base.httpRequest"))))

    def test_network_with_pin_allowed(self):
        self.assertEqual(mod.preflight(workflow(
            node("HTTP", "n8n-nodes-base.httpRequest"),
            pinData={"HTTP": [{"json": {"status": "fixture"}}]})), [])

    def test_retry_write_without_idempotency_denied(self):
        n = node("Insert", "n8n-nodes-base.mySql", retryOnFail=True)
        n["parameters"] = {"operation": "insert"}
        self.assertIn("RETRY_WITHOUT_IDEMPOTENCY:Insert", mod.preflight(workflow(n)))

    def test_retry_write_with_idempotency_marker(self):
        n = node("Insert", "n8n-nodes-base.mySql", retryOnFail=True)
        n["parameters"] = {"operation": "insert", "idempotencyKey": "fixture-1"}
        self.assertEqual(mod.preflight(workflow(n)), [])

    def test_secret_pattern_denied(self):
        n = node("HTTP", "n8n-nodes-base.httpRequest")
        n["parameters"] = {"headerParameters": "Authorization: Bearer sk-EXAMPLE"}
        self.assertIn("PLAINTEXT_SECRET_PATTERN:HTTP", mod.preflight(
            workflow(n, pinData={"HTTP": [{"json": {}}]})))

    def test_workflow_mcp_exposure_denied(self):
        self.assertIn("UNAPPROVED_WORKFLOW_MCP_EXPOSURE", mod.preflight(
            workflow(node("Set", "n8n-nodes-base.set"), availableInMCP=True)))

    def test_duplicate_node_name_denied(self):
        self.assertIn("DUPLICATE_NODE_NAME", mod.preflight(workflow(
            node("Same", "n8n-nodes-base.set"), node("Same", "n8n-nodes-base.set"))))

    def test_malformed_input_denied(self):
        self.assertEqual(mod.preflight({"nodes": "not-list"}), ["INVALID_WORKFLOW"])

    def test_explicit_synthetic_approval_not_a_production_grant(self):
        self.assertEqual(mod.preflight(workflow(
            node("Call", "n8n-nodes-base.executeWorkflow")), approved=True), [])


if __name__ == "__main__":
    unittest.main()
