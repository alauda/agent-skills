# ACP Dark Mode Implementation Guide

Comprehensive guide for implementing dark mode using ACP design tokens.

## Overview

ACP design tokens fully support dark mode with:
- **Full color palette** for dark backgrounds
- **WCAG AA contrast compliance** in both modes
- **Multiple implementation methods** (CSS media queries, class-based, system preference)
- **Seamless user experience** across light and dark interfaces

## Color Palette: Dark Mode

### Dark Mode Hex Values

All dark mode colors are optimized for:
- Readability on dark backgrounds
- Reduced eye strain in low-light environments
- WCAG AA contrast compliance
- Visual hierarchy consistency

| Element | Light | Dark | Ratio |
|---------|-------|------|-------|
| **Backgrounds** | - | - | - |
| Main bg | #ffffff | #1a1a1a | - |
| Primary bg | #f4f6f8 | #2d3748 | - |
| Panel bg | #eef4ff | #1e3a5f | - |
| **Info** | - | - | - |
| Info bg | #e3f2fd | #1e3a8a | - |
| Info border | #90caf9 | #60a5fa | 4.5:1 |
| **Success** | - | - | - |
| Success bg | #d7f5e9 | #064e3b | - |
| Success border | #4caf50 | #10b981 | 4.5:1 |
| **Process** | - | - | - |
| Process bg | #e8f2ff | #1e40af | - |
| Process border | #2196f3 | #3b82f6 | 4.5:1 |
| **Text** | - | - | - |
| Primary text | #1a202c | #f3f4f6 | 15:1 |
| Secondary text | #4a5568 | #e5e7eb | 13:1 |
| Tertiary text | #718096 | #d1d5db | 10:1 |

## Implementation Methods

### Method 1: CSS Media Query (Recommended)

Automatically uses system dark mode preference:

```css
/* Default: Light mode */
:root {
  --color-bg-main: #ffffff;
  --color-text-primary: #1a202c;
  /* ... other light colors ... */
}

/* Dark mode: When system prefers dark */
@media (prefers-color-scheme: dark) {
  :root {
    --color-bg-main: #1a1a1a;
    --color-text-primary: #f3f4f6;
    /* ... other dark colors ... */
  }
}

/* Usage: Colors automatically update */
body {
  background-color: var(--color-bg-main);
  color: var(--color-text-primary);
}
```

**Pros:**
- Respects user's system preference
- No JavaScript needed
- Simplest implementation
- Works in all modern browsers

**Cons:**
- Can't provide manual toggle (without JavaScript)

### Method 2: Class-Based Toggle

Manual toggle with `.dark` class:

```html
<!-- HTML structure -->
<div class="dark">
  <!-- Dark mode content -->
</div>
```

```css
/* Light mode (default) */
:root {
  --color-bg-main: #ffffff;
  --color-text-primary: #1a202c;
}

/* Dark mode: Add .dark class anywhere in hierarchy */
.dark {
  --color-bg-main: #1a1a1a;
  --color-text-primary: #f3f4f6;
}

/* Usage: CSS variables update */
body {
  background-color: var(--color-bg-main);
  color: var(--color-text-primary);
}
```

```javascript
// JavaScript toggle
function toggleDarkMode() {
  document.documentElement.classList.toggle('dark');
  localStorage.setItem(
    'theme',
    document.documentElement.classList.contains('dark') ? 'dark' : 'light'
  );
}

// Load saved preference
function initDarkMode() {
  const savedTheme = localStorage.getItem('theme');
  if (savedTheme === 'dark') {
    document.documentElement.classList.add('dark');
  }
}

// On page load
window.addEventListener('load', initDarkMode);
```

**Pros:**
- User can manually toggle
- Can save preference to localStorage
- Full control over when dark mode applies

**Cons:**
- Requires JavaScript
- More implementation complexity

### Method 3: Combined Approach (Best Practice)

Respects system preference + allows manual override:

```javascript
// Combined approach: System preference + manual toggle
function initDarkMode() {
  const savedTheme = localStorage.getItem('theme');
  const prefersDark = window.matchMedia(
    '(prefers-color-scheme: dark)'
  ).matches;

  // Use saved preference, fall back to system preference
  const isDark = savedTheme === 'dark' || (savedTheme !== 'light' && prefersDark);

  if (isDark) {
    document.documentElement.classList.add('dark');
  }
}

function toggleDarkMode() {
  const isDark = document.documentElement.classList.toggle('dark');
  localStorage.setItem('theme', isDark ? 'dark' : 'light');
}

// Listen for system preference changes
window
  .matchMedia('(prefers-color-scheme: dark)')
  .addEventListener('change', (e) => {
    if (!localStorage.getItem('theme')) {
      // Only auto-update if user hasn't manually set theme
      if (e.matches) {
        document.documentElement.classList.add('dark');
      } else {
        document.documentElement.classList.remove('dark');
      }
    }
  });

// Initialize on page load
window.addEventListener('load', initDarkMode);
```

