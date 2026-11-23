"""Offline policy checks. NOT a replacement for real n8n authorization."""
import re
from collections import Counter
SECRET = re.compile(r"authorization|api[_-]?key|access[_-]?token|refresh[_-]?token|password|client[_-]?secret|cookie", re.I)
TOKEN = re.compile(r"(?i)(bearer\\s+[^\\s,;]+|sk-[A-Za-z0-9_-]{8,}|ghp_[A-Za-z0-9_]+)")
SIDE_EFFECTS = {"n8n-nodes-base.executeWorkflow", "n8n-nodes-base.executeCommand", "n8n-nodes-base.readWriteFile", "n8n-nodes-base.dataTable"}

def redact(value, key=""):
    if SECRET.search(key):
        return "[REDACTED]"
    if isinstance(value, dict):
        return {k: redact(v, str(k)) for k, v in value.items()}
    if isinstance(value, list):
        return [redact(v) for v in value]
    if isinstance(value, str):
        return TOKEN.sub("[REDACTED]", value)
    return value

def assess(workflow, *, authenticated_approval=False):
    """Conservative synthetic preflight. Approval flag is NOT identity proof."""
    if not isinstance(workflow, dict) or not isinstance(workflow.get("nodes"), list):
        return ["INVALID_WORKFLOW"]
    nodes = workflow["nodes"]
    if any(not isinstance(n, dict) for n in nodes):
        return ["INVALID_NODE"]
    names = [n.get("name") for n in nodes]
    errors = []
    if any(not isinstance(n, str) or not n for n in names):
        errors.append("INVALID_NODE_NAME")
    if any(count > 1 for count in Counter(names).values()):
        errors.append("DUPLICATE_NODE_NAME")
    if workflow.get("availableInMCP") and not authenticated_approval:
        errors.append("UNAPPROVED_MCP_EXPOSURE")
    for node in nodes:
        name, typ = node.get("name", "<unnamed>"), node.get("type", "")
        params = node.get("parameters", {})
        if not isinstance(params, dict):
            errors.append(f"INVALID_PARAMETERS:{name}")
            continue
        if node.get("availableInMCP") and not authenticated_approval:
            errors.append(f"UNAPPROVED_NODE_MCP:{name}")
        if typ in SIDE_EFFECTS and not authenticated_approval:
            errors.append(f"UNPINNED_SIDE_EFFECT:{name}")
        if typ == "n8n-nodes-base.httpRequest" and not authenticated_approval and name not in workflow.get("pinData", {}):
            errors.append(f"UNPINNED_NETWORK:{name}")
        if node.get("retryOnFail") and params.get("operation") in ("insert", "create", "send", "delete", "update"):
            errors.append(f"RETRY_WRITE_REQUIRES_EXTERNAL_DEDUP_PROOF:{name}")
        if redact(params) != params:
            errors.append(f"POTENTIAL_PLAINTEXT_SECRET:{name}")
    return errors

class SyntheticIdempotencyLedger:
    """Memory-only illustration; NOT n8n or database idempotency proof."""
    def __init__(self):
        self.seen = set()
        self.writes = []
    def commit(self, key, payload):
        if not isinstance(key, str) or not key:
            raise ValueError("unique operation key required")
        if key in self.seen:
            return False
        self.seen.add(key)
        self.writes.append((key, payload))
        return True
