# Atlas Credential Rotation Playbook (cluster0.wmcojpw, DB `talk`)

**Status at time of writing (2026-10-28):** leaked password in harithkavish.github.io
public git history CONFIRMED still the live one (exact match with `HERMES_ATLAS_URI`
in `/opt/hermes/state/.env`). Never rotate from inside a session — every value is a
placeholder for Harith to fill at rotation time.

## Consumers (every place the password lives)

| # | Consumer | Where | How to update |
|---|----------|-------|---------------|
| 1 | Hermes gateway + explore memory | `/opt/hermes/state/.env` → `HERMES_ATLAS_URI` | `hermes config set HERMES_ATLAS_URI <new>` (or edit .env), then restart Hermes services (`hmaint` → update → `hdone`) |
| 2 | memory-diary Cloudflare Worker | Worker secret `MONGODB_ATLAS_URI` (NOT in repo) | `cd worker && wrangler secret put MONGODB_ATLAS_URI` — or `secretctl push -Target wrangler:...` |
| 3 | my_chatgpt backend memory-tool | runtime `MONGO_URI` env on its host (repo has placeholders only) | Update the runtime .env on that host |

No other consumer: SkinNet-Analyzer, gallery, music etc. reference placeholders only.
The memory-diary Android app holds no credential by design (public, decompilable).

## Order of operations (approx 5 min + restarts)

1. **Atlas console** (Harith only): cluster0 → Database Access → user `harithkavish40`
   → Edit Password → auto-generate, copy the new connection string.
2. **Hermes**: update `HERMES_ATLAS_URI`, restart in maintenance order. Verify with any
   explore memory read.
3. **memory-diary Worker**: `wrangler secret put MONGODB_ATLAS_URI`. Verify with a
   worker health/login curl.
4. **my_chatgpt backend** (if still running anywhere): update `MONGO_URI`, restart.
5. **After verification**: resolve the 12 harithkavish.github.io secret-scanning alerts
   as "revoked". History scrubbing optional — the old password is burnt.

## Evidence (2026-10-28)

- 12 open secret-scanning alerts on harithkavish.github.io, `publicly_leaked=true`
  (re-verified; unchanged since Oct 7). Of these, only those matching user
  `harithkavish40` + cluster0.wmcojpw are real; the rest are doc placeholders.
- Blob f272ee9… (public history) password == live `HERMES_ATLAS_URI` password.
- AgroCloud-Finance-Pro AWS keys (alerts 1–2): DEAD via STS GetCallerIdentity
  (`InvalidClientTokenId`) — the Oct 23 "LIVE" report was wrong. Cleanup-only: dead key
  still at HEAD on `development` in 3 Uploader.jsx copies; resolve alerts as revoked.

## Liveness re-check method

Boolean-only comparison, no secret values printed:

```bash
# Leaked blob (via gh api git/blobs/<sha>) vs live .env, URL-decoded, exact match
# Example (prints only true/false, never the value):
# python3 -c "
# import os, re, urllib.parse
# leaked = 'mongodb+srv://user:PASSWORD@cluster0.wmcojpw.mongodb.net/'
# live = open('/opt/hermes/state/.env').read()
# m = re.search(r'HERMES_ATLAS_URI=mongodb\\+srv://[^:]+:([^@\r\n]+)@', live)
# if m:
#     live_pw = urllib.parse.unquote(m.group(1))
#     leaked_pw = urllib.parse.unquote(re.search(r':([^@]+)@', leaked).group(1))
#     print(live_pw == leaked_pw)
# else:
#     print(False)
# "
```

See `scripts/aws-key-liveness-probe.py` in the jarvis repo for the AWS equivalent of this check.