## Using ACP Token Files

### With CSS Variables (design-tokens.css)

```html
<!-- Import ACP tokens -->
<link rel="stylesheet" href="path/to/design-tokens.css">
```

```css
/* CSS automatically includes dark mode */
:root { /* Light mode colors */ }
@media (prefers-color-scheme: dark) { :root { /* Dark colors */ } }

/* Use variables directly */
body {
  background-color: var(--color-backgrounds-main);
  color: var(--color-text-primary);
}
```

### With Tailwind CSS (tailwind.config.js)

```javascript
// Import ACP config
const acpConfig = require('path/to/tailwind.config.js');

module.exports = {
  ...acpConfig,
  darkMode: ['class', 'media'],
  // ... other config
};
```

```html
<!-- Use Tailwind dark mode utilities -->
<div class="bg-acp-bg-main dark:bg-acp-dark-bg-main">
  Content
</div>
```

### With TypeScript (design-tokens.ts)

```typescript
import { designTokens } from './design-tokens.ts';

// Access colors based on mode
const bgColor = isDarkMode
  ? designTokens.colors.dark.backgrounds.main
  : designTokens.colors.light.backgrounds.main;
```

## Testing Dark Mode

### Visual Inspection
1. Enable dark mode in your system settings
2. Load the application
3. Verify all colors are correct
4. Check contrast ratios meet WCAG AA

### Contrast Testing
```javascript
// Function to check contrast ratio
function getContrastRatio(color1, color2) {
  // Convert hex to RGB, calculate relative luminance, compute ratio
  // Use tools: WebAIM Contrast Checker
}
```

### Browser Tools
```css
/* Chrome DevTools: Color Picker */
/* 1. Inspect element with color
   2. Click color swatch in Styles
   3. Check contrast ratio
   4. Ensure 4.5:1 minimum for text */
```

### Testing Checklist
- [ ] All backgrounds are dark (no bright colors)
- [ ] All text is light (no dark text)
- [ ] Contrast ratios meet 4.5:1 (normal text) / 3:1 (large text)
- [ ] Borders are visible (not too dark)
- [ ] Shadows are visible (not too dark)
- [ ] Links are distinguishable
- [ ] Focus indicators visible
- [ ] Icons/images readable
- [ ] Cards have proper borders/shadows
- [ ] Disabled states clear
- [ ] Empty states visible
- [ ] Loading states visible
- [ ] Error messages readable
- [ ] Status badges clear

## Common Dark Mode Issues

### Issue 1: Text Too Dark
**Problem:** Dark text on dark background (low contrast)

```css
/* Bad: Dark gray on dark background */
color: #4a5568;  /* Secondary text color from light mode */
background-color: #1a1a1a;
/* Contrast: 3:1 - FAILS */

/* Good: Light gray on dark background */
color: #e5e7eb;  /* Secondary text color from dark mode */
background-color: #1a1a1a;
/* Contrast: 13:1 - PASSES */
```

**Solution:** Use dark-mode-specific text colors

### Issue 2: Borders Invisible
**Problem:** Dark borders on dark background

```css
/* Bad: Dark border on dark background */
border: 1px solid #555d6f;
background-color: #1a1a1a;
/* Invisible! */

/* Good: Use darker shade or CSS variable */
border: 1px solid var(--color-borders-primary);
/* Automatically updates in dark mode */
```

**Solution:** Use CSS variables for borders

### Issue 3: Shadows Not Visible
**Problem:** Shadows have no effect on dark backgrounds

```css
/* Bad: Shadow doesn't show on dark bg */
box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
background-color: #2d3748;
/* Too subtle to see */

/* Good: Adjust shadow for dark mode */
box-shadow: 0 4px 6px rgba(0, 0, 0, 0.3);
@media (prefers-color-scheme: dark) {
  box-shadow: 0 4px 6px rgba(255, 255, 255, 0.1);  /* Light shadow */
}
```

**Solution:** Adjust shadows for dark backgrounds

### Issue 4: Images Too Bright
**Problem:** Images not adjusted for dark mode

```html
<!-- Bad: Bright image on dark background -->
<img src="bright-chart.png" alt="Chart">

<!-- Good: Provide dark-mode version -->
<img
  class="light-mode"
  src="bright-chart.png"
  alt="Chart"
>
<img
  class="dark-mode"
  src="dark-chart.png"
  alt="Chart"
>

<style>
.light-mode { display: block; }
.dark-mode { display: none; }

@media (prefers-color-scheme: dark) {
  .light-mode { display: none; }
  .dark-mode { display: block; }
}
</style>
```

**Solution:** Provide dark-mode-specific images or adjust via CSS

## Dark Mode CSS Patterns

