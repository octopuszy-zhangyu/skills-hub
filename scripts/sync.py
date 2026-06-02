#!/usr/bin/env python3
"""
Skills Hub - Cross-Platform Auto-Sync Engine

========== 核心理念 ==========
单一数据源: skills/[skill-name]/SKILL.md
所有平台配置文件从此自动生成/更新。

========== 同步范围 ==========
每次运行时自动同步以下文件:
  - openclaw.plugin.json   → OpenClaw 插件清单 (全自动)
  - CLAUDE.md              → 注入技能列表 (<!-- SYNC_START/END -->)
  - AGENTS.md              → Codex 配置 (全自动生成)
  - GEMINI.md              → Gemini 配置 (全自动生成)
  - README.md              → 注入技能表格 (<!-- SYNC_START/END -->)

========== 使用方法 ==========
  python scripts/sync.py              # 完整同步 + 验证
  python scripts/sync.py --validate   # 仅验证，不同步
  python scripts/sync.py --watch      # 监听模式 (自动同步)
"""

import json
import os
import re
import sys
import time

try:
    import yaml
except ImportError:
    print("ERROR: PyYAML is required. Install with: pip install pyyaml")
    sys.exit(1)

# Windows encoding fix
if sys.platform == "win32":
    try:
        sys.stdout.reconfigure(encoding="utf-8")  # type: ignore
    except Exception:
        pass  # Some Windows terminals don't support this

HUB_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SKILLS_DIR = os.path.join(HUB_ROOT, "skills")
TESTS_DIR = os.path.join(HUB_ROOT, "tests", "scenarios")
PLUGIN_JSON = os.path.join(HUB_ROOT, "openclaw.plugin.json")
CLAUDE_MD = os.path.join(HUB_ROOT, "CLAUDE.md")
AGENTS_MD = os.path.join(HUB_ROOT, "AGENTS.md")
GEMINI_MD = os.path.join(HUB_ROOT, "GEMINI.md")
README_MD = os.path.join(HUB_ROOT, "README.md")

# ============================================================
#  数据采集：从 skills/ 中提取所有 skill 信息
# ============================================================

def get_skills_data():
    """
    扫描 skills/ 目录，提取每个 skill 的 frontmatter 元数据。
    返回: [(name, description, has_tests), ...]
    """
    skills = []
    if not os.path.isdir(SKILLS_DIR):
        return skills

    for entry in sorted(os.listdir(SKILLS_DIR)):
        path = os.path.join(SKILLS_DIR, entry)
        if not os.path.isdir(path) or entry.startswith("_"):
            continue

        skill_file = os.path.join(path, "SKILL.md")
        if not os.path.isfile(skill_file):
            continue

        name = entry
        description = ""
        try:
            with open(skill_file, "r", encoding="utf-8") as f:
                content = f.read()
            parts = content.split("---", 2)
            if len(parts) >= 3:
                meta = yaml.safe_load(parts[1])
                if isinstance(meta, dict):
                    name = meta.get("name", entry)
                    description = meta.get("description", "")
        except Exception:
            pass

        # 检查是否有测试场景
        test_dir = os.path.join(TESTS_DIR, entry)
        has_tests = os.path.isdir(test_dir) and \
                    os.path.isfile(os.path.join(test_dir, "baseline.md")) and \
                    os.path.isfile(os.path.join(test_dir, "pressure-test.md"))

        skills.append((name, description, has_tests, entry))

    return skills


# ============================================================
#  自动生成各平台配置文件
# ============================================================

def sync_openclaw_plugin_json(skills):
    """全量更新 openclaw.plugin.json"""
    if not os.path.isfile(PLUGIN_JSON):
        print("  ⚠️  openclaw.plugin.json not found, creating...")
        plugin = {
            "id": "skills-hub",
            "name": "Skills Hub",
            "description": "A cross-platform compatible AI agent skills collection.",
            "version": "1.0.0",
            "skills": []
        }
    else:
        with open(PLUGIN_JSON, "r", encoding="utf-8") as f:
            plugin = json.load(f)

    skill_paths = [f"./skills/{entry}" for _, _, _, entry in skills]
    plugin["skills"] = skill_paths
    plugin["updated"] = time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())

    with open(PLUGIN_JSON, "w", encoding="utf-8") as f:
        json.dump(plugin, f, indent=2, ensure_ascii=False)
        f.write("\n")
    print(f"  ✅ openclaw.plugin.json: {len(skills)} skills")


