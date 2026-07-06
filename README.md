# 🧠 agent-vault — Obsidian Shared Memory Layer + Minion Fleet

Give your AI agents **persistent, human-readable memory** backed by your Obsidian vault, plus a fleet of specialized minions for research, design, development, testing, automation, and memory keeping.

```
git clone https://github.com/yuzuriaichi/agent-vault.git ~/shared-memory-layer
```

---

## 📋 What's In This Repo

### Core Memory Layer
| File | Purpose |
|---|---|
| `vault_bridge.py` | Python engine — read/write/search any Obsidian vault |
| `memory_agent.py` | CLI wrapper — save research/decisions/sessions, search, list |
| `SKILL.md` | Hermes skill definition for the shared memory layer |
| `templates/` | Structured note templates (research, decisions, sessions) |

### Minion Fleet (`minions/`)
| Minion | Role | File |
|---|---|---|
| 🧠 **Echo** | Foreman — coordinates all tasks, enforces safety | `minions/echo.py` |
| 🔬 **Sage** | Researcher — deep-dive on any topic, beautiful md reports | `minions/sage.py` |
| 🎨 **Kiki** | Designer — UI/UX, design systems, mockups | `minions/kiki.py` |
| 💻 **Pip** | Developer — code, PRs, refactoring, repos | `minions/pip.py` |
| 🛡️ **Gizmo** | Quality Guardian — code review, testing, security | `minions/gizmo.py` |
| ⚡ **Spark** | Automation Tinkerer — cron jobs, feeds, watches | `minions/spark.py` |
| 🧠 **Noodle** | Memory Keeper — vault tidy, digests, reminders | `minions/noodle.py` |
| `cron-jobs.md` | Schedule reference for background tasks | |

### Documentation (`docs/`)
| File | Purpose |
|---|---|
| `architecture.md` | System design and component architecture |
| `research-agentic-os.md` | Research findings on building an Agentic OS |
| `minion-deployment-guide.md` | Minion roles, safety protocols, commands |
| `setup-complete-guide.md` | One-page setup for a fresh Hermes instance |

---

## 🚀 Quick Start

```bash
# 1. Clone
git clone https://github.com/yuzuriaichi/agent-vault.git ~/shared-memory-layer

# 2. Set your vault path (change this!)
export OBSIDIAN_VAULT_PATH=~/my-obsidian-vault

# 3. Test it
python3 ~/shared-memory-layer/memory_agent.py list

# 4. Save something
python3 ~/shared-memory-layer/memory_agent.py write research "Topic" "Findings"

# 5. Register skills with your Hermes (see docs/setup-complete-guide.md)
```

---

## 🧠 Architecture Overview

The system has three layers:

```
┌─────────────────────────────────────────────┐
│           🧸 Minion Fleet                    │
│  Echo (coordinator) → delegates to →        │
│  Sage · Kiki · Pip · Gizmo · Spark · Noodle │
├─────────────────────────────────────────────┤
│           🛡️ Safety Layer                    │
│  Human-in-the-loop · Task budgets ·         │
│  Retry logic · Audit logging                │
├─────────────────────────────────────────────┤
│           💾 Memory Layer                    │
│  vault_bridge.py ⇄ Obsidian vault           │
│  Research/ · Decisions/ · Sessions/ ·       │
│  Notes/ · Projects/                         │
└─────────────────────────────────────────────┘
```

All minions run on **deepseek-v4-flash** for cost-effective background operation.

---

## 🔧 Custom Vault Path

The tool checks in order:
1. `vault_path` argument passed to `Vault()` in Python
2. `OBSIDIAN_VAULT_PATH` environment variable
3. Defaults to `~/baby's vault/`

---

## 📝 License

MIT — use it anywhere, change anything, share freely.
