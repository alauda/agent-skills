# ACP UI Development - Quick Start Guide

Get started with ACP design tokens in 5 minutes.

## What Are Design Tokens?

Design tokens are the smallest, atomic units of design. They represent design decisions (colors, spacing, typography) in a reusable format that works across different technologies.

Instead of hardcoding colors like `#d7f5e9`, you use a token name like `--color-success-bg`.

## Choose Your Integration Method

### 1. CSS Variables (Any Project)

**Easiest for:** CSS/SCSS projects, basic websites

```html
<!-- Link the CSS file -->
<link rel="stylesheet" href="path/to/design-tokens.css">
```

```css
/* Use tokens directly in CSS */
body {
  background-color: var(--color-backgrounds-main);
  color: var(--color-text-primary);
}

/* Automatically switches to dark mode */
```

**Dark mode:** Automatic! Respects system preference and `.dark` class.

### 2. TypeScript/JavaScript (Next.js/React)

**Easiest for:** React, Next.js, TypeScript projects

```bash
# Copy design-tokens.ts to your project
cp design-tokens.ts src/lib/tokens.ts
```

```typescript
// Import tokens
import { designTokens } from '@/lib/tokens';

// Use in styled-components or CSS-in-JS
const styles = {
  container: {
    backgroundColor: designTokens.colors.light.backgrounds.main,
    color: designTokens.colors.light.text.primary,
  },
};
```

**For dark mode:**
```typescript
const bgColor = isDarkMode
  ? designTokens.colors.dark.backgrounds.main
  : designTokens.colors.light.backgrounds.main;
```

### 3. Tailwind CSS (Next.js/React with Tailwind)

**Easiest for:** Next.js/React using Tailwind

```javascript
// Copy tailwind.config.js or merge it with yours
module.exports = {
  // ... existing config
  theme: {
    extend: {
      colors: {
        acp: {
          'bg-main': '#ffffff',
          'bg-primary': '#f4f6f8',
          // ... all ACP colors
        },
      },
    },
  },
  darkMode: ['class', 'media'],
};
```

```jsx
// Use Tailwind classes
<div className="bg-acp-bg-main dark:bg-acp-dark-bg-main text-acp-text-primary dark:text-acp-dark-text-primary">
  Content
</div>
```

**Dark mode:** Automatic via `dark:` prefix or system preference

### 4. JSON (Design Tools, Automation)

**Easiest for:** Figma plugins, design tool integration

```javascript
// Load tokens
fetch('design-tokens.json')
  .then(res => res.json())
  .then(tokens => {
    const lightColors = tokens.modes.light.colors;
    const darkColors = tokens.modes.dark.colors;
  });
```

## Basic Usage Examples

### Change Background Color
```css
/* Before: Hardcoded */
body { background-color: #f4f6f8; }

/* After: Using token */
body { background-color: var(--color-backgrounds-primary); }
```

### Create an Alert Card
```html
<!-- HTML -->
<div class="alert-card">
  <h3>Information</h3>
  <p>This is an info message</p>
</div>

<!-- CSS -->
<style>
.alert-card {
  background-color: var(--color-info-bg);
  border: 1px solid var(--color-info-border);
  border-radius: var(--radius-md);
  padding: var(--space-px4);
  box-shadow: var(--shadow-subtle);
}

.alert-card h3 {
  color: var(--color-text-primary);
  font-size: var(--font-size-lg);
  font-weight: 600;
}

.alert-card p {
  color: var(--color-text-secondary);
  font-size: var(--font-size-base);
  margin-top: var(--space-px2);
}
</style>
```

### Success State Button
```jsx
<button className="btn btn-success">
  Operation Successful
</button>

<style>
.btn {
  padding: var(--space-px4);
  border-radius: var(--radius-md);
  font-size: var(--font-size-base);
  font-weight: 500;
  border: none;
  cursor: pointer;
  transition: all var(--transition-fast);
}

.btn-success {
  background-color: var(--color-success-bg);
  color: var(--color-success-dark);
  border: 1px solid var(--color-success-border);
}

.btn-success:hover {
  background-color: var(--color-success-border);
  color: white;
}
</style>
```

