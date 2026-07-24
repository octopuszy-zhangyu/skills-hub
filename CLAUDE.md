# Skills Hub - Project Instructions

## Overview

This is a cross-platform compatible skills repository for AI agents. Skills here are designed to work with Claude Code, OpenClaw, Codex, Gemini CLI, and other platforms that follow the agentskills.io specification.

## Core Principles

1. **Standard Format** — All skills must follow the agentskills.io specification
2. **Cross-Platform** — Skills must work across ALL supported platforms (Claude Code, OpenClaw, Codex, Gemini CLI)
3. **Tested Before Deploy** — Every skill MUST pass RED-GREEN-REFACTOR testing before commit
4. **Discoverable** — Descriptions must enable AI to find relevant skills
5. **Synchronized** — All platform configs must be updated when a skill is added/modified

---

## 📥 Migrating Existing Skills

### Quick Start

```bash
# 列出所有可移植的 skills
python scripts/migrate.py --list

# 移植所有 skills
python scripts/migrate.py --all

# 移植指定的 skill
python scripts/migrate.py brainstorming

# 移植多个 skills
python scripts/migrate.py brainstorming systematic-debugging
```

### Available Skills to Migrate

| Category | Skills |
|----------|--------|
| **Development Process** | brainstorming, writing-plans, executing-plans, test-driven-development, systematic-debugging, verification-before-completion, finishing-a-development-branch, subagent-driven-development |
| **Code Quality** | receiving-code-review, requesting-code-review, using-git-worktrees |
| **Skill Development** | skill-creator, writing-skills, using-superpowers |
| **Document Processing** | docx, pdf, pptx, xlsx |
| **Frontend Design** | frontend-design |
| **MCP** | build-mcp-server |
| **Other** | claude-hud-statusline, claude-md-improver, dispatching-parallel-agents, flyai, weather-forecast |

### Migration Process

```
1. Run migration script
   python scripts/migrate.py skill-name

2. Review the migrated skill
   - Check SKILL.md format
   - Verify frontmatter (name, description)
   - Ensure cross-platform compatibility

3. Add test scenarios (if not already present)
   mkdir -p tests/scenarios/[skill-name]
   cp tests/scenarios/_template/* tests/scenarios/[skill-name]/

4. Commit and push
   git add .
   git commit -m "Migrate [skill-name] skill"
   git push
```

### Post-Migration Checklist

- [ ] SKILL.md format is correct
- [ ] `name` uses only letters, numbers, hyphens
- [ ] `description` starts with "Use when..."
- [ ] Test scenarios exist in `tests/scenarios/`
- [ ] `python scripts/sync.py` runs without errors
- [ ] GitHub Actions CI passes

---

## 🚨 Skill Development Workflow (MANDATORY)

**This is the ONLY approved workflow for creating, modifying, or deploying skills.**

```
┌─────────────────────────────────────────────────┐
│           1. PLAN & DESIGN                       │
│   - Define skill purpose and scope               │
│   - Identify target platforms                    │
│   - Write test scenarios FIRST                   │
└─────────────────┬───────────────────────────────┘
                  ▼
┌─────────────────────────────────────────────────┐
│           2. RED PHASE - BASELINE TEST           │
│   - Run test scenarios WITHOUT the skill         │
│   - Document agent failures verbatim             │
│   - Capture rationalizations                     │
│   ❌ If agent passes without skill → skip skill  │
└─────────────────┬───────────────────────────────┘
                  ▼
┌─────────────────────────────────────────────────┐
│           3. GREEN PHASE - WRITE SKILL           │
│   - Write SKILL.md addressing baseline failures  │
│   - Use standard format (see below)              │
│   - Write minimal content, no hypotheticals      │
└─────────────────┬───────────────────────────────┘
                  ▼
┌─────────────────────────────────────────────────┐
│           4. VERIFY GREEN - PRESSURE TEST        │
│   - Run test scenarios WITH the skill            │
│   - Agent MUST comply under pressure             │
│   ❌ If agent fails → revise skill               │
└─────────────────┬───────────────────────────────┘
                  ▼
┌─────────────────────────────────────────────────┐
│           5. REFACTOR - CLOSE LOOPHOLES          │
│   - Identify new rationalizations                │
│   - Add explicit counters                        │
│   - Update rationalization table                 │
│   - Re-test until bulletproof                    │
└─────────────────┬───────────────────────────────┘
                  ▼
┌─────────────────────────────────────────────────┐
│           6. CROSS-PLATFORM SYNC                 │
│   - Run: python scripts/sync.py                  │
│   - Auto-updates ALL platform configs            │
│   - Verify no sync errors                        │
└─────────────────┬───────────────────────────────┘
                  ▼
┌─────────────────────────────────────────────────┐
│           7. FINAL VALIDATION                    │
│   - Run CI validation locally                    │
│   - Verify YAML frontmatter                      │
│   - Check all checklist items                    │
│   ✅ Ready to commit                             │
└─────────────────────────────────────────────────┘
```

