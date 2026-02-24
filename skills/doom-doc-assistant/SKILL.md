---
name: doom-doc-assistant
description: 自动生成符合 Doom 框架规范的产品文档，支持需求文档转化、架构分析和多类型文档生成
---

# Doom 文档助手

## When to use

当用户请求以下任务时激活本技能：

- **需求文档转化**：用户提供需求文档、PRD 或功能说明，需要转化为面向用户的产品文档
- **文档生成**：创建或编写 Doom 框架产品文档（HowTo、故障排除、功能说明、概念文档等）
- **文档架构分析**：评估现有文档结构是否需要调整、拆分或合并
- **质量评估**：识别并改进现有的低质量文档
- **规范查询**：需要查询 Doom 框架术语、组件使用方法或文档规范

## Instructions

遵循以下工作流程生成符合 Doom 框架规范的文档。

---

## 阶段一：架构分析

### 第一步：读取需求文档

理解用户提供的功能需求或原始文档：

1. 如果用户提供了需求文档内容，仔细阅读并提取核心信息
2. 识别需求范围（简单单一功能 vs 复杂多功能）
3. 明确目标用户群体（运维工程师、开发工程师、管理员等）

### 第二步：分析现有文档结构（⚠️ 关键步骤）

检索目标仓库的文档结构，评估是否需要调整：

1. **多关键词交叉验证**（防止关键词匹配陷阱）：
   ```bash
   # 使用多个相关关键词搜索，交叉验证文档位置
   grep -r "关键词1" /path/to/docs/ --include="*.mdx" -l
   grep -r "关键词2" /path/to/docs/ --include="*.mdx" -l
   grep -r "关键词3" /path/to/docs/ --include="*.mdx" -l
   ```

   **示例**：如果需求是"应用备份"，应该搜索：
   - `backup application` / `application backup`
   - `backup policy` / `backup schedule`
   - `PVC backup` / `volume backup`

   **避免错误**：不要只搜索 `velero` 就断定文档位置，因为 velero 可能在虚拟化（KubeVirt）场景中也有使用。

2. **验证目录功能与需求匹配**：
   - 读取找到的文档，确认其所属功能域是否与需求匹配
   - 检查目录下的其他文档，确认是否属于同一功能模块
   - 对比需求中的产品/模块名称与目录结构

3. **评估现有文档质量**：
   - 是否符合 Doom 规范（文件命名、元数据、结构）
   - 是否过时或需要更新
   - 结构是否清晰，内容是否完整

4. **判断是否需要调整架构**：
   - 需要新建文档还是修改现有文档？
   - 是否需要拆分一篇复杂文档为多篇？
   - 是否需要合并多篇相关文档？

### 第三步：决策执行方案（⚠️ 关键步骤）

根据需求复杂度和现有文档情况，制定执行方案：

#### 3.1 修改 vs 新建决策树

**首先判断是修改现有文档还是新建文档**：

```
需求类型判断：
├─ UI 表单字段增强 / 参数新增 → 修改现有文档
│  └─ 在现有的操作步骤中新增字段说明
├─ 功能模块的全新能力 → 新建文档
│  ├─ 独立功能介绍 → function 文档
│  ├─ 场景化操作指南 → howto 文档
│  └─ 概念解释 → concept 文档
└─ 需求范围判断：
   ├─ 简单单一功能 → 单篇 HowTo 或 Function 文档
   ├─ 复杂多功能 → 拆分为多篇文档（intro + howto + concept）
   └─ 影响现有文档 → 评估是修改/重写/保留
```

#### 3.2 文档结构调整

```
文档结构调整：
├─ 需要新建目录？
├─ 需要调整 weight 排序？
└─ 需要更新 index.mdx 的 Overview？
```

**向用户说明你的分析结果和建议方案，等待确认后再继续。**

### 第四步：确定文档类型

根据需求判断最合适的文档类型：

| 文档类型 | 适用场景 | 模板文件 |
|---------|---------|---------|
| intro | 产品/模块介绍 | intro-template.mdx |
| quickstart | 快速入门指南 | quickstart-template.mdx |
| concept | 核心概念解释 | concept-template.mdx |
| function | 功能特性说明 | function-template.mdx |
| howto | 实用操作指南 | howto-template.mdx |
| troubleshooting | 故障排除 | troubleshooting-template.mdx |
| installation | 安装指导 | installation-template.mdx |
| upgrade | 升级指导 | upgrade-template.mdx |
| arch | 架构设计说明 | arch-template.mdx |

---

## 阶段二：文档生成

### 第五步：读取对应模板

根据确定的文档类型读取模板。模板位于 Skill 内部，使用相对于 SKILL.md 的路径：

```
templates/<文档类型>-template.mdx
```

**可用模板**：
- intro-template.mdx
- quickstart-template.mdx
- concept-template.mdx
- function-template.mdx
- howto-template.mdx
- troubleshooting-template.mdx
- installation-template.mdx
- upgrade-template.mdx
- arch-template.mdx