## Common Tasks

### Set Up Dark Mode
```html
<!-- CSS approach (automatic) -->
<link rel="stylesheet" href="design-tokens.css">
<!-- Automatically includes dark mode! -->

<!-- OR class-based approach -->
<html class="dark">
  <!-- Add .dark class to enable dark mode -->
</html>
```

### Use Spacing Consistently
```css
/* Never use arbitrary values */
padding: 13px;        /* ❌ Don't */
padding: var(--space-px4);  /* ✅ Do */

/* Standard spacing values: 4px, 8px, 12px, 16px, 20px, 24px, 32px, 48px, 64px */
```

### Create Card Components
```html
<div class="card">
  <h2>Card Title</h2>
  <p>Card content</p>
</div>

<style>
.card {
  background-color: var(--color-backgrounds-main);
  border: 1px solid var(--color-borders-primary);
  border-radius: var(--radius-md);
  padding: var(--space-px4);
  box-shadow: var(--shadow-medium);
}
</style>
```

### Match Text Color to Background
```css
/* Light background: Dark text */
.light-bg {
  background-color: var(--color-backgrounds-panel);  /* Light blue */
  color: var(--color-text-primary);                   /* Dark text */
}

/* Dark background: Light text */
.dark-bg {
  background-color: var(--color-backgrounds-primary); /* Dark gray */
  color: var(--color-text-primary);                   /* Light text when in dark mode */
}
```

## File Locations

All token files are in `.claude/skills/ui-development/tokens/`:

- **design-tokens.json** - Source (canonical format)
- **design-tokens.ts** - TypeScript (React/Next.js)
- **design-tokens.css** - CSS custom properties
- **design-tokens.module.css** - CSS module
- **tailwind.config.js** - Tailwind configuration
- **colors.module.css** - CSS utilities

## Next Steps

1. **Choose integration method** (CSS, TypeScript, Tailwind, or JSON)
2. **Copy token files** to your project
3. **Import/link tokens** in your code
4. **Replace hardcoded colors** with token variables
5. **Test in dark mode** - Should work automatically!

## Quick Reference

### Color Usage
- **Blue (#90caf9)** - Information, alerts, guidance
- **Green (#4caf50)** - Success, completion, confirmations
- **Teal (#4db6ac)** - Processing, investigation, workflow
- **Gray (#cbd7e0)** - Borders, dividers, inactive

### Spacing Scale
- **4px** - Minimal spacing
- **8px** - Small gaps
- **12px** - Comfortable spacing
- **16px** - Standard padding
- **24px** - Large spacing
- **32px+** - Section breaks

### Font Sizes
- **12px (xs)** - Small labels
- **14px (sm)** - Form text, helpers
- **16px (base)** - Body text (default)
- **18px (lg)** - Large text
- **24px (2xl)** - Section headings
- **32px+ (3xl, 4xl)** - Page headings

## Troubleshooting

### Colors not showing
- Check token file is imported/linked
- Verify CSS variable names are correct
- Check browser DevTools > Computed styles

### Dark mode not working
- Make sure CSS file imported (includes dark mode)
- Check system preference or `.dark` class
- Test in DevTools > Rendering > Emulate CSS media feature

### Colors look wrong
- Verify using correct token for the context
- Check contrast (should be 4.5:1+)
- Test in both light and dark modes

## Get Help

See detailed guides:
- **Token Reference**: `reference/design-tokens.md`
- **Design Patterns**: `reference/design-patterns.md`
- **Guidelines**: `reference/guidelines.md`
- **Accessibility**: `reference/accessibility.md`
- **Dark Mode**: `reference/dark-mode.md`

Or check the **FAQ**: `docs/faq.md`
