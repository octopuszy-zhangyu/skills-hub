# Skills Hub - Codex (OpenAI) Instructions

本文件由 sync.py 自动生成，请勿手动编辑。

## 技能列表

当前共 2 个技能：

| Skill | 描述 | 测试 |
|-------|------|-------|
| [multi-cloud-docs-search](skills/multi-cloud-docs-search/) | Use when users ask about cloud provider documentation, produ... | ✅ |
| [weather-forecast](skills/weather-forecast/) | Use when users ask about weather, weather forecast, temperat... | ✅ |

## 安装方式

将 skills 目录复制到 Codex 的 skills 路径:

```bash
cp -r skills/* ~/.agents/skills/
```

## Skill 标准

遵循 agentskills.io 规范:
- 每个 skill 位于 `skills/[skill-name]/SKILL.md`
- YAML frontmatter 包含 `name` 和 `description`
- Markdown 正文包含使用说明

<!-- SYNC_INFO -->
此文件与 CLAUDE.md、GEMINI.md、openclaw.plugin.json 同步。
修改技能后运行 `python scripts/sync.py` 自动更新所有平台配置。
<!-- SYNC_INFO_END -->
