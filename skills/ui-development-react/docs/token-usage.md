# ACP Design Tokens - Usage Guide

Detailed guide for using design tokens in different contexts.

## Color Tokens

### Accessing Colors by Category

```typescript
// TypeScript access pattern
designTokens.colors.light.{category}.{name}

Examples:
- designTokens.colors.light.backgrounds.main
- designTokens.colors.light.info.bg
- designTokens.colors.light.success.border
- designTokens.colors.light.text.primary
```

### CSS Variable Pattern

```css
--color-{category}-{name}

Examples:
--color-backgrounds-main
--color-info-bg
--color-success-border
--color-text-primary
```

### Color Categories & Usage

#### Backgrounds
```css
/* Main backgrounds */
--color-backgrounds-main: #ffffff;         /* Primary content area */
--color-backgrounds-primary: #f4f6f8;      /* Top chrome, panels */
--color-backgrounds-panel: #eef4ff;        /* Sidebars, guidance */
--color-backgrounds-secondary: #fafafa;    /* Alternate backgrounds */
```

**Usage Example:**
```css
.page { background-color: var(--color-backgrounds-main); }
.header { background-color: var(--color-backgrounds-primary); }
.sidebar { background-color: var(--color-backgrounds-panel); }
```

#### Info (Blue)
```css
--color-info-bg: #e3f2fd;        /* Light blue background */
--color-info-border: #90caf9;    /* Blue border */
--color-info-dark: #1e3a8a;      /* Dark blue (dark mode) */
```

**Usage Example:**
```css
.alert {
  background-color: var(--color-info-bg);
  border: 1px solid var(--color-info-border);
  color: var(--color-info-dark);
}
```

#### Success (Green)
```css
--color-success-bg: #d7f5e9;      /* Light green background */
--color-success-border: #4caf50;  /* Green border */
--color-success-dark: #064e3b;    /* Dark green (dark mode) */
```

**Usage Example:**
```css
.success-badge {
  background-color: var(--color-success-bg);
  border: 1px solid var(--color-success-border);
  color: white;
}
```

#### Process (Blue Process)
```css
--color-process-bg: #e8f2ff;     /* Light blue background */
--color-process-border: #2196f3; /* Process blue border */
--color-process-dark: #1e40af;   /* Dark process blue */
```

**Usage Example:**
```css
.processing {
  background-color: var(--color-process-bg);
  border: 1px solid var(--color-process-border);
}
```

#### Text Colors
```css
--color-text-primary: #1a202c;     /* Main text */
--color-text-secondary: #4a5568;   /* Secondary text */
--color-text-tertiary: #718096;    /* Tertiary/hint text */
--color-text-disabled: #cbd5e0;    /* Disabled text */
```

**Usage Example:**
```css
body { color: var(--color-text-primary); }
.label { color: var(--color-text-secondary); }
.hint { color: var(--color-text-tertiary); }
.disabled { color: var(--color-text-disabled); }
```

#### Border Colors
```css
--color-borders-primary: #cbd7e0;   /* Main borders */
--color-borders-secondary: #cbd5e1; /* Secondary borders */
--color-borders-light: #e2e8f0;     /* Light borders */
```

**Usage Example:**
```css
.card { border: 1px solid var(--color-borders-primary); }
.divider { border-top: 1px solid var(--color-borders-secondary); }
.subtle { border: 1px solid var(--color-borders-light); }
```

## Spacing Tokens

### Spacing Scale
```css
--space-px0: 0;          /* 0px */
--space-px1: 0.25rem;    /* 4px */
--space-px2: 0.5rem;     /* 8px */
--space-px4: 1rem;       /* 16px - Standard padding */
--space-px6: 1.5rem;     /* 12px - Note: Non-standard but intentional */
--space-px8: 2rem;       /* 32px */
--space-px12: 3rem;      /* 48px */
--space-px16: 4rem;      /* 64px */
--space-px20: 5rem;      /* 80px */
--space-px24: 6rem;      /* 96px */
--space-px32: 8rem;      /* 128px */
--space-px48: 12rem;     /* 192px */
--space-px64: 16rem;     /* 256px */
```

### Using Spacing

