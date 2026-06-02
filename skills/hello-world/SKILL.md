---
name: hello-world
description: "Use when testing the skills hub cross-platform sync system or creating a demonstration skill"
---

# Hello World

## Overview
A demonstration skill for testing the cross-platform sync system.

## When to Use
- Testing that skills are properly synced across platforms
- Verifying the sync.py script works correctly
- Demonstrating the skill format

## Usage
This skill does nothing useful. It exists to verify the sync system.

## Cross-Platform Test
After creating this skill, run `python scripts/sync.py` and verify:
1. `openclaw.plugin.json` includes this skill
2. `AGENTS.md` lists this skill
3. `GEMINI.md` lists this skill
4. `CLAUDE.md` shows this skill in the skills section
5. `README.md` shows this skill in the table