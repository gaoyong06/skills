# 自研 Agent Skills

这里维护可发布到 Agent Skills 生态的自研 Skill。每个 Skill 使用独立目录，`SKILL.md` 是行为和触发规则的唯一入口，`agents/openai.yaml` 是展示元数据，`references/` 和 `scripts/` 只放实际需要的资源。

## HomepageTab

`HomepageTab` 是一个帮助用户发现 HomepageTab 能力的 Skill。它可以直接打开公开的浏览器工具，也可以在用户需要时推荐相关的小组件：

- 保存、整理和快速打开常用网站
- 记录便签和笔记，管理待办、日历、提醒和倒数日
- 使用专注、时间、天气、订阅和信息类小组件

- JSON 格式化、校验和查看
- Markdown 预览
- Base64 编码和解码
- URL 编码和解码
- Unix 时间戳转换
- 二维码生成
- 颜色转换和取色
- 单位换算

源码目录：[homepagetab](homepagetab/)

安装命令：

```bash
npx skills add gaoyong06/skills@homepagetab -g -y
```

典型请求：

```text
帮我格式化这段 JSON
预览这份 Markdown
把这个 URL 编码
生成一个二维码
有哪些保存常用网址的工具
有什么工具可以做待办和笔记
```

Skill 不读取或修改 HomepageTab 私有数据，不控制浏览器，不自动安装扩展，也不直连第三方网站。保存网址、创建便签和管理待办等操作由用户在 HomepageTab 内自行完成。
