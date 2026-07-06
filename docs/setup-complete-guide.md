# 🚀 Complete Setup Guide for a Fresh Hermes Instance

Use this guide to set up agent-vault on any new Hermes machine.

## Step 1: Clone the Repo

```bash
git clone https://github.com/yuzuriaichi/agent-vault.git ~/shared-memory-layer
```

## Step 2: Set Your Vault Path

```bash
export OBSIDIAN_VAULT_PATH=~/my-obsidian-vault
```

Add permanently to your Hermes `.env` file:
```
OBSIDIAN_VAULT_PATH=~/my-obsidian-vault
```

## Step 3: Register Hermes Skills

Tell your Hermes to register these skills from the repo:

| Skill | File | Category |
|---|---|---|
| Vault Shared Memory | `SKILL.md` | memory |
| Echo — Foreman | `minions/echo-skill.md` | minions |
| Sage — Researcher | `minions/sage.py` → skill | minions |
| Kiki — Designer | `minions/kiki.py` → skill | minions |
| Pip — Developer | `minions/pip.py` → skill | minions |
| Gizmo — Guardian | `minions/gizmo.py` → skill | minions |
| Spark — Automation | `minions/spark.py` → skill | minions |
| Noodle — Memory | `minions/noodle.py` → skill | minions |

## Step 4: Test the Memory Layer

```bash
python3 ~/shared-memory-layer/memory_agent.py list
python3 ~/shared-memory-layer/memory_agent.py write research "Test" "Testing the setup"
python3 ~/shared-memory-layer/memory_agent.py search "Test"
```

## Step 5: Set Up Cron Jobs (Optional)

See `minions/cron-jobs.md` for the two recommended cron jobs:
- **Noodle Vault Tidy** — Every 12 hours
- **Noodle Weekly Digest** — Sundays at 9 AM

## Step 6: Launch a Minion

```bash
python3 ~/shared-memory-layer/minions/echo.py status
python3 ~/shared-memory-layer/minions/sage.py status
```

## Platform Notes

- **Linux/macOS:** Use `python3` in all commands
- **Windows:** Use `python` instead of `python3`
- **Vault path with spaces:** Always quote the path (e.g., `"~/my vault/"`)
- **Path resolution:** Set absolute paths in `.env` for best results

## Troubleshooting

| Problem | Fix |
|---|---|
| `ModuleNotFoundError: No module named 'vault_bridge'` | Run commands from the repo root, or check `sys.path` in the script |
| `Vault not found at ...` | Set `OBSIDIAN_VAULT_PATH` to your actual vault location |
| `command not found: python3` | Use `python` (Windows) or install Python |
| Minion script fails to import | Scripts expect to be run from `~/shared-memory-layer/` root |
