#!/usr/bin/env bash
set -euo pipefail

# Executes only disposable JSON fixtures in the real n8n CLI, inside a
# network-disconnected container. Never mount a home directory or credentials.
IMAGE="docker.n8n.io/n8nio/n8n:2.2.0"
ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/../.." && pwd)"
WORK="$(mktemp -d)"
trap 'rm -rf "$WORK"' EXIT
mkdir -p "$WORK/data"
chmod 777 "$WORK/data"

docker pull "$IMAGE"
run_fixture() {
  local file="$1"
  local output="$2"
  local workflow_id="${file%.json}"
  if [[ "$file" == "positive.json" ]]; then workflow_id="offline-positive"; else workflow_id="offline-network"; fi
  set +e
  timeout 100s docker run --rm --user "$(id -u):$(id -g)" --network none --cap-drop ALL \
    --security-opt no-new-privileges --pids-limit 256 --memory 1200m \
    -e N8N_USER_FOLDER=/tmp/n8n-data \
    -e N8N_ENCRYPTION_KEY=synthetic-test-only-not-a-secret \
    -e N8N_DIAGNOSTICS_ENABLED=false \
    -e N8N_VERSION_NOTIFICATIONS_ENABLED=false \
    -e N8N_TEMPLATES_ENABLED=false \
    -v "$ROOT/integration/n8n-runtime:/fixtures:ro" \
    -v "$WORK/data:/tmp/n8n-data" \
    "$IMAGE" import:workflow --input="/fixtures/$file" > "$output" 2>&1
  local import_status=$?
  if [[ "$import_status" -ne 0 ]]; then set -e; return "$import_status"; fi
  timeout 100s docker run --rm --user "$(id -u):$(id -g)" --network none --cap-drop ALL \
    --security-opt no-new-privileges --pids-limit 256 --memory 1200m \
    -e N8N_USER_FOLDER=/tmp/n8n-data \
    -e N8N_ENCRYPTION_KEY=synthetic-test-only-not-a-secret \
    -e N8N_DIAGNOSTICS_ENABLED=false \
    -e N8N_VERSION_NOTIFICATIONS_ENABLED=false \
    -e N8N_TEMPLATES_ENABLED=false \
    -v "$ROOT/integration/n8n-runtime:/fixtures:ro" \
    -v "$WORK/data:/tmp/n8n-data" \
    "$IMAGE" execute --id="$workflow_id" >> "$output" 2>&1
  local status=$?
  set -e
  return "$status"
}

echo "Real n8n runtime positive fixture (offline)"
if ! run_fixture positive.json "$WORK/positive.log"; then
  tail -n 80 "$WORK/positive.log"
  echo "FAIL: positive fixture failed"
  exit 1
fi
if ! grep -Eqi 'execution finished|execution successful|successfully executed|finished execution' "$WORK/positive.log"; then
  tail -n 80 "$WORK/positive.log"
  echo "FAIL: expected execution success evidence not present"
  exit 1
fi

echo "Real n8n runtime negative fixture (network disabled)"
if run_fixture blocked-network.json "$WORK/negative.log"; then
  echo "FAIL: blocked external HTTP unexpectedly succeeded"
  exit 1
fi
if ! grep -Eqi 'example.com|External HTTP|ENETUNREACH|EAI_AGAIN|network|request failed|not connected' "$WORK/negative.log"; then
  tail -n 80 "$WORK/negative.log"
  echo "FAIL: failure did not show HTTP/network attempt evidence"
  exit 1
fi
echo "PASS: isolated real runtime positive and blocked-network fixtures"
