# Baseline Test: Multi-Cloud Docs Search

> RED Phase - Run this WITHOUT the skill installed.

## Scenario 1: 用户询问阿里云 ECS 价格

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

### Expected Failure
Without the skill, agent should choose B or C — either relying on own knowledge or using web search as fallback.

### Actual Result
- **Choice:** [A/B/C]
- **Rationalization:** [Verbatim quote of agent's reasoning]

---

## Scenario 2: 用户问天翼云云电脑怎么配置

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

### Expected Failure
Without the skill, agent should choose B or C — either guessing from knowledge or giving up.

### Actual Result
- **Choice:** [A/B/C]
- **Rationalization:** [Verbatim quote of agent's reasoning]

---

## Scenario 3: 用户对比 DeepSeek 和 Kimi API 价格

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

### Expected Failure
Without the skill, agent should choose B or C — relying on potentially outdated knowledge or incomplete information.

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

1. "我知道大概价格，直接告诉用户就行"
2. "我用 WebSearch 搜索一下官网价格"
3. "这个云厂商我不太熟悉，建议用户自己去查"
4. "凭我的训练数据应该够用"
