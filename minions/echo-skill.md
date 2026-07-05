---
name: vault-shared-memory
category: memory
description: Persistent cross-session shared memory backed by an Obsidian vault. Agents read, write, and search markdown notes that persist across all sessions, cron jobs, and conversations.
---

# Vault Shared Memory

Persistent, cross-session shared memory backed by your **Obsidian vault**. Every agent, skill, cron job, and conversation can read from and write to this vault — it's the "institutional memory" that spans all runs.

## ⚙️ First-Time Setup

Before the skill works, your Hermes needs to know where your vault is:

```bash
# Clone the repo (one-time)
git clone https://github.com/yuzuriaichi/agent-vault.git ~/shared-memory-layer

# Set your vault path (change this to YOUR vault's location)
export OBSIDIAN_VAULT_PATH=~/my-obsidian-vault
```

Or set it permanently in your Hermes `.env` file:
```
OBSIDIAN_VAULT_PATH=~/my-obsidian-vault
```

If you **don't** set it, the tool will look for `~/baby's vault/` by default.

## Trigger Conditions

Use this skill when:
- The user asks you to **save, remember, or record** something for later
- You complete a **research task** and want to persist findings
- A **decision** is made that should be referable in future sessions
- You start a task and want to **check what's already known** about a topic
- The user asks "what did we find about X?" or "do we have notes on Y?"

## Provided Tools

All commands use `~/shared-memory-layer/` as the install path. Adjust if you placed the repo elsewhere.

### Save a research note

```shell
python3 ~/shared-memory-layer/memory_agent.py write research \
  "Topic Title" \
  "Your findings and notes here"
```

### Save a decision

```shell
python3 ~/shared-memory-layer/memory_agent.py write decision \
  "Decision Title" \
  "Context and decision details"
```

### Save a session summary

```shell
python3 ~/shared-memory-layer/memory_agent.py write session \
  "Session Title" \
  "What happened during this session"
```

### Search existing notes

```shell
python3 ~/shared-memory-layer/memory_agent.py search "your keywords"
```

### Read a specific note

```shell
python3 ~/shared-memory-layer/memory_agent.py read "Research/Your Topic"
```

### List all notes

```shell
python3 ~/shared-memory-layer/memory_agent.py list
```

## Python API (for scripts and cron jobs)

```python
from vault_bridge import Vault

# Custom vault path — only needed if OBSIDIAN_VAULT_PATH isn't set
vault = Vault(vault_path="~/my-obsidian-vault")

# Or just use the env var default
vault = Vault()

vault.save_research("Topic", "Detailed findings")
vault.save_decision("Title", context="...", decision="...")
results = vault.search("keyword")
note = vault.read_note("Research/Topic")
```

## Folder Structure in the Vault

Any Obsidian vault — the tool creates these folders on first write:

```
your vault/
├── Research/           ← Research findings, investigations
├── Decisions/          ← Decision logs with context & rationale
├── Sessions/           ← Session summaries and outcomes
├── Notes/              ← General notes
└── Projects/           ← Project-specific notes
```

All folders auto-create on first write — zero setup needed.

## Best Practices

1. **Save research immediately** after completing an investigation — don't wait for the user to ask
2. **Search before starting** a task that looks familiar — check what's already in the vault
3. **Link decisions to their context** — always include why, not just what
4. **Use the `read` command** when the user asks "what did we find about X?" — pull from vault first
5. **Save session summaries** for long interactive sessions so next time we pick up where we left off
