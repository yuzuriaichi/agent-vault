#!/usr/bin/env python3
"""
Vault Bridge — shared memory layer backed by an Obsidian vault.

Agents read from and write to the vault as their persistent,
human-readable "institutional memory." The vault becomes the
knowledge graph that spans all agent runs, cron jobs, and
research sessions.

Usage:
    from vault_bridge import Vault

    vault = Vault()
    vault.write_note("Projects/My Project", "# My Project\n## Goals\n- ...")
    results = vault.search("agentic OS")
    vault.save_decision("We decided to use Obsidian as shared memory")
"""

import os
import re
import json
import glob
import datetime
from pathlib import Path
from typing import List, Dict, Optional, Union


class Vault:
    """Interface to the Obsidian vault as a shared memory store."""

    def __init__(self, vault_path: Optional[str] = None):
        self.vault_path = Path(vault_path or os.environ.get(
            "OBSIDIAN_VAULT_PATH",
            str(Path.home() / "baby's vault")
        )).expanduser().resolve()

        if not self.vault_path.exists():
            print(f"⚠️  Vault not found at {self.vault_path}")
            print(f"   └─ Set OBSIDIAN_VAULT_PATH in your .env to point to YOUR vault.")
            print(f"   └─ Example: export OBSIDIAN_VAULT_PATH=~/my-obsidian-vault")

    # ── Core Operations ──────────────────────────────────────────────

    def write_note(self, path: str, content: str, folder: str = "") -> str:
        """Write a markdown note into the vault.

        Args:
            path: Note filename or relative path (e.g. "Research/Agentic OS"
                  or just "My Note"). .md is appended automatically.
            content: Full markdown content.
            folder: Optional subfolder under vault root.

        Returns:
            Absolute path to the written file.
        """
        note_path = self._resolve_path(path, folder)
        note_path.parent.mkdir(parents=True, exist_ok=True)
        note_path.write_text(content, encoding="utf-8")
        return str(note_path)

    def read_note(self, path: str, folder: str = "") -> Optional[str]:
        """Read a note from the vault.

        Args:
            path: Note name or relative path.
            folder: Optional subfolder.

        Returns:
            Content as string, or None if not found.
        """
        note_path = self._resolve_path(path, folder)
        if note_path.exists():
            return note_path.read_text(encoding="utf-8")
        # Try without .md
        if not note_path.suffix:
            note_path = note_path.with_suffix(".md")
            if note_path.exists():
                return note_path.read_text(encoding="utf-8")
        return None

    def search(self, query: str, max_results: int = 10) -> List[Dict]:
        """Full-text search across all vault notes.

        Uses simple keyword matching (case-insensitive). For more
        advanced search, Obsidian's native search is better — this
        is for agent-quick retrieval.

        Args:
            query: Search keywords.
            max_results: Maximum notes to return.

        Returns:
            List of {path, title, snippet, score} dicts.
        """
        results = []
        query_lower = query.lower()
        terms = query_lower.split()

        for md_file in self.vault_path.rglob("*.md"):
            if ".obsidian" in str(md_file):
                continue
            try:
                text = md_file.read_text(encoding="utf-8")
            except Exception:
                continue

            # Score: count matching terms
            text_lower = text.lower()
            score = sum(1 for t in terms if t in text_lower)
            if score == 0:
                continue

            # Extract title from first heading
            title = self._extract_title(text, md_file)

            # Build snippet around first match
            snippet = self._build_snippet(text, terms[0]) if terms else text[:200]

            results.append({
                "path": str(md_file.relative_to(self.vault_path)),
                "title": title,
                "snippet": snippet,
                "score": score,
            })

        results.sort(key=lambda r: r["score"], reverse=True)
        return results[:max_results]

    def list_notes(self, folder: str = "") -> List[str]:
        """List all markdown notes in the vault (or a subfolder)."""
        search_path = self.vault_path
        if folder:
            search_path = search_path / folder

        notes = []
        for md_file in search_path.rglob("*.md"):
            if ".obsidian" in str(md_file):
                continue
            notes.append(str(md_file.relative_to(self.vault_path)))
        return sorted(notes)

    def create_folder(self, folder: str) -> str:
        """Create a folder structure inside the vault."""
        path = self.vault_path / folder
        path.mkdir(parents=True, exist_ok=True)
        return str(path)

    # ── Structured Note Types ───────────────────────────────────────

    def save_research(self, topic: str, findings: str,
                      sources: Optional[List[str]] = None,
                      tags: Optional[List[str]] = None) -> str:
        """Save a research note to the vault."""
        tags_str = " ".join(f"#{t}" for t in (tags or []))
        date = datetime.date.today().isoformat()
        sources_str = ""
        if sources:
            sources_str = "\n".join(f"- {s}" for s in sources)

        content = f"""# {topic}

**Date:** {date}
**Tags:** {tags_str}

## Findings

{findings}

## Sources

{sources_str}

---
*Auto-saved by Hermes shared memory layer*
"""
        safe_name = re.sub(r'[^a-zA-Z0-9_\u4e00-\u9fff -]', '', topic)[:60]
        return self.write_note(f"Research/{safe_name}", content)

    def save_decision(self, title: str, context: str = "",
                      decision: str = "", rationale: str = "") -> str:
        """Save a decision log to the vault."""
        date = datetime.date.today().isoformat()
        content = f"""# Decision: {title}

**Date:** {date}

## Context

{context or "No additional context."}

## Decision

{decision or "See above."}

## Rationale

{rationale or "No rationale recorded."}

---
*Auto-saved by Hermes shared memory layer — decisions persist across sessions*
"""
        safe_name = re.sub(r'[^a-zA-Z0-9_\u4e00-\u9fff -]', '', title)[:50]
        return self.write_note(f"Decisions/{date}_{safe_name}", content)

    def save_session(self, title: str, summary: str,
                     key_outcomes: Optional[List[str]] = None,
                     tags: Optional[List[str]] = None) -> str:
        """Save a session summary to the vault."""
        tags_str = " ".join(f"#{t}" for t in (tags or []))
        date = datetime.date.today().isoformat()
        outcomes_str = ""
        if key_outcomes:
            outcomes_str = "\n".join(f"- {o}" for o in key_outcomes)

        content = f"""# Session: {title}

**Date:** {date}
**Tags:** {tags_str}

## Summary

{summary}

## Key Outcomes

{outcomes_str or "- No specific outcomes noted."}

---
*Auto-saved by Hermes shared memory layer*
"""
        safe_name = re.sub(r'[^a-zA-Z0-9_\u4e00-\u9fff -]', '', title)[:50]
        return self.write_note(f"Sessions/{date}_{safe_name}", content)

    # ── Internal Helpers ────────────────────────────────────────────

    def _resolve_path(self, path: str, folder: str = "") -> Path:
        """Resolve a note path relative to the vault."""
        if not path.endswith(".md"):
            path += ".md"
        if folder:
            return self.vault_path / folder / path
        return self.vault_path / path

    def _extract_title(self, text: str, filepath: Path) -> str:
        """Extract title from frontmatter or first heading."""
        # Check frontmatter
        if text.startswith("---"):
            end = text.find("---", 3)
            if end != -1:
                for line in text[3:end].split("\n"):
                    if line.startswith("title:"):
                        return line.split(":", 1)[1].strip().strip("\"'")
        # Check first heading
        for line in text.split("\n"):
            if line.startswith("# ") and not line.startswith("##"):
                return line[2:].strip()
        return filepath.stem

    def _build_snippet(self, text: str, term: str, width: int = 120) -> str:
        """Extract a snippet around the first occurrence of a term."""
        idx = text.lower().find(term.lower())
        if idx == -1:
            return text[:width]
        start = max(0, idx - width // 2)
        end = min(len(text), idx + width // 2)
        snippet = text[start:end].replace("\n", " ")
        if start > 0:
            snippet = "..." + snippet
        if end < len(text):
            snippet = snippet + "..."
        return snippet.strip()
