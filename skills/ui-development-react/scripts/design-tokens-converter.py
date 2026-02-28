#!/usr/bin/env python3
"""
ACP Design Tokens Converter

Converts design tokens between multiple formats:
- JSON (source format)
- TypeScript (for Next.js/React)
- CSS (CSS custom properties)
- Tailwind (Tailwind CSS config)

Supports both light and dark mode token generation.
"""

import os
import sys
import json
from pathlib import Path
import argparse
from typing import Dict, Any, Optional


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
    # Auto-detect and add scripts directory for cross-script imports
    for p in parents:
        scripts_dir = p / '.claude' / 'scripts'
        if scripts_dir.exists():
            scripts_dir_str = str(scripts_dir)
            if scripts_dir_str not in sys.path:
                sys.path.insert(0, scripts_dir_str)
            break


_activate_project_venv()


class DesignTokensConverter:
    """Convert design tokens between formats"""

    def __init__(self, tokens_path: str):
        """Initialize with path to tokens.json file"""
        self.tokens_path = Path(tokens_path)
        self.tokens = self._load_tokens()

    def _load_tokens(self) -> Dict[str, Any]:
        """Load tokens from JSON file"""
        if not self.tokens_path.exists():
            raise FileNotFoundError(f"Token file not found: {self.tokens_path}")

        with open(self.tokens_path, 'r') as f:
            return json.load(f)

    def to_typescript(self, output_path: str, mode: str = 'light') -> None:
        """Convert tokens to TypeScript format"""
        ts_content = self._generate_typescript(mode)
        Path(output_path).write_text(ts_content)
        print(f"✓ Generated TypeScript tokens: {output_path}")

    def _generate_typescript(self, mode: str) -> str:
        """Generate TypeScript content"""
        modes = self.tokens.get('modes', {})
        colors = modes.get(mode, {}).get('colors', {})
        spacing = self.tokens.get('spacing', {})
        typography = self.tokens.get('typography', {})
        effects = self.tokens.get('effects', {})

        ts_code = '''// Auto-generated design tokens for ACP
// This file is generated from design-tokens.json
// Do not edit manually - regenerate with design-tokens-converter.py

export const designTokens = {
  colors: {
'''

        # Add colors
        for category, color_values in colors.items():
            ts_code += f"    {category}: {{\n"
            for name, value in color_values.items():
                ts_code += f"      {name}: '{value}',\n"
            ts_code += "    },\n"

        ts_code += '''  },
  spacing: {
'''

        # Add spacing
        for name, value in spacing.items():
            ts_code += f"    {name}: '{value}',\n"

        ts_code += '''  },
  typography: {
'''

        # Add typography
        for category, values in typography.items():
            ts_code += f"    {category}: {{\n"
            if isinstance(values, dict):
                for key, val in values.items():
                    ts_code += f"      {key}: {repr(val)},\n"
            ts_code += "    },\n"

        ts_code += '''  },
  effects: {
'''

        # Add effects
        for category, effect_values in effects.items():
            ts_code += f"    {category}: {{\n"
            for name, value in effect_values.items():
                ts_code += f"      {name}: '{value}',\n"
            ts_code += "    },\n"

        ts_code += '''  },
} as const;

export type DesignTokens = typeof designTokens;
'''

        return ts_code

    def to_css(self, output_path: str) -> None:
        """Convert tokens to CSS custom properties"""
        css_content = self._generate_css()
        Path(output_path).write_text(css_content)
        print(f"✓ Generated CSS tokens: {output_path}")

    def _generate_css(self) -> str:
        """Generate CSS custom properties"""
        css = '''/* Auto-generated CSS custom properties
 * Generated from design-tokens.json
 * Supports both light and dark modes
 */

:root {
  /* Light mode colors (default) */
'''

        # Light mode colors
        light_colors = self.tokens.get('modes', {}).get('light', {}).get('colors', {})
        for category, color_values in light_colors.items():
            for name, value in color_values.items():
                var_name = f"--color-{category}-{name}".replace('_', '-')
                css += f"  {var_name}: {value};\n"

        # Spacing
        css += "\n  /* Spacing scale */\n"
        spacing = self.tokens.get('spacing', {})
        for name, value in spacing.items():
            var_name = f"--space-{name}".replace('_', '-')
            css += f"  {var_name}: {value};\n"

        # Typography
        css += "\n  /* Typography */\n"
        typography = self.tokens.get('typography', {})
        if 'sizes' in typography:
            for name, value in typography['sizes'].items():
                var_name = f"--font-size-{name}".replace('_', '-')
                css += f"  {var_name}: {value};\n"

        # Effects
        css += "\n  /* Effects */\n"
        effects = self.tokens.get('effects', {})
        if 'shadows' in effects:
            for name, value in effects['shadows'].items():
                var_name = f"--shadow-{name}".replace('_', '-')
                css += f"  {var_name}: {value};\n"

        if 'radii' in effects:
            for name, value in effects['radii'].items():
                var_name = f"--radius-{name}".replace('_', '-')
                css += f"  {var_name}: {value};\n"

        # Dark mode
        dark_colors = self.tokens.get('modes', {}).get('dark', {}).get('colors', {})
        css += '''\n}

/* Dark mode colors */
@media (prefers-color-scheme: dark) {
  :root {
'''

        for category, color_values in dark_colors.items():
            for name, value in color_values.items():
                var_name = f"--color-{category}-{name}".replace('_', '-')
                css += f"    {var_name}: {value};\n"

        css += '''  }
}

/* Alternative: dark class selector */
.dark {
'''

        for category, color_values in dark_colors.items():
            for name, value in color_values.items():
                var_name = f"--color-{category}-{name}".replace('_', '-')
                css += f"  {var_name}: {value};\n"

        css += '''}\n'''

        return css

    def to_tailwind(self, output_path: str) -> None:
        """Convert tokens to Tailwind CSS config"""
        tailwind_content = self._generate_tailwind()
        Path(output_path).write_text(tailwind_content)
        print(f"✓ Generated Tailwind config: {output_path}")

    def _generate_tailwind(self) -> str:
        """Generate Tailwind config"""
        light_colors = self.tokens.get('modes', {}).get('light', {}).get('colors', {})
        dark_colors = self.tokens.get('modes', {}).get('dark', {}).get('colors', {})
        spacing = self.tokens.get('spacing', {})

        config = '''/** @type {import('tailwindcss').Config} */

module.exports = {
  theme: {
    extend: {
      colors: {
        acp: {
'''

        # Add light mode colors
        for category, color_values in light_colors.items():
            for name, value in color_values.items():
                config += f"          '{category}-{name}': '{value}',\n"

        config += '''        },
      },
      spacing: {
'''

        # Add spacing
        for name, value in spacing.items():
            config += f"        '{name}': '{value}',\n"

        config += '''      },
    },
  },
  plugins: [],
  darkMode: ['class', 'media'],
  corePlugins: {
    darkMode: true,
  },
};
'''

        return config

    def to_json(self, output_path: str, mode: Optional[str] = None) -> None:
        """Convert/export tokens to JSON format"""
        # Just copy the source JSON if no mode specified, or extract specific mode
        if mode and mode in self.tokens.get('modes', {}):
            filtered = {
                'version': self.tokens.get('version', '1.0.0'),
                'modes': {mode: self.tokens['modes'][mode]},
                'spacing': self.tokens.get('spacing', {}),
                'typography': self.tokens.get('typography', {}),
                'effects': self.tokens.get('effects', {}),
            }
            output_json = json.dumps(filtered, indent=2)
        else:
            output_json = json.dumps(self.tokens, indent=2)

        Path(output_path).write_text(output_json)
        print(f"✓ Generated JSON tokens: {output_path}")


def main():
    parser = argparse.ArgumentParser(
        description='Convert ACP design tokens between formats'
    )

    parser.add_argument('--from', dest='from_format', default='json',
                        help='Source format (default: json)')
    parser.add_argument('--to', dest='to_format', required=True,
                        choices=['typescript', 'css', 'tailwind', 'json'],
                        help='Target format')
    parser.add_argument('--mode', choices=['light', 'dark'], default='light',
                        help='Color mode for generation (default: light)')
    parser.add_argument('--input', required=True,
                        help='Input file path')
    parser.add_argument('--output', required=True,
                        help='Output file path')

    args = parser.parse_args()

    try:
        converter = DesignTokensConverter(args.input)

        if args.to_format == 'typescript':
            converter.to_typescript(args.output, args.mode)
        elif args.to_format == 'css':
            converter.to_css(args.output)
        elif args.to_format == 'tailwind':
            converter.to_tailwind(args.output)
        elif args.to_format == 'json':
            converter.to_json(args.output, args.mode)

        return 0

    except Exception as e:
        print(f"✗ Error: {e}", file=sys.stderr)
        return 1


if __name__ == '__main__':
    sys.exit(main())
