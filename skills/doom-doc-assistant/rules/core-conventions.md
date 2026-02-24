# Doom 框架核心约定

## 文档目录与文件组织

### 文件命名规范

- **格式**: `xxx/xxx.mdx`
- **字符**: 仅允许小写字母、数字、下划线
- **示例**:
  - `deployment_guide.mdx` ✓
  - `Deployment-Guide.mdx` ✗
  - `部署指南.mdx` ✗

### 多语言文档一致性

- 所有语言的目录和文件名完全一致
- 生成的文档链接除语言标识外完全相同

### 排序控制

使用 `weight` 元数据字段控制左侧导航排序

### 目录 index.mdx

每个目录下应包含 index.mdx 文件：

```mdx
# 左导航名称

<Overview />
```

## 静态资源管理

### 两种资源目录

1. **全局静态资源**: `docs/public/`
   - 引用方式: `![](/xxx.png)`
   - 适用于: 全局共享资源

2. **文档专属资源**: `docs/en/<module>/guides/assets/`
   - 引用方式: `![](./assets/xxx.png)`
   - 适用于: 模块或文档专属资源

### 静态资源语言

- 仅提供英文版本
- 无需提供多语言版本

## 图片使用规范

### 图片类型

1. **绘制图例**: 架构图、流程图等
2. **UI 截图**: 界面操作截图

### 使用原则

1. **优先文字描述**: 能用语言描述的 UI 操作优先用文字
2. **截图需登记**: 必须使用截图时向文档团队反馈登记
3. **优先英文版本**: 绘制图例优先提供英文版本

## 链接使用规范

### 站内文档链接

使用相对路径：
```markdown
[文档名称](./module/guides/xxx.mdx)
```

### 章节锚点链接

1. **添加锚点**:
   ```mdx
   ## Hello World {#custom_id}
   ```

2. **引用锚点**:
   ```markdown
   [章节名称](./module/guides/xxx.mdx#custom_id)
   ```

3. **锚点命名**: 仅使用小写字母、数字、下划线

### 跨站点链接

使用 `ExternalSiteLink` 组件：
```mdx
<ExternalSiteLink name="devops" href="/overview/arch.html" children="DevOps 架构" />
```

### 子站点入口

使用 `ExternalSite` 组件：
```mdx
<ExternalSite name="connectors" />
```

### 外部网站链接

优先使用英文版本的链接

## 核心原则

### 英文版本优先

- 优先保证英文版本正确性与可读性
- 内容无法保证多语言时，优先保证英文版本

### 命令行操作优先

- 优先提供命令行操作方式
- 条件允许时同时提供 Web 界面操作

## 引用文档 (Reference)

Doom 框架支持跨仓库内容引用功能：

### 基本语法

在 Markdown 文件中：
```markdown
<!-- reference-start#name -->

<!-- reference-end -->
```

在 MDX 文件中：
```mdx
{/* reference-start#name */}

{/* reference-end */}
```

### 配置方式

在 `doom.config.yaml` 中配置：
```yaml
reference:
  - repo: alauda-public/product-doc-guide
    branch: main
    sources:
      - name: anchor
        path: docs/index.mdx#介绍
        ignoreHeading: false
```

### 重要说明

- 引用远程仓库图片时，静态资源自动存储到 `public/_remotes/<name>` 目录
- 可以将 `*/public/_remotes` 加入 `.gitignore`
- 支持 frontmatterMode 控制元数据合并行为

## 子站点注册

### sites.yaml 配置

```yaml
- name: servicemeshv1
  displayName:
    en: Alauda Service Mesh v1
    zh: Alauda Service Mesh v1
  base: /servicemeshv1
  version: "4.2"
  repo: https://github.com/alauda/asm-docs
```

### 配置字段

- `name`: 子站点唯一标识符
- `displayName`: 中英文显示名称
- `base`: URL 路径前缀
- `version`: 文档版本
- `repo`: 对应的文档仓库地址

## RAG 搜索优化

### 文档块语义连贯

1. **满足规则前提下使用原始 Markdown 语法**
2. **标题要能描述段落含义**
3. **Tab 标签页不能只包含代码，需包含描述**

### queries 字段使用

详见 `rules/metadata-rules.md`

## Document Types & Strategic Objectives

Every document must align with a specific type and objective to ensure clarity and professional standards.

### HowTo Documents (Scenario-Oriented)
- **Objective**: Solve specific problems in real-world scenarios.
- **Characteristics**: 
    - **Scenario-Oriented**: Provides end-to-end solutions.
    - **High Practicality**: Answers "How do I achieve X?" with actionable steps.
    - **Reproducibility**: Users should be able to replicate results by following the guide.
- **Structure**: Title (Verb-first) -> Introduction -> Scenarios -> Prerequisites -> Steps (using `<Steps />`) -> Verification.

### Function Guides (Feature-Oriented)
- **Objective**: Systematically explain what a feature is and how it works.
- **Characteristics**:
    - **Concept-Oriented**: Explains the "What" and "Why" behind a feature.
    - **CLI-First**: Prioritize command-line instructions over UI screenshots.
    - **Systematic**: Focuses on the principles, configuration items, and technical advantages.
- **Difference from HowTo**: Function guides answer "What is it?", while HowTo guides answer "How to do it?".

### Concept Documents (Theory-Oriented)
- **Objective**: Introduce core concepts, parameters, and background theories.
- **Characteristics**:
    - **Detailed Definition**: Clear definitions of technical terms and architectural components.
    - **Consolidation**: Simple concepts can be grouped into one document; complex ones deserve their own.
- **Usage**: Use for in-depth "Understanding XXX" articles.

### Troubleshooting Documents (Solution-Oriented)
- **Objective**: Identify, diagnose, and resolve common issues.
- **Structure**: Problem Description -> Root Cause Analysis -> Solution/Workaround.

## shared 目录约定

`shared` 目录用于存放：
- 公共组件
- 可复用的文档片段
- CRD 定义
- OpenAPI 定义

shared 目录中的内容**不会自动生成文档数据**。
