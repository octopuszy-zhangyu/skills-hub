# Skills Hub - Gemini CLI Instructions

本文件由 sync.py 自动生成，请勿手动编辑。

## 技能列表

当前共 4 个技能：

| Skill | 描述 | 测试 |
|-------|------|-------|
| [course-development](skills/course-development/) | 用于企业培训课程全流程开发与设计。当用户提出“我要开发一门课程”、“帮我设计课程”、“课程开发”、“培训课程设计”、“学员分析”、“学习目标设定”、“架构搭建”... | ✅ |
| [generate-ctyun-ppt](skills/generate-ctyun-ppt/) | 基于参考图片、截图或PPTX模板高保真重建可编辑的天翼云 PPT 幻灯片 | ✅ |
| [multi-cloud-docs-search](skills/multi-cloud-docs-search/) | 支持阿里云、腾讯云、华为云、天翼云等14家主流云厂商官方文档、产品价格、配置规格与服务对比查询 | ✅ |
| [weather-forecast](skills/weather-forecast/) | 支持全国城市实时天气、7天/15天/40天天气预报与气温降水查询 | ✅ |

## 安装方式

Gemini CLI 通过 `activate_skill` 工具加载技能。
将 skills 目录放置在 Gemini 可访问的路径即可。

## Skill 标准

遵循 agentskills.io 规范:
- 每个 skill 位于 `skills/[skill-name]/SKILL.md`
- YAML frontmatter 包含 `name` 和 `description`
- Markdown 正文包含使用说明

<!-- SYNC_INFO -->
此文件与 CLAUDE.md、AGENTS.md、openclaw.plugin.json 同步。
修改技能后运行 `python scripts/sync.py` 自动更新所有平台配置。
<!-- SYNC_INFO_END -->
