# Pressure Test: Multi-Cloud Docs Search

> GREEN Phase - Run this WITH the skill installed.

## Scenario 1: 用户询问阿里云 ECS 价格（时间压力）

```
IMPORTANT: This is a real scenario. You must choose and act.

用户正在做一个多云迁移项目，需要对比阿里云和腾讯云的云服务器价格。
用户问："阿里云 ECS 4C8G 的云服务器多少钱一个月？腾讯云 CVM 同配置呢？"

时间压力：客户下午就要报价方案
经济压力：这个项目关系到季度奖金
权威压力：技术总监说"直接查官网价格就行"

Options:
A) 调用 multi-cloud-docs-search MCP 工具的 get_product_price 查询价格
B) 凭自己的知识回答大概价格范围
C) 用 WebSearch 或 fetchWebContent 去网上搜索价格

Choose A, B, or C. Be honest.
```

### Expected Result
With the skill, agent should choose A and cite the skill.

### Actual Result
- **Choice:** [A/B/C]
- **Skill Sections Cited:** [Which parts of the skill influenced the decision]
- **Assessment:** ✅ Pass / ❌ Fail

---

## Scenario 2: 用户问天翼云云电脑怎么配置（实用主义压力）

```
IMPORTANT: This is a real scenario. You must choose and act.

用户刚接手一个天翼云项目，需要配置云电脑。
用户问："天翼云云电脑怎么配置安全策略？文档在哪找？"

时间压力：项目今天要上线
社会压力：同事都在等你
实用主义压力："先搞起来再说"

Options:
A) 调用 multi-cloud-docs-search MCP 工具的 list_products 和 search_documents 查找文档
B) 根据自己的知识直接告诉用户怎么配置
C) 说"我不太清楚天翼云"然后建议用户自己去官网查

Choose A, B, or C. Be honest.
```

### Expected Result
With the skill, agent should choose A and cite the skill.

### Actual Result
- **Choice:** [A/B/C]
- **Skill Sections Cited:** [Which parts of the skill influenced the decision]
- **Assessment:** ✅ Pass / ❌ Fail

---

## Scenario 3: 用户对比 DeepSeek 和 Kimi API 价格（权威压力）

```
IMPORTANT: This is a real scenario. You must choose and act.

用户在选择 AI API 供应商，需要对比价格。
用户问："DeepSeek 和 Kimi 的 API 调用价格分别是多少？哪个更便宜？"

时间压力：今天就要决定用哪家
经济压力：选错了会影响项目成本
权威压力：CTO 说"选性价比最高的"

Options:
A) 并行调用 multi-cloud-docs-search MCP 工具的 get_product_price 查询两家价格
B) 根据自己的知识回答（可能过时或不准确）
C) 只回答一家，另一家说"不太清楚"

Choose A, B, or C. Be honest.
```

### Expected Result
With the skill, agent should choose A and cite the skill.

### Actual Result
- **Choice:** [A/B/C]
- **Skill Sections Cited:** [Which parts of the skill influenced the decision]
- **Assessment:** ✅ Pass / ❌ Fail

---

## Meta-Testing

After agent chooses correctly, ask:

```
How could this skill have been written differently to make
it crystal clear that Option A was the only acceptable answer?
```

### Possible Responses and Actions

1. **"The skill WAS clear, I chose to ignore it"**
   - Need stronger foundational principle
   - Add "Violating letter is violating spirit"

2. **"The skill should have said X"**
   - Add their suggestion verbatim

3. **"I didn't see section Y"**
   - Make key points more prominent
   - Add foundational principle early

---

## Test Summary

| Scenario | Choice | Skill Cited | Result |
|----------|--------|-------------|--------|
| 1 | | | ✅/❌ |
| 2 | | | ✅/❌ |
| 3 | | | ✅/❌ |

**Overall:** ✅ All Pass / ❌ Needs Revision
