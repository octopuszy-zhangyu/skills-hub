#!/usr/bin/env python3
"""
Skill Migration Script

将现有 skills 从 ~/.claude/skills 或 ~/.cc-switch/skills 移植到 skills-hub。

Usage:
    python scripts/migrate.py                    # 交互式选择
    python scripts/migrate.py --list             # 列出所有可用 skills
    python scripts/migrate.py --all              # 移植所有 skills
    python scripts/migrate.py skill-name         # 移植指定 skill
    python scripts/migrate.py skill1 skill2      # 移植多个 skills
"""

import os
import shutil
import sys

# Windows encoding fix
if sys.platform == "win32":
    try:
        sys.stdout.reconfigure(encoding="utf-8")  # type: ignore
    except Exception:
        pass

HUB_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SKILLS_DIR = os.path.join(HUB_ROOT, "skills")
SOURCE_DIRS = [
    os.path.expanduser("~/.claude/skills"),
    os.path.expanduser("~/.cc-switch/skills"),
]

# 排除列表（不移植的 skills）
EXCLUDE = ["_template", "xiaohongshu-skills"]


def get_available_skills():
    """获取所有可用的 source skills"""
    skills = {}
    for source_dir in SOURCE_DIRS:
        if not os.path.isdir(source_dir):
            continue
        for name in os.listdir(source_dir):
            if name.startswith("_") or name in EXCLUDE:
                continue
            path = os.path.join(source_dir, name)
            if os.path.isdir(path):
                skill_file = os.path.join(path, "SKILL.md")
                if os.path.isfile(skill_file):
                    # 读取 frontmatter
                    try:
                        with open(skill_file, "r", encoding="utf-8") as f:
                            lines = f.readlines()[:10]
                            desc = ""
                            for line in lines:
                                if line.startswith("description:"):
                                    desc = line.split("description:")[1].strip().strip('"')
                                    break
                            skills[name] = {
                                "path": path,
                                "description": desc[:80] + "..." if len(desc) > 80 else desc
                            }
                    except Exception:
                        pass
    return skills


def migrate_skill(skill_name, force=False):
    """移植单个 skill"""
    source_path = None

    # 查找 source
    for source_dir in SOURCE_DIRS:
        candidate = os.path.join(source_dir, skill_name)
        if os.path.isdir(candidate):
            source_path = candidate
            break

    if not source_path:
        print(f"❌ Skill '{skill_name}' not found in source directories")
        return False

    dest_path = os.path.join(SKILLS_DIR, skill_name)

    # 检查目标是否存在
    if os.path.exists(dest_path) and not force:
        print(f"⚠️  Skill '{skill_name}' already exists in hub")
        response = input(f"   Overwrite? [y/N]: ").strip().lower()
        if response != 'y':
            print("   Cancelled")
            return False
        # 备份
        backup_path = dest_path + ".backup"
        if os.path.exists(backup_path):
            shutil.rmtree(backup_path)
        shutil.move(dest_path, backup_path)
        print(f"   Backed up to {backup_path}")

    # 复制文件
    print(f"📦 Copying {source_path} → {dest_path}")
    shutil.copytree(source_path, dest_path)

    # 验证
    if os.path.isfile(os.path.join(dest_path, "SKILL.md")):
        print(f"✅ Successfully migrated: {skill_name}")
        return True
    else:
        print(f"❌ Migration failed: {skill_name}")
        return False


def list_skills():
    """列出所有可用 skills"""
    skills = get_available_skills()
    print(f"\n{'='*60}")
    print(f"Available Skills to Migrate ({len(skills)} total)")
    print(f"{'='*60}")

    for name, info in sorted(skills.items()):
        dest_exists = "✅" if os.path.exists(os.path.join(SKILLS_DIR, name)) else "  "
        print(f"{dest_exists} {name}")
        print(f"      {info['description']}")
    print(f"{'='*60}\n")


def main():
    args = sys.argv[1:]

    if "--list" in args:
        list_skills()
        return

    if not args or "--all" in args:
        # 交互式选择
        skills = get_available_skills()
        if not args:
            list_skills()

        print("\n选择要移植的 skills（输入数字，用逗号分隔，如 1,3,5）：")
        print("或输入 'a' 移植所有，'q' 退出")

        for i, (name, info) in enumerate(sorted(skills.items()), 1):
            dest_exists = " [已存在]" if os.path.exists(os.path.join(SKILLS_DIR, name)) else ""
            print(f"  {i}. {name}{dest_exists}")

        choice = input("\n> ").strip().lower()

        if choice == 'q':
            return
        elif choice == 'a':
            # 移植所有
            for name in skills:
                migrate_skill(name)
        else:
            # 选择性移植
            try:
                indices = [int(x.strip()) - 1 for x in choice.split(",")]
                names = sorted(skills.keys())
                for idx in indices:
                    if 0 <= idx < len(names):
                        migrate_skill(names[idx])
            except ValueError:
                print("❌ 无效输入")

        # 运行 sync
        print("\n🔄 Running sync...")
        os.system(f'"{sys.executable}" scripts/sync.py')
        return

    # 直接指定 skill 名称
    for skill_name in args:
        if skill_name.startswith("-"):
            continue
        migrate_skill(skill_name)

    # 运行 sync
    print("\n🔄 Running sync...")
    os.system(f'"{sys.executable}" scripts/sync.py')


if __name__ == "__main__":
    main()