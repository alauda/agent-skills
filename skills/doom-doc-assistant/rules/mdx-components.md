# Doom MDX 组件使用手册

## 基础 Markdown 语法

### 加粗
```markdown
**文本**
```

### 斜体
```markdown
*文本*
```

### 标题
```markdown
# 一级标题
## 二级标题
### 三级标题
#### 四级标题
```

### 图片
```markdown
![图片名称](图片路径)
```

### 行内代码
```markdown
正文 `inline code` 正文
```

**注意**: 标记与正文之间需保留空格

### 列表

**无序列表**:
```markdown
- 列表项 1
- 列表项 2
```

**有序列表**:
```markdown
1. 列表项 1
2. 列表项 2
```

## 自定义容器

### ::: 语法

```mdx
:::tip
这是提示信息
:::

:::info
这是说明信息
:::

:::warning
这是注意信息
:::

:::danger
这是警告信息
:::

:::note
这是注释信息
:::

:::details
这是详情信息
:::

:::tip 自定义标题
这是带标题的提示
:::
```

### Directive 组件

当 `:::` 语法在列表或其他组件中无法使用时，使用 Directive 组件：

```mdx
<Directive type="tip" title="自定义标题">
这是提示内容
</Directive>

<Directive type="info" title="说明">
这是说明内容
</Directive>

<Directive type="warning" title="注意">
这是注意事项
</Directive>

<Directive type="danger" title="警告">
这是警告内容
</Directive>
```

### 类型适用性

| 类型 | 颜色 | 适用场景 |
|-----|------|---------|
| NOTE | 灰色 | 补充非关键信息，帮助理解背景，不影响主要任务执行 |
| TIP | 绿色 | 实用建议和优化技巧，提升任务效率或使用体验 |
| INFO | 蓝色 | 中立且重要信息，如关键细节或背景知识，无警示意味 |
| WARNING | 黄色 | 潜在风险提醒，需谨慎操作，帮助预防问题，风险通常不严重 |
| DANGER | 红色 | 严重风险警告，可能导致不可逆后果，需立即关注并小心处理 |

### 使用原则（重要）

**避免指令滥用**：过多的 `:::` 指令会导致"警报疲劳"，降低用户对真正重要信息的关注度。

**核心约束**：
1. **一篇文档中，`:::` 指令总数不应超过 3-4 个**
2. **优先级原则**：DANGER > WARNING > TIP > INFO > NOTE
3. **能用普通文本表达的内容，不要用指令**
4. **能用简单格式（加粗、列表）表达的，不要用指令**

**使用前自检**：
- 这条信息真的需要特殊视觉强调吗？
- 如果去掉指令，用加粗或列表是否足够？
- 文档中是否已经有多个类似的指令了？

**可接受的替代方案**：
- 使用 **加粗文本** 强调关键词
- 使用无序列表列举要点
- 使用普通段落陈述背景信息
- 将次要内容放入 `:::details` 折叠区块（不计入上述 3-4 个限制）

**反例**：
```mdx
:::note
本文档介绍数据库部署流程。
:::

:::info
部署前需要准备配置文件。
:::

:::tip
建议使用 YAML 格式配置。
:::

:::warning
配置文件路径必须正确。
:::

部署完成。
:::tip
可以使用 kubectl 验证。
:::
```
❌ 一篇文档中有 5 个指令，过多。

**正例**：
```mdx
本文档介绍数据库部署流程。**部署前需要准备配置文件**，建议使用 YAML 格式。

:::warning
配置文件路径必须正确，否则部署将失败。
:::

部署完成后，可以使用 `kubectl get pods` 验证服务状态。

:::tip
如需查看详细日志，可使用 `kubectl logs` 命令。
:::
```
✅ 只保留 2 个指令，其他信息用普通文本或加粗表达。

## 代码块

### 基本使用

````markdown
```js title="hello.js"
console.log('Hello World');
```
````

### 代码行高亮

````markdown
```js {1,3-5}
console.log('Hello World');
const a = 1;
console.log(a);
```
````

## Doom 框架组件

### Overview - 文档概览

**用途**: 展示文档目录

**使用场景**: 目录页 index.mdx

```mdx
# 架构

<Overview />
```

### Term - 术语组件

**用途**: 标记可替换术语，动态挂载注入

**语法**:
```mdx
<Term name="company" textCase="capitalize" />
<Term name="product" textCase="lower" />
<Term name="productShort" textCase="upper" />
```

**参数**:
- `name`: 术语标识名
  - `company`: 公司品牌
  - `product`: 产品品牌
  - `productShort`: 产品品牌简称
  - `alaudaCloudLink`: Alauda Cloud 链接
- `textCase`: 大小写转换
  - `lower`: 小写
  - `upper`: 大写
  - `capitalize`: 首字母大写

### TermsTable - 术语表

**用途**: 展示内置术语列表

```mdx
<TermsTable />
```

### ExternalSite - 外部站点引用

**用途**: 引用外部站点入口

```mdx
<ExternalSite name="connectors" />
```

### ExternalSiteLink - 外部站点链接

**用途**: 引用外部站点的具体文档

```mdx
<ExternalSiteLink name="connectors" href="link.mdx#hash" children="Content" />
```

**重要**: 使用 `children` 属性传递文本，避免渲染在 `p` 元素内

### AcpApisOverview / ExternalApisOverview - API 概览

**用途**: 引用外部站点 API 概览

```mdx
<AcpApisOverview />
<ExternalApisOverview name="connectors" />
```

### JsonViewer - JSON 查看器

**用途**: 展示 JSON 数据

```mdx
<JsonViewer value={{ key: 'value' }} />
```

## 多 Tab 页签

```mdx
<Tabs>
  <Tab label="Tab 1">
    Tab 1 content
  </Tab>
  <Tab label="Tab 2">
    Tab 2 content
  </Tab>
</Tabs>
```

## 可视化步骤

```mdx
<Steps>
### 第 1 步

步骤 1 的正文

### 第 2 步

步骤 2 的正文
</Steps>
```

## 自定义标题锚点

```mdx
## Hello World {#custom_id}

[章节名称](./module/guides/xxx.mdx#custom_id)
```

## Front Matter

```yaml
---
title: Hello world
---
```

访问 Front Matter 属性：
```mdx
---
title: Hello world
---

# {frontmatter.title}
```

## 基于例子的学习

详细的"基于例子的学习"工作流请参见 SKILL.md 的第七步。

**简要说明**：
- 不要穷尽解释所有组件参数
- 优先在用户文档仓库中查找真实用例并模仿
- 参见 SKILL.md 中的完整步骤和信任优先级

## 参考文档

- [Doom Markdown 文档](https://doom.alauda.cn/usage/markdown.html)
- [Rspress 内置组件](https://rspress.dev/guide/default-theme/components)