在模板基础上填充内容，确保结构完整。

### 第六步：按需读取核心规范

规范文件位于 Skill 内部，使用相对于 SKILL.md 的路径：

**必读规范**：

- **rules/metadata-rules.md**
  - 确保生成正确的 Frontmatter 元数据（weight、author、category、queries 等）

- **rules/language-style.md**
  - 遵循语气、用词、用户视角、完整性、简洁性等原则

- **rules/content-elements.md**
  - 正确使用列表、表格、信息标识符、链接、代码块等元素

- **rules/core-conventions.md**
  - 遵循文件命名、静态资源、链接使用、RAG 优化等约定

**按需规范**：

- **rules/mdx-components.md**
  - 使用正确的 Doom 框架组件（Overview、Term、Directive、ExternalSiteLink 等）

- **rules/terminology-guide.md**
  - 正确使用术语和缩略语

- **rules/terminology-consistency.md**
  - 避免造新词，优先使用官方社区术语（Kubernetes 官方文档、OpenShift 文档等）

### 第七步：基于例子的学习

**重要**：不要穷尽记忆所有组件参数。使用 grep 检索真实用例并模仿。

**步骤**：

1. **首先询问用户当前文档仓库的路径**

2. **在用户指定的文档仓库中查找组件使用示例**：
   ```bash
   # 在用户指定的文档仓库中查找组件使用示例
   grep -r "<Tabs" <用户指定的仓库路径> --include="*.mdx" -A 5
   grep -r "<ExternalSiteLink" <用户指定的仓库路径> --include="*.mdx" -A 2
   grep -r "<Directive" <用户指定的仓库路径> --include="*.mdx" -A 3
   grep -r "<Overview" <用户指定的仓库路径> --include="*.mdx" -A 2
   ```

3. **如果用户仓库没有足够示例**，询问用户是否允许从 GitHub 读取开源参考仓库：
   - acp-docs: https://github.com/alauda/acp-docs
   - immutable-infra-docs: https://github.com/alauda/immutable-infra-docs

4. **如果用户允许**，使用工具获取参考仓库内容并搜索

**信任优先级**（当发现规则冲突时）：
- 🥇 **最高**：用户文档仓库的真实用例
- 🥈 **中等**：acp-docs、immutable-infra-docs 等开源参考仓库（需用户授权）
- 🥉 **最低**：Skill 内置的规范文档

### 第八步：检索术语

在生成文档时，对于涉及的关键术语，首先遵循 `rules/terminology-consistency.md` 的规范：

**核心约束**：极力避免造新词，优先使用 Kubernetes 官方文档和 OpenShift 文档中的标准术语。

当遇到官方文档和 OpenShift 文档中都不存在的术语时，**必须提醒用户反复斟酌**。

然后使用 `rules/terminology-guide.md` 中提供的术语表进行对照。

术语表按分类组织，包含完整的术语对照和 badCases：
- **公共术语 (common)**：install、create、procedure、instance、cluster plugin 等
- **AIT 术语**：global cluster、workload cluster、control plane、node、administrator、developer 等
- **ACP 术语**：Application、Helm Chart App、ClusterIP、LoadBalancer、subnet 等
- **Ecosystem 术语**：Single-Primary、Multi-Primary、Redis Sentinel、Redis Cluster 等
- **AI 术语**：Large Language Model、LLM、Inference Service、AI Agent 等

**使用术语的原则**：
1. 优先使用术语表中定义的标准翻译
2. 避免使用 badCases 中列出的不当用法
3. 缩略语首次出现时给出全称
4. 全文保持术语一致性

### 第九步：生成文档

基于以上信息生成完整文档，确保：

#### 1. 元数据完整

```yaml
---
weight: 10
author: "your-email@domain.com"
category: "howto"
queries:
  - how to [task]
  - [task] guide
---
```

#### 2. 结构完整

遵循模板结构，不删除必选节点。

#### 3. MDX 组件正确使用

- 目录页使用 `<Overview />`
- 可替换术语使用 `<Term name="..." textCase="..." />`
- 提示信息使用 `:::tip` 或 `<Directive type="tip" title="...">`
- 外部链接使用 `<ExternalSiteLink name="..." href="..." children="..." />`

**重要约束：避免 `:::` 指令滥用**
- 一篇文档中，`:::` 指令总数不应超过 3-4 个（`:::details` 折叠区块不计入此限制）
- 优先级：DANGER > WARNING > TIP > INFO > NOTE
- 能用普通文本表达的，不要用指令
- 能用加粗或列表表达的，不要用指令
- 参见 `rules/mdx-components.md` 的详细使用原则和正反例

#### 4. 语言风格规范

- 客观陈述，口吻友好
- 避免口语化、行话、成语俗语
- 使用主谓结构，避免长连句
- 提供具体、可执行的操作步骤

