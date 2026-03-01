# YAML 检测与校验机制设计

**日期**: 2026-03-01
**Skill**: doom-doc-assistant
**状态**: 设计草案

---

## 问题一：如何主动识别文档中的 YAML？

### 1.1 现状分析

当前流程的问题：
```
用户: "检查这个文件的 YAML"
    ↓
我: 读取指定文件，检查 YAML
    ↓
问题: 需要用户告知位置，不能主动发现
```

### 1.2 YAML 识别规则

#### 规则 1: 代码块检测

在 MDX 文件中检测 YAML 代码块：

```regex
```yaml
...
```

```yaml
...
```
```

#### 规则 2: 内容特征检测

即使没有明确标记，根据内容特征识别 YAML：

```yaml
# 包含 Kubernetes 资源标识
apiVersion: group/version
kind: ResourceName
metadata:
  name: value
```

常见 Kubernetes 资源类型：
- Deployment, Service, ConfigMap, Secret
- Cluster, MachineDeployment, KubeadmControlPlane
- CustomResourceDefinition

#### 规则 3: 文件扩展名

独立文件检测：
- `.yaml` 文件
- `.yml` 文件

### 1.3 识别流程设计

```python
def detect_yaml_in_document(content: str) -> list[dict]:
    """
    主动检测文档中的所有 YAML 代码块

    Returns:
        [
            {
                "type": "code_block",  # 或 "standalone_file"
                "start_line": 10,
                "end_line": 50,
                "language": "yaml",
                "has_k8s_resources": True,
                "is_complete": True,  # 是否完整（无省略标记）
                "confidence": "high"  # high/medium/low
            },
            ...
        ]
    """
```

#### 完整性检测

检测 YAML 是否为完整示例：

```python
def check_completeness(yaml_content: str) -> dict:
    """
    检查 YAML 示例的完整性

    Returns:
        {
            "is_complete": False,
            "has_ellipsis": True,  # 是否有省略标记
            "missing_sections": ["preKubeadmCommands", "postKubeadmCommands"],
            "ellipses_positions": [25, 30, 45]
        }
    """
    # 检查省略标记
    has_ellipsis = bool(re.search(r'#\s*\.\.\.', yaml_content))

    # 检查必要字段
    required_fields = ['apiVersion', 'kind', 'metadata']
    missing = [f for f in required_fields if f not in yaml_content]

    return {
        "is_complete": not has_ellipsis and not missing,
        "has_ellipsis": has_ellipsis,
        "missing_fields": missing
    }
```

### 1.4 Phase 0 增强

在 Phase 0（Intake & Diagnosis）中自动检测：

```markdown
## Phase 0: Intake & Diagnosis (增强版)

### 0.1 Collect Task Information
[现有内容]

### 0.2 Explore Existing Documentation
[现有内容]

### 0.3 YAML Detection (新增)

自动检测文档中的 YAML：

```bash
# 扫描所有相关文档
find /path/to/docs -name "*.mdx" -exec yaml_detect.py {} \;
```

输出结果：
```
Found 8 files with YAML blocks:
- en/create-cluster/huawei-dcs.mdx: 3 blocks
- en/how-to/node-configuration.mdx: 8 blocks
...
```

### 0.4 Output Diagnosis Report
[现有内容，增加 YAML 检测摘要]
```

---

## 问题二：如何呈现多文档/多 YAML 块的检查报告？

### 2.1 报告层次结构

```
YAML Validation Report
├── Summary (总计)
│   ├── Files scanned: 8
│   ├── YAML blocks: 37
│   ├── Errors: 6
│   └── Warnings: 1
│
├── By File (按文件分组)
│   ├── en/how-to/node-configuration.mdx
│   │   ├── Summary: 6 errors
│   │   └── Details
│   │       ├── Block #2 (Line 54): Indentation error
│   │       ├── Block #3 (Line 72): Indentation error
│   │       └── ...
│   │
│   └── en/machine-configuration/managing.mdx
│       ├── Summary: 1 warning
│       └── Details
│           └── Block #1 (Line 14): Octal format (mode: 0644)
│
├── By Severity (按严重程度分组)
│   ├── Errors (6)
│   │   └── [列表]
│   └── Warnings (1)
│       └── [列表]
│
└── Complete Details (完整详情)
    └── [每个问题的详细信息]
```

### 2.2 报告格式设计

#### 格式 1: 控制台输出 (简洁版)

