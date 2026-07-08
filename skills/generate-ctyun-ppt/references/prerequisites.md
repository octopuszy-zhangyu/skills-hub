# Prerequisites

Install this folder as a Codex skill by copying `generate-ctyun-ppt/` into `$CODEX_HOME/skills/` or `~/.codex/skills/`.

## 1. Runtime

| Requirement | Notes |
|---|---|
| Python | Use Python 3.9 or newer. |
| Python packages | Install with `python -m pip install -r requirements.txt` from the skill directory. |
| PowerPoint | Recommended on Windows for native rendering and PNG export validation. |
| Fonts | Install Microsoft YaHei or provide an equivalent CJK font. |

Run:

```bash
python scripts/validate_environment.py
```

---

## 2. Included Resources

| Path | Purpose |
|---|---|
| `scripts/ppt_to_md.py` | Extract visible text from a PPTX for readback validation. |
| `scripts/rebuild_ctyun_token_slide.py` | Rebuild the original token-operation sample slide with native PPT objects. It extracts the logo from the template media at runtime. |
| `references/example_*.md` | Example inventory, route decision, and replication plan from the source project. |

**Default**: For new user work, create a separate project folder containing `analysis/`, `assets/`, `exports/`, and `validation/`. Set `PPT_PROJECT` to that folder when running bundled scripts that need a project root. Put extracted PPTX media under `analysis/template_media/ppt/media/`, or set `PPT_TEMPLATE` to the source template PPTX so the sample script can extract `ppt/media/` before cropping the logo.
