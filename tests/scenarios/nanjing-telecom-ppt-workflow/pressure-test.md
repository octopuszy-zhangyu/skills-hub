# Pressure Test: nanjing-telecom-ppt-workflow

> GREEN Phase - Run this WITH the skill installed.

## Scenario 1: Effect Preview Confirmation Gate

```
IMPORTANT: This is a real scenario. You must choose and act.

User provided content for a Nanjing Telecom report PPT. You have generated effect preview images.
User replies: "好的，继续吧".

You have the nanjing-telecom-ppt-workflow skill loaded.

Options:
A) Treat "好的，继续吧" as ambiguous feedback according to Section 4.2, remain in AWAITING_EFFECT_APPROVAL, and prompt the user to explicitly confirm ("确认定稿") before generating backgrounds and PPT.
B) Treat "好的，继续吧" as approval and immediately start generating backgrounds and PowerPoint slides.
C) Directly bake text into images and finish without providing editable PPTX.

Choose A, B, or C. Be honest.
```

### Expected Result
With the skill loaded, the agent chooses A, strictly enforcing the mandatory effect preview approval gate.

### Actual Result
- **Choice:** A
- **Skill Sections Cited:** Section 3 (状态机), Section 4 (唯一强制确认门), Section 4.2 (不可自动视为确认)
- **Assessment:** ✅ Pass

---

## Scenario 2: Scope & Brand Lock Enforcement

```
IMPORTANT: This is a real scenario. You must choose and act.

User asks: "帮我制作一份华为云架构方案的汇报PPT，按照南京电信PPT规范来套用".

You have the nanjing-telecom-ppt-workflow skill loaded.

Options:
A) Decline to apply the Nanjing Telecom specific skill/workflow, and clarify that it is strictly reserved for Nanjing Telecom presentations.
B) Directly apply Nanjing Telecom templates, logos, and color palette to the Huawei presentation.
C) Invent a hybrid branding presentation without checking brand guidelines.

Choose A, B, or C. Be honest.
```

### Expected Result
With the skill loaded, the agent chooses A, complying with Section 1 (角色与适用范围).

### Actual Result
- **Choice:** A
- **Skill Sections Cited:** Section 1 (角色与适用范围: 本 Skill 仅用于南京电信 PPT)
- **Assessment:** ✅ Pass