```
╔═══════════════════════════════════════════════════════════════════╗
║                    YAML Validation Report                        ║
╠═══════════════════════════════════════════════════════════════════╣
║  Files: 8   Blocks: 37   Errors: 6   Warnings: 1               ║
╠═══════════════════════════════════════════════════════════════════╣
║                                                                  ║
║  ❌ ERRORS (6)                                                   ║
║  ├─ en/how-to/node-configuration.mdx: 6 blocks                 ║
║  │  ├─ Block #2 (Line 54): Indentation: 2 spaces → 4 spaces   ║
║  │  ├─ Block #3 (Line 72): Indentation: 2 spaces → 4 spaces   ║
║  │  └─ ...                                                     ║
║                                                                  ║
║  ⚠️  WARNINGS (1)                                               ║
║  └─ en/machine-configuration/managing.mdx:                     ║
║     └─ Block #1 (Line 14): mode: 0644 → mode: 0o644           ║
║                                                                  ║
╚═══════════════════════════════════════════════════════════════════╝
```

#### 格式 2: Markdown (详细版)

```markdown
## YAML Validation Report

### Summary
| Metric | Count |
|--------|-------|
| Files scanned | 8 |
| YAML blocks | 37 |
| Errors | 6 |
| Warnings | 1 |

### By File

#### ❌ en/how-to/node-configuration.mdx
| Block | Line | Issue | Fix |
|-------|------|-------|-----|
| #2 | 54 | Indentation: 2 spaces | Change to 4 spaces |
| #3 | 72 | Indentation: 2 spaces | Change to 4 spaces |
| ...

#### ⚠️ en/machine-configuration/managing.mdx
| Block | Line | Issue | Fix |
|-------|------|-------|-----|
| #1 | 14 | Octal format: `mode: 0644` | Change to `mode: 0o644` or `mode: 420` |

### Full Details
[展开所有详细信息]
```

#### 格式 3: JSON (机器可读)

```json
{
  "summary": {
    "files_scanned": 8,
    "yaml_blocks": 37,
    "errors": 6,
    "warnings": 1
  },
  "results": [
    {
      "file": "en/how-to/node-configuration.mdx",
      "status": "error",
      "blocks": [
        {
          "block_id": 2,
          "line": 54,
          "severity": "error",
          "issue": "Indentation error",
          "fix": "Change 2 spaces to 4 spaces"
        }
      ]
    }
  ]
}
```

### 2.3 交互式报告设计

支持用户交互的报告：

```bash
$ yaml_check.py /path/to/docs

Found 8 files with YAML blocks. 6 errors, 1 warning.

View details by:
  [1] File          [2] Severity      [3] All          [q] Quit
Your choice: 1

  Files with issues:
  [1] en/how-to/node-configuration.mdx (6 errors)
  [2] en/machine-configuration/managing.mdx (1 warning)
  [b] Back

Your choice: 1

  Block #2 (Line 54): Indentation error
  ┌────────────────────────────────────────┐
  │   ```yaml                             │
  │   ---                                  │
  │   apiVersion: cluster.x-k8s.io/v1beta1  │
  │   kind: MachineDeployment              │
  │   ^^^ Only 2 spaces, should be 4       │
  └────────────────────────────────────────┘

  [f] Fix this  [s] Skip  [q] Quit
```

---

## 问题三：如何激活 skill 去检查 YAML？

### 3.1 触发机制设计

#### 选项 1: 默认检查 (推荐)

**原则**: 所有文档生成任务都进行 YAML 检查

```
Phase 2 (Execution)
  ↓
  2.1 Restructure Existing Documents
  ↓
  2.2 Load Template
  ↓
  2.3 Load Specifications
  ↓
  2.4 Example-Driven Learning
  ↓
  2.5 Generate Document
  ↓
  2.6 YAML Validation ← **新增：始终执行**
      ↓
      2.6a Kubernetes YAML (有 K8s 资源时)
      ↓
  2.7 Self-Verification
```

**检测逻辑**：

```python
def should_validate_yaml(generated_content: str) -> bool:
    """
    判断是否需要 YAML 检查

    规则：
    1. 生成的文档包含 YAML 代码块 → 检查
    2. 修改的文档包含 YAML 代码块 → 检查
    3. 否则 → 跳过
    """
    return bool(re.search(r'```yaml', generated_content))
