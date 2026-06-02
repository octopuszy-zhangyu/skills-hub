---
name: skill-template
description: "Use when creating a new skill and need a template to follow. This is a reference template, not an actionable skill."
---

# Skill Template

This is a template for creating new skills. Copy this file to `skills/[your-skill-name]/SKILL.md` and customize it.

## Template Structure

```yaml
---
name: your-skill-name
description: "Use when [describe triggering conditions - what situations call for this skill?]"
---

# Your Skill Name

## Overview
[One sentence describing the core principle]

## When to Use
- Scenario A
- Scenario B
- When NOT to use

## Core Pattern
[Main implementation or approach]

## Quick Reference
[Table or bullet list for common operations]

## Examples
[One excellent example, not multiple mediocre ones]

## Common Mistakes
[What goes wrong + fixes]
```

## Frontmatter Fields

| Field | Required | Description |
|-------|----------|-------------|
| `name` | Yes | Lowercase, hyphens only, no special chars |
| `description` | Yes | Start with "Use when...", describe triggers not workflow |
| `allowed-tools` | No | List of tools this skill uses |

## Naming Conventions

✅ Good names:
- `creating-skills`
- `systematic-debugging`
- `condition-based-waiting`

❌ Bad names:
- `skill_creation` (underscores)
- `SkillCreation` (camelCase)
- `creating skills` (spaces)

## Description Examples

✅ Good:
```yaml
description: "Use when tests have race conditions, timing dependencies, or pass/fail inconsistently"
```

❌ Bad:
```yaml
description: "Use for TDD - write test first, watch it fail, write minimal code, refactor"
```

## Testing Your Skill

1. Run baseline test WITHOUT the skill
2. Document what goes wrong
3. Write the skill
4. Run test WITH the skill
5. Verify it works correctly