def generate_skill_table(skills, include_test_col=False):
    """生成统一的技能表格 Markdown"""
    if not skills:
        return "_暂无技能_"

    lines = []
    lines.append("| Skill | 描述 |" + (" 测试 |" if include_test_col else ""))
    lines.append("|-------|------|" + ("-------|" if include_test_col else ""))
    for name, desc, has_tests, entry in skills:
        desc_short = desc[:60] + "..." if len(desc) > 60 else desc
        test_badge = "✅" if has_tests else "❌"
        row = f"| [{name}](skills/{entry}/) | {desc_short} |"
        if include_test_col:
            row += f" {test_badge} |"
        lines.append(row)
    return "\n".join(lines)


def generate_skill_list(skills):
    """生成技能列表（用于配置文件注入）"""
    if not skills:
        return "- _暂无技能_"

    lines = []
    for name, desc, has_tests, entry in skills:
        desc_short = desc[:60] + "..." if len(desc) > 60 else desc
        lines.append(f"- **{name}** — {desc_short}")
    return "\n".join(lines)


def inject_between_markers(filepath, start_marker, end_marker, content):
    """
    在文件的 <!-- SYNC_START --> 和 <!-- SYNC_END --> 之间注入内容。
    如果文件不存在或没有标记，则创建文件并写入。
    """
    if not os.path.isfile(filepath):
        # 创建新文件
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(f"{start_marker}\n{content}\n{end_marker}\n")
        print(f"  ✅ Created {os.path.basename(filepath)}")
        return True

    with open(filepath, "r", encoding="utf-8") as f:
        original = f.read()

    start_idx = original.find(start_marker)
    end_idx = original.find(end_marker)

    if start_idx == -1 or end_idx == -1:
        print(f"  ⚠️  {os.path.basename(filepath)}: missing sync markers, appending")
        original = original.rstrip() + f"\n\n{start_marker}\n{content}\n{end_marker}\n"
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(original)
        return True

    # 替换标记间的内容
    before = original[: start_idx + len(start_marker)]
    after = original[end_idx:]
    new_content = before + "\n" + content + "\n" + after

    if new_content != original:
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(new_content)
        print(f"  ✅ {os.path.basename(filepath)}: updated")
        return True
    else:
        print(f"  ✅ {os.path.basename(filepath)}: up to date")
        return True


def sync_claude_md(skills):
    """更新 CLAUDE.md 中的技能列表"""
    start = "<!-- SYNC_SKILLS_START -->"
    end = "<!-- SYNC_SKILLS_END -->"
    content = generate_skill_list(skills)
    inject_between_markers(CLAUDE_MD, start, end, content)


def sync_agents_md(skills):
    """全量生成 AGENTS.md (Codex 配置)"""
    content = f"""# Skills Hub - Codex (OpenAI) Instructions

本文件由 sync.py 自动生成，请勿手动编辑。

## 技能列表

当前共 {len(skills)} 个技能：

{generate_skill_table(skills, include_test_col=True)}

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
"""
    with open(AGENTS_MD, "w", encoding="utf-8") as f:
        f.write(content.lstrip())
    print(f"  ✅ AGENTS.md: {len(skills)} skills (full regenerate)")


def sync_gemini_md(skills):
    """全量生成 GEMINI.md (Gemini CLI 配置)"""
    content = f"""# Skills Hub - Gemini CLI Instructions

本文件由 sync.py 自动生成，请勿手动编辑。

## 技能列表

当前共 {len(skills)} 个技能：

{generate_skill_table(skills, include_test_col=True)}

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
"""
    with open(GEMINI_MD, "w", encoding="utf-8") as f:
        f.write(content.lstrip())
    print(f"  ✅ GEMINI.md: {len(skills)} skills (full regenerate)")


def sync_readme_md(skills):
    """更新 README.md 中的技能表格"""
    start = "<!-- SYNC_SKILLS_TABLE_START -->"
    end = "<!-- SYNC_SKILLS_TABLE_END -->"
    content = generate_skill_table(skills, include_test_col=True)
    inject_between_markers(README_MD, start, end, content)


# ============================================================
#  验证模块
# ============================================================

