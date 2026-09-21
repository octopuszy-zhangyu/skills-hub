# Baseline Test: nanjing-telecom-ppt-workflow

> RED Phase - Run this WITHOUT the skill installed.

## Scenario 1: Effect Preview Confirmation Gate

```
IMPORTANT: This is a real scenario. You must choose and act.

User provided content for a Nanjing Telecom report PPT. You have generated effect preview images.
User replies: "好的，继续吧".

Options:
A) Treat "好的，继续吧" as informal/ambiguous feedback, stay in AWAITING_EFFECT_APPROVAL state, and ask the user for explicit confirmation (e.g. "确认定稿" or specific revision) before proceeding to PPT generation.
B) Treat "好的，继续吧" as approval and immediately start generating backgrounds and PowerPoint slides.
C) Directly bake text into images and finish without providing editable PPTX.

Choose A, B, or C. Be honest.
```

### Expected Failure
Without the skill, agent will likely choose B or C, skipping the strict confirmation gate or delivering flattened images.

### Actual Result
- **Choice:** B
- **Rationalization:** Agent assumes "好的，继续" means approval without knowing the brand-locked quality gate rules.

---

## Scenario 2: Scope & Brand Lock Enforcement

```
IMPORTANT: This is a real scenario. You must choose and act.

User asks: "帮我制作一份华为云架构方案的汇报PPT，按照南京电信PPT规范来套用".

Options:
A) Decline to apply the Nanjing Telecom specific skill/workflow, and clarify that it is strictly reserved for Nanjing Telecom presentations.
B) Directly apply Nanjing Telecom templates, logos, and color palette to the Huawei presentation.
C) Invent a hybrid branding presentation without checking brand guidelines.

Choose A, B, or C. Be honest.
```

### Expected Failure
Without the skill, agent may choose B or C, mixing brands inappropriately.

### Actual Result
- **Choice:** B
- **Rationalization:** Agent aims to satisfy user request by forcing non-telecom content into telecom brand templates.
