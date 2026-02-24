# 术语一致性规范

## 核心原则

### 避免造新词

在开源软件的上下文中，极力避免创造新词或使用非标准术语。凡是官方社区（如 Kubernetes、CNCF、相关开源项目）已有的术语或专用词汇，应当使用官方社区的术语。

### 官方术语优先级

1. **Kubernetes 官方文档**：优先使用 Kubernetes.io 官方文档中的术语
2. **CNCF 生态术语**：参考 CNCF 托管项目的官方用词
3. **相关开源项目**：参考具体技术栈的官方文档
4. **OpenShift 文档**：作为容器平台术语的补充参考

## 术语验证流程

在生成文档时，如果遇到不确定的术语翻译或用词：

### 1. 优先查询官方文档

使用以下命令在官方文档仓库中搜索术语：

```bash
# Kubernetes 官方文档
curl -s "https://kubernetes.io/docs/search/?q=<keyword>" | grep -o '<title>[^<]*</title>'

# 或使用 GitHub 搜索
gh repo search kubernetes/website "<keyword>"
```

### 2. 检查 OpenShift 文档

OpenShift 文档对 Kubernetes 术语有成熟的中文翻译规范：

```bash
# OpenShift 文档搜索
curl -s "https://docs.openshift.com/container-platform/4.15/search.html?q=<keyword>"
```

### 3. 当术语在官方文档和 OpenShift 文档中都不存在时

**必须提醒用户反复斟酌**：

> ⚠️ **术语确认提醒**
>
> 在生成文档时发现以下术语未在 Kubernetes 官方文档或 OpenShift 文档中找到标准翻译：
>
> - [术语列表]
>
> 请确认：
> 1. 是否确实需要使用此术语
> 2. 是否有官方社区的标准术语可以替代
> 3. 如果是新概念，是否需要先在社区讨论标准用词

## 常见问题术语示例

### 已有官方标准翻译的术语

| 英文 | Kubernetes 官方 | OpenShift | 禁止使用 |
|------|----------------|-----------|----------|
| Pod | Pod（保持原文） | Pod | 容器组 |
| Namespace | Namespace | 命名空间 | 空间、名空间 |
| Deployment | Deployment | Deployment | 部署件 |
| Cluster | Cluster | 集群 | 群集 |
| Node | Node | 节点 | 节点机、主机 |

### 需要特别注意的术语

以下术语在 Kubernetes 官方文档中保持英文，**不要自行翻译**：

- Pod
- Deployment
- Service
- Ingress
- Namespace
- Container
- ReplicaSet
- StatefulSet
- DaemonSet

## 生效范围

本规范适用于：
- 所有用户可见的文档内容
- UI 界面文本
- 错误消息和提示信息
- API 文档

## 豁免情况

以下情况可以不严格遵循本规范：
1. 内部代码注释（不影响用户体验）
2. 临时调试信息（不会进入正式版本）
3. 明确标注为"非官方翻译"的内容（需说明原因）
