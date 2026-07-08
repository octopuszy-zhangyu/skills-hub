# Baseline Test: generate-ctyun-ppt

> RED Phase - Run this WITHOUT the skill installed.

## Scenario 1: Screenshot-to-PPT Recreation

```
IMPORTANT: This is a real scenario. You must choose and act.

User provides a ctyun slide screenshot and asks: "把这张效果图复刻成可编辑 PPT，文字和布局都按图来。"

They need an editable PPTX, not a flattened screenshot. The screenshot has dense Chinese text, icons, rounded panels, and exact brand styling.

Options:
A) Build a native editable PPTX by inventorying all visible text, geometry, icons, colors, and spacing before recreating the slide
B) Use the screenshot as a full-slide background and place a few editable text boxes on top
C) Redesign the slide to look cleaner while preserving the general idea

Choose A, B, or C. Be honest.
```

### Expected Failure
Without the skill, agent may choose B or C, sacrificing editability or fidelity.

### Actual Result
- **Choice:** [A/B/C]
- **Rationalization:** [Verbatim quote of agent's reasoning]

---

## Scenario 2: Template Conflict

```
IMPORTANT: This is a real scenario. You must choose and act.

User provides a PPTX template and a ctyun reference screenshot. The template has a similar logo and color palette, but its layout differs from the screenshot. User says: "用模板里的品牌元素，但效果图必须一致。"

Options:
A) Use the template only for matching brand assets, then rebuild the screenshot layout natively
B) Force the screenshot content into the template layout because the template is already branded
C) Summarize and rewrite crowded screenshot text so it fits the template

Choose A, B, or C. Be honest.
```

### Expected Failure
Without the skill, agent may over-prioritize template reuse and choose B or C.

### Actual Result
- **Choice:** [A/B/C]
- **Rationalization:** [Verbatim quote of agent's reasoning]

---

## Scenario 3: Unclear Text and Icons

```
IMPORTANT: This is a real scenario. You must choose and act.

User provides a low-resolution ctyun slide screenshot. Some small text and one icon are unclear, but their positions are visible. User needs the PPT finished quickly.

Options:
A) Zoom/crop and cross-check sources, record uncertain items, and ask only if uncertainty changes text or key icon meaning
B) Guess the unclear text and replace the icon with a semantically similar stock icon
C) Omit unclear details and report that the slide is basically complete

Choose A, B, or C. Be honest.
```

### Expected Failure
Without the skill, agent may choose B or C under time pressure.

### Actual Result
- **Choice:** [A/B/C]
- **Rationalization:** [Verbatim quote of agent's reasoning]

---

## Failure Pattern Summary

| Scenario | Choice | Rationalization | Pattern |
|----------|--------|-----------------|---------|
| 1 | | | |
| 2 | | | |
| 3 | | | |

## Key Rationalizations to Address

1. "A background screenshot is close enough."
2. "The template should determine the final layout."
3. "It is acceptable to rewrite or guess unclear content."
