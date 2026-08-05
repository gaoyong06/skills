---
name: content-topic-research
description: Research evidence-based content topics from real audience questions, public discussions, search results, competitor pages, and product context. Use when asked to find article topics, discover audience pain points, analyze content opportunities, plan promotional articles, or prepare an evidence-backed brief for Zhijuanyun, Paopaopaike, Homepage Tab, or PopPlan. Do not use this skill as a substitute for final copywriting.
---

# Content Topic Research

## Purpose

把“想写什么”转化为“目标用户正在讨论什么、为什么值得写、产品能提供什么帮助”。输出选题研究简报，不直接把推测写成事实，也不自动声称内容会带来流量或收入。

## Workflow

### 1. Define the brief

先确认以下信息；缺失时使用明确假设并标注：

- 产品和产品页面；
- 目标人群及其具体身份；
- 内容目标：认知、获客、转化、留存或教育；
- 发布渠道和地域；
- 需要的选题数量、时间范围和语言。

先从 [products-context.md](references/products-context.md) 选择一个主产品和一类主要用户。优先区分教师、教研人员、家长、学生、开发者、普通效率工具用户等具体人群，不把多个产品或“互联网用户”当作单一人群。只有在明确做品牌或产品组合内容时，才同时研究多个产品。

### 2. Collect evidence

优先收集公开、可追溯的材料：用户问题、搜索结果、问答、社区讨论、评论、竞品页面、产品文档和用户提供的真实案例。使用浏览器或网页抓取能力访问来源；来源受限时，记录限制，不用模型记忆补齐。

每条证据记录：

```text
source_url: https://example.com/...
source_title: 页面标题
observed_at: YYYY-MM-DD
evidence_type: user_quote | search_result | competitor_observation | product_fact
excerpt: 原文摘录或准确摘要
```

### 3. Extract and cluster needs

保留用户原话和原始语境，去掉重复表达后按问题聚类。优先识别：

- 高频且具体的任务阻碍；
- 用户已经在使用的替代方案；
- 情绪强、代价清楚的问题；
- 与产品能力直接相关但尚未被满足的问题。

分别标记 `fact`、`user_voice`、`inference`，不能把推断冒充用户需求或市场数据。

### 4. Generate candidate topics

每个选题只表达一个核心观点，并包含：

- 目标用户；
- 用户问题；
- 核心观点；
- 证据来源；
- 产品关联点；
- 标题候选；
- 文章切入角度；
- CTA；
- 风险和证据缺口。

先写清楚事实和用户问题，再使用 `mimeng-writing` 处理标题、情绪和叙事，不要用情绪化标题掩盖证据不足。

### 5. Score and rank

按照 [topic-scoring.md](references/topic-scoring.md) 给候选选题评分。可以运行 `scripts/score_topics.py` 进行加权排序；没有可靠数据的维度必须降低证据分，不得用臆测填满。

### 6. Produce the brief

输出 Markdown 研究简报，默认包含：

```markdown
# 内容选题研究：产品 / 人群 / 日期

## 研究范围
...

## 证据摘要
...

## 推荐选题
### 1. 选题标题
- 总分：x.xx / 5
- 目标人群：...
- 用户问题：...
- 核心观点：...
- 证据：...
- 产品关联：...
- 标题候选：...
- 文章结构：...
- CTA：...
- 风险与待验证项：...

## 不推荐选题
说明证据不足、产品关联弱或合规风险高的原因。

## 下一步验证
列出需要补充的用户访谈、搜索数据或产品事实。
```

## Evidence and safety rules

- 不虚构搜索量、用户数量、收入、转化率、平台能力、教师案例或第三方评价。
- 每个外部事实附来源链接和观察日期；无法访问来源时明确写“未验证”。
- 清楚区分用户原话、事实观察和内容推断。
- 涉及教师副业和收入时，不使用“保证赚钱”“轻松月入”“躺赚”等承诺。
- 涉及试卷时，提示原创性、授权、学校内部资料、答案准确性和个人信息风险。
- 不复制受版权保护的文章、试题或评论；只提取必要的短摘录或摘要。
- 不把单个案例推导成普遍需求；标注样本范围和证据强度。
- 网络不可用时，仍可基于用户提供的材料做初步假设，但必须标记证据边界。
- 研究简报完成后，等待用户确认选题，再进入文章创作或写入内容仓库。

## Product context

四个产品的初始背景和已知边界见 [products-context.md](references/products-context.md)。不要在没有产品事实的情况下补写收益规则、结算比例、用户规模、用户案例或具体功能；需要这些信息时，先向用户索取或标记待验证。

详细约束见：

- [source-guidelines.md](references/source-guidelines.md)
- [products-context.md](references/products-context.md)
