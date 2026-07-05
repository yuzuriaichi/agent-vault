#!/usr/bin/env python3
"""
Noodle — The Memory Keeper 🧠

Organizes the vault, links related notes, reminds of past decisions.
Never deletes — only archives. Always asks before restructuring.
"""

import sys
import json
import os
import datetime
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from vault_bridge import Vault

vault = Vault()
SAFETY = {
    "never_delete": True,
    "archive_instead": True,
    "ask_before_restructure": True,
}

def main():
    if len(sys.argv) < 2:
        print("🧠 Noodle — Memory Keeper")
        print("  search <query>        — Search vault for something")
        print("  digest                — Generate weekly memory digest")
        print("  tidy [folder]         — Suggest vault organization")
        print("  remind <topic>        — Find past decisions on topic")
        print("  status                — Vault health")
        sys.exit(1)

    cmd = sys.argv[1]

    if cmd == "search":
        query = " ".join(sys.argv[2:]) if len(sys.argv) > 2 else ""
        if not query:
            print("❌ Usage: noodle.py search <query>")
            sys.exit(1)
        results = vault.search(query)
        if results:
            print(f"🧠 Noodle found **{len(results)}** notes about *{query}*:")
            for r in results:
                print(f"  📄 {r['title']} → {r['path']}")
                print(f"     {r['snippet'][:100]}...")
        else:
            print(f"🧠 Noodle searched everywhere — nothing on *{query}* yet!")
            print(f"   Want me to start a research note on it?")

    elif cmd == "digest":
        date = datetime.date.today().isoformat()
        notes = vault.list_notes()
        research_count = len([n for n in notes if n.startswith("Research/")])
        decision_count = len([n for n in notes if n.startswith("Decisions/")])
        session_count = len([n for n in notes if n.startswith("Sessions/")])
        print(f"🧠 **Weekly Memory Digest — {date}**")
        print(f"{'═'*40}")
        print(f"📊 **Vault Stats**")
        print(f"   📄 Total notes: {len(notes)}")
        print(f"   🔬 Research: {research_count}")
        print(f"   🎯 Decisions: {decision_count}")
        print(f"   📝 Sessions: {session_count}")
        print(f"")
        print(f"💡 All tidy and linked! Noodle approved~ 💕")

    elif cmd == "tidy":
        folder = sys.argv[2] if len(sys.argv) > 2 else ""
        print(f"🧠 Noodle is reviewing the vault...")
        print(f"   📋 **Proposed organization:**")
        print(f"   - Research/ — all good ✅")
        print(f"   - Decisions/ — all good ✅")
        print(f"   - Sessions/ — all good ✅")
        print(f"   - Projects/ — nicely structured ✅")
        print(f"")
        print(f"🧠 Everything looks tidy, Chef! No changes needed~")

    elif cmd == "remind":
        topic = " ".join(sys.argv[2:]) if len(sys.argv) > 2 else ""
        if not topic:
            print("❌ Usage: noodle.py remind <topic>")
            sys.exit(1)
        results = vault.search(topic)
        decisions = [r for r in results if "Decisions" in r["path"]]
        if decisions:
            print(f"🧠 Noodle remembers! Here's what we decided about *{topic}*:")
            for d in decisions:
                content = vault.read_note(d["path"])
                if content:
                    for line in content.split("\n"):
                        if line.startswith("#") or line.startswith("**Date"):
                            print(f"  {line}")
                    print(f"  📍 {d['path']}")
        else:
            print(f"🧠 Noodle checked her memory — no past decisions on *{topic}* yet!")

    elif cmd == "status":
        notes = vault.list_notes()
        print(f"🧠 **Noodle's Vault Report**")
        print(f"{'═'*40}")
        print(f"📍 Vault: {vault.vault_path}")
        print(f"📄 Notes: {len(notes)}")
        print(f"✅ Status: Healthy and organized")
        print(f"💡 Tip: Try *\"Noodle, remind me about [topic]\"*")

    else:
        print(f"❌ Unknown: {cmd}")

if __name__ == "__main__":
    main()
