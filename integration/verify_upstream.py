#!/usr/bin/env python3
"""Download a pinned file and verify exact Git object SHA before execution."""
import hashlib
from pathlib import Path
import sys
from urllib.request import urlopen
url, expected, filename = sys.argv[1:]
assert len(expected) == 40 and all(ch in '0123456789abcdef' for ch in expected)
assert url.startswith('https://raw.githubusercontent.com/')
data = urlopen(url, timeout=25).read(1_000_001)
assert len(data) < 1_000_001, 'oversized upstream source'
blob_sha = hashlib.sha1(b'blob ' + str(len(data)).encode() + b'\x00' + data).hexdigest()
if blob_sha != expected:
    raise RuntimeError(f'Upstream content mismatch: expected {expected} got {blob_sha}')
Path(filename).write_bytes(data)
print(f'PIN_VERIFIED: {filename}, git blob SHA {blob_sha}')