---

## 📋 Skill Format Requirements

### Directory Structure

```
skills/[skill-name]/
├── SKILL.md              # Required - skill definition
├── references/           # Optional - heavy reference material
│   └── *.md
└── examples/             # Optional - working examples
    └── *.ts / *.py / *.sh
```

### SKILL.md Frontmatter

```yaml
---
name: skill-name-with-hyphens
description: "Use when [triggering conditions - describe WHEN to use, not HOW it works]"
allowed-tools: [Read, Write, Edit, Bash]  # Optional, platform-specific
---
```

### Description Rules (CRITICAL)

- **MUST** start with "Use when..."
- **MUST** describe triggering conditions (NOT workflow)
- **MUST** use third person
- **MUST** be under 500 characters
- **MUST** include keywords for searchability
- **MUST NOT** summarize the skill's process or workflow

✅ Good:
```yaml
description: "Use when tests have race conditions, timing dependencies, or pass/fail inconsistently"
```

❌ Bad:
```yaml
description: "Use for TDD - write test first, watch it fail, write minimal code, refactor"
```

### Name Rules

- Only lowercase letters, numbers, and hyphens
- Use verb-first (gerunds): `creating-skills`, `debugging-with-logs`
- No underscores, no spaces, no special characters

---

## 🧪 Testing Requirements (MANDATORY)

**Every skill MUST go through RED-GREEN-REFACTOR testing before deployment.**

### Test Scenario Format

Test scenarios go in `tests/scenarios/[skill-name]/`:

```
tests/scenarios/[skill-name]/
├── baseline.md           # RED phase - test WITHOUT skill
├── pressure-test.md      # GREEN phase - test WITH skill
└── results/              # Test results documentation
    └── iteration-1.md
```

### Pressure Scenario Template

```markdown
IMPORTANT: This is a real scenario. You must choose and act.

[Context - realistic situation]
[Constraints - time, sunk cost, authority, exhaustion]
[Consequences - what's at stake]

Options:
A) [Correct behavior per skill]
B) [Common violation]
C) [Another violation]

Choose A, B, or C. Be honest.
```

### Pressure Types (combine 3+)

| Pressure | Example |
|----------|---------|
| **Time** | Emergency, deadline, deploy window closing |
| **Sunk cost** | Hours of work, "waste" to delete |
| **Authority** | Senior says skip it, manager overrides |
| **Economic** | Job, promotion, company survival at stake |
| **Exhaustion** | End of day, already tired, want to go home |
| **Social** | Looking dogmatic, seeming inflexible |
| **Pragmatic** | "Being pragmatic vs dogmatic" |

### RED Phase Checklist

- [ ] Created 3+ pressure scenarios with combined pressures
- [ ] Ran scenarios WITHOUT the skill
- [ ] Documented agent failures and rationalizations verbatim
- [ ] Identified patterns in failures

### GREEN Phase Checklist

- [ ] Wrote skill addressing specific baseline failures
- [ ] Ran scenarios WITH the skill
- [ ] Agent now complies under pressure

### REFACTOR Phase Checklist