```

#### 选项 2: 按需检查

用户明确指定时检查：

```
/user: "生成 XX 文档并检查 YAML"
/user: "检查文档中的 YAML"
```

**问题**：依赖用户记忆，容易遗漏

#### 选项 3: 混合模式 (推荐)

```python
# 默认检查，但可以跳过
def validate_yaml_with_skip(content: str, skip: bool = False) -> bool:
    """
    Args:
        content: 文档内容
        skip: 用户是否明确跳过检查

    Returns:
        是否通过检查
    """
    if skip:
        print("⚠️ YAML validation skipped by user request")
        return True

    return do_validate(content)
```

### 3.2 在 Phase 0 中预判断

在 Phase 0（Intake）时就判断是否需要 YAML 检查：

```markdown
## Phase 0: Intake & Diagnosis

### 0.1 Collect Task Information

[收集信息]

### 0.2 Explore Existing Documentation

[探索现有文档]

### 0.3 YAML Detection (新增)

```python
# 自动检测
yaml_detection = detect_yaml_in_docs(
    docs_path="/path/to/docs",
    file_patterns=["**/*.mdx", "**/*.yaml"]
)

if yaml_detection['total_blocks'] > 0:
    print(f"📋 Detected {yaml_detection['total_blocks']} YAML blocks")
    print(f"   Files affected: {len(yaml_detection['files'])}")
    print(f"   Will validate in Phase 2.6")
else:
    print("✅ No YAML detected, will skip validation")
```

### 0.4 Output Diagnosis Report

[在报告中增加 YAML 检测信息]
```

### 3.3 技能配置

在 SKILL.md 中添加配置选项：

```yaml
# Skill Configuration
validation:
  yaml:
    enabled: true              # 是否启用
    auto_detect: true          # 是否自动检测
    fail_on_error: false       # 发现错误是否失败
    skip_incomplete: false     # 是否跳过不完整的示例

kubernetes:
  enabled: true               # K8s schema 检查
  versions: ["1.34", "1.33"]   # 支持的 K8s 版本
```

---

## 四、实现优先级

| 优先级 | 功能 | 复杂度 | 价值 |
|--------|------|--------|------|
| P0 | 修复 yaml_check.py 误报 | 低 | 高 |
| P1 | 实现默认检查机制 | 低 | 高 |
| P2 | 实现报告汇总 | 中 | 高 |
| P3 | 实现 YAML 自动检测 | 中 | 中 |
| P4 | 实现交互式报告 | 高 | 中 |

---

## 五、伪代码实现

### 5.1 自动检测

```python
def auto_detect_yaml(docs_path: str) -> dict:
    """
    Phase 0 中调用：自动检测所有 YAML
    """
    results = {
        'total_blocks': 0,
        'files_with_yaml': [],
        'by_file': {}
    }

    for mdx_file in find_mdx_files(docs_path):
        content = read_file(mdx_file)
        blocks = extract_yaml_blocks(content)

        if blocks:
            results['total_blocks'] += len(blocks)
            results['files_with_yaml'].append(mdx_file)
            results['by_file'][mdx_file] = {
                'count': len(blocks),
                'has_k8s': any(has_k8s_resources(b) for b in blocks)
            }

    return results
```

### 5.2 批量验证

```python
def batch_validate(docs_path: str, detection_result: dict) -> dict:
    """
    Phase 2 中调用：批量验证所有 YAML
    """
    report = {
        'summary': {'total': 0, 'errors': 0, 'warnings': 0},
        'by_file': {},
        'by_severity': {'error': [], 'warning': []}
    }

    for file_path in detection_result['files_with_yaml']:
        file_result = validate_file(file_path)
        report['by_file'][file_path] = file_result

        # 汇总
        report['summary']['total'] += file_result['blocks']
        report['summary']['errors'] += file_result['errors']
        report['summary']['warnings'] += file_result['warnings']

    return report
```

### 5.3 报告生成

```python
def generate_report(validation_result: dict, format: str = 'console') -> str:
    """
    生成检查报告
    """
    if format == 'console':
        return generate_console_report(validation_result)
    elif format == 'markdown':
        return generate_markdown_report(validation_result)
    elif format == 'json':
        return json.dumps(validation_result, indent=2)
```

---

## 六、待讨论的问题

1. **性能问题**：大型文档库的检查可能很慢，如何优化？
2. **缓存机制**：是否需要缓存检查结果？
3. **增量检查**：如何只检查修改过的文件？
4. **CI/CD 集成**：如何在 CI/CD 中使用这个检查？