### Pattern 1: Full Theme Switch
```css
:root {
  --bg-primary: #ffffff;
  --text-primary: #1a202c;
  --border-color: #cbd7e0;
}

@media (prefers-color-scheme: dark) {
  :root {
    --bg-primary: #1a1a1a;
    --text-primary: #f3f4f6;
    --border-color: #4b5563;
  }
}

/* All elements automatically switch */
body { background: var(--bg-primary); color: var(--text-primary); }
```

### Pattern 2: Selective Override
```css
/* Use light mode by default */
color: #1a202c;

/* Override for dark mode only */
@media (prefers-color-scheme: dark) {
  color: #f3f4f6;
}
```

### Pattern 3: Filter Adjustments
```css
/* Darken images in light mode, brighten in dark mode */
img { filter: brightness(1); }

@media (prefers-color-scheme: dark) {
  img { filter: brightness(1.1); }
}
```

## Framework-Specific Implementation

### Next.js
```javascript
// next.config.js
module.exports = {
  // Dark mode support
};
```

```jsx
// pages/_app.tsx
import { useEffect, useState } from 'react';

export default function App() {
  const [isDark, setIsDark] = useState(false);

  useEffect(() => {
    const prefersDark = window.matchMedia('(prefers-color-scheme: dark)').matches;
    setIsDark(prefersDark);
  }, []);

  return (
    <div className={isDark ? 'dark' : ''}>
      {/* Content */}
    </div>
  );
}
```

### React
```jsx
import { createContext, useState, useEffect } from 'react';

export const ThemeContext = createContext();

export function ThemeProvider({ children }) {
  const [isDark, setIsDark] = useState(false);

  useEffect(() => {
    const prefersDark = window.matchMedia('(prefers-color-scheme: dark)').matches;
    setIsDark(prefersDark);
  }, []);

  const toggleTheme = () => {
    setIsDark(!isDark);
    localStorage.setItem('theme', isDark ? 'light' : 'dark');
  };

  return (
    <ThemeContext.Provider value={{ isDark, toggleTheme }}>
      {children}
    </ThemeContext.Provider>
  );
}
```

### Vue
```vue
<template>
  <div :class="{ dark: isDark }">
    <!-- Content -->
  </div>
</template>

<script>
export default {
  data() {
    return {
      isDark: false,
    };
  },
  mounted() {
    this.isDark = window.matchMedia('(prefers-color-scheme: dark)').matches;
  },
};
</script>
```

## Accessibility in Dark Mode

### Contrast Requirements (Same in Both Modes)
- Normal text: 4.5:1 minimum
- Large text (18px+): 3:1 minimum
- UI components: 3:1 minimum

### Testing Dark Mode Accessibility
1. Enable dark mode
2. Test with WAVE or Axe DevTools
3. Verify all contrast ratios
4. Test keyboard navigation (should be identical)
5. Test with screen reader (colors shouldn't matter)

### Focus Indicators
Focus indicators must be visible in both modes:

```css
:focus {
  outline: 2px solid var(--color-info-border);  /* Automatic mode switch */
  outline-offset: 2px;
}
```

## Performance Considerations

### Optimization Tips
1. **Use CSS variables**: No JavaScript overhead
2. **Avoid JavaScript for system preference**: Use media queries
3. **Cache preference**: Store in localStorage
4. **Lazy load images**: Load dark-mode images only when needed
5. **Use CSS filters sparingly**: They're resource-intensive

### Bundle Size
- CSS approach: ~2KB additional CSS
- JavaScript approach: ~1KB additional JS
- Combined: ~3KB total overhead

## Troubleshooting Dark Mode

### Dark mode not activating
```javascript
// Check system preference
const prefersDark = window.matchMedia('(prefers-color-scheme: dark)').matches;
console.log('System prefers dark:', prefersDark);

// Check class
console.log('Has dark class:', document.documentElement.classList.contains('dark'));

// Check CSS variables
console.log(getComputedStyle(document.documentElement).getPropertyValue('--color-bg-main'));
```

### Colors not updating
```css
/* Make sure using CSS variables */
background-color: var(--color-bg-main);  /* Good */
background-color: #ffffff;               /* Bad */
```

### Contrast still failing
```css
/* Use ACP tokens, not custom colors */
color: var(--color-text-primary);     /* Guaranteed WCAG AA */
color: #888888;                        /* Might fail dark mode */
```

## Resources

- [MDN: Prefers Color Scheme](https://developer.mozilla.org/en-US/docs/Web/CSS/@media/prefers-color-scheme)
- [CSS Tricks: Dark Mode](https://css-tricks.com/a-complete-guide-to-dark-mode-on-the-web/)
- [Web.dev: Dark Mode](https://web.dev/prefers-color-scheme/)
- [WCAG Dark Mode](https://www.w3.org/WAI/test-evaluate/contrast.html)
