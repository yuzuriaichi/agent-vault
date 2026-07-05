#!/usr/bin/env python3
"""
Shared Memory Agent — the bridge between Hermes and the Obsidian vault.

This agent is designed to be called by other agents (via syscall or
delegate_task) to read, write, and search the vault as shared memory.

Usage:
    python3 memory_agent.py write research "Agentic OS" "Found that..."
    python3 memory_agent.py search "agentic OS"
    python3 memory_agent.py read "Research/Agentic OS"
    python3 memory_agent.py list
"""

import sys
import json
import os

# Add parent to path so vault_bridge is importable
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from vault_bridge import Vault


def main():
    if len(sys.argv) < 2:
        print("Usage: memory_agent.py <command> [args...]")
        print("Commands:")
        print("  write <type> <title> <content>   — Save a note")
        print("    types: research, decision, session, note")
        print("  read <path>                       — Read a note")
        print("  search <query>                    — Search vault")
        print("  list [folder]                     — List notes")
        print("  folders                           — List folders")
        sys.exit(1)

    vault = Vault()
    command = sys.argv[1]

    if command == "write":
        if len(sys.argv) < 5:
            print("Usage: memory_agent.py write <type> <title> <content>")
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

        print(f"✅ Saved → {path}")

    elif command == "read":
        if len(sys.argv) < 3:
            print("Usage: memory_agent.py read <path>")
            sys.exit(1)
        content = vault.read_note(sys.argv[2])
        if content:
            print(content)
        else:
            print(f"❌ Note not found: {sys.argv[2]}")
            sys.exit(1)

    elif command == "search":
        query = " ".join(sys.argv[2:]) if len(sys.argv) > 2 else ""
        if not query:
            print("Usage: memory_agent.py search <query>")
            sys.exit(1)
        results = vault.search(query)
        if results:
            print(json.dumps(results, indent=2, ensure_ascii=False))
        else:
            print(f"No results found for: {query}")

    elif command == "list":
        folder = sys.argv[2] if len(sys.argv) > 2 else ""
        notes = vault.list_notes(folder)
        for n in notes:
            print(f"  📄 {n}")

    elif command == "folders":
        vault_path = vault.vault_path
        folders = set()
        for md_file in vault_path.rglob("*.md"):
            if ".obsidian" in str(md_file):
                continue
            rel = md_file.parent.relative_to(vault_path)
            if str(rel) != ".":
                folders.add(str(rel))
        for f in sorted(folders):
            print(f"  📁 {f}/")

    else:
        print(f"❌ Unknown command: {command}")
        sys.exit(1)


if __name__ == "__main__":
    main()
