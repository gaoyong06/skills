# Source Guidelines

## Source priority

优先级从高到低：

1. 用户提供的真实反馈、访谈记录和产品数据；
2. 可追溯的公开问答、论坛、评论和搜索结果；
3. 竞品官网、产品页面和公开文档；
4. 行业报告和媒体文章；
5. 模型推断，仅可作为待验证假设。

## Source record

每条来源至少记录：

```yaml
url: https://example.com/page
title: Page title
observed_at: 2026-08-05
type: user_quote
excerpt: "准确的短摘录或忠实摘要"
scope: "该来源代表谁，样本有什么限制"
```

## Search limitations

如果页面、搜索引擎或社区需要登录、反爬或无法访问：

- 记录 URL 和失败原因；
- 不把页面标题或搜索摘要当作完整证据；
- 不用其他来源猜测缺失内容；
- 在简报中列为“待验证项”。

## Content boundaries

外部文章、用户原话和评论保持原意，不大段复制。对外发布前检查版权、商标、个人信息、学校内部资料和试卷授权问题。
