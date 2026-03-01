# YAML 校验问题分析报告

**日期**: 2026-03-01
**Skill**: doom-doc-assistant
**版本**: 1.0

---

## 一、问题概述

在文档 YAML 校验过程中，发现 skill 现有检查工具未能检测到 `mode: 0644` 这样的 YAML 1.2 规范问题。经过深入分析，发现根本原因是：**检查时使用了错误的 YAML 解析器**。

---

## 二、问题时间线

| 阶段 | 操作 | 发现 |
|------|------|------|
| **1. 初始检查** | 只检查独立的 .yaml 文件 | 漏掉 MDX 中的 YAML 代码块 |
| **2. 用户指出** | "很多 YAML 在 MDX 中" | 意识到检查范围不完整 |
| **3. 扩展检查** | 检查 MDX 中的 YAML 代码块 | 使用 PyYAML，发现缩进问题但漏掉格式问题 |
| **4. 用户提问** | "有发现不符合 YAML spec 的问题吗？比如 0644 vs 0o644" | 我给出模糊回答，未深入检查 |
| **5. 用户质疑** | 选中 `mode: 0644`，问为什么检查不出来 | 意识到问题严重性 |
| **6. 深入分析** | 发现 skill 中已有 `yaml_check.py` | 使用 ruamel.yaml (YAML 1.2) |
| **7. 验证** | 安装 ruamel.yaml，运行 yaml_check.py | **成功检测到 `mode: 0644` 问题** |
| **8. 进一步发现** | 测试不完整的示例 YAML | 发现 yaml_check.py 误报 `false` |

---

## 三、根本原因分析

### 3.1 两种 YAML 解析器的差异

| 解析器 | YAML 版本 | `0644` 的解析结果 |
|--------|-----------|------------------|
| **PyYAML** | YAML 1.1 (默认) | 解析为八进制 644 → 十进制 420 ✅ |
| **ruamel.yaml** | YAML 1.2 | 解析为十进制 644 ❌ (错误) |

### 3.2 我的检查代码问题

```python
# ❌ 我使用的检查方法
import yaml
yaml.safe_load(content)  # PyYAML，YAML 1.1 解析器

# ✅ skill 中的正确方法
from ruamel.yaml import YAML
yaml = YAML()
yaml.version = (1, 2)  # 强制使用 YAML 1.2
yaml.load(content)
```

### 3.3 为什么 skill 中有正确工具但没用？

```
skill/doom-doc-assistant/
├── scripts/
│   └── yaml_check.py      # ✅ 正确的工具 (ruamel.yaml + YAML 1.2)
├── references/
│   └── kubernetes-validation.md  # ✅ 文档说明了如何使用
└── SKILL.md                # ❌ 我没有仔细阅读执行流程
```

**问题**：我在检查时直接写了 Python 脚本，**没有使用 skill 中已有的 `yaml_check.py`**。

---

## 四、发现的实际问题

### 4.1 YAML 1.2 规范问题 (1 个)

| 文件 | 行号 | 问题 |
|------|------|------|
| `en/machine-configuration/managing.mdx` | 53 | `mode: 0644` (Butane 配置) |

**问题描述**：在 YAML 1.2 中，`0644` 会被解析为十进制 644，而不是八进制的 420（即 `0o644`）。

### 4.2 YAML 语法错误 (6 个)

| 文件 | 问题 |
|------|------|
| `en/how-to/node-configuration.mdx` | 6 个代码块缩进错误 (2 空格 → 4 空格) |

### 4.3 yaml_check.py 的误报

发现 `yaml_check.py` 会把标准 YAML 1.2 布尔值 `true`/`false` 也报错：

```python
# 问题代码 (yaml_check.py 第 37 行)
YAML11_PATTERNS = [
    (r'(?<![\'"])\\b(yes|no|on|off|true|false|TRUE|FALSE|...|ON|OFF)\\b(?![\'"])', ...),
]

# 问题：`true` 和 `false` 是 YAML 1.2 的标准布尔值，不应该包含在这个模式中
```

### 4.4 误报分析 (permissions: "0644")

`yaml_check.py` 会把字符串 `"0644"` 也报出来，如：

```yaml
permissions: "0644"  # 字符串，正确
```

这不是真正的问题，因为引号内是字符串，不是 YAML 数字。

**原因**：Cluster API 的 `KubeadmConfigSpec.files[].permissions` 字段定义为字符串类型，这是合理的设计：
- 避免 YAML 1.2 八进制解析问题
- 符合系统管理员使用习惯
- Go 语言能正确处理字符串形式的八进制

---

## 五、不完整示例 YAML 的处理

### 5.1 文档中的省略标记

文档中使用 `# ...` 来标记省略内容：

```yaml
# 独立注释行
# ... (preKubeadmCommands & postKubeadmCommands) ...

# 在 content 块内
content: |
  # ... (Admission Configuration Content) ...
```

### 5.2 处理结果

| 检查项 | 结果 | 说明 |
|--------|------|------|
| **YAML 语法** | ✅ 通过 | `# ...` 注释不影响结构 |
| **YAML 1.2 规范** | ✅ 通过 | 省略标记是安全的 |
| **yaml_check.py** | ⚠️ 有误报 | `false` 被错误标记 |

**结论**：使用 `# ...` 注释来标记省略内容是**正确且安全的设计**。

---

## 六、环境变更记录

### 6.1 安装的软件

