# Agent Skill 开发最佳实践 (AGENTS.md)

你好，AI 开发助手。当你接手本仓库的 Skill 开发任务时，请必须进行“思维转换（Mindset Shift）”。你不是在开发一个传统的软件系统，而是在为另一个 AI 编写“行为指导手册”。

请严格遵守以下开发最佳实践：

## 1. 声明式优先 (Declarative over Imperative)
* **❌ 错误做法 (传统思维)**：编写一堆 Python 脚本去解析 YAML、读取 Markdown，然后再拼接成一个巨大的 Prompt 字符串发送给大模型。
* **✅ 正确做法 (Agentic 思维)**：在 `SKILL.md` 中用清晰的自然语言告诉执行阶段的 AI：“请使用你的文件读取工具查看 `doom.config.yaml`，从中提取模板配置。” 相信 AI 自身的文本理解能力。

## 2. 避免大文件，拥抱模块化 (Modular Knowledge)
* 不要把几千字的规范全部塞进 `SKILL.md`。这会导致指令混淆，且消耗过多的 Token。
* 将独立的知识点拆分到单独的文件中（例如 `rules/components.md`）。
* 在 `SKILL.md` 的工作流中设置明确的指针。例如：“当用户要求编写功能说明时，**必须首先读取** `rules/style-guides.md` 获取语气规范。”

## 3. 善用原生工具 (Leverage Native Tools)
* 执行这个 Skill 的 AI（如 Claude Code）自带了强悍的终端执行、文件读取和全局搜索工具。
* 在 `SKILL.md` 的指令中，鼓励 AI 使用这些工具。例如：“你需要查询术语时，请使用 `grep -i <keyword> /path/to/terms.yaml` 命令获取官方翻译。”

## 4. 复杂逻辑外包给 MCP (Model Context Protocol)
* 如果你发现某个任务对大模型来说过于复杂（比如需要连接公司内网数据库查数据，或者在十万行的 JSON 中做精确的语义打分推荐）。
* **绝对不要写中间解析脚本**。直接开发一个符合 MCP 标准的轻量级 Server，将该能力暴露为一个 Tool 给 AI 调用。

## 5. 工作流 (Workflow) 必须是线性的
* 在 `SKILL.md` 中定义流程时，使用有序列表（1, 2, 3...）明确先后顺序。
* 要求 AI 在进入下一步之前，必须确认上一步的验证已经通过。例如：“在生成正文前，必须先输出 Frontmatter 元数据供自我检查。”

## 6. 强化“基于例子的学习” (Example-Driven)
* 在编写 `SKILL.md` 时，不要试图用自然语言穷尽解释 `doom` 框架的每一个 React 组件参数。
* **正确做法**：在指令中教导未来的 AI：“当你想使用 Tabs 组件时，请使用你的检索工具，在 `acp-docs` 仓库中运行 `grep -r "<Tabs" .` 找到最近的 3 个使用案例，模仿它们的写法。”
* 这种基于实时代码库的 RAG（检索增强生成）模式，比写死规则要健壮得多。
