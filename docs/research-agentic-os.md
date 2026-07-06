# 🔬 Research Summary — Building an Agentic OS

Research conducted 2026-07-05 across academic papers, web sources, Reddit, and GitHub.

## What We Know

An Agentic OS is a coordination + governance layer that runs a fleet of AI agents as one coherent system. It maps to the 5 jobs of a traditional OS: resource management, process scheduling, memory, I/O, and permissions.

## Key Players in 2026

| Project | Type | Stars/Reach | Notes |
|---|---|---|---|
| AIOS (agiresearch) | Open-source kernel | ⭐6k | COLM 2025 paper, 12K lines Python, full kernel with scheduler/memory/tools |
| OpenFang (RightNow-AI) | Open-source Agent OS | ⭐18k | Rust-based, most popular dedicated Agent OS, v0.6.9 |
| MemoryOS (BAI-LAB) | Memory OS for agents | ⭐1.5k | EMNLP 2025 Oral, Python, personalized agent memory |
| SLES 16 (SUSE) | Enterprise Linux | — | First Linux distro with built-in agentic AI via MCP |
| Slack | Collaboration platform | — | Agents as "digital teammates" in channels |
| Microsoft | Azure AI Agent Service | — | Platform-level orchestration across M365 |

## The 6-Layer Agent Stack (O'Reilly 2026)

1. **Models & Inference** — Commoditizing. Reasoning models (o1, DeepSeek R1, Claude) let single agents replace multi-step chains. Pattern: prototype on closed, deploy on open-weight.
2. **Protocols & Tools** — MCP won (97M monthly downloads, adopted by all major labs). Security is the open problem (82% of MCP servers have path traversal vulnerabilities).
3. **Memory & Knowledge** — Three tiers: in-context, vector retrieval (pgvector), persistent cross-session. "Context engineering" replaced "prompt engineering."
4. **Frameworks & SDKs** — Every major lab ships their own SDK. LangGraph v1.0 at Uber, JPMorgan, Klarna. Most teams use too much framework.
5. **Eval & Observability** — Biggest gap: 89% have observability, only 52% have evals.
6. **Guardrails & Governance** — Newest layer. OWASP MCP Top 10. Runtime governance is "the missing layer."

## Protocol Ecosystem

| Protocol | Purpose | Status |
|---|---|---|
| **MCP** (Anthropic) | Agent → Tool | ✅ Won (97M downloads) |
| **A2A** (Google) | Agent → Agent | 🔶 50+ launch partners, growing |
| **ACP** (IBM) | Agent commerce | 🔶 Niche |
| **UCP** (Google) | Google commerce | 🔶 Niche |

## The 11 Components of an Agentic OS

| # | Component | Our Status |
|---|---|---|
| 1 | **Memory System** | ✅ **Done** — agent-vault + Obsidian |
| 2 | **Identity System** | ✅ Done — 7 minions with clear roles |
| 3 | **Skills/Tools Registry** | ✅ Done — Hermes skills + agent-reach |
| 4 | **Scheduling** | ✅ Partial — cron jobs active |
| 5 | **Permission/Governance** | ✅ Done — safety protocols |
| 6 | **Observability** | ✅ Done — Echo's audit logs |
| 7 | **Human-in-the-Loop** | ✅ Done — approval gates |
| 8 | **Context Management** | ⚠️ Partial — vault search works |
| 9 | **Agent-to-Agent Comms** | ❌ Missing — need A2A |
| 10 | **LLM Routing** | ❌ Missing — need smart model routing |
| 11 | **Priority Scheduling** | ❌ Missing — need AIOS-style scheduler |

## Community Lessons Learned

- "Add complexity only when something specific breaks, not before"
- "Start with a 50-line script + MCP servers before reaching for LangGraph"
- "Build evals BEFORE deploying, not after"
- "Multi-agent systems with 4+ agents create 6+ failure points exponentially"
- "Human-in-the-loop gates are non-negotiable for production"

## Open-Source Projects Worth Watching

- **AIOS** (agiresearch) — github.com/agiresearch/AIOS — 6k⭐ — Reference kernel architecture
- **OpenFang** (RightNow-AI) — github.com/RightNow-AI/openfang — 18k⭐ — Rust Agent OS
- **MemoryOS** (BAI-LAB) — github.com/BAI-LAB/MemoryOS — 1.5k⭐ — EMNLP 2025
- **Agent-OS** (kase1111-hash) — Natural language as OS substrate
- **awesome-agentOS** (Egv2) — Curated list of 100+ Agent OS projects

## Recommended Build Roadmap

**Phase 1** — Complete memory layer ✅
**Phase 2** — Agent-to-agent communication (A2A or custom MCP-based)
**Phase 3** — Priority scheduler (FIFO/RR/priority like AIOS)
**Phase 4** — LLM routing (auto-pick cheapest model)
**Phase 5** — Full observability dashboard