| 软件 | 版本 | 安装命令 | 用途 |
|------|------|----------|------|
| **ruamel.yaml** | 0.19.1 | `pip3 install --user ruamel.yaml` | YAML 1.2 解析器 |

### 6.2 创建的临时文件

| 文件 | 用途 |
|------|------|
| `/tmp/check.yaml` | 临时存储要检查的 YAML 内容 |
| `/tmp/check_block.yaml` | 临时存储单个 YAML 代码块 |
| `/tmp/yaml_check_report.json` | YAML 检查报告 |

### 6.3 清理方法

```bash
# 1. 卸载 ruamel.yaml (可选)
pip3 uninstall ruamel.yaml

# 2. 删除临时文件
rm -f /tmp/check.yaml
rm -f /tmp/check_block.yaml
rm -f /tmp/yaml_check_report.json
```

---

## 七、建议的解决方案

### 7.1 短期方案：改进 skill 文档

在 `SKILL.md` 中明确说明检查流程：

```markdown
## YAML 检查

**必须使用 skill 中提供的检查工具**：

1. **YAML 1.2 语法检查**: `scripts/yaml_check.py`
   - 使用 ruamel.yaml 解析器
   - 强制 YAML 1.2 规范
   - 能检测 0644 → 0o644 这类问题

2. **不要使用**: `import yaml` (PyYAML)
   - 仅支持 YAML 1.1
   - 无法检测格式规范问题
```

### 7.2 中期方案：修复 yaml_check.py

#### 问题 1: 误报 `true`/`false`

```python
# 修改前
YAML11_PATTERNS = [
    (r'(?<![\'"])\\b(yes|no|on|off|true|false|TRUE|FALSE|...|ON|OFF)\\b(?![\'"])', ...),
]

# 修改后
YAML11_PATTERNS = [
    (r'(?<![\'"])\\b(yes|no|on|off|...|ON|OFF)\\b(?![\'"])', ...),  # 移除 true/false
    (r'(?<![\'"])\\b(TRUE|FALSE|YES|NO)\\b(?![\'"])', ...),  # 只检查大写的非标准值
]
```

#### 问题 2: 误报字符串中的 `0644`

改进正则表达式，跳过引号内的内容：

```python
def check_yaml11_patterns(content: str) -> list[dict]:
    """改进版本，减少误报"""
    warnings = []
    lines = content.splitlines()
    for lineno, line in enumerate(lines, start=1):
        if line.strip().startswith('#'):
            continue

        for pattern, message_tmpl in YAML11_PATTERNS:
            for match in re.finditer(pattern, line):
                # 改进的引号检测
                before = line[:match.start()]
                after = line[match.end():]

                # 检查是否在引号内
                single_quotes = before.count("'") % 2
                double_quotes = before.count('"') % 2
                if single_quotes or double_quotes:
                    continue

                # 检查后面是否紧跟 : （是键，不是值）
                if after.strip().startswith(':'):
                    continue

                warnings.append({
                    "line": lineno,
                    "value": match.group(0),
                    "message": message_tmpl.format(match.group(0)),
                })
    return warnings
```

### 7.3 长期方案：集成到 skill 执行流程

在 Phase 2.6 (Kubernetes YAML Validation) 之前，先运行 YAML 1.2 检查：

```markdown
## Phase 2.6: YAML Validation

### Step 1: YAML 1.2 语法检查 (强制)
```bash
python3 scripts/yaml_check.py <file.yaml>
```

### Step 2: Kubernetes schema 检查 (条件)
- 仅当包含 Kubernetes 资源时运行
- 使用 kubeconform/kubval
```

---

## 八、待进一步讨论的问题

### 8.1 YAML 自动识别问题

**现状**：skill 需要用户告知 YAML 所在位置，不能主动发现

**需要设计**：
- 如何自动识别文档中的 YAML 代码块？
- 识别规则是什么？
- 如何处理不完整的示例 YAML？

### 8.2 报告呈现问题

**现状**：每次只报告单个 YAML 的检查结果

**需要设计**：
- 多文档的汇总报告格式
- 多 YAML 块的汇总报告格式
- 如何区分严重程度（错误 vs 警告）

### 8.3 检查触发机制

**现状**：不明确何时触发 YAML 检查

**需要设计**：
- 默认对所有文档检查？还是按需检查？
- 如何在 Phase 0（Intake）中判断是否需要 YAML 检查？
- 如何在 Phase 2（Execution）中集成 YAML 检查？

---

## 九、经验教训

1. **Use the tools you have** - skill 中已有正确的工具，应该先使用它，而不是重新发明
2. **Read the documentation** - `kubernetes-validation.md` 已经说明了检查流程
3. **Understand the difference** - YAML 1.1 和 YAML 1.2 在数字格式上有重要差异
4. **Trust user feedback** - 用户的质疑往往指向真正的问题
5. **Test edge cases** - 不完整的示例 YAML 也需要考虑

---

## 十、后续行动

| 优先级 | 行动 | 负责人 |
|--------|------|--------|
| P0 | 修复 `mode: 0644` 问题 | 用户确认 |
| P1 | 修复 yaml_check.py 误报 (`true`/`false`) | Skill 维护者 |
| P2 | 设计 YAML 自动识别机制 | Skill 维护者 |
| P3 | 设计报告呈现格式 | Skill 维护者 |
| P4 | 集成到 skill 执行流程 | Skill 维护者 |
