# Atlas Credential Rotation Playbook (DB `talk`)

**Status:** written before rotation. Never rotate from inside a session — every value is a placeholder for Harith to fill at rotation time.

## Consumers (every place the credential lives)

| # | Consumer | Where | How to update |
|---|----------|-------|---------------|
| 1 | Hermes gateway + explore memory | `HERMES_ATLAS_URI` env var | `hermes config set HERMES_ATLAS_URI <new>` (or edit `.env`), then restart Hermes services (`hmaint` → update → `hdone`) |
| 2 | memory-diary Cloudflare Worker | Worker secret `MONGODB_ATLAS_URI` (NOT in repo) | `cd worker && wrangler secret put MONGODB_ATLAS_URI` — or `secretctl push -Target wrangler:...` |
| 3 | my_chatgpt backend memory-tool | runtime `MONGO_URI` env on its host | Update the runtime `.env` on that host |

No other consumer: SkinNet-Analyzer, gallery, music etc. reference placeholders only.
The memory-diary Android app holds no credential by design (public, decompilable).

## Order of operations (approx 5 min + restarts)

1. **Atlas console** (Harith only): Database Access → your Atlas database user
   → Edit Password → auto-generate, copy the new connection string.
2. **Hermes**: update `HERMES_ATLAS_URI`, restart in maintenance order. Verify with any
   explore memory read.
3. **memory-diary Worker**: `wrangler secret put MONGODB_ATLAS_URI`. Verify with a
   worker health/login curl.
4. **my_chatgpt backend** (if still running anywhere): update `MONGO_URI`, restart.
5. **After verification**: resolve the secret-scanning alerts for this cluster as
   "revoked". History scrubbing optional — the old password is burnt.

## Liveness re-check method

Boolean-only comparison, no secret values printed. Template (replace the leaked URI with the actual blob value before running):

```bash
python3 -c "
import os, re, urllib.parse
leaked = 'mongodb+srv://user:***@cluster0.wmcojpw.mongodb.net/'  # replace with actual leaked URI from gh api git/blobs/<sha>
live = open('/opt/hermes/state/.env').read()
m = re.search(r'HERMES_ATLAS_URI=mongodb\\+srv://[^:]+:([^@\r\n]+)@', live)
if m:
    live_pw = urllib.parse.unquote(m.group(1))
    leaked_pw = urllib.parse.unquote(re.search(r'://[^:]+:([^@]+)@', leaked).group(1))
    print(live_pw == leaked_pw)
else:
    print(False)
"
```