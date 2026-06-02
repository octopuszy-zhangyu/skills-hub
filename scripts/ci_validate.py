#!/usr/bin/env python3
"""
CI Validation Script for GitHub Actions.

This script is called by .github/workflows/validate-skills.yml
to validate skill frontmatter and plugin.json.
"""

import json
import os
import sys

try:
    import yaml
except ImportError:
    print("FAIL: PyYAML is required. Install with: pip install pyyaml")
    sys.exit(1)


def validate_frontmatter():
    """Validate YAML frontmatter of all SKILL.md files."""
    skills_dir = "skills"
    errors = 0

    if not os.path.isdir(skills_dir):
        print("No skills directory found")
        return 0

    for entry in sorted(os.listdir(skills_dir)):
        skill_dir = os.path.join(skills_dir, entry)
        if not os.path.isdir(skill_dir):
            continue
        if entry.startswith("_"):
            continue

        skill_file = os.path.join(skill_dir, "SKILL.md")
        if not os.path.isfile(skill_file):
            print(f"FAIL {entry}: Missing SKILL.md")
            errors += 1
            continue

        with open(skill_file, encoding="utf-8") as f:
            content = f.read()

        parts = content.split("---", 2)
        if len(parts) < 3:
            print(f"FAIL {entry}: Invalid YAML frontmatter")
            errors += 1
            continue

        try:
            meta = yaml.safe_load(parts[1])
            if not isinstance(meta, dict):
                print(f"FAIL {entry}: Frontmatter is not a dictionary")
                errors += 1
                continue

            if "name" not in meta:
                print(f"FAIL {entry}: Missing required field: name")
                errors += 1
                continue

            if "description" not in meta:
                print(f"FAIL {entry}: Missing required field: description")
                errors += 1
                continue

            desc = meta["description"]
            if not desc.startswith("Use when"):
                print(f"FAIL {entry}: description should start with 'Use when...'")
                errors += 1
                continue

            print(f"OK {entry}: Valid frontmatter")

        except yaml.YAMLError as e:
            print(f"FAIL {entry}: YAML error: {e}")
            errors += 1

    return errors


def validate_plugin_json():
    """Validate openclaw.plugin.json structure."""
    if not os.path.isfile("openclaw.plugin.json"):
        print("FAIL: openclaw.plugin.json not found")
        return 1

    with open("openclaw.plugin.json", encoding="utf-8") as f:
        plugin = json.load(f)

    required = ["id", "name", "description", "version", "skills"]
    for field in required:
        if field not in plugin:
            print(f"FAIL Missing required field: {field}")
            return 1

    print(f"OK openclaw.plugin.json is valid")
    print(f"   Skills listed: {len(plugin['skills'])}")
    return 0


def main():
    errors = 0

    # Validate frontmatter
    print("--- Validating YAML Frontmatter ---")
    errors += validate_frontmatter()

    # Validate plugin.json
    print("--- Validating openclaw.plugin.json ---")
    errors += validate_plugin_json()

    if errors > 0:
        print(f"\nFAIL: Found {errors} error(s)")
        sys.exit(1)
    else:
        print("\nOK: All validations passed")


if __name__ == "__main__":
    main()
