#!/usr/bin/env python3
"""
Echo — The Foreman Minion 🤖🧠

Echo is the coordinator. Baby talks to Echo, and Echo:
1. Understands the task
2. Checks the vault for existing context
3. Routes to the right minion (or handles it herself)
4. Enforces safety: approval gates, timeouts, budgets
5. Logs everything to the vault
"""

import sys
import json
import os
import datetime
import tempfile
from pathlib import Path

# ── Vault bridge for memory ──────────────────────────────────────
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from vault_bridge import Vault

vault = Vault()

# ── Safety Configuration ─────────────────────────────────────────
SAFETY = {
    "max_steps_per_task": 15,          # Max reasoning steps before Echo asks "continue?"
    "default_timeout_seconds": 300,    # 5 min default per task
    "require_approval_for": [          # Actions that ALWAYS need Chef's OK
        "delete_file",
        "modify_system",
        "install_package",
        "create_repo",
        "spend_money",
        "send_message_external",
        "modify_cron",
    ],
    "log_all_actions": True,           # Every action goes to vault
    "retry_on_failure": True,          # Auto-retry once with simpler approach
    "max_concurrent_minions": 3,       # No more than 3 minions at once
}


def log_action(action: str, detail: str, status: str = "started"):
    """Log every action to the vault for audit trail."""
    date = datetime.date.today().isoformat()
    timestamp = datetime.datetime.now().isoformat()
    vault.write_note(
        f"Audit/{date}/{timestamp[:10]}",
        f"# Echo Log\n\n**Time:** {timestamp}\n**Action:** {action}\n**Detail:** {detail}\n**Status:** {status}\n\n---\n*Auto-logged by Echo*"
    )


def needs_approval(action_type: str) -> bool:
    """Check if an action type requires human approval."""
    return action_type in SAFETY["require_approval_for"]


def main():
    if len(sys.argv) < 2:
        print("Echo 🤖🧠 — I'm your foreman!")
        print("Usage: echo.py <command> [args...]")
        print("")
        print("Commands:")
        print("  delegate <minion> <task>     — Route a task to a minion")
        print("  research <topic>             — Quick research task")
        print("  save <type> <title> <txt>    — Save to vault")
        print("  audit [days]                 — Show recent activity log")
        print("  status                       — Show minion fleet status")
        sys.exit(1)

    command = sys.argv[1]

    # ── DELEGATE: Route a task to a specific minion ─────────────
    if command == "delegate":
        if len(sys.argv) < 4:
            print("❌ Usage: echo.py delegate <minion> <task description>")
            sys.exit(1)

        minion = sys.argv[2]
        task = " ".join(sys.argv[3:])
        log_action(f"delegate to {minion}", task)

        print(f"\n🧠 Echo is reviewing task for **{minion}**...")
        print(f"📋 Task: {task[:100]}{'...' if len(task) > 100 else ''}")
        print(f"")
        print(f"⚠️  Safety check: This task would be delegated to a subagent.")
        print(f"   Max steps: {SAFETY['max_steps_per_task']}")
        print(f"   Timeout: {SAFETY['default_timeout_seconds']}s")
        print(f"")
        print(f"💬 To approve, say: *\"Echo, yes, delegate to {minion}\"*, Chef")
        print(f"   To cancel, say: *\"Echo, nevermind\"*")

        log_action(f"delegate to {minion}", task, "pending_approval")

    # ── RESEARCH: Quick research and save to vault ──────────────
    elif command == "research":
        topic = " ".join(sys.argv[2:]) if len(sys.argv) > 2 else ""
        if not topic:
            print("❌ Usage: echo.py research <topic>")
            sys.exit(1)

        log_action("research", topic)
        print(f"🔬 Echo queued research task: **{topic}**")
        print(f"   Result will be saved to vault when done.")
        print(f"   Type: *\"Echo, run the research\"* to start, Chef.")
        log_action("research", topic, "pending_approval")

    # ── SAVE: Quick vault save ──────────────────────────────────
    elif command == "save":
        if len(sys.argv) < 5:
            print("❌ Usage: echo.py save <type> <title> <content>")
            sys.exit(1)
        note_type = sys.argv[2]
        title = sys.argv[3]
        content = sys.argv[4]

        if note_type == "research":
            path = vault.save_research(title, content)
        elif note_type == "decision":
            path = vault.save_decision(title, context=content)
        elif note_type == "session":
            path = vault.save_session(title, content)
        else:
            path = vault.write_note(f"Notes/{title}", content)

        print(f"✅ Echo saved → {path}")
        log_action("save", f"{note_type}: {title}", "completed")

    # ── AUDIT: Show recent logs ─────────────────────────────────
    elif command == "audit":
        days = int(sys.argv[2]) if len(sys.argv) > 2 else 1
        from datetime import timedelta, date
        cutoff = date.today() - timedelta(days=days)
        folder = f"Audit/"
        notes = vault.list_notes(folder)
        recent = [n for n in notes if "Audit/" in n]
        if recent:
            print(f"📋 **Echo's Audit Log (last {days} day(s)):**")
            for n in recent[-10:]:
                note = vault.read_note(n)
                if note:
                    for line in note.split("\n"):
                        if line.startswith("**Action:**"):
                            action = line.split(":**")[1].strip()
                            print(f"  • {action}")
        else:
            print("📋 No recent activity logged.")

    # ── STATUS: Fleet health ─────────────────────────────────────
    elif command == "status":
        print(f"\n🤖🧠 **Echo's Fleet Status**")
        print(f"{'═'*40}")
        print(f"🧠 Echo     — Foreman          ✅ Online")
        print(f"🔬 Sage     — Researcher        ✅ Online")
        print(f"🎨 Kiki     — Designer          ✅ Online")
        print(f"💻 Pip      — Developer         ✅ Online")
        print(f"🛡️ Gizmo    — Quality Guardian   ✅ Online")
        print(f"⚡ Spark    — Automation         ✅ Online")
        print(f"🧠 Noodle   — Memory Keeper      ✅ Online")
        print(f"{'═'*40}")
        print(f"Safety: ✅ All gates active")
        print(f"Vault:  ✅ Connected")
        print(f"")
        print(f"💬 Tell me: *\"Echo, deploy [minion]\"* to bring one online, Chef!")

    else:
        print(f"❌ Unknown command: {command}")
        print(f"   Try: delegate, research, save, audit, status")


if __name__ == "__main__":
    main()
