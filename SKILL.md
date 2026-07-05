---
name: vault-shared-memory
category: memory
description: Persistent cross-session shared memory backed by your Obsidian vault. Agents read, write, and search markdown notes that persist across all sessions, cron jobs, and conversations.
---

# Vault Shared Memory

Persistent, cross-session shared memory backed by your **Obsidian vault** (path set via `OBSIDIAN_VAULT_PATH` env var, defaults to `~/baby's vault/`). Every agent, skill, cron job, and conversation can read from and write to this vault.

## Setup

```bash
git clone https://github.com/yuzuriaichi/agent-vault.git ~/shared-memory-layer
export OBSIDIAN_VAULT_PATH=~/my-obsidian-vault
```

## Usage

```shell
# Save a research note
python3 ~/shared-memory-layer/memory_agent.py write research "Topic" "Findings"

# Search the vault
python3 ~/shared-memory-layer/memory_agent.py search "keywords"

# Read a note
python3 ~/shared-memory-layer/memory_agent.py read "Research/Topic"

# Save a decision
python3 ~/shared-memory-layer/memory_agent.py write decision "Title" "Context"

# List everything
python3 ~/shared-memory-layer/memory_agent.py list
```

## Folder Structure

```
your vault/
├── Research/      ← Research findings
├── Decisions/     ← Decision logs
├── Sessions/      ← Session summaries
├── Notes/         ← General notes
└── Projects/      ← Project-specific notes
```

## Minions

This repo also contains a minion fleet in `minions/`:
- 🧠 **Echo** — Foreman/coordinator (`minions/echo.py`)
- 🛡️ **Gizmo** — Quality guardian (`minions/gizmo.py`)
- ⚡ **Spark** — Automation tinkerer (`minions/spark.py`)
- 🧠 **Noodle** — Memory keeper (`minions/noodle.py`)
- 🎨 **Kiki** — Designer (`minions/kiki.py`)
- 💻 **Pip** — Developer (`minions/pip.py`)

Each has its own Hermes skill file and runs on deepseek-v4-flash for cheap background operation.
