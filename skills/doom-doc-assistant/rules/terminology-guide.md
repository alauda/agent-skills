# Terminology Guide

## Terminology Categories

Terms in the Doom framework are categorized into three types:

1. **Replaceable Terms**: Use the `<Term />` component (dynamic replacement).
2. **Fixed Terms**: Standard technical translations; use as-is.
3. **Heading Terms**: Standardized terms for document titles and navigation.

## Replaceable Terms

### Usage
Used for brand or product names that may vary across environments.

```mdx
<Term name="company" textCase="capitalize" />
<Term name="product" textCase="lower" />
```

### Available Keys

| name | en | zh (Ref) | Description |
| :--- | :--- | :--- | :--- |
| company | Alauda | 灵雀云 | Brand name |
| product | Alauda Container Platform | 灵雀云容器平台 | Product brand |
| productShort | ACP | ACP | Short brand name |

## Fixed Terms

### Common Terms (common)

| en | zh (Ref) | Description |
| :--- | :--- | :--- |
| install | 安装 | Installing Operators, plugins, or products. |
| create | 创建 | Creating instances, apps, or resources. |
| procedure | 操作步骤 | Standardized heading for actionable steps. |
| cluster plugin | 集群插件 | Add-ons for the cluster. |
| instance | 实例 | A running instance of a service or app. |
| architecture | 架构 | Cluster or service architecture (e.g., Primary-Replica). |
| parameter | 参数 | Configuration inputs. |
| audit | 审计 | Kubernetes security audit logs. |
| log | 日志 | Container and system logs. |
| credential | 凭证 | Authentication information. |
| overcommit ratio | 超售比 | Resource overcommitment ratio. |

### AIT Terms (ait)

| en | zh (Ref) | Description |
| :--- | :--- | :--- |
| global cluster | global cluster | Management cluster (recommended with `global` style). |
| workload cluster | workload cluster | Clusters where business workloads run. |
| Bare Metal | Bare Metal | Installing K8s directly on physical machines.<br/><br/>**Hyphenation Rule**:<br/>- Use `Bare Metal` (no hyphen) as a proper noun or feature name.<br/>- Use `bare-metal` (hyphenated) as an attributive adjective before a noun: `a bare-metal server`.<br/>- Use `bare metal` (no hyphen) in predicative position: `the server is bare metal`. |
| control plane | control plane | Kubernetes components running on management nodes. |
| node | node | Generic term for cluster nodes (avoid master/slave). |
| administrator | administrator | System or platform admin. |
| developer | developer | Application developer. |
| release notes | release notes | List of updates and fixes. |
| Dual-stack Network | Dual-stack Network | Support for both IPv4 and IPv6.<br/><br/>**Hyphenation Rule**:<br/>- Use `Dual-stack Network` (capitalized) as a feature name.<br/>- Use `dual-stack` (lowercase, hyphenated) as an attributive adjective: `dual-stack networking`.<br/>- Use `dual stack` (no hyphen) in predicative position: `the network is dual stack`. |
| OperatorHub | OperatorHub | Web console to discover and install Operators. |

### ACP Terms (acp)

| en | zh (Ref) | Description |
| :--- | :--- | :--- |
| Application | Application | Native K8s resources (Workloads, Services, etc.). |
| Helm Chart App | Helm Chart App | Apps deployed via Helm templates. |
| ClusterIP | Virtual IP | Internal service IP. |
| NodePort | Host Port | External access via host port. |
| LoadBalancer | LoadBalancer | External access via load balancer. |
| ALB | ALB | Alauda LoadBalancer. |
| subnet | subnet | Network subnets (Kube-OVN, Calico). |

### Ecosystem Terms (ecosystem)

| en | zh (Ref) | Description |
| :--- | :--- | :--- |
| Single-Primary | Single-Primary | MGR mode. |
| Multi-Primary | Multi-Primary | MGR mode. |
| Redis Sentinel | Redis Sentinel | Redis high availability mode. |
| Redis Cluster | Redis Cluster | Redis distributed mode. |
| Master | Master | Redis official term (confirm context before use). |
| Replica | Replica | Redis official term. |

### AI Terms (ai)

| en | zh (Ref) | Description |
| :--- | :--- | :--- |
| Large Language Model | LLM | Large-scale AI model trained on text data. |
| Inference Service | Inference Service | Providing predictions from a trained model. |
| AI Agent | AI Agent | Autonomous entity perceiving environment and taking actions. |
| Training | Training | Process of training a model with data. |

## Quick Reference Table

| Global Terms | Local Equivalents |
| :--- | :--- |
| **global cluster** | Management Cluster |
| **workload cluster** | Business Cluster |
| **control plane** | K8s Control Plane |
| **Application** | Native App |
| **Helm Chart App** | Template App |
| **subnet** | Subnet |

## Standardized Heading Terms

| Heading Name | Description |
| :--- | :--- |
| **Overview** | Directory overview |
| **Introduction** | High-level intro |
| **Architecture** | System architecture |
| **Quick Start** | Fast-track guide |
| **Install** | Installation guide |
| **Upgrade** | Upgrade guide |
| **Features** | Feature list |
| **Concepts** | Core concepts |
| **HowTo** | Scenario guides |
| **Trouble Shooting** | Issue resolution |

## Usage Principles

1. **No Inventing**: Never create custom abbreviations.
2. **Full Name First**: Provide the full name on first mention: `OIDC (OpenID Connect)`.
3. **Consistency**: Ensure the same term is used throughout the documentation.
4. **Avoid Bad Cases**: Check `terminology-consistency.md` for prohibited terms.
