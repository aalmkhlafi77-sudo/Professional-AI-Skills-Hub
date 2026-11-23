#!/usr/bin/env bash
set -euo pipefail
# Only synthetic credentials, disposable SQLite, no n8n network access.
ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
IMAGE="docker.n8n.io/n8nio/n8n:2.2.0"
WORK="$(mktemp -d)"
trap 'rm -rf "$WORK"' EXIT
mkdir -p "$WORK/data" "$WORK/fixtures"
chmod 777 "$WORK/data"
# Fixed, public fixture values are intentionally not secrets.
python3 - "$WORK/fixtures/credentials.json" <<'PY'
import json,sys
json.dump([{"id":"test-credential-1","name":"synthetic-header","type":"httpHeaderAuth","data":{"name":"X-Test-Key","value":"FAKE_ONLY_CREDENTIAL_SENTINEL_926418"},"isManaged":False}],open(sys.argv[1],"w"))
PY
docker pull "$IMAGE" >/dev/null
set +e
timeout 100s docker run --rm --user "$(id -u):$(id -g)" --network none --cap-drop ALL \
  --security-opt no-new-privileges --pids-limit 256 --memory 1200m \
  -e N8N_USER_FOLDER=/tmp/n8n-data \
  -e N8N_ENCRYPTION_KEY=synthetic-only-encryption-key-0123456789 \
  -e N8N_DIAGNOSTICS_ENABLED=false \
  -e N8N_VERSION_NOTIFICATIONS_ENABLED=false \
  -v "$WORK/data:/tmp/n8n-data" \
  -v "$WORK/fixtures:/fixtures:ro" \
  "$IMAGE" import:credentials --input=/fixtures/credentials.json > "$WORK/import.log" 2>&1
status=$?
set -e
if [[ "$status" -ne 0 ]]; then
  echo "FAIL: n8n credential import failed; logs withheld to avoid secret disclosure"
  exit 1
fi
python3 - "$WORK/data/database.sqlite" "$WORK/import.log" <<'PY'
import sqlite3,sys,pathlib
root=pathlib.Path(sys.argv[1]).parent
candidates=list(root.rglob("database.sqlite"))
assert len(candidates)==1, f"FAIL: expected exactly one n8n SQLite database, found {len(candidates)}"
db=candidates[0]
con=sqlite3.connect(str(db))
tables=[r[0] for r in con.execute("SELECT name FROM sqlite_master WHERE type='table'")]
assert "credentials_entity" in tables, "FAIL: missing n8n credentials table"
rows=con.execute("SELECT name,type,data FROM credentials_entity").fetchall()
assert len(rows)==1 and rows[0][0]=="synthetic-header", "FAIL: missing imported credential"
raw=rows[0][2]
if isinstance(raw,bytes): raw=raw.decode("utf-8",errors="replace")
assert "FAKE_ONLY_CREDENTIAL_SENTINEL_926418" not in raw, "FAIL: plaintext secret stored"
assert "X-Test-Key" not in raw, "FAIL: plaintext credential data stored"
assert raw, "FAIL: empty credential data"
log=pathlib.Path(sys.argv[2]).read_text()
assert "FAKE_ONLY_CREDENTIAL_SENTINEL_926418" not in log, "FAIL: secret leaked in import log"
print("PASS: real n8n credential import; credential data not plaintext in SQLite or import log")
PY
