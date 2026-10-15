# Policy engine

Makes every repository the account owns match [schemas/policy.yaml](../../schemas/policy.yaml),
the data behind [standards/BRANCHING.md](../../standards/BRANCHING.md) and
[standards/PROJECT.md](../../standards/PROJECT.md).

- `engine.py`: inspect, plan, and (with `--apply`) enforce. A dry run changes nothing.
- `templates/`: the governed workflows every repository carries, compared by git blob hash.
- `.github/workflows/policy.yml`: runs it every 15 minutes as the policy GitHub App.

## The policy App

The engine acts as its own GitHub App, separate from Jarvis's.
- Enforcement needs Administration on every repository. Jarvis must never hold that, or he could rewrite the rules he works under.
- The App is not in any ruleset's bypass list. It can set the rules; it cannot skip them.

Permissions:

| Permission | Level |
|---|---|
| Administration | read and write |
| Contents | read and write |
| Pull requests | read and write |
| Checks | read and write |
| Workflows | read and write |
| Metadata | read |

Install it on **All repositories**, so new repositories are included automatically.

Settings in this repository:
- variable `POLICY_APP_ID`;
- secret `POLICY_APP_PRIVATE_KEY`;
- variable `POLICY_APPLY` = `true` to leave dry-run mode.

## Local dry run

```
python tools/policy/engine.py                 # uses `gh auth token`; changes nothing
python tools/policy/engine.py --repo jarvis
```
