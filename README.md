# 🧠 agent-vault — Obsidian Shared Memory Layer for AI Agents

Give your AI agents persistent, human-readable memory backed by **your Obsidian vault**. Research findings, decisions, and session summaries automatically get saved as markdown notes you can read, edit, and organize in Obsidian.

```
git clone https://github.com/yuzuriaichi/agent-vault.git ~/shared-memory-layer
```

## ✨ What it does

- **Agents write** research, decisions, and session notes straight into your vault as `.md` files
- **Agents search** the vault before answering — no re-researching what's already known
- **You read everything** in Obsidian — it's your vault, your data, your control
- **Works across Hermes instances** — clone on any machine, same shared memory

## 🚀 Quick Start

### 1. Set your vault path

```bash
export OBSIDIAN_VAULT_PATH=~/my-obsidian-vault
```

Or add it to your Hermes `.env`:
```
OBSIDIAN_VAULT_PATH=~/my-obsidian-vault
```

### 2. Save something

```bash
python3 ~/shared-memory-layer/memory_agent.py write research \
  "Quantum Computing" \
  "Found that quantum supremacy was achieved in..."
```

### 3. Search later

```bash
python3 ~/shared-memory-layer/memory_agent.py search "quantum"
```

## 📁 What gets saved

```
your vault/
├── Research/    ← Research findings with dates & tags
├── Decisions/   ← Decision logs with context & rationale
├── Sessions/    ← Session summaries & outcomes
├── Notes/       ← General notes
└── Projects/    ← Project-specific notes
```

## 📦 What's in the box

| File | What it does |
|---|---|
| `vault_bridge.py` | Core Python module — read/write/search Obsidian vault |
| `memory_agent.py` | CLI agent — call this from any Hermes or terminal |
| `SKILL.md` | Hermes skill file — register so agents auto-use it |
| `templates/` | Note templates for structured saving |

## 🤖 Register as a Hermes Skill

Tell your Hermes:

> *"Register the vault-shared-memory skill from ~/shared-memory-layer/SKILL.md"*

Once registered, your agent will automatically save research, log decisions, and search your vault for context — without you having to ask.

## 🔧 Custom Vault Path

The tool checks these in order:
1. `vault_path` argument passed to `Vault()` in Python
2. `OBSIDIAN_VAULT_PATH` environment variable
3. Defaults to `~/baby's vault/`

## 📝 License

MIT — use it anywhere, change anything, share freely.
