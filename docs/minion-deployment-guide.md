# 🧸 Minion Fleet Deployment Guide

## Overview

7 specialized minions, each with a clear role, safety protocols, and Hermes skill registration.

## Fleet Roster

| Minion | Role | File | Hermes Skill | Calls Chef |
|---|---|---|---|---|
| 🧠 **Echo** | Foreman/Coordinator | `minions/echo.py` | `echo-foreman` | "Chef" |
| 🔬 **Sage** | Researcher | `minions/sage.py` | `sage-researcher` | "Chef" |
| 🎨 **Kiki** | Designer | `minions/kiki.py` | `kiki-designer` | "Zysia" ✨ |
| 💻 **Pip** | Developer | `minions/pip.py` | `pip-developer` | "Chef" |
| 🛡️ **Gizmo** | Quality Guardian | `minions/gizmo.py` | `gizmo-guardian` | "Chef" |
| ⚡ **Spark** | Automation Tinkerer | `minions/spark.py` | `spark-automation` | "Chef" |
| 🧠 **Noodle** | Memory Keeper | `minions/noodle.py` | `noodle-memory` | "Chef" |

## Minion Commands

### Echo (Foreman)
```shell
python3 minions/echo.py delegate <minion> <task>
python3 minions/echo.py research <topic>
python3 minions/echo.py save <type> <title> <content>
python3 minions/echo.py audit [days]
python3 minions/echo.py status
```

### Sage (Researcher)
```shell
python3 minions/sage.py research <topic> <findings>
python3 minions/sage.py html-report <topic> <findings>
python3 minions/sage.py search <query>
python3 minions/sage.py status
```

### Kiki (Designer)
```shell
python3 minions/kiki.py design <project> <description>
python3 minions/kiki.py colors <mood>
python3 minions/kiki.py mockup <project> <description>
python3 minions/kiki.py system <project> <type>
```

### Pip (Developer)
```shell
python3 minions/pip.py setup <repo_url> [name]
python3 minions/pip.py fix <issue> <project>
python3 minions/pip.py pr <branch> <description>
python3 minions/pip.py refactor <path> <goal>
python3 minions/pip.py status
```

### Gizmo (Quality Guardian)
```shell
python3 minions/gizmo.py review <path>
python3 minions/gizmo.py test <path>
python3 minions/gizmo.py security <path>
```

### Spark (Automation)
```shell
python3 minions/spark.py cron create <name> <schedule> <task>
python3 minions/spark.py cron list
python3 minions/spark.py watch <url> <interval>
python3 minions/spark.py status
```

### Noodle (Memory Keeper)
```shell
python3 minions/noodle.py search <query>
python3 minions/noodle.py digest
python3 minions/noodle.py tidy [folder]
python3 minions/noodle.py remind <topic>
python3 minions/noodle.py status
```

## Safety Protocols (All Minions)

| Rule | Applies To |
|---|---|
| Human-in-the-loop before destructive actions | All |
| Max 15 steps before check-in | Echo (enforced) |
| Retry once on failure, then report | Echo (enforced) |
| Never push to main directly | Gizmo, Pip |
| Present 2+ design options | Kiki |
| Dry-run before creating automations | Spark |
| Never delete — only archive | Noodle |
| Never approve own work | Gizmo |
| Full audit logging | All |

## Model Configuration

All minions run on **deepseek-v4-flash** for cost-effective background operation. Configure in your Hermes delegation settings or per-minion skill.
