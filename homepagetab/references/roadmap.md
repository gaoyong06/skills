# HomepageTab Skill 产品路线图

本文档规划的是 HomepageTab Skill 的能力演进，不替代 HomepageTab Web、浏览器扩展或服务端本身的产品路线图。每个阶段都要以前一阶段的真实使用数据和安全边界为前提，不因“AI 能做”而扩张范围。

## 产品定位

HomepageTab Skill 是 HomepageTab 工具的 AI 入口：用户用自然语言描述任务，Skill 帮他找到合适的交互式工具并打开。首要价值是减少寻找工具和切换页面的成本，而不是接管用户的浏览器或个人数据。

## 阶段总览

| 阶段 | 状态 | 核心能力 | 进入条件 |
| --- | --- | --- | --- |
| MVP · 工具发现 | 当前实施 | 识别任务、打开 8 个公开工具、安装引导、安全边界 | 工具深链稳定，Skill 包通过校验 |
| D0 · 发布与发现 | 紧随 MVP | 公开仓库、搜索关键词、跨 Skill 交接、安装说明和来源追踪 | 仓库已发布，`npx skills find` 能检索到 Skill |
| P1 · 安全预填 | 规划中 | 对 JSON、Markdown、Base64、URL 等内容进行用户确认后的有限预填 | Web 版提供稳定预填协议和长度限制 |
| P2 · 确认后保存 | 远期 | 创建便签、待办、倒数日、常用网址 | OAuth / MCP、细粒度权限、撤销和审计完成 |
| P3 · 生态入口 | 远期 | 工具目录、组件能力声明、第三方 Agent 调用 | 公共 Agent API、组件安全模型和治理机制完成 |

## MVP：工具发现

### 功能清单

- 自然语言识别以下 8 类工具：JSON、Markdown、Base64、URL、时间戳、二维码、颜色、单位换算。
- 生成 `web.homepagetab.com` 的 `#open=` 深链。
- 链接附带 `utm_source=skills`，用于聚合统计 Skill 带来的访问和安装转化。
- 无法判断时回退到工具箱入口，不生成猜测性链接。
- 用户明确需要长期使用时，提供 Chrome、Edge、Firefox 安装链接。
- 对隐私、远程代码、浏览器控制和第三方访问保持明确边界。

### MVP 不做

- 不把对话内容写入链接。
- 不读取本地文件、剪贴板、书签、历史记录或 HomepageTab 私有数据。
- 不自动安装扩展，不修改新标签页或搜索引擎。
- 不调用私有 API，不保存设备 ID、Cookie、Token 或 API Key。

### MVP 验收

- 八个工具 ID 均能被 Skill 识别并生成合法深链。
- 无效工具 ID 会被拒绝，而不是生成不可用链接。
- 工具深链在 Web 版打开后能进入对应工具。
- Skill 文档不承诺未实现的预填、保存或浏览器自动化能力。

## D0：发布与发现

Skill 的发现不是 HomepageTab 自动注册出来的，而是依赖公开仓库、稳定的 `SKILL.md` 元数据和可被检索的任务关键词。D0 只优化可发现性，不扩张产品权限。

### 发布清单

- 使用稳定的 GitHub 仓库和 Skill slug：`homepagetab`；展示名称保持 `HomepageTab`。
- `SKILL.md` 描述同时覆盖品牌词、工具词和任务词：JSON formatter、Markdown preview、Base64、URL encoder、timestamp、QR code、color picker、unit converter、developer tools、web utilities。
- 保持 model-invoked 形态，使其他 Agent 能根据任务描述交接给 `$homepagetab`。
- 在仓库 README 提供安装命令、工具列表、典型示例和公开 Web 版链接。
- 发布后使用多个搜索词验证，而不是只搜索品牌名：`HomepageTab`、`JSON formatter`、`Markdown preview`、`Base64 encoder`、`QR code generator`、`developer browser tools`。
- 工具链接保留 `utm_source=skills`，只用于聚合访问和安装转化，不记录对话正文或敏感内容。

### D0 验收

- `npx skills find` 能通过品牌词和至少 3 个任务词检索到 `homepagetab`。
- 从公开仓库全新安装后，Skill 目录包含可校验的 `SKILL.md`、元数据、工具清单和链接脚本。
- 其他 Skill 可以根据“预览 Markdown”“格式化 JSON”等任务将工作交接给 `$homepagetab`。
- 不因关键词扩展而匹配私有数据、浏览器控制或自动安装类请求。

`skills.sh` 的线上索引、排序和安装参数以发布时的 CLI 与站点行为为准；本地无法联网时，不把搜索结果或安装量当作已验证事实。

## P1：安全预填

### 目标

减少用户打开工具后的复制粘贴步骤，但仍让用户掌握数据是否进入链接。

### 前置能力

- Web 版正式定义预填参数和版本化协议。
- 预填数据只进入 URL fragment，不发送给 HomepageTab 服务端。
- 每个工具定义最大长度、允许字符和清理规则。
- Skill 在生成前明确提示：内容会出现在聊天记录、浏览器历史和复制链接中。

### 首批候选

1. JSON Viewer：预填待查看 JSON。
2. Markdown Preview：预填短 Markdown 文本。
3. Base64 Tool：预填短文本。
4. URL Encode Tool：预填 URL 或查询字符串。

二维码、颜色和单位换算不优先做文本预填，优先使用工具自身输入控件，避免链接过长和格式歧义。

## P2：确认后保存

这是产品能力扩展，不是简单的 Skill 文案升级。必须先建设正式 Agent API 或 MCP：

- OAuth 或设备授权，不使用隐式登录状态。
- `notes:write`、`todos:write`、`bookmarks:write` 等细粒度 scope。
- 创建、更新、删除均要求用户确认；支持撤销或回滚。
- 请求幂等、错误可解释、操作可审计。
- 明确数据保留、删除和跨设备同步规则。

首批可评估动作：

- “把这段内容保存为便签”。
- “创建一个下周五的待办”。
- “把这几个网址整理到常用网站”。

在上述基础设施完成前，Skill 只提供对应工具或 Web 版入口，不模拟保存成功。

## P3：生态入口

长期方向是让 HomepageTab 成为可被 Agent 发现和调用的工具生态：

- 公开工具能力目录和版本信息。
- 每个组件声明输入、输出、权限和副作用。
- 第三方组件使用受限权限和审核后的能力描述。
- 支持工具组合，但每一步都要有明确输入输出和失败处理。
- 只记录聚合指标，不收集对话正文或敏感内容。

## 指标与复盘

MVP 只观察与核心价值直接相关的指标：

- 工具链接点击率。
- 各工具打开占比。
- 工具打开后有效交互率（由 HomepageTab 侧聚合统计，避免 Skill 读取用户内容）。
- Skill 带来的扩展安装转化率。
- 无效深链率、用户纠错率和隐私相关反馈。

不要用“调用次数”单独判断成功；如果用户打开了错误工具，调用量反而会掩盖问题。每个阶段结束前，先复盘正确匹配率、错误边界和用户反馈，再决定是否进入下一阶段。
