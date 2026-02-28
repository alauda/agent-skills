#!/usr/bin/env python3
"""
YAML 1.2 spec compliance checker for Kubernetes manifests.
Uses ruamel.yaml which implements YAML 1.2 (unlike pyyaml which is YAML 1.1).

Requirements: Python 3.6+
"""

import sys
import re
from pathlib import Path

# Check Python version
if sys.version_info < (3, 6):
    print(f"ERROR: Python 3.6+ required. You have Python {sys.version_info.major}.{sys.version_info.minor}")
    sys.exit(2)

try:
    from ruamel.yaml import YAML
    from ruamel.yaml.scanner import ScannerError
    from ruamel.yaml.parser import ParserError
    from ruamel.yaml.constructor import ConstructorError
except ImportError:
    print("ERROR: ruamel.yaml not installed.")
    print("")
    print("Install with:")
    print("  pip3 install --user ruamel.yaml")
    print("")
    print("Or use a virtual environment:")
    print("  python3 -m venv .venv && source .venv/bin/activate")
    print("  pip install ruamel.yaml")
    sys.exit(2)


# Patterns that are valid YAML 1.1 but behave differently in YAML 1.2
YAML11_PATTERNS = [
    (r'(?<![\'"])\b(yes|no|on|off|true|false|TRUE|FALSE|YES|NO|ON|OFF)\b(?![\'"])',
     "Bare boolean-like value '{}' — in YAML 1.2, only `true`/`false` are booleans. "
     "If you intend a boolean, use `true` or `false`. If string, quote it."),
    (r'(?<!\w)0[0-7]+(?!\w)',
     "Octal literal '{}' — YAML 1.2 requires `0o` prefix (e.g. `0o755`). "
     "YAML 1.1 style `0755` is parsed as decimal in 1.2."),
]


def check_yaml11_patterns(content: str) -> list[dict]:
    """
    Scan raw text for YAML 1.1 legacy patterns that changed in 1.2.

    NOTE: Quote detection is heuristic (simple counting) and may produce false positives
    for escaped quotes. This is acceptable for a linting tool - when in doubt, we prefer
    to warn rather than miss a potential issue.
    """
    warnings = []
    lines = content.splitlines()
    for lineno, line in enumerate(lines, start=1):
        # Skip comment lines
        stripped = line.strip()
        if stripped.startswith('#'):
            continue
        for pattern, message_tmpl in YAML11_PATTERNS:
            for match in re.finditer(pattern, line):
                # Skip if inside a quoted string (heuristic - see note above)
                before = line[:match.start()]
                single_quotes = before.count("'") % 2
                double_quotes = before.count('"') % 2
                if single_quotes or double_quotes:
                    continue
                # Skip if it's a key (followed by :) — keys are always strings
                after = line[match.end():].lstrip()
                if after.startswith(':'):
                    continue
                warnings.append({
                    "line": lineno,
                    "value": match.group(0),
                    "message": message_tmpl.format(match.group(0)),
                })
    return warnings


def validate_file(filepath: str) -> dict:
    """
    Validate a YAML file for YAML 1.2 compliance.
    Returns a result dict with keys: valid, errors, warnings, doc_count.
    """
    path = Path(filepath)
    if not path.exists():
        return {"valid": False, "errors": [f"File not found: {filepath}"], "warnings": [], "doc_count": 0}

    content = path.read_text(encoding="utf-8")
    errors = []
    warnings = []
    doc_count = 0

    # Stage 1: YAML 1.2 parse
    yaml = YAML()
    yaml.version = (1, 2)  # Enforce YAML 1.2
    try:
        from io import StringIO
        docs = list(yaml.load_all(StringIO(content)))
        doc_count = len(docs)
    except ScannerError as e:
        mark = e.problem_mark
        errors.append({
            "type": "parse_error",
            "line": mark.line + 1 if mark else None,
            "column": mark.column + 1 if mark else None,
            "message": f"{e.problem} {e.context or ''}".strip(),
        })
        return {"valid": False, "errors": errors, "warnings": warnings, "doc_count": 0}
    except ParserError as e:
        mark = e.problem_mark
        errors.append({
            "type": "parse_error",
            "line": mark.line + 1 if mark else None,
            "column": mark.column + 1 if mark else None,
            "message": f"{e.problem} {e.context or ''}".strip(),
        })
        return {"valid": False, "errors": errors, "warnings": warnings, "doc_count": 0}
    except ConstructorError as e:
        errors.append({
            "type": "constructor_error",
            "line": None,
            "column": None,
            "message": str(e),
        })
        return {"valid": False, "errors": errors, "warnings": warnings, "doc_count": 0}

    # Stage 2: YAML 1.1 legacy pattern warnings
    warnings = check_yaml11_patterns(content)

    return {
        "valid": True,
        "errors": errors,
        "warnings": warnings,
        "doc_count": doc_count,
    }


def print_report(filepath: str, result: dict):
    print(f"\n{'='*60}")
    print(f"YAML 1.2 Check: {filepath}")
    print(f"{'='*60}")

    if not result["valid"]:
        print("🔴 YAML PARSE FAILED\n")
        for err in result["errors"]:
            loc = ""
            if err.get("line"):
                loc = f" (line {err['line']}, col {err.get('column', '?')})"
            print(f"  ✗{loc}: {err['message']}")
        print("\n⚠  Fix YAML syntax errors before running K8s schema validation.")
        return False

    doc_str = f"{result['doc_count']} document{'s' if result['doc_count'] != 1 else ''}"
    print(f"✅ YAML syntax valid ({doc_str} found)\n")

    if result["warnings"]:
        print(f"⚠️  YAML 1.1 Legacy Patterns ({len(result['warnings'])} found):")
        for w in result["warnings"]:
            print(f"  • Line {w['line']}: {w['message']}")
        print()
    else:
        print("✅ No YAML 1.1 legacy patterns detected\n")

    return True


def main():
    if len(sys.argv) < 2:
        print("Usage: yaml_check.py <file.yaml> [file2.yaml ...]")
        sys.exit(1)

    all_valid = True
    for filepath in sys.argv[1:]:
        result = validate_file(filepath)
        ok = print_report(filepath, result)
        if not ok:
            all_valid = False

    sys.exit(0 if all_valid else 1)


if __name__ == "__main__":
    main()
