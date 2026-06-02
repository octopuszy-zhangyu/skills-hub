---
name: skills-hub-manager
description: Use when creating, debugging, testing, or publishing skills for AI agents. Manages a multi-platform compatible skills repository.
---

# Skills Hub Manager

A comprehensive skill for managing a cross-platform compatible skills repository.

## Overview

This hub contains skills compatible with Claude Code, OpenClaw, Codex, and other AI agent platforms. Each skill follows the agentskills.io specification for maximum compatibility.

## Hub Structure

```
skills-hub/
├── SKILL.md                    # This file
├── CLAUDE.md                   # Project-level instructions
├── README.md                   # GitHub landing page
├── .claude/
│   └── settings.json           # Claude Code config
├── .github/
│   └── workflows/
│       └── validate-skills.yml # CI validation
├── skills/                     # Skills collection
│   └── [skill-name]/
│       ├── SKILL.md            # Required
│       ├── references/         # Optional
│       └── examples/          # Optional
└── tests/
    └── scenarios/             # Test cases
```

## Skill Standard Format

Every skill must follow this format:

```yaml
---
name: skill-name-with-hyphens
description: "Use when [triggering conditions - describe when to use this skill]"
allowed-tools: [Read, Write, Edit, Bash]  # Optional
---

# Skill Name

## Overview
Core principle in 1-2 sentences.

## When to Use
- Scenario A
- Scenario B

## Core Pattern
[Implementation details]

## Quick Reference
[Common operations table]
```

## Cross-Platform Compatibility

| Platform | Installation Path | Notes |
|----------|-------------------|-------|
| Claude Code | `~/.claude/skills/` | Auto-discovers `SKILL.md` |
| OpenClaw | `~/.openclaw/skills/` | Same format |
| Codex | `~/.agents/skills/` | Same format |
| 魔塔社区 | GitHub repo | Reads `skills/*/SKILL.md` |

## Creating a New Skill

1. **Create directory**: `skills/[skill-name]/`
2. **Write SKILL.md**: Follow standard format above
3. **Test**: Run test scenarios without skill, then with skill
4. **Validate**: Ensure YAML frontmatter is correct
5. **Publish**: Commit and push to GitHub

## Validation Checklist

- [ ] `name` uses only letters, numbers, hyphens
- [ ] `description` starts with "Use when..."
- [ ] `description` describes triggering conditions (not workflow)
- [ ] YAML frontmatter is valid
- [ ] SKILL.md exists in skill directory
- [ ] Test scenarios pass

## Publishing to GitHub

1. Fork or create repository on GitHub
2. Add skills to `skills/` directory
3. Push changes
4. Platforms like 魔塔社区 can now read your skills

## Importing Skills

To use skills from this hub:

```bash
# Clone the repository
git clone https://github.com/YOUR_USERNAME/skills-hub.git

# Copy skills to your platform
cp -r skills/* ~/.claude/skills/        # Claude Code
cp -r skills/* ~/.openclaw/skills/      # OpenClaw
cp -r skills/* ~/.agents/skills/        # Codex
```