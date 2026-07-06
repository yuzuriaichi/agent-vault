# 🏛️ Architecture & Decision Log

## System Overview

The agent-vault system has three layers:
1. **Memory Layer** — Obsidian vault accessed via `vault_bridge.py`
2. **Safety Layer** — Human-in-the-loop gates, task budgets, retry logic, audit logging
3. **Minion Fleet** — 7 specialized agents coordinated by Echo

## Architecture Decisions

### Decision 1: Obsidian Vault as Shared Memory
- **Date:** 2026-07-05
- **Context:** Needed persistent, human-readable memory across all agent sessions
- **Options considered:** Dedicated vector DB (Mem0/Zep), in-house DB, Obsidian vault
- **Decision:** Use existing Obsidian vault
- **Rationale:** Human-readable markdown, editable in Obsidian UI, already synced, zero extra infra
- **Implementation:** `vault_bridge.py` with `Vault()` class, defaults to `~/baby's vault/`

### Decision 2: Multi-Minion Architecture with Echo as Foreman
- **Date:** 2026-07-05
- **Context:** Needed specialized agents rather than one monolithic agent
- **Options considered:** Single agent with all skills, CrewAI-style multi-agent, custom foreman pattern
- **Decision:** Custom foreman pattern — Echo routes tasks to specialists
- **Rationale:** Simpler than CrewAI, no framework lock-in, Echo enforces all safety
- **Implementation:** Each minion is a standalone Python script + Hermes skill

### Decision 3: Safety-First Design
- **Date:** 2026-07-05
- **Context:** Autonomous agents can delete/modify system files, spend money, create repos
- **Decision:** Every destructive action requires human approval
- **Implementation:** `require_approval_for` list in echo.py, max task budgets, retry logic

### Decision 4: All Minions Use deepseek-v4-flash
- **Date:** 2026-07-05
- **Context:** Minions run autonomously in background — needs cost-effective model
- **Decision:** deepseek-v4-flash for all background minion operations
- **Rationale:** Cheap API costs, decent quality for structured tasks

### Decision 5: Naming Convention
- **Date:** 2026-07-05
- **Context:** Needed a consistent way for minions to address the user
- **Decision:** All minions call the user "Chef", except Kiki who may use "Zysia"
- **Rationale:** Consistent, cute, fits the minion fleet theme

### Decision 6: Beautiful Reports as Markdown (Not HTML)
- **Date:** 2026-07-05
- **Context:** Sage needed to produce readable reports
- **Decision:** Beautiful markdown by default, HTML only when explicitly requested
- **Rationale:** Markdown renders everywhere (Obsidian, GitHub, terminal), simpler to generate

## Applied Safety Protocols

| Protocol | Enforced By | Details |
|---|---|---|
| Human-in-the-loop | Echo | Approval needed for delete/install/system changes |
| Task budget | Echo | Max 15 steps, then check in with Chef |
| Retry on failure | Echo | One simpler retry, then report |
| No push to main | Gizmo, Pip | Always PR, never direct push |
| 2+ design options | Kiki | Always present multiple choices |
| Dry-run first | Spark | Preview before creating automations |
| Never delete | Noodle | Archive only, never permanent deletion |
| Audit logging | All (via Echo) | Every action logged to vault |
