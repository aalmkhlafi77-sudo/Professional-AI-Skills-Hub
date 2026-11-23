"""Conservative, offline preflight for synthetic n8n workflow JSON.

No n8n API, credentials, network, node execution, or production access.
This is a *supplementary* guardrail, not a complete n8n security validator.
"""
from collections import Counter

SIDE_EFFECT_TYPES = {
    "n8n-nodes-base.executeWorkflow",
    "n8n-nodes-base.executeCommand",
    "n8n-nodes-base.readWriteFile",
    "n8n-nodes-base.dataTable",
}
NETWORK_TYPES = {"n8n-nodes-base.httpRequest"}
RETRYABLE_TYPES = NETWORK_TYPES | {"n8n-nodes-base.postgres", "n8n-nodes-base.mySql"}


def preflight(workflow, *, mode="test", approved=False):
    """Return stable reason codes. Fail closed for uncertain node types.

    The 'approved' flag is a synthetic explicit authorization marker, NOT
    proof of user identity or a replacement for n8n access control.
    """
    errors = []
    if not isinstance(workflow, dict) or not isinstance(workflow.get("nodes"), list):
        return ["INVALID_WORKFLOW"]
    names = [n.get("name") for n in workflow["nodes"] if isinstance(n, dict)]
    if len(names) != len(workflow["nodes"]) or any(not isinstance(n, str) or not n for n in names):
        errors.append("INVALID_NODE")
    if any(v > 1 for v in Counter(names).values()):
        errors.append("DUPLICATE_NODE_NAME")
    for node in workflow["nodes"]:
        if not isinstance(node, dict):
            continue
        name = node.get("name", "<unnamed>")
        kind = node.get("type", "")
        params = node.get("parameters", {})
        if not isinstance(params, dict):
            errors.append(f"INVALID_PARAMETERS:{name}")
            continue
        if mode == "test" and kind in SIDE_EFFECT_TYPES and not approved:
            errors.append(f"UNPINNED_SIDE_EFFECT:{name}")
        if mode == "test" and kind in NETWORK_TYPES and not node.get("pinData") and not approved:
            errors.append(f"UNPINNED_NETWORK:{name}")
        if kind in RETRYABLE_TYPES and node.get("retryOnFail") and params.get("operation") in {"create", "insert", "send", "delete", "update"}:
            if not params.get("idempotencyKey"):
                errors.append(f"RETRY_WITHOUT_IDEMPOTENCY:{name}")
        if kind == "n8n-nodes-base.httpRequest":
            headers = str(params.get("headerParameters", ""))
            if any(x in headers.lower() for x in ("bearer sk-", "api_key=sk-", "authorization: bearer sk-")):
                errors.append(f"PLAINTEXT_SECRET_PATTERN:{name}")
        if node.get("availableInMCP") is True and not approved:
            errors.append(f"UNAPPROVED_MCP_EXPOSURE:{name}")
    if workflow.get("availableInMCP") is True and not approved:
        errors.append("UNAPPROVED_WORKFLOW_MCP_EXPOSURE")
    return errors
