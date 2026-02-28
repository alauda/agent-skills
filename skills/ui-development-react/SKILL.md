---
name: ui-development-react
description: UI design system and visual identity tokens for Alauda Container Platform. Provides design tokens (TypeScript, CSS, JSON), dark mode support, and implementation guidelines for React and other frameworks.
---

# UI Development Skill: ACP Design System

## Overview

The **UI Development Skill** provides a comprehensive design system for Alauda Container Platform (ACP). It encodes the complete visual identity, design tokens, and implementation guidelines that ensure consistency across all ACP user interfaces.

This skill is designed to be used company-wide by:
- Frontend developers building new UI features
- Product designers maintaining visual consistency
- Full-stack engineers integrating design tokens into applications
- Teams adopting ACP design standards

## Visual Identity

### Color Philosophy

ACP uses a **professional, cool-toned palette** emphasizing clarity and information hierarchy:

- **Primary Blues**: Professional, trustworthy feeling (backgrounds, panels, info states)
- **Success Greens**: Positive, completion states (confirmations, successful operations)
- **Process Teals**: Active workflow states (investigations, pending operations)
- **Neutral Grays**: Hierarchy and separation (borders, dividers, subtle elements)

### Color Palette

#### Light Mode (Default)

| Category | Color | Hex | Usage |
|----------|-------|-----|-------|
| **Backgrounds** | Main | #ffffff | Primary content areas |
| | Primary BG | #f4f6f8 | Top chrome, secondary panels |
| | Panel BG | #eef4ff | Left sidebars, guidance areas |
| **Accents** | Info BG | #e3f2fd | Alert boxes, key information |
| | Info Border | #90caf9 | Info element borders |
| **Success** | Success BG | #d7f5e9 | Success states, completion |
| | Success Border | #4caf50 | Success indicators |
| **Process** | Process BG | #e8f2ff | Processing steps, workflows |
| | Process Border | #2196f3 | Process state indicators |
| **Teal** | Teal BG | #e0f2f1 | Hypothesis/investigation states |
| | Teal Border | #4db6ac | Teal state indicators |
| **Borders** | Primary | #cbd7e0 | Panel borders, main dividers |
| | Secondary | #cbd5e1 | Card separators, subtle lines |

#### Dark Mode

Dark mode variants maintain WCAG AA contrast ratios while preserving visual hierarchy:

| Category | Color | Hex | Usage |
|----------|-------|-----|-------|
| **Backgrounds** | Main | #1a1a1a | Primary content areas |
| | Primary BG | #2d3748 | Top chrome, secondary panels |
| | Panel BG | #1e3a5f | Left sidebars, guidance areas |
| **Accents** | Info BG | #1e3a8a | Alert boxes |
| | Info Border | #60a5fa | Info element borders |
| **Success** | Success BG | #064e3b | Success states |
| | Success Border | #10b981 | Success indicators |
| **Process** | Process BG | #1e40af | Processing steps |
| | Process Border | #3b82f6 | Process indicators |
| **Teal** | Teal BG | #134e4a | Hypothesis states |
| | Teal Border | #14b8a6 | Teal indicators |
| **Borders** | Primary | #4b5563 | Panel borders |
| | Secondary | #555d6f | Card separators |

### Spacing System

ACP uses a **10px base unit grid system**:

```
4px   (1 unit)
8px   (2 units)
12px  (3 units)
16px  (4 units) - Standard padding/margin
20px  (5 units)
24px  (6 units) - Large spacing
32px  (8 units) - Section spacing
48px  (12 units)
64px  (16 units) - Major section gaps
```

### Typography

**Font Stack (System Fonts)**
```
font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto,
             "Helvetica Neue", Arial, sans-serif;
```

**Font Sizes**
- **Body**: 14px / 1.5 line-height
- **Small**: 12px / 1.4 line-height
- **Large**: 16px / 1.6 line-height
- **Heading 4**: 18px / 1.4 line-height, 500 weight
- **Heading 3**: 20px / 1.3 line-height, 600 weight
- **Heading 2**: 24px / 1.2 line-height, 600 weight
- **Heading 1**: 32px / 1.1 line-height, 700 weight

