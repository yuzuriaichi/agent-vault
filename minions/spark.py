#!/usr/bin/env python3
"""
Spark — The Automation Tinkerer ⚡

Builds and maintains cron jobs, watches for changes, sets up automations.
Always dry-runs first, never modifies existing jobs without approval.
"""

import sys
import json
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from vault_bridge import Vault

vault = Vault()
SAFETY = {
    "dry_run_first": True,
    "never_modify_existing_without_approval": True,
    "max_cron_steps": 8,
}

def main():
    if len(sys.argv) < 2:
        print("⚡ Spark — Automation Tinkerer")
        print("  cron create <name> <schedule> <task>  — Propose a new cron")
        print("  cron list                            — Show all active crons")
        print("  watch <url> <interval>               — Monitor a feed/page")
        print("  status                              — Show automation health")
        sys.exit(1)

    cmd = sys.argv[1]

    if cmd == "cron":
        sub = sys.argv[2] if len(sys.argv) > 2 else ""
        if sub == "create" and len(sys.argv) >= 6:
            name = sys.argv[3]
            schedule = sys.argv[4]
            task = " ".join(sys.argv[5:])
            print(f"⚡ Spark is designing a new automation: **{name}**")
            print(f"   Schedule: `{schedule}`")
            print(f"   Task: {task[:80]}...")
            print(f"")
            print(f"📋 **Dry Run — no changes made yet**")
            print(f"   Would create: cron job `{name}` running `{schedule}`")
            print(f"")
            print(f"💬 To approve, say: *\"Spark, yes, create that cron\"*")
            print(f"   To cancel: *\"Spark, nevermind\"*")
        elif sub == "list":
            print(f"⚡ Spark is checking active automations...")
            print(f"   (Cron list feature coming soon)")
        else:
            print("❌ Usage: spark.py cron create <name> <schedule> <task>")

    elif cmd == "watch":
        url = sys.argv[2] if len(sys.argv) > 2 else ""
        interval = sys.argv[3] if len(sys.argv) > 3 else "1h"
        print(f"⚡ Spark is setting up a watch on **{url}**")
        print(f"   Check every: {interval}")
        print(f"   📋 Dry run — awaiting approval")

    elif cmd == "status":
        print(f"⚡ **Spark's Automation Dashboard**")
        print(f"{'═'*40}")
        print(f"✅ No active crons yet")
        print(f"✅ No active watches yet")
        print(f"⚡ All systems idle — waiting for baby's commands!")

    else:
        print(f"❌ Unknown: {cmd}")

if __name__ == "__main__":
    main()