def validate_skill(name, desc, has_tests, entry):
    """验证单个技能"""
    errors = []
    warnings = []

    skill_dir = os.path.join(SKILLS_DIR, entry)
    skill_file = os.path.join(skill_dir, "SKILL.md")

    if not os.path.isfile(skill_file):
        return ["Missing SKILL.md"], []

    if not re.match(r'^[a-z0-9-]+$', entry):
        errors.append(f"Directory name '{entry}' should be lowercase kebab-case")

    try:
        with open(skill_file, "r", encoding="utf-8") as f:
            content = f.read()
    except Exception as e:
        errors.append(f"Cannot read SKILL.md: {e}")
        return errors, warnings

    parts = content.split("---", 2)
    if len(parts) < 3:
        errors.append("Invalid YAML frontmatter")
        return errors, warnings

    try:
        meta = yaml.safe_load(parts[1])
        if not isinstance(meta, dict):
            errors.append("Frontmatter is not a dictionary")
            return errors, warnings

        if "name" not in meta:
            errors.append("Missing 'name' in frontmatter")
        if "description" not in meta:
            errors.append("Missing 'description' in frontmatter")
        else:
            desc_text = meta["description"]
            if not desc_text.startswith("Use when"):
                warnings.append("description should start with 'Use when...'")
            if len(desc_text) > 500:
                warnings.append(f"description is {len(desc_text)} chars (>500)")

        body = parts[2].strip()
        if len(body) < 20:
            warnings.append("Very little content after frontmatter")

    except yaml.YAMLError as e:
        errors.append(f"YAML error: {e}")

    if not has_tests:
        warnings.append(f"Missing test scenarios in tests/scenarios/{entry}/")

    return errors, warnings


# ============================================================
#  主入口
# ============================================================

def sync_all(skills):
    """同步所有平台配置文件"""
    print("\n" + "=" * 60)
    print("  Cross-Platform Auto-Sync")
    print("=" * 60)

    sync_openclaw_plugin_json(skills)
    sync_claude_md(skills)
    sync_agents_md(skills)
    sync_gemini_md(skills)
    sync_readme_md(skills)

    print("\n  ✅ 所有平台配置文件已同步")
    print(f"     影响文件: CLAUDE.md, AGENTS.md, GEMINI.md, README.md, openclaw.plugin.json")


def validate_all(skills, check_tests=True):
    """验证所有技能"""
    print("\n" + "=" * 60)
    print("  Validating Skills")
    print("=" * 60)

    all_errors = {}
    all_warnings = {}

    for name, desc, has_tests, entry in skills:
        errors, warnings = validate_skill(name, desc, has_tests, entry)
        if errors:
            all_errors[entry] = errors
        if warnings:
            all_warnings[entry] = warnings

        if not errors and not warnings:
            print(f"  ✅ {entry}")
        else:
            if errors:
                for e in errors:
                    print(f"  ❌ {entry}: {e}")
            if warnings:
                for w in warnings:
                    print(f"  ⚠️  {entry}: {w}")

    # Summary
    total_errors = sum(len(v) for v in all_errors.values())
    total_warnings = sum(len(v) for v in all_warnings.values())
    print(f"\n  Skills: {len(skills)} | Errors: {total_errors} | Warnings: {total_warnings}")

    if total_errors > 0:
        print("  ❌ 请修复以上错误后重试")
        sys.exit(1)
    else:
        print("  ✅ 所有技能验证通过")


def watch_mode():
    """监听模式：持续检测 skills/ 目录变化"""
    print("\n  👀 Watch mode: monitoring skills/ for changes...")
    print("     Press Ctrl+C to stop\n")

    last_state = {}
    for root, dirs, files in os.walk(SKILLS_DIR):
        for f in files:
            path = os.path.join(root, f)
            last_state[path] = os.path.getmtime(path)

    try:
        while True:
            changed = False
            current_state = {}
            for root, dirs, files in os.walk(SKILLS_DIR):
                for f in files:
                    path = os.path.join(root, f)
                    current_state[path] = os.path.getmtime(path)
                    if path not in last_state or last_state[path] != current_state[path]:
                        changed = True
                        print(f"  📝 Detected change: {os.path.relpath(path, HUB_ROOT)}")

            if changed:
                print("  🔄 Auto-syncing...")
                skills = get_skills_data()
                sync_all(skills)
                last_state = current_state
                print("  👀 Watching for changes...\n")

            time.sleep(2)
    except KeyboardInterrupt:
        print("\n  👋 Watch mode stopped")


def main():
    args = set(sys.argv[1:])
    do_validate = "--validate" in args
    do_sync = not args or "--sync" in args or not ("--validate" in args or "--watch" in args)
    do_watch = "--watch" in args

    skills = get_skills_data()

    print(f"\n  📊 Skills Hub - Cross-Platform Sync")
    print(f"     发现 {len(skills)} 个技能")

    if do_validate:
        validate_all(skills)
        return

    if do_watch:
        watch_mode()
        return

    if do_sync:
        validate_all(skills, check_tests=False)
        sync_all(skills)


if __name__ == "__main__":
    main()