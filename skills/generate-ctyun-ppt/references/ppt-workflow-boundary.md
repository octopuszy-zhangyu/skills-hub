# PPT Workflow Boundary

Use this reference when the full `ppt-master` repository is not installed. If a local `ppt-master` skill exists, read its `SKILL.md` and workflow files as the stronger authority.

## 1. Route Selection

| User input | Action |
|---|---|
| Reference images or screenshots only | Rebuild native PPT pages from the images. |
| Reference images plus PPTX template | Use the PPTX only for brand assets, fonts, colors, background objects, and matching reusable native objects. |
| PPTX already has the same page structure | Clone the matching slide and replace or adjust native objects. |
| PPTX structure conflicts with screenshots | Create blank slides and reconstruct the screenshot layout. |

**Hard rule**: Preserve screenshot page count and order unless the user explicitly asks otherwise.

---

## 2. Project Layout

| Folder | Contents |
|---|---|
| `sources/` | User-provided screenshots, templates, and source files copied into the project. |
| `analysis/` | `reference_inventory.md`, `route_decision.md`, `replication_plan.md`, extracted media indexes. |
| `assets/` | Cropped logos, icons, illustrations, and reusable images. |
| `exports/` | Final PPTX files. |
| `validation/` | Rendered PNGs, overlay comparisons, readback text, and `replication_report.md`. |

---

## 3. Validation Loop

1. Render the generated PPTX to PNG using PowerPoint or LibreOffice.
2. Compare each output PNG with the matching reference image.
3. Fix visible text, geometry, style, and object completeness.
4. Run `python scripts/ppt_to_md.py <pptx> -o validation/readback.md`.
5. Update `validation/replication_report.md` with resolved and unresolved differences.

**Hard rule**: Do not deliver a deck that uses full-slide screenshots as backgrounds. Use native PowerPoint objects for text, basic shapes, lines, tables, and rebuildable icons.
