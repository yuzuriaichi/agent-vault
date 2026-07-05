---
name: vault-shared-memory
category: memory
---

# Vault Shared Memory

Persistent, cross-session shared memory backed by the user's **Obsidian vault** at `/root/baby's vault/`. Every agent, skill, cron job, and conversation can read from and write to this vault — it's the "institutional memory" that spans all runs.

## Trigger Conditions

Use this skill when:
- The user asks you to **save, remember, or record** something for later
- You complete a **research task** and want to persist findings
- A **decision** is made that should be referable in future sessions
- You start a task and want to **check what's already known** about a topic
- The user asks "what did we find about X?" or "do we have notes on Y?"

## Provided Tools

The vault bridge lives at `/root/workspace/shared-memory-layer/`. Use it like this:

### Save a research note

```shell
python3 /root/workspace/shared-memory-layer/memory_agent.py write research \
  "Topic Title" \
  "Your findings and notes here"
```

### Save a decision

```shell
python3 /root/workspace/shared-memory-layer/memory_agent.py write decision \
  "Decision Title" \
  "Context and decision details"
```

### Save a session summary

```shell
python3 /root/workspace/shared-memory-layer/memory_agent.py write session \
  "Session Title" \
  "What happened during this session"
```

### Search existing notes

```shell
python3 /root/workspace/shared-memory-layer/memory_agent.py search "your keywords"
```

### Read a specific note

```shell
python3 /root/workspace/shared-memory-layer/memory_agent.py read "Research/Agentic OS"
```

### List all notes

```shell
python3 /root/workspace/shared-memory-layer/memory_agent.py list
```

## Python API (for scripts and cron jobs)

```python
from vault_bridge import Vault
vault = Vault()
vault.save_research("Topic", "Detailed findings")
vault.save_decision("Title", context="...", decision="...")
results = vault.search("keyword")
note = vault.read_note("Research/Topic")
```

## Folder Structure in the Vault

```
baby's vault/
├── Research/           ← Research findings, investigations
├── Decisions/          ← Decision logs with context & rationale
├── Sessions/           ← Session summaries and outcomes
├── Notes/              ← General notes
└── Projects/           ← Project-specific notes
```

Folders are auto-created on first write — no setup needed.

## Best Practices

1. **Save research immediately** after completing an investigation — don't wait for the user to ask
2. **Search before starting** a task that looks familiar — check what's already in the vault
3. **Link decisions to their context** — always include why, not just what
4. **Use the `read` command** when the user asks "what did we find about X?" — pull from vault first
5. **Save session summaries** for long interactive sessions so next time we pick up where we left off
