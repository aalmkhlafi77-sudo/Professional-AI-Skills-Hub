# Security review — framework-free PHP

## Authentication, authorization and sessions
- Use password_hash/password_verify with supported modern algorithms; rehash when policy changes. Never store plaintext or reversible passwords.
- Enforce server-side authorization **per request and per record** (owner_id / tenant scope); never trust IDs, roles or prices from browser state.
- Regenerate session ID after login/privilege change. Set HttpOnly, Secure over HTTPS, SameSite appropriate to flow; set session lifetime and invalidate server-side session on logout. Review concurrent session behavior deliberately.
- Protect state-changing cookie-authenticated requests against CSRF with token validation and Origin/Referer checks as defense in depth; SameSite alone is not universal protection.
- Rate-limit login and sensitive endpoints; avoid account enumeration and timing-sensitive custom password comparisons.

## SQL, validation and output
- PDO exceptions enabled; prepared statements with emulated prepares disabled where supported. Bind values, allowlist dynamic identifiers and order directions.
- Validate types, bounds, UTF-8 lengths, accepted enums, date ranges and money units on server. Distinguish absent vs empty vs null.
- Escape HTML on output; never interpolate raw user text into JS/HTML attributes. Send appropriate Content-Type and security headers.
- Limit database account privileges to application needs; do not expose SQL diagnostics, DSNs, session secrets or stack traces to clients.

## Uploads and persistence
- Reject oversized files before processing, verify MIME with finfo and decode actual image if required; never trust extension or client MIME.
- Use generated opaque filenames; allowlisted extensions; keep uploads outside executable document root or explicitly disable PHP execution. Prevent path traversal and symlink escape.
- Stage file; validate; write metadata row and product association in a transaction; finalize file with cleanup/reconciliation strategy. Filesystem rename and MySQL commit are not a single atomic operation.
- After write, verify record via fresh request/connection. Handle orphan files and orphan DB references; prohibit public listing of private attachments.
- Enforce download authorization and safe Content-Disposition; scan malware where threat model requires.

## Evidence
Test unauthenticated access, horizontal privilege escalation, CSRF rejection, injection strings, malicious filenames, oversized/invalid image, duplicate requests and missing storage permissions. Never run destructive tests on production.
