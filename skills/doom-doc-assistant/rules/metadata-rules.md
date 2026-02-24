# Frontmatter 元数据规范

## 基础元数据（必填）

所有 Doom 框架文档必须包含以下基础元数据：

```yaml
---
weight: 10
author: "your-email@domain.com"
category: "howto"
---
```

### weight - 排序权重

- **用途**: 控制文档在左侧导航中的显示顺序
- **规则**:
  - 权重越小越靠前
  - 支持小数形式（如 15.1）
  - 同目录下文档按权重排序

### author - 文档作者

- **格式**: 用户邮箱地址
- **用途**: 标识文档所有者，便于后续自动化通知

### category - 文档类型

可选值及适用场景：

| category | 文档类型 | 使用场景 |
|----------|---------|---------|
| `index` | 目录 | 目录页 index.mdx |
| `introduction` | 介绍文档 | 产品/模块介绍 |
| `feature` | 功能说明 | 功能特性说明 |
| `releasenote` | 发版说明 | 版本更新记录 |
| `architecture` | 架构文档 | 架构设计说明 |
| `concept` | 概念文档 | 核心概念解释 |
| `quickstart` | 快速开始 | 快速入门指南 |
| `howto` | 实用指南 | HowTo 文档 |
| `troubleshooting` | 问题处理 | 故障排除文档 |
| `permissions` | 权限说明 | 权限配置说明 |
| `api` | API 参考 | API 接口文档 |

## RAG 优化元数据（推荐）

为提升智能文档 RAG 搜索效果，添加 queries 字段：

```yaml
---
queries:
  - how to install ACP
  - how to install ACP Core and global cluster
  - ACP installation guide
---
```

### queries 编写规则

1. **用户视角**: 站在用户角度，列出可能提出的问题
2. **英文编写**: 统一使用英文
3. **数量适中**: 3 个左右最佳
4. **覆盖主题**: 能涵盖文档主题内容
5. **避免重复**: 不同文档 queries 应有所区分

### queries 编写示例

**好的示例**：
```yaml
queries:
  - how to deploy application on ACP
  - application deployment guide
  - create and deploy workloads
```

**不好的示例**：
```yaml
# 太少
queries:
  - deployment

# 太多
queries:
  - deploy
  - deployment
  - how to deploy
  - deployment guide
  - create deployment
  - application deployment
```

## 文档标题与元数据关系

- **默认行为**: 使用正文中的一级标题作为导航标题
- **自定义标题**: 在 Frontmatter 中设置 `title` 字段

```yaml
---
title: "Custom Navigation Title"
---

# Actual Document Title
```

## 元数据完整示例

### HowTo 文档示例
```yaml
---
weight: 30
author: "developer@domain.com"
category: "howto"
queries:
  - how to scale database
  - database scaling guide
  - expand database capacity
---
```

### 故障排除文档示例
```yaml
---
weight: 50
author: "ops@domain.com"
category: "troubleshooting"
queries:
  - pod crashloopbackoff error
  - troubleshoot pod crashes
  - container restart issues
---
```

### 架构文档示例
```yaml
---
weight: 20
author: "architect@domain.com"
category: "architecture"
queries:
  - cluster architecture overview
  - ACP platform architecture
  - multi-cluster architecture
---
```

## RAG 搜索优化建议

### 文档块语义连贯

智能文档使用 markdown header 标签切分长文档，因此：

1. 满足规范前提下，尽量使用 markdown 原始语法编写文档
2. `#` 标签的标题要能最直接描述文档段落含义
3. `#` 标签的段落、`<Tab>` 标签页中不能只包含代码，需同时包含描述