```css
/* Padding */
.component {
  padding: var(--space-px4);              /* 16px */
  padding-top: var(--space-px6);          /* 12px */
  padding-bottom: var(--space-px6);       /* 12px */
}

/* Margin */
.section {
  margin-bottom: var(--space-px8);        /* 32px */
  margin-top: var(--space-px4);           /* 16px */
}

/* Gap in Grid/Flex */
.grid {
  display: grid;
  gap: var(--space-px4);                  /* 16px gap */
}

/* Width/Height (rarely) */
.sidebar {
  width: var(--space-px48);               /* 192px */
}
```

## Typography Tokens

### Font Size

```css
--font-size-xs: 0.75rem;    /* 12px - Small labels */
--font-size-sm: 0.875rem;   /* 14px - Form helper text */
--font-size-base: 1rem;     /* 16px - Body text (default) */
--font-size-lg: 1.125rem;   /* 18px - Large text */
--font-size-xl: 1.25rem;    /* 20px - Subheadings */
--font-size-2xl: 1.5rem;    /* 24px - Section headings */
--font-size-3xl: 1.875rem;  /* 30px - Page headings */
--font-size-4xl: 2.25rem;   /* 36px - Hero headings */
```

**Usage Example:**
```css
body { font-size: var(--font-size-base); }
h1 { font-size: var(--font-size-4xl); }
h2 { font-size: var(--font-size-2xl); }
h3 { font-size: var(--font-size-xl); }
.small { font-size: var(--font-size-sm); }
```

### Line Height

```css
--line-height-tight: 1.1;      /* Headings */
--line-height-snug: 1.2;       /* Subheadings */
--line-height-normal: 1.5;     /* Body text */
--line-height-relaxed: 1.6;    /* Body text with more space */
--line-height-loose: 1.8;      /* Chinese text, accessibility */
```

**Usage Example:**
```css
body { line-height: var(--line-height-normal); }
h1 { line-height: var(--line-height-tight); }
.chinese { line-height: var(--line-height-loose); }
.accessible { line-height: var(--line-height-relaxed); }
```

### Font Family

```css
--font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto,
               'Helvetica Neue', Arial, sans-serif;
```

**Usage Example:**
```css
body { font-family: var(--font-family); }
```

## Effects Tokens

### Shadows

```css
--shadow-none: none;
--shadow-subtle: 0 1px 2px rgba(0, 0, 0, 0.05);
--shadow-medium: 0 4px 6px rgba(0, 0, 0, 0.1);
--shadow-strong: 0 10px 15px rgba(0, 0, 0, 0.15);
```

**Usage Example:**
```css
.card { box-shadow: var(--shadow-medium); }
.flat { box-shadow: var(--shadow-none); }
.elevated { box-shadow: var(--shadow-strong); }
:focus { box-shadow: var(--shadow-strong); }
```

### Border Radius

```css
--radius-sm: 4px;     /* Small elements */
--radius-md: 8px;     /* Standard (cards, buttons) */
--radius-lg: 12px;    /* Panels, containers */
--radius-xl: 16px;    /* Large sections */
```

**Usage Example:**
```css
input { border-radius: var(--radius-sm); }
button { border-radius: var(--radius-md); }
.panel { border-radius: var(--radius-lg); }
.modal { border-radius: var(--radius-xl); }
```

### Transitions

```css
--transition-fast: 200ms;       /* Quick interactions */
--transition-standard: 300ms;   /* Normal interactions */
--transition-slow: 500ms;       /* Complex animations */
```

**Usage Example:**
```css
button {
  transition: all var(--transition-fast);
}

.modal {
  transition: all var(--transition-slow);
}

@keyframes fadeIn {
  from { opacity: 0; }
  to { opacity: 1; }
}

.content {
  animation: fadeIn var(--transition-standard) ease-in-out;
}
```

## Dark Mode Token Access

### TypeScript Dark Mode

```typescript
const bgColor = isDarkMode
  ? designTokens.colors.dark.backgrounds.main
  : designTokens.colors.light.backgrounds.main;

// Or use a helper function
function getColor(category: string, name: string, isDark: boolean) {
  const colors = isDark
    ? designTokens.colors.dark[category]
    : designTokens.colors.light[category];
  return colors[name];
}

// Usage
const infoBg = getColor('info', 'bg', isDarkMode);
```

