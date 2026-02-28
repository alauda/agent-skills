#!/usr/bin/env python3
"""
ACP Design Validator

Audits code files for design token compliance:
- Detects hardcoded colors (should use tokens)
- Checks spacing consistency
- Identifies non-standard border radius values
- Generates compliance reports

Helps maintain consistency across the codebase.
"""

import os
import sys
import re
import json
from pathlib import Path
from typing import List, Dict, Tuple
import argparse


def _activate_project_venv():
    """Auto-detect project .venv and switch to it"""
    here = Path(__file__).resolve()
    parents = list(here.parent.parent.parents)
    for p in parents:
        vpy = p / '.venv' / 'bin' / 'python3'
        if vpy.exists():
            if sys.executable != str(vpy):
                os.execv(str(vpy), [str(vpy)] + sys.argv)
            break


_activate_project_venv()


class DesignValidator:
    """Validate code files for design token compliance"""

    # Pattern for hex colors
    HEX_COLOR_PATTERN = re.compile(r'["\']?(#[0-9a-fA-F]{6}|#[0-9a-fA-F]{3})["\']?')

    # Pattern for hardcoded pixel values (spacing)
    PX_PATTERN = re.compile(r'(\d+)px')

    # Pattern for border-radius values
    RADIUS_PATTERN = re.compile(r'border-radius\s*:\s*(\d+)px')

    # Known allowed colors (from ACP design system)
    ALLOWED_COLORS = {
        '#ffffff', '#f4f6f8', '#eef4ff', '#e3f2fd', '#90caf9',
        '#d7f5e9', '#4caf50', '#e8f2ff', '#2196f3',
        '#e0f2f1', '#4db6ac', '#cbd7e0', '#cbd5e1',
        '#1a1a1a', '#2d3748', '#1e3a5f', '#1e3a8a', '#60a5fa',
        '#064e3b', '#10b981', '#1e40af', '#3b82f6',
        '#134e4a', '#14b8a6', '#4b5563', '#555d6f',
        '#000000', '#000', '#fff', # Allow basic black/white
    }

    # Known allowed spacing values (10px grid)
    ALLOWED_SPACING = {4, 8, 12, 16, 20, 24, 32, 48, 64}

    # Known allowed border-radius values
    ALLOWED_RADII = {4, 8, 12, 16}

    def __init__(self, tokens_path: Optional[str] = None):
        """Initialize validator with optional tokens file"""
        self.tokens = {}
        self.issues: List[Dict] = []

        if tokens_path and Path(tokens_path).exists():
            with open(tokens_path, 'r') as f:
                self.tokens = json.load(f)
                self._update_allowed_colors()

    def _update_allowed_colors(self) -> None:
        """Update allowed colors from loaded tokens"""
        for mode in ['light', 'dark']:
            colors = self.tokens.get('modes', {}).get(mode, {}).get('colors', {})
            for category, color_values in colors.items():
                for name, value in color_values.items():
                    self.ALLOWED_COLORS.add(value.lower())

    def audit_file(self, file_path: str) -> Dict[str, List]:
        """Audit a single file for design violations"""
        path = Path(file_path)
        if not path.exists():
            return {'errors': [f"File not found: {file_path}"]}

        with open(path, 'r', encoding='utf-8', errors='ignore') as f:
            content = f.read()
            lines = content.split('\n')

        file_issues = {
            'colors': [],
            'spacing': [],
            'radius': [],
        }

        for line_num, line in enumerate(lines, 1):
            # Skip comments and imports
            if line.strip().startswith(('/*', '//', 'import ', 'require')):
                continue

            # Check for hardcoded colors
            color_matches = self.HEX_COLOR_PATTERN.findall(line)
            for color in color_matches:
                if color.lower() not in self.ALLOWED_COLORS:
                    file_issues['colors'].append({
                        'line': line_num,
                        'color': color,
                        'code': line.strip(),
                    })

            # Check for suspicious spacing values (avoid false positives)
            if any(css_prop in line for css_prop in ['padding', 'margin', 'gap', 'width', 'height']):
                px_matches = self.PX_PATTERN.findall(line)
                for px_value in px_matches:
                    try:
                        value = int(px_value)
                        if value not in self.ALLOWED_SPACING and value not in [0, 1, 2, 3]:
                            file_issues['spacing'].append({
                                'line': line_num,
                                'value': f"{value}px",
                                'code': line.strip(),
                            })
                    except ValueError:
                        pass

            # Check border-radius values
            if 'border-radius' in line or 'borderRadius' in line:
                radius_matches = self.RADIUS_PATTERN.findall(line)
                for radius_value in radius_matches:
                    try:
                        value = int(radius_value)
                        if value not in self.ALLOWED_RADII:
                            file_issues['radius'].append({
                                'line': line_num,
                                'value': f"{value}px",
                                'code': line.strip(),
                            })
                    except ValueError:
                        pass

        return file_issues

    def audit_directory(self, directory: str, extensions: List[str] = None) -> Dict:
        """Audit all files in a directory"""
        if extensions is None:
            extensions = ['.tsx', '.ts', '.jsx', '.js', '.css', '.scss']

        path = Path(directory)
        if not path.is_dir():
            return {'error': f"Directory not found: {directory}"}

        all_issues = {}
        file_count = 0

        for ext in extensions:
            for file_path in path.rglob(f"*{ext}"):
                # Skip node_modules and common build directories
                if any(skip in str(file_path) for skip in ['node_modules', '.next', 'dist', 'build']):
                    continue

                file_count += 1
                issues = self.audit_file(str(file_path))

                # Only include files with issues
                if any(issues.get(cat, []) for cat in ['colors', 'spacing', 'radius']):
                    all_issues[str(file_path)] = issues

        return {
            'total_files_scanned': file_count,
            'files_with_issues': len(all_issues),
            'issues': all_issues,
        }

    def generate_report(self, audit_results: Dict, mode: str = 'light') -> str:
        """Generate a compliance report from audit results"""
        report = f'''# ACP Design Token Compliance Report
Mode: {mode}

## Summary
- Total files scanned: {audit_results.get('total_files_scanned', 0)}
- Files with issues: {audit_results.get('files_with_issues', 0)}

## Issues Found

'''

        issues = audit_results.get('issues', {})

        if not issues:
            report += "✓ No design token compliance issues found!\n"
            return report

        # Group by issue type
        color_issues = []
        spacing_issues = []
        radius_issues = []

        for file_path, file_issues in issues.items():
            color_issues.extend([(file_path, issue) for issue in file_issues.get('colors', [])])
            spacing_issues.extend([(file_path, issue) for issue in file_issues.get('spacing', [])])
            radius_issues.extend([(file_path, issue) for issue in file_issues.get('radius', [])])

        if color_issues:
            report += f"### Hardcoded Colors ({len(color_issues)} issues)\n\n"
            for file_path, issue in color_issues[:10]:  # Limit to first 10
                report += f"**{file_path}:{issue['line']}**\n"
                report += f"- Color: `{issue['color']}`\n"
                report += f"- Line: `{issue['code']}`\n"
                report += f"- Fix: Use design token instead\n\n"
            if len(color_issues) > 10:
                report += f"... and {len(color_issues) - 10} more color issues\n\n"

        if spacing_issues:
            report += f"### Non-standard Spacing ({len(spacing_issues)} issues)\n\n"
            for file_path, issue in spacing_issues[:10]:
                report += f"**{file_path}:{issue['line']}**\n"
                report += f"- Value: `{issue['value']}`\n"
                report += f"- Line: `{issue['code']}`\n"
                report += f"- Fix: Use spacing token (4, 8, 12, 16, 20, 24, 32, 48, 64px)\n\n"
            if len(spacing_issues) > 10:
                report += f"... and {len(spacing_issues) - 10} more spacing issues\n\n"

        if radius_issues:
            report += f"### Non-standard Border Radius ({len(radius_issues)} issues)\n\n"
            for file_path, issue in radius_issues[:10]:
                report += f"**{file_path}:{issue['line']}**\n"
                report += f"- Value: `{issue['value']}`\n"
                report += f"- Line: `{issue['code']}`\n"
                report += f"- Fix: Use border radius token (4, 8, 12, 16px)\n\n"
            if len(radius_issues) > 10:
                report += f"... and {len(radius_issues) - 10} more radius issues\n\n"

        return report