#### 5. 链接规范

- 站内文档使用相对路径
- 章节锚点使用 `{#anchor_id}` 格式
- 外部站点使用 `<ExternalSiteLink />` 组件

#### 6. 代码规范

- 行内代码使用反引号，与正文保留空格
- 代码块指定语言类型 ` ```yaml `
- 命令前说明执行环境和工具
- 变量使用 `<>` 标记

### 第十步：自我校验

生成文档后，执行以下检查：

#### 格式检查

- [ ] Frontmatter 元数据是否完整
- [ ] 标题层级是否正确（最多四级）
- [ ] MDX 组件语法是否正确

#### 内容检查

- [ ] 术语使用是否一致（已查询术语表）
- [ ] 是否避免了造新词（已参考官方文档和 OpenShift 文档）
- [ ] **`:::` 指令数量控制**：一篇文档中不超过 3-4 个（details 不计入限制）
- [ ] 操作步骤是否具体可执行
- [ ] 是否包含必要的前提条件和预期结果
- [ ] 是否提供了验证方法

#### 链接检查

- [ ] 相对链接路径是否正确
- [ ] 锚点链接格式是否符合规范
- [ ] 外部链接是否使用了正确组件

#### 语言检查

- [ ] 是否避免了口语化表达
- [ ] 是否保持了全文一致性
- [ ] 是否提供了足够的上下文信息

---

## 重要提示

### 常见错误案例（⚠️ 必读）

以下是在实际使用中发现的典型错误，务必避免：

#### 错误案例 1：关键词匹配陷阱

**错误表现**：
- 需求是"应用备份"功能的 UI 字段增强
- 只搜索了 `velero` 关键词
- 找到了 `virtualization/virtualization/backup_recovery/functions/velero.mdx`
- **错误假设**这是 Velero 的主文档位置

**正确做法**：
- 使用多个相关关键词交叉验证：`backup application`、`backup policy`、`backup schedule`
- 读取找到的文档，确认其功能域（KubeVirt 虚拟化 vs 通用应用备份）
- 检查目录结构，确认文档所属模块

**教训**：单一关键词搜索可能导致误判，必须多关键词交叉验证。

#### 错误案例 2：文档类型误判

**错误表现**：
- 需求是"在 UI 表单中新增 4 个字段"
- 错误判断为"新功能"，建议新建 function 和 howto 两篇文档

**正确做法**：
- 这是**对现有 UI 表单的字段增强**，不是独立的新功能模块
- 应该在现有的 backup-app.mdx 中，新增字段说明
- 不需要新建文档

**教训**：UI 字段增强 ≠ 新功能，要仔细判断是修改现有文档还是新建文档。

#### 错误案例 3：路径假设错误

**错误表现**：
- 没有验证目录用途就直接假设文档位置
- 没有检查目录下其他文档的功能域

**正确做法**：
- 读取目标目录下的 index.mdx 和其他文档
- 确认该目录的功能范围与需求是否匹配
- 必要时对比需求中的产品/模块名称

**教训**：永远不要基于单个文件的路径就断定整个目录的用途。

---

### 核心原则

1. **英文优先**：优先保证英文版本正确性
2. **CLI 优先**：优先提供命令行操作方式
3. **术语一致性**：
   - 极力避免造新词
   - 优先使用 Kubernetes 官方文档和 OpenShift 文档的标准术语
   - 当官方文档中没有对应术语时，必须提醒用户反复斟酌
4. **安全提示**：涉及风险操作时使用 `<Directive type="danger">` 或 `:::danger` 标注
5. **可维护性**：配置建议保存在 ConfigMap，避免硬编码

### 常用术语快速查询

术语已内置在 `rules/terminology-guide.md` 中，按以下分类快速查找：

**集群相关**：
- global cluster → global 集群
- workload cluster → 业务集群
- control plane → 控制平面
- node → 节点

**角色相关**：
- administrator → 管理员
- developer → 开发人员

**应用相关**：
- Application → 原生应用
- OAM Application → OAM 应用
- Helm Chart App → 模版应用

**网络相关**：
- Dual-stack Network → 双栈网络
- Single-stack Network → 单栈网络
- subnet → 子网

**Service 类型**：
- ClusterIP → 虚拟 IP
- NodePort → 主机端口
- LoadBalancer → 负载均衡器

---

## 输出格式

完成文档生成后，按以下格式输出：

```markdown
## 📋 文档分析结果

**需求类型**：[简单/复杂]
**建议文档类型**：[howto/concept/function 等]
**执行方案**：[新建/修改/拆分/合并]

## 📄 生成的文档

[完整的 MDX 文档内容]

## ✅ 校验结果

- [x] 格式检查通过
- [x] 内容检查通过
- [x] 链接检查通过
- [x] 语言检查通过

## 💡 建议

[如有需要调整的架构或内容建议]
```