**Font Weights**
- 300: Light
- 400: Regular (default)
- 500: Medium (interactive, accents)
- 600: Semi-bold (subheadings)
- 700: Bold (main headings)

### Effects & Interactions

**Border Radius**
- Subtle: 4px (form inputs, small elements)
- Standard: 8px (cards, buttons)
- Large: 12px (panels, containers)
- Extra Large: 16px (major sections)

**Shadows**
- Subtle: `0 1px 2px rgba(0, 0, 0, 0.05)`
- Medium: `0 4px 6px rgba(0, 0, 0, 0.1)`
- Strong: `0 10px 15px rgba(0, 0, 0, 0.15)`

**Transitions**
- Fast: 200ms (micro-interactions, hovers)
- Standard: 300ms (modal opens, page transitions)
- Slow: 500ms (complex animations)

## Design Patterns

### Card Pattern
Cards are the fundamental building block of ACP interfaces:
- White background (#ffffff light, #2d3748 dark)
- Subtle border: 1px solid (#cbd7e0 light, #4b5563 dark)
- Border radius: 8px
- Padding: 16px (4 units)
- Standard shadow

**Variants:**
- **Alert Card**: Blue background (#e3f2fd light) for informational content
- **Success Card**: Green background (#d7f5e9 light) for completion states
- **Process Card**: Teal background (#e0f2f1 light) for workflow states

### Color Usage Guidelines

**Info States (Blue)**
- Use for informational alerts, monitor updates, guidance
- Blue encourages reading and attention without alarm

**Success States (Green)**
- Use for completion, confirmations, successful operations
- Green = "action completed successfully"

**Process States (Teal)**
- Use for investigation steps, workflow states, pending operations
- Teal indicates "something is being processed or analyzed"

**Warning States (Orange/Amber)**
- Reserved for warnings and cautions (not fully implemented yet)
- Use sparingly to indicate issues requiring attention

**Error States (Red)**
- Reserved for critical errors (not in current palette)
- Use for failures and critical alerts

### Layout Patterns

**Standard Layout**
1. **Header/Chrome** - Navigation and title bar (24px height typically)
2. **Left Sidebar** - Guidance, prompts, navigation (280-320px wide)
3. **Content Area** - Main content (flexible width)
4. **Right Panel** (optional) - Details, sidebar (240-280px wide)

**Responsive Behavior**
- Mobile (< 768px): Stack vertically, hide sidebars or use drawer
- Tablet (768px - 1024px): Collapse sidebar to icons
- Desktop (> 1024px): Full layout

### Component Patterns

#### Interactive States

**Buttons/Controls**
- Default: Base color with standard shadow
- Hover: 1 shade darker, medium shadow
- Active: 2 shades darker, strong shadow
- Disabled: Gray (#cbd7e0 light), no shadow, 50% opacity text

**Form Inputs**
- Default: White bg, subtle border
- Focus: Info border color, medium shadow
- Disabled: Gray bg, border, reduced opacity
- Error: Red border, error background tint

#### Data Display

**Tables**
- Header row: Primary background color
- Alternating rows: White and #f4f6f8
- Hover row: #eef4ff highlight
- Borders: Secondary color between rows

**Status Indicators**
- Success badge: Green background + white text
- Warning badge: Orange background + white text
- Error badge: Red background + white text
- Info badge: Blue background + white text

## Localization

ACP interfaces support **English and Simplified Chinese**.

**Guidelines:**
- All text strings should use tokens for dynamic language switching
- Chinese text requires adjusted line heights (1.6-1.8) due to character complexity
- Consider text expansion in layouts (Chinese is more compact than English)
- Use font stacks that support Chinese characters properly

## Accessibility (WCAG AA Compliance)

### Color Contrast

All color combinations meet **WCAG AA minimum 4.5:1 contrast ratio** for text:
- Body text (14px): 4.5:1 minimum
- Large text (18px+): 3:1 minimum
- UI components: 3:1 minimum

### Keyboard Navigation

- All interactive elements must be keyboard accessible
- Focus indicators must be visible (use info border color)
- Tab order should follow logical reading order
- Proper semantic HTML (`<button>`, `<a>`, form elements)

### Screen Readers

- Use semantic HTML structure
- Provide `alt` text for meaningful images
- Use ARIA labels for complex interactions
- Proper heading hierarchy (`<h1>` to `<h6>`)

## Dark Mode Implementation

### Usage Detection

```javascript
// CSS Media Query (preferred)
@media (prefers-color-scheme: dark) {
  /* dark mode styles */
}

// Or with CSS class (for manual toggle)
.dark { /* dark mode styles */ }

// Or in JavaScript
const isDark = window.matchMedia('(prefers-color-scheme: dark)').matches;
```

### Token Adaptation

When implementing dark mode:
1. Use CSS custom properties for color swaps
2. Maintain all contrast ratios
3. Keep accent colors consistent with brand
4. Test all color combinations for readability
5. Ensure dark backgrounds don't cause eye strain

## Integration Guides

### With Next.js + Tailwind CSS

1. Use `tailwind.config.js` from `/tokens/`
2. Extend with Tailwind's theme configuration
3. Access colors via Tailwind classes: `bg-acp-blue-50`, `text-acp-green-600`
4. Dark mode via `dark:` prefix: `dark:bg-acp-blue-900`

### With CSS Variables

1. Import `design-tokens.css` in your main stylesheet
2. Use variables: `background: var(--color-primary-bg)`
3. Override for dark mode in media query
4. Variables are namespaced: `--color-*`, `--space-*`, `--font-*`

### With TypeScript

1. Import from `design-tokens.ts`: `import { designTokens } from '@acp/tokens'`
2. Use in styled-components or CSS-in-JS: `color: designTokens.colors.primary.blue`
3. Type-safe token access with IntelliSense
4. Easy refactoring across codebase

## Common Usage Patterns

### Semantic Color Names

Prefer semantic names over raw hex values:
- ✅ `background-color: var(--color-success-bg);`
- ❌ `background-color: #d7f5e9;`

### Spacing Scales

Always use spacing tokens:
- ✅ `padding: var(--space-4);` (16px)
- ❌ `padding: 16px;`

### Typography Pairs

Follow established typography hierarchy:
- ✅ `<h2>Heading</h2>` with Heading 2 style + `<p>Body</p>` with Body style
- ❌ Mixing font sizes randomly

### Dark Mode Testing

Always test designs in both modes:
- Compare light mode to dark mode side-by-side
- Check all color contrasts in dark mode
- Verify text readability on dark backgrounds
- Test interactive states in both modes

## File Structure

This skill provides several token export formats:

- **TypeScript** (`design-tokens.ts`) - For Next.js/React projects
- **CSS** (`design-tokens.css`) - For any CSS project
- **JSON** (`design-tokens.json`) - For design tools and automation
- **Tailwind Config** (`tailwind.config.js`) - For Tailwind CSS projects
- **CSS Module** (`colors.module.css`) - For CSS Modules projects

## Reference Documentation

Detailed documentation is available in the `/references/` directory:

- `design-tokens.md` - Complete token specifications
- `design-patterns.md` - Visual pattern examples
- `guidelines.md` - Design do's and don'ts
- `accessibility.md` - WCAG compliance details
- `dark-mode.md` - Dark mode implementation guide

## Documentation & Guides

Quick guides available in the `/docs/` directory:

- `quick-start.md` - Getting started with tokens
- `token-usage.md` - How to use different token formats
- `best-practices.md` - Implementation best practices
- `visual-identity.md` - ACP brand identity overview
- `faq.md` - Common questions and answers

## Getting Started

1. **Choose your integration method**:
   - Next.js/React: Use `design-tokens.ts` + Tailwind
   - CSS/SCSS: Use `design-tokens.css` + CSS variables
   - Design Tools: Use `design-tokens.json`

2. **Import or reference tokens** in your project

3. **Apply tokens consistently** throughout your UI

4. **Test in both light and dark modes**

5. **Run design validator** to check for consistency:
   ```bash
   python3 scripts/design-validator.py audit --path=src --mode=dark
   ```

## Support & Maintenance

For questions or to report design system issues, refer to the FAQ or contact the design systems team.

Design tokens are versioned - check `design-tokens.json` for the current version.