def main():
    parser = argparse.ArgumentParser(
        description='Validate code for ACP design token compliance'
    )

    parser.add_argument('--path', required=True,
                        help='File or directory path to audit')
    parser.add_argument('--mode', choices=['light', 'dark'], default='light',
                        help='Color mode for validation (default: light)')
    parser.add_argument('--tokens', help='Path to design-tokens.json file')
    parser.add_argument('--output', help='Output file for report (default: print to stdout)')
    parser.add_argument('--extensions', nargs='+',
                        default=['.tsx', '.ts', '.jsx', '.js', '.css', '.scss'],
                        help='File extensions to audit')

    args = parser.parse_args()

    try:
        validator = DesignValidator(args.tokens)
        path = Path(args.path)

        if path.is_file():
            print(f"Auditing file: {args.path}")
            results = validator.audit_file(args.path)
        else:
            print(f"Auditing directory: {args.path}")
            results = validator.audit_directory(args.path, args.extensions)

        report = validator.generate_report(results, args.mode)

        if args.output:
            Path(args.output).write_text(report)
            print(f"✓ Report written to: {args.output}")
        else:
            print(report)

        # Return exit code based on issues found
        issues_count = sum(
            len(v.get('colors', [])) + len(v.get('spacing', [])) + len(v.get('radius', []))
            for v in results.get('issues', {}).values()
        )
        return 1 if issues_count > 0 else 0

    except Exception as e:
        print(f"✗ Error: {e}", file=sys.stderr)
        return 1


if __name__ == '__main__':
    sys.exit(main())
