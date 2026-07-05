# ⏰ Minion Cron Jobs — Schedule Reference

Active cron jobs for the minion fleet. Set these up on any new Hermes instance to keep the minions working in the background.

---

## 🧠 Noodle — Vault Tidy

**Frequency:** Every 12 hours
**Purpose:** Checks vault health, suggests organization improvements, reports back to Chef.

### Setup command for a new Hermes:

```shell
cronjob create \
  --name noodle-vault-tidy \
  --schedule "every 12h" \
  --skill vault-shared-memory \
  --skill noodle-memory \
  --prompt "You are Noodle 🧠 — the Memory Keeper minion. Run the vault tidy routine: check the vault at the path from OBSIDIAN_VAULT_PATH env var (default ~/baby's vault/) for organization, suggest any improvements, and report back to Chef with a brief status. If everything is tidy, just say so cheerfully."
```

---

## 🧠 Noodle — Weekly Memory Digest

**Frequency:** Every Sunday at 9:00 AM
**Purpose:** Generates a "This week we learned..." summary with new notes, decisions, and connections.

### Setup command for a new Hermes:

```shell
cronjob create \
  --name noodle-weekly-digest \
  --schedule "0 9 * * 0" \
  --skill vault-shared-memory \
  --skill noodle-memory \
  --prompt "You are Noodle 🧠 — the Memory Keeper minion. Generate a weekly memory digest for Chef. Check the vault at the path from OBSIDIAN_VAULT_PATH env var (default ~/baby's vault/) and summarize: how many new notes were added this week, what topics were researched, what decisions were made, and any interesting connections between notes. Present it as a warm, friendly weekly summary."
```

---

## 📋 Quick Setup for a Fresh Hermes

Run these two commands:

```shell
# 1. Clone the repo
git clone https://github.com/yuzuriaichi/agent-vault.git ~/shared-memory-layer

# 2. Set your vault path (change this!)
export OBSIDIAN_VAULT_PATH=~/my-obsidian-vault

# 3. Register the skills (ask your Hermes to register vault-shared-memory, noodle-memory)

# 4. Create the cron jobs (copy-paste the two commands above)

# 5. Set OBSIDIAN_VAULT_PATH permanently in your Hermes .env file
```

---

## 🗺️ Future Crons (Planned)

| Minion | Job | Frequency | Status |
|---|---|---|---|
| 🔬 Sage | Daily research digest | Every 24h | ⏳ Pending Chef's order |
| ⚡ Spark | Morning briefing | Daily @ 8am | ⏳ Pending Chef's order |
| 🛡️ Gizmo | Security scan | Daily | ⏳ Pending Chef's order |
| 💻 Pip | Nightly build | Daily @ 2am | ⏳ Pending Chef's order |
