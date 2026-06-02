# Skills Hub

> 一个跨平台兼容的 AI Agent Skills 集合，支持 Claude Code、OpenClaw、Codex 等主流平台。

[![License](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Platform](https://img.shields.io/badge/Platform-Claude%20Code%20%7C%20OpenClaw%20%7C%20Codex-orange)]()

## 📖 简介

这是一个个人 Skills Hub，用于创建、调试、发布和收集 AI Agent Skills。所有 Skills 遵循 [agentskills.io](https://agentskills.io) 规范，兼容主流 AI Agent 平台。

## ✨ 特性

- **跨平台兼容** — 同时支持 Claude Code、OpenClaw、Codex 等平台
- **标准格式** — 遵循 agentskills.io 规范，可被公共 hub 读取
- **可测试** — 每个 skill 都配有测试场景
- **CI 验证** — 自动验证 skill 格式正确性

## 🚀 快速开始

### 安装 Skills

```bash
# 克隆仓库
git clone https://github.com/YOUR_USERNAME/skills-hub.git
cd skills-hub

# Claude Code
cp -r skills/* ~/.claude/skills/

# OpenClaw
cp -r skills/* ~/.openclaw/skills/

# Codex
cp -r skills/* ~/.agents/skills/
```

### 创建新 Skill

```bash
# 创建 skill 目录
mkdir -p skills/my-new-skill

# 创建 SKILL.md
cat > skills/my-new-skill/SKILL.md << 'EOF'
---
name: my-new-skill
description: "Use when [describe triggering conditions]"
---

# My New Skill

## Overview
...
EOF
```

### 移植现有 Skills

```bash
# 列出所有可移植的 skills
python scripts/migrate.py --list

# 移植所有 skills
python scripts/migrate.py --all

# 移植指定的 skill
python scripts/migrate.py brainstorming
```

## 📂 目录结构

```
skills-hub/
├── SKILL.md              # Hub 管理 skill
├── README.md             # 本文件
├── CLAUDE.md             # 项目级指令
├── .github/workflows/    # CI 配置
├── skills/               # Skills 集合
│   └── [skill-name]/
│       ├── SKILL.md      # Skill 定义（必需）
│       ├── references/   # 参考文件（可选）
│       └── examples/     # 示例（可选）
└── tests/                # 测试场景
```

## 📋 Skill 规范

每个 Skill 必须包含以下 YAML frontmatter：

```yaml
---
name: skill-name-with-hyphens
description: "Use when [触发条件 - 描述何时使用此 skill]"
---
```

### 命名规则

- 只使用字母、数字、连字符
- 使用动词开头（如 `creating-skills`）
- 清晰描述功能

### 描述规则

- 以 "Use when..." 开头
- 描述触发条件，而非工作流程
- 使用第三人称

## 🧪 开发工作流

每个 Skill 的开发必须遵循 **RED-GREEN-REFACTOR** 测试流程：

```
1. RED   → 编写测试场景，在不安装 skill 的情况下运行，观察 agent 失败
2. GREEN → 编写 SKILL.md，安装后重新测试，agent 应通过
3. REFACTOR → 关闭漏洞，添加反制措施，重新验证
```

详细规范请参阅 [CLAUDE.md](CLAUDE.md)。

### 同步命令

```bash
# 完整同步 + 验证
python scripts/sync.py

# 仅验证
python scripts/sync.py --validate

# 仅同步 openclaw.plugin.json
python scripts/sync.py --sync
```

## 📋 技能列表

<!-- SYNC_SKILLS_TABLE_START -->
| Skill | 描述 | 测试 |
|-------|------|-------|
| [weather-forecast](skills/weather-forecast/) | Use when users ask about weather, weather forecast, temperat... | ✅ |
<!-- SYNC_SKILLS_TABLE_END -->

---

## 🔧 支持的平台

| 平台 | 安装路径 | 说明 |
|------|---------|------|
| [Claude Code](https://code.claude.com) | `~/.claude/skills/` | Anthropic 官方 CLI |
| [OpenClaw](https://github.com/openclaw/openclaw) | `~/.openclaw/skills/` | 开源 Claude 框架 |
| [Codex](https://github.com/openai/codex) | `~/.agents/skills/` | OpenAI 官方 CLI |
| 魔塔社区 | GitHub 仓库 | 公共 skill hub |

## 🤝 贡献

欢迎提交 PR 或创建 Issue！

## 🔒 安全声明

**本仓库是公开的。** 请确保不提交任何敏感信息：

- ❌ API 密钥、Token、密码
- ❌ 个人隐私信息
- ❌ 本地文件路径
- ❌ `.env` 文件

提交前请运行 `git diff --cached` 审查所有变更。

## 📄 许可证

MIT License