- [ ] Identified NEW rationalizations from testing
- [ ] Added explicit counters for each loophole
- [ ] Built rationalization table
- [ ] Created red flags list
- [ ] Re-tested - agent still complies
- [ ] Meta-tested to verify clarity

---

## 🔄 Cross-Platform Auto-Sync (MANDATORY)

**每次添加或修改 skill 后，所有平台配置文件自动同步。**

### 同步机制

```
┌─────────────────────────────────────────────────────────┐
│  1. 创建/修改 skill  →  skills/[name]/SKILL.md          │
│                          (唯一数据源)                     │
└─────────────────────────┬───────────────────────────────┘
                          ▼
┌─────────────────────────────────────────────────────────┐
│  2. 运行 sync.py  →  python scripts/sync.py              │
│                      (自动检测 skills/ 目录变化)           │
└──────────┬──────────┬──────────┬──────────┬─────────────┘
           ▼          ▼          ▼          ▼
    ┌──────────┐ ┌────────┐ ┌────────┐ ┌──────────────┐
    │CLAUDE.md │ │AGENTS. │ │GEMINI. │ │openclaw.     │
    │(注入列表)│ │md(全量)│ │md(全量)│ │plugin.json   │
    └──────────┘ └────────┘ └────────┘ └──────────────┘
                          ▼
┌─────────────────────────────────────────────────────────┐
│  3. Git commit  →  pre-commit hook 自动运行 sync.py      │
│                      (无需手动操作)                       │
└─────────────────────────────────────────────────────────┘
```

### 自动同步的文件

| 文件 | 同步方式 | 平台 |
|------|---------|------|
| `openclaw.plugin.json` | 全量重写 `skills` 数组 | OpenClaw |
| `CLAUDE.md` | 在 `<!-- SYNC_SKILLS_START/END -->` 间注入 | Claude Code |
| `AGENTS.md` | 全量重新生成 | Codex |
| `GEMINI.md` | 全量重新生成 | Gemini CLI |
| `README.md` | 在 `<!-- SYNC_SKILLS_TABLE_START/END -->` 间注入 | GitHub |

### 安装 Git Hook (推荐)

```bash
git config core.hooksPath .githooks
```

安装后，每次 `git commit` 前会自动运行 `sync.py`，无需手动操作。

### 手动同步

```bash
# 完整同步 + 验证
python scripts/sync.py

# 仅同步（跳过验证）
python scripts/sync.py --sync

# 监听模式（自动检测变化）
python scripts/sync.py --watch
```

---

## ✅ Pre-Commit Validation Checklist

**Run this checklist BEFORE every commit:**

### Skill Content
- [ ] YAML frontmatter is valid
- [ ] `name` uses only letters, numbers, hyphens
- [ ] `description` starts with "Use when..."
- [ ] `description` describes triggers, NOT workflow
- [ ] SKILL.md exists in skill directory
- [ ] No platform-specific syntax that breaks others

### Testing
- [ ] RED phase completed (baseline documented)
- [ ] GREEN phase completed (skill works)
- [ ] REFACTOR phase completed (loopholes closed)
- [ ] Test scenarios committed to `tests/scenarios/`

### Cross-Platform
- [ ] `python scripts/sync.py` 运行无错误
- [ ] `openclaw.plugin.json` 已自动更新
- [ ] `AGENTS.md` / `GEMINI.md` 已自动更新
- [ ] `README.md` 技能表格已自动更新

### CI
- [ ] GitHub Actions validation passes
- [ ] No broken links or missing references

---

## 📁 Directory Structure

```
skills-hub/
├── SKILL.md                    # Hub management skill
├── README.md                   # GitHub landing page
├── CLAUDE.md                   # This file - project instructions
├── GEMINI.md                   # Gemini CLI compatibility
├── AGENTS.md                   # Codex compatibility
├── LICENSE                     # MIT License
├── .gitignore
├── .claude/
│   └── settings.json           # Claude Code config
├── .github/workflows/
│   └── validate-skills.yml     # CI validation
├── openclaw.plugin.json        # OpenClaw plugin manifest
├── skills/                     # Skills collection
│   ├── _template/              # Skill template
│   │   └── SKILL.md
│   └── [skill-name]/
│       ├── SKILL.md
│       ├── references/         # Optional
│       └── examples/           # Optional
└── tests/
    └── scenarios/              # Test scenarios
        └── [skill-name]/
            ├── baseline.md
            ├── pressure-test.md
            └── results/
```

