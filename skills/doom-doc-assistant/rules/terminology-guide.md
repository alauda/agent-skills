# 术语使用指南

## 术语分类

Doom 框架文档中的术语分为三类：

1. **可替换术语**: 需使用 `<Term />` 组件标记，动态替换
2. **固定术语**: 直接使用标准翻译，无需特殊标记
3. **标题术语**: 专用于文档标题命名

## 可替换术语

### 使用场景

品牌名称、产品名称等需要在不同环境替换的术语

### 使用方法

```mdx
<Term name="company" textCase="capitalize" />
<Term name="product" textCase="lower" />
<Term name="productShort" textCase="upper" />
```

### 可用术语

| name | en | zh | 说明 |
|-----|----|----| ---- |
| company | Alauda | 灵雀云 | 公司品牌 |
| product | Alauda Container Platform | 灵雀云容器平台 | 产品品牌 |
| productShort | ACP | ACP | 产品品牌简称 |
| alaudaCloudLink | [Alauda Cloud](https://cloud.alauda.io) | [Alauda Cloud](https://cloud.alauda.cn) | 链接 |

## 固定术语

以下是常用术语的标准翻译，请严格按照此表使用：

### 公共术语 (common)

| en | zh | badCases (en/zh) | 说明 |
|----|----|------------------|------|
| install | 安装 | - | 安装 Operator/安装集群插件/产品 |
| create | 创建 | - | Create Operator Backed App，创建模版应用、创建实例 |
| procedure | 操作步骤 | en: Steps, Operation Steps | OCP 也使用 Procedure，AI 建议专业些 |
| cluster plugin | 集群插件 | - | 集群插件 |
| operator | operator | - | - |
| product | 产品 | - | - |
| view | 视图 | en: perspective / zh: 卡片 | ACP 的 UI 设计，常用在功能在 UI 位置的描述 |
| customer portal | customer portal | - | 在产品中遇到故障时，文案提示会引导至 Customer Portal |
| instance | 实例 | - | 通常指一个运行中的应用或服务，包含多个资源（SVC、PVC、secret、Pod 等） |
| architecture | 架构 | - | 组成一个集群服务的架构类型，常见的集群架构有：主从、多主、分布式、哨兵 |
| parameter | 参数 | - | 参数用于控制应用或服务以什么样的值进行工作 |
| Helm Chart | Helm Chart | - | 应用模板（Helm Chart）为一个描述 Kubernetes 相关资源的文件集合 |
| audit | 审计 | - | 平台对接了 Kubernetes 审计，提供了安全相关的时序操作记录 |
| log | 日志 | - | 平台对接了 Kubernetes 的日志，能够快速采集 Kubernetes 集群的容器日志 |
| token | 令牌 | - | 系统颁发给用户的令牌，承载了用户的身份、权限等信息 |
| credential | 凭证 | - | 系统登录认证信息 |
| Virtual GPU / vGPU | 虚拟 GPU | - | vGPU（虚拟GPU）是指通过虚拟化技术将物理GPU资源分割并分配给多个虚拟机的技术 |
| Physical GPU / pGPU | 物理 GPU | - | pGPU（直通GPU）是指将物理主机上的整块GPU卡直接挂载到虚拟机上使用的技术 |
| overcommit ratio | 超售比 | - | 集群、命名空间超售比 |

### AIT 术语 (ait)

| en | zh | badCases (en/zh) | 说明 |
|----|----|------------------|------|
| Alauda | Alauda | zh: 平台自研 | 专有名词，公司名，用在 Operator 来源、子产品 Title、插件名称等地 |
| Curated | Curated | en: Certify / zh: 平台认证 | 特指 OperatorHub 中，Operator 的 source 分类 |
| Community | Community | - | 特指 OperatorHub 中，Operator 的 source 分类 |
| Marketplace | Marketplace | - | 特指 OperatorHub 中，Operator 的 source 分类 |
| global cluster | global 集群 | en: Management Cluster / zh: 管理集群 | 特指 global 集群，文档中建议添加样式 `global` cluster |
| workload cluster | 业务集群 | en: business cluster | - |
| Infrastructure Provisioning Model | Infrastructure Provisioning Model | - | 用来描述基础设施是谁提供 |
| Platform-Provisioned | Platform-Provisioned | - | 当集群的 OS 由我们提供，比如 DCS 集群，HCS 集群 |
| User-Provisioned | User-Provisioned | - | 同 Platform-Provisioned |
| Bare Metal | 裸金属 | - | 常用在描述需要直接在物理机上安装 Kuberenetes 的场景 |
| Kubernetes Provider | Kubernetes Provider | zh: 接入集群、注册集群、公有云集群 | 用来区分 Kubernetes 由谁提供 |
| Management Mode | Management Mode | - | 用来描述其他供应商怎么托管在平台 |
| control plane | 控制平面 | en: master | 运行在 master 节点的 kubernetes 组件 |
| node | 节点 | en: slave node, master node | 不再使用控制节点、计算节点这种描述 |
| administrator | 管理员 | zh: 平台管理员 | 专有名词，特指管理员 |
| developer | 开发人员 | zh: 业务人员 | 专有名词，特指开发人员 |
| release notes | release notes | zh: 更新列表、更新说明、发版说明 | 建议不翻译，约定俗成 |
| Dual-stack Network | 双栈网络 | zh: 双栈 | 指同时支持IPv4和IPv6的网络环境 |
| Single-stack Network | 单栈网络 | - | 指仅支持单一IP协议(IPv4或IPv6)的网络环境 |
| IPv4 | IPv4 | en: ipV4, ipv4, Ipv4 | 专有名词 |
| IPv6 | IPv6 | en: ipV6, ipv6, Ipv6 | 专有名词 |
| alert | 告警 | - | 告警 |
| dashboard | 监控面板 | - | 监控面板 |
| panel | 图表 | - | 图表 |
| metric | 指标 | - | 指标 |
| indicator | 内置指标 | - | 内置指标 |
| OperatorHub | OperatorHub | en: Operator Hub / zh: Operator Hub | OperatorHub 是平台管理员用来发现和安装 Operator 的 Web 控制台界面 |
| LDAP | LDAP | - | 专有名词，是一种成熟、灵活且受良好支持的与目录服务器交互的标准机制 |
| OIDC | OIDC | en: OpenId Connect / zh: OpenId Connect | 专有名词，OIDC（OpenId Connect）是基于 OAuth 2.0 协议的身份认证标准协议 |
| Identity Provider | Identity Provider | - | 专有名词，身份提供者 |
| IDP | IDP | - | Identity Provider 的缩写 |
| role | 角色 | - | 角色是操作权限的集合 |
| region | 地域 | - | 地理区域，地域之间故障完全隔离 |

### ACP 术语 (acp)

| en | zh | 说明 |
|----|----|------|
| OAM Application | OAM 应用 | OAM 应用 |
| Application | 原生应用 | 特指原生应用，由一个或多个关联的计算组件（Workloads）、内部路由（Services）等 Kubernetes 原生资源构成 |
| Custom Application | 自定义应用 | 自定义应用 |
| Helm Chart App | 模版应用 | 模版应用 |
| HR | HR | 模版应用缩写 |
| ClusterIP | 虚拟 IP | 虚拟 IP |
| NodePort | 主机端口 | 主机端口 |
| LoadBalancer | 负载均衡器 | 负载均衡器 |
| LB | LB | 负载均衡器缩写 |
| Alauda LoadBalancer | ALB | ALB 全称 |
| ALB | ALB | ALB |
| Upload Packages | 上架软件包 | 上架软件包 |
| Fully Qualified Domain Name | 全域名 | 管理员通过域名管理功能，可统一管理用于本平台的企业网络域名资源 |
| FQDN | FQDN | Fully Qualified Domain Name 的缩写 |
| Wildcard Domain | 泛域名 | 泛域名 |
| subnet | 子网 | 子网，支持为使用 Kube-OVN、Calico 容器网络模式的集群划分并管理子网资源 |

### Ecosystem 术语 (ecosystem)

| en | zh | 说明 |
|----|----|------|
| Single-Primary | 单主模式 | 主 = Primary 适用于 MGR。但如果从数据复制角度，Source and Replicas |
| Multi-Primary | 多主模式 | 主 = Primary 适用于 MGR。但如果从数据复制角度，Source and Replicas |
| Redis Sentinel | 哨兵模式 | 哨兵模式 |
| Redis Cluster | 集群模式 | 集群模式 |
| Master | 主节点 | Redis 官方用法。用于其他用途时，需二次确认 |
| Replica | 从节点 | Redis 官方用法。用于其他用途时，需二次确认 |
| Partition | 分区 | 分区 |
| Message Retention Period | 消息保留时长 | 消息保留时长 |
| Consumer Group | 消费者组 | 消费者组 |
| Lag | 堆积量 | 堆积量 |

### AI 术语 (ai)

| en | zh | 说明 |
|----|----|------|
| Large Language Model | 大语言模型 | LLM（Large Language Model，大语言模型）是一种基于海量文本数据训练的人工智能模型 |
| LLM | LLM | Large Language Model 的缩写 |
| Inference Service | 推理服务 | Inference Service（推理服务）是指在机器学习或深度学习领域，为训练好的模型提供高性能、可扩展的预测或推理功能的服务 |
| AI Agent | 智能体 | AI Agent（智能体）是能够感知环境、自主决策并执行任务的人工智能实体 |
| Agent | 智能体 | AI Agent 的缩写 |
| Text Generation | 文本生成 | Text Generation（文本生成）是指利用自然语言处理（NLP）技术，根据给定的输入自动产生连贯、有意义的文本内容的过程 |
| Text Classification | 文本分类 | Text Classification（文本分类）是指将文本数据分配到预定义的类别或标签中的过程 |
| Text-to-Image | 图像生成 | Text-to-Image（文本到图像）是指利用人工智能技术，根据输入的文本描述自动生成相应图像的过程 |
| Training | 训练 | Training 是指利用人工智能技术，根据输入数据对模型进行训练 |

## 快速查询表 (Quick Reference)

以下为核心高频术语对照：

### 集群与角色 (Cluster & Role)
- **global cluster** → global 集群
- **workload cluster** → 业务集群
- **control plane** → 控制平面
- **node** → 节点
- **administrator** → 管理员
- **developer** → 开发人员

### 应用与网络 (App & Network)
- **Application** → 原生应用
- **OAM Application** → OAM 应用
- **Helm Chart App** → 模版应用
- **Dual-stack Network** → 双栈网络
- **Single-stack Network** → 单栈网络
- **subnet** → 子网

### 服务类型 (Service Types)
- **ClusterIP** → 虚拟 IP
- **NodePort** → 主机端口
- **LoadBalancer** → 负载均衡器

## 术语使用注意事项

1. **禁止自行创造缩略语**
2. **缩略语首次出现给出全称**:
   ```markdown
   使用 BGP（Border Gateway Protocol，边界网关协议）协议。
   ```
3. **避免 badCases**:
   - 查看上表中的 badCases 列
   - 避免使用列出的不当用法
4. **全文保持一致**:
   - 术语选定后全文保持一致
   - 不使用同义词混用

## 标题术语

### 标准标题列表

| 标题名称 | 描述 |
|---------|------|
| Navigation | 文档导航页 |
| Overview | 概述目录 |
| Introduction | 介绍 |
| Architecture | 架构 |
| Quick Start | 快速开始 |
| Release Notes | 发布说明 |
| Install | 安装 |
| Installing XXX | 安装 XXX |
| Upgrade | 升级 |
| Upgrading XXX | 升级 XXX |
| Configure | 配置 |
| Configuring XXX | 配置 XXX |
| Features | 功能概览 |
| Concepts | 概念 |
| Understanding XXX | 深入理解 XXX |
| Guides | 功能指南目录 |
| HowTo | 实用指南目录 |
| Trouble Shooting | 故障排除 |
| Permissions | 权限说明 |
| API Reference | API 参考 |
| Kubernetes APIs | Kubernetes API 参考 |
| Advanced APIs | 高级 API 参考 |
| CLI Reference | CLI 参考 |

### 使用原则

- 左侧导航显示的标题
- 使用标准化标题术语
- 保持导航结构清晰一致