### CSS Dark Mode (Automatic)

```css
/* Light mode (default) */
:root {
  --color-bg-main: #ffffff;
  --color-text-primary: #1a202c;
}

/* Dark mode automatically switches */
@media (prefers-color-scheme: dark) {
  :root {
    --color-bg-main: #1a1a1a;
    --color-text-primary: #f3f4f6;
  }
}

/* Usage: Colors automatically update! */
body {
  background-color: var(--color-bg-main);
  color: var(--color-text-primary);
}
```

## Common Patterns

### Button Component
```css
.btn {
  padding: var(--space-px4);
  border-radius: var(--radius-md);
  font-size: var(--font-size-base);
  font-weight: 500;
  border: none;
  cursor: pointer;
  transition: all var(--transition-fast);
}

.btn-primary {
  background-color: var(--color-info-border);
  color: white;
}

.btn-primary:hover {
  background-color: var(--color-info-dark);
  box-shadow: var(--shadow-medium);
}

.btn:disabled {
  background-color: var(--color-borders-primary);
  color: var(--color-text-disabled);
  cursor: not-allowed;
}
```

### Card Component
```css
.card {
  background-color: var(--color-backgrounds-main);
  border: 1px solid var(--color-borders-primary);
  border-radius: var(--radius-md);
  padding: var(--space-px4);
  box-shadow: var(--shadow-subtle);
}

.card-title {
  font-size: var(--font-size-lg);
  font-weight: 600;
  color: var(--color-text-primary);
  margin-bottom: var(--space-px2);
}

.card-description {
  font-size: var(--font-size-base);
  color: var(--color-text-secondary);
  line-height: var(--line-height-normal);
}
```

### Alert Component
```css
.alert {
  border-radius: var(--radius-md);
  padding: var(--space-px4);
  margin-bottom: var(--space-px4);
}

.alert-info {
  background-color: var(--color-info-bg);
  border: 1px solid var(--color-info-border);
  color: var(--color-info-dark);
}

.alert-success {
  background-color: var(--color-success-bg);
  border: 1px solid var(--color-success-border);
  color: var(--color-success-dark);
}
```

### Form Input
```css
input,
select,
textarea {
  padding: var(--space-px2) var(--space-px4);
  border: 1px solid var(--color-borders-primary);
  border-radius: var(--radius-sm);
  font-size: var(--font-size-base);
  font-family: var(--font-family);
  transition: all var(--transition-fast);
}

input:focus,
select:focus,
textarea:focus {
  outline: none;
  border-color: var(--color-info-border);
  box-shadow: 0 0 0 3px var(--color-info-bg);
}

input:disabled,
select:disabled,
textarea:disabled {
  background-color: var(--color-borders-light);
  color: var(--color-text-disabled);
  cursor: not-allowed;
}
```

## Tips & Best Practices

### ✅ DO
- Always use tokens instead of hardcoding colors
- Pair similar tokens consistently
- Test in both light and dark modes
- Use semantic color names when possible

### ❌ DON'T
- Don't mix token and hardcoded values
- Don't override tokens without good reason
- Don't ignore dark mode
- Don't use arbitrary values

## Converting Existing Code

### Before (Bad)
```css
.component {
  background-color: #f4f6f8;
  color: #1a202c;
  border: 1px solid #cbd7e0;
  padding: 16px;
  margin: 12px;
  border-radius: 8px;
  box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
}
```

### After (Good)
```css
.component {
  background-color: var(--color-backgrounds-primary);
  color: var(--color-text-primary);
  border: 1px solid var(--color-borders-primary);
  padding: var(--space-px4);
  margin: var(--space-px3);
  border-radius: var(--radius-md);
  box-shadow: var(--shadow-medium);
}
```

## Migration Checklist

- [ ] All colors use `--color-*` tokens or TypeScript imports
- [ ] All spacing uses `--space-*` tokens
- [ ] All typography uses font tokens
- [ ] All shadows use `--shadow-*` tokens
- [ ] All radii use `--radius-*` tokens
- [ ] All transitions use `--transition-*` tokens
- [ ] Dark mode tested and working
- [ ] No hardcoded hex colors remain
- [ ] No arbitrary pixel values remain
- [ ] Design validator passes
