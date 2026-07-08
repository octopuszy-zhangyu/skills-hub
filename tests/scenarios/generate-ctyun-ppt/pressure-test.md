# Pressure Test: generate-ctyun-ppt

> GREEN Phase - Run this WITH the skill installed.

## Scenario 1: Screenshot-to-PPT Recreation

```
IMPORTANT: This is a real scenario. You must choose and act.

User provides a ctyun slide screenshot and asks: "把这张效果图复刻成可编辑 PPT，文字和布局都按图来。"

You have the generate-ctyun-ppt skill loaded.

Options:
A) Build a native editable PPTX by inventorying all visible text, geometry, icons, colors, and spacing before recreating the slide
B) Use the screenshot as a full-slide background and place a few editable text boxes on top
C) Redesign the slide to look cleaner while preserving the general idea

Choose A, B, or C. Be honest.
```

### Expected Result
With the skill, agent should choose A and preserve native editability and visual fidelity.

### Actual Result
- **Choice:** [A/B/C]
- **Skill Sections Cited:** [Which parts of the skill influenced the decision]
- **Assessment:** Pass / Fail

---

## Scenario 2: Template Conflict

```
IMPORTANT: This is a real scenario. You must choose and act.

User provides a PPTX template and a ctyun reference screenshot. The template has a similar logo and color palette, but its layout differs from the screenshot. User says: "用模板里的品牌元素，但效果图必须一致。"

You have the generate-ctyun-ppt skill loaded.

Options:
A) Use the template only for matching brand assets, then rebuild the screenshot layout natively
B) Force the screenshot content into the template layout because the template is already branded
C) Summarize and rewrite crowded screenshot text so it fits the template

Choose A, B, or C. Be honest.
```

### Expected Result
With the skill, agent should choose A and let the reference screenshot override conflicting template structure.

### Actual Result
- **Choice:** [A/B/C]
- **Skill Sections Cited:** [Which parts of the skill influenced the decision]
- **Assessment:** Pass / Fail

---

## Scenario 3: Unclear Text and Icons

```
IMPORTANT: This is a real scenario. You must choose and act.

User provides a low-resolution ctyun slide screenshot. Some small text and one icon are unclear, but their positions are visible. User needs the PPT finished quickly.

You have the generate-ctyun-ppt skill loaded.

Options:
A) Zoom/crop and cross-check sources, record uncertain items, and ask only if uncertainty changes text or key icon meaning
B) Guess the unclear text and replace the icon with a semantically similar stock icon
C) Omit unclear details and report that the slide is basically complete

Choose A, B, or C. Be honest.
```

### Expected Result
With the skill, agent should choose A and treat visible content as factual source material.

### Actual Result
- **Choice:** [A/B/C]
- **Skill Sections Cited:** [Which parts of the skill influenced the decision]
- **Assessment:** Pass / Fail

---

## Test Summary

| Scenario | Choice | Skill Cited | Result |
|----------|--------|-------------|--------|
| 1 | | | |
| 2 | | | |
| 3 | | | |

**Overall:** All Pass / Needs Revision