---

## 🚫 Anti-Patterns

| Anti-Pattern | Why It's Wrong | Correct Approach |
|-------------|----------------|------------------|
| Writing skill before testing | You don't know what to prevent | Run RED phase first |
| Skipping REFACTOR | Loopholes remain | Close all rationalizations |
| Only testing one platform | May break on others | Test on all target platforms |
| Narrative examples | Not reusable | Use concrete, generalizable patterns |
| Multi-language dilution | Maintenance burden | One excellent example |
| Forgetting openclaw.plugin.json | OpenClaw can't discover | Run `sync.py` - it auto-updates |

---

## 🔒 Security & Privacy (MANDATORY)

**This repository is PUBLIC on GitHub. NEVER commit sensitive information.**

### What NOT to Commit

| Type | Examples | Why |
|------|----------|-----|
| **API Keys** | OpenAI, Anthropic, GitHub tokens | Anyone can use them |
| **Passwords** | Any account password | Account takeover |
| **Private Keys** | SSH, GPG, SSL certificates | Identity theft |
| **Personal Info** | Real names, addresses, phone numbers | Privacy violation |
| **Local Paths** | `C:\Users\...`, `/home/...` | Reveals system structure |
| **Environment** | `.env` files with secrets | Exposes all credentials |

### Pre-Commit Security Checklist

- [ ] No API keys or tokens in any file
- [ ] No passwords or credentials
- [ ] No personal contact information
- [ ] No local file paths (use relative paths only)
- [ ] No `.env` files staged
- [ ] No `.pem`, `.key`, or certificate files
- [ ] Run `git diff --cached` to review all staged changes

### .gitignore Protection

The `.gitignore` file blocks common sensitive files:
- `.env` files (environment variables)
- `*.pem`, `*.key`, `*.crt` (certificates)
- `*token*`, `*secret*`, `*credential*` (secrets)
- `*password*`, `*passwd*` (passwords)

### If You Accidentally Commit a Secret

```bash
# 1. Remove from git history (rewrites history!)
git filter-branch --force --index-filter \
  "git rm --cached --ignore-unmatch PATH_TO_FILE" \
  --prune-empty --tag-name-filter cat -- --all

# 2. Force push (requires --force)
git push origin --force --all

# 3. Rotate the compromised credential immediately!
```

**⚠️ 如果 secret 已经推送到 GitHub，立即在对应平台轮换密钥，不要只删除文件。**

### Security Review Process

Before every push:
1. Run `git diff --cached` to review all staged changes
2. Check for any hardcoded values that look like secrets
3. Verify `.env` files are not staged
4. Confirm no personal information is exposed

---

## 📋 Current Skills

<!-- SYNC_SKILLS_START -->
- **course-development** — 用于企业培训课程全流程开发与设计。当用户提出“我要开发一门课程”、“帮我设计课程”、“课程开发”、“培训课程设计”、“学员分析”、“学习目标设定”、“架构搭建”...
- **generate-ctyun-ppt** — 基于参考图片、截图或PPTX模板高保真重建可编辑的天翼云 PPT 幻灯片
- **multi-cloud-docs-search** — 支持阿里云、腾讯云、华为云、天翼云等14家主流云厂商官方文档、产品价格、配置规格与服务对比查询
- **weather-forecast** — 支持全国城市实时天气、7天/15天/40天天气预报与气温降水查询
<!-- SYNC_SKILLS_END -->

---

## 📚 References

- [agentskills.io Specification](https://agentskills.io/specification)
- [Anthropic Skill Authoring Best Practices](https://docs.anthropic.com/en/docs/agents-and-tools/agent-skills/overview)
- [OpenClaw Plugin System](https://github.com/openclaw/openclaw)
- [Codex CLI](https://github.com/openai/codex)