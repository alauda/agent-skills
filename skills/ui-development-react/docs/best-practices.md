# ACP UI Development - Best Practices

Production-ready guidelines for implementing ACP design system.

## Design Token Best Practices

### 1. Always Use Tokens
**Rule:** Never hardcode colors, spacing, or typography values.

```javascript
// ❌ Bad
const styles = {
  backgroundColor: '#f4f6f8',
  padding: '16px',
  fontSize: '16px',
};

// ✅ Good
import { designTokens } from '@/lib/tokens';

const styles = {
  backgroundColor: designTokens.colors.light.backgrounds.primary,
  padding: designTokens.spacing.px4,
  fontSize: designTokens.typography.sizes.base,
};
```

### 2. Maintain Consistent Spacing Ratios
**Rule:** Use the spacing scale consistently. Never create custom spacing values.

```css
/* ❌ Bad: Custom spacing values */
.card {
  padding: 13px;    /* Not in scale */
  margin: 25px;     /* Not in scale */
  gap: 7px;         /* Not in scale */
}

/* ✅ Good: Using spacing scale */
.card {
  padding: var(--space-px4);    /* 16px */
  margin: var(--space-px6);     /* 12px */
  gap: var(--space-px2);        /* 8px */
}
```

### 3. Follow Typography Hierarchy
**Rule:** Use heading and text sizes in order. Don't skip levels.

```html
<!-- ❌ Bad: Skipped hierarchy -->
<h1>Page Title</h1>
<h3>This should be h2</h3>

<!-- ✅ Good: Proper hierarchy -->
<h1>Page Title</h1>
<h2>Section Title</h2>
<h3>Subsection Title</h3>
```

### 4. Use Semantic Color Names
**Rule:** Choose colors based on semantic meaning, not arbitrary preference.

```css
/* ❌ Bad: Arbitrary color choice */
.status {
  background-color: var(--color-info-bg);  /* Not a status state */
  color: var(--color-info-dark);
}

/* ✅ Good: Semantic color selection */
.processing {
  background-color: var(--color-process-bg);
  border-color: var(--color-process-border);
}

.success {
  background-color: var(--color-success-bg);
  border-color: var(--color-success-border);
}
```

### 5. Test Everything in Dark Mode
**Rule:** All UIs must look good in both light and dark modes.

```css
/* ❌ Bad: Not tested in dark mode */
.component {
  background-color: var(--color-info-bg);  /* May look wrong in dark */
  color: #1a202c;                           /* Hard to read in dark */
}

/* ✅ Good: Tested in both modes */
.component {
  background-color: var(--color-info-bg);
  color: var(--color-text-primary);  /* Auto-switches in dark mode */
}
```

## Component Development Best Practices

### 6. Make Focus States Obvious
**Rule:** All interactive elements must have visible focus indicators.

```css
/* ❌ Bad: Hidden focus state */
button:focus {
  outline: none;  /* Inaccessible! */
}

/* ✅ Good: Visible focus indicator */
button:focus {
  outline: 2px solid var(--color-info-border);
  outline-offset: 2px;
}
```

### 7. Provide Clear Hover States
**Rule:** Interactive elements should give visual feedback on hover.

```css
/* ❌ Bad: No hover feedback */
button {
  background-color: var(--color-info-border);
}

/* ✅ Good: Clear hover state */
button {
  background-color: var(--color-info-border);
  transition: all var(--transition-fast);
}

button:hover {
  background-color: var(--color-info-dark);
  box-shadow: var(--shadow-medium);
}
```

### 8. Show Disabled States Clearly
**Rule:** Disabled elements should be visually distinct.

```css
/* ❌ Bad: Same appearance when disabled */
button {
  background-color: var(--color-info-border);
}

/* ✅ Good: Clear disabled appearance */
button:disabled {
  background-color: var(--color-borders-primary);
  color: var(--color-text-disabled);
  cursor: not-allowed;
  opacity: 0.6;
}
```

### 9. Use Card Pattern Consistently
**Rule:** All content containers should use the card pattern.

```css
/* ✅ Good: Standard card pattern */
.card {
  background-color: var(--color-backgrounds-main);
  border: 1px solid var(--color-borders-primary);
  border-radius: var(--radius-md);
  padding: var(--space-px4);
  box-shadow: var(--shadow-subtle);
}
```

### 10. Handle Loading States
**Rule:** Show loading states for operations that take time.

```jsx
// ❌ Bad: No feedback
function Component() {
  const [data, setData] = useState(null);

  const handleClick = async () => {
    const result = await fetchData();  // No feedback!
    setData(result);
  };

  return <button onClick={handleClick}>Load</button>;
}

// ✅ Good: Clear loading state
function Component() {
  const [data, setData] = useState(null);
  const [isLoading, setIsLoading] = useState(false);

  const handleClick = async () => {
    setIsLoading(true);
    try {
      const result = await fetchData();
      setData(result);
    } finally {
      setIsLoading(false);
    }
  };

  return (
    <button onClick={handleClick} disabled={isLoading}>
      {isLoading ? 'Loading...' : 'Load'}
    </button>
  );
}
```

## Accessibility Best Practices

### 11. Verify Color Contrast
**Rule:** All text must meet WCAG AA contrast ratios (4.5:1 for normal text).

```css
/* ❌ Bad: Low contrast */
.text {
  color: #718096;           /* Secondary text */
  background-color: #f4f6f8; /* Primary bg */
  /* Ratio: 3.5:1 - FAILS AA */
}

/* ✅ Good: WCAG AA compliant */
.text {
  color: var(--color-text-primary);    /* #1a202c */
  background-color: var(--color-backgrounds-primary); /* #f4f6f8 */
  /* Ratio: 10:1 - PASSES AA+ */
}
```

### 12. Include Alt Text for Images
**Rule:** All meaningful images must have descriptive alt text.

```jsx
/* ❌ Bad: No alt text */
<img src="chart.png" />

/* ✅ Good: Descriptive alt text */
<img src="chart.png" alt="Monthly revenue chart showing 20% increase" />

/* ✅ Good: Decorative images marked */
<img src="decoration.png" alt="" />
```

### 13. Label Form Inputs
**Rule:** All form inputs must have associated labels.

```jsx
/* ❌ Bad: No label */
<input type="email" placeholder="Email" />

/* ✅ Good: Associated label */
<label htmlFor="email">Email Address</label>
<input id="email" type="email" required />
```

### 14. Use Semantic HTML
**Rule:** Use proper semantic elements for meaning.

```jsx
/* ❌ Bad: Div used as button */
<div onClick={handleClick}>Click me</div>

/* ✅ Good: Proper button element */
<button onClick={handleClick}>Click me</button>

/* ❌ Bad: Div used as link */
<div onClick={() => navigate('/page')}>Go to page</div>

/* ✅ Good: Proper link element */
<a href="/page">Go to page</a>
```

### 15. Keyboard Navigation
**Rule:** All interactive elements must be keyboard accessible.

```jsx
/* ❌ Bad: Not keyboard accessible */
<div onClick={handleAction}>Click me</div>

/* ✅ Good: Keyboard accessible */
<button onClick={handleAction}>Click me</button>

/* Or use div with proper ARIA */
<div
  role="button"
  tabIndex={0}
  onClick={handleAction}
  onKeyDown={(e) => {
    if (e.key === 'Enter' || e.key === ' ') {
      handleAction();
    }
  }}
>
  Click me
</div>
```

## Responsive Design Best Practices

### 16. Mobile-First Approach
**Rule:** Design for mobile first, then enhance for larger screens.

```css
/* ❌ Bad: Desktop-first */
.grid {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
}

@media (max-width: 768px) {
  .grid {
    grid-template-columns: 1fr;
  }
}

/* ✅ Good: Mobile-first */
.grid {
  display: grid;
  grid-template-columns: 1fr;
  gap: var(--space-px4);
}

@media (min-width: 768px) {
  .grid {
    grid-template-columns: repeat(2, 1fr);
  }
}

@media (min-width: 1024px) {
  .grid {
    grid-template-columns: repeat(3, 1fr);
  }
}
```

### 17. Flexible Layouts
**Rule:** Use flexible layouts that accommodate content of varying lengths.

```css
/* ❌ Bad: Fixed widths break with expansion */
.title {
  width: 200px;      /* Fixed width */
  white-space: nowrap; /* Forces overflow */
}

/* ✅ Good: Flexible layout */
.title {
  max-width: 100%;   /* Responsive */
  word-wrap: break-word;
  line-height: var(--line-height-normal);
}
```

### 18. Touch Target Size
**Rule:** Interactive elements should be at least 44px for touch targets.

```css
/* ❌ Bad: Too small for touch */
button {
  padding: var(--space-px1);   /* Only 4px */
  height: 24px;               /* Too small */
}

/* ✅ Good: Touch-friendly */
button {
  padding: var(--space-px2);   /* 8px padding */
  min-height: 44px;           /* Touch-friendly height */
}
```

## Localization Best Practices

### 19. Support Text Expansion
**Rule:** Plan for text expansion when supporting multiple languages.

```css
/* ❌ Bad: Fixed width doesn't accommodate expansion */
.label {
  width: 100px;
  overflow: hidden;
  text-overflow: ellipsis;
}

/* ✅ Good: Flexible width for expansion */
.label {
  max-width: 100%;
  flex-wrap: wrap;
  line-height: var(--line-height-normal);
}

/* Adjust for Chinese text */
.chinese {
  line-height: var(--line-height-loose);
}
```

### 20. Prepare for Right-to-Left (RTL)
**Rule:** Use logical CSS properties to support future RTL languages.

```css
/* ❌ Bad: Physical properties */
.sidebar {
  margin-left: var(--space-px4);
  padding-right: var(--space-px8);
}

/* ✅ Good: Logical properties */
.sidebar {
  margin-inline-start: var(--space-px4);  /* Left in LTR, right in RTL */
  padding-inline-end: var(--space-px8);   /* Right in LTR, left in RTL */
}
```

## Performance Best Practices

### 21. Minimize Animations
**Rule:** Keep animations fast and purposeful. Respect user preferences.

```css
/* ✅ Good: Respectful animations */
@media (prefers-reduced-motion: reduce) {
  * {
    animation-duration: 0.01ms !important;
    animation-iteration-count: 1 !important;
    transition-duration: 0.01ms !important;
  }
}

.component {
  transition: all var(--transition-standard);
}
```

### 22. Use CSS Variables Over JS
**Rule:** Prefer CSS variables for styling to reduce JavaScript overhead.

```javascript
/* ❌ Bad: Lots of JS for styling */
function applyTheme(isDark) {
  const styles = isDark ? darkColors : lightColors;
  document.body.style.backgroundColor = styles.bg;
  document.body.style.color = styles.text;
  // ... more JS
}

/* ✅ Good: CSS handles theme switching */
/* CSS already includes dark mode with media queries */
body {
  background-color: var(--color-bg-main);  /* Automatic! */
  color: var(--color-text-primary);
}
```

### 23. Leverage CSS Grid & Flexbox
**Rule:** Use modern layout techniques instead of floats and positioning.

```css
/* ✅ Good: Modern layout */
.grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
  gap: var(--space-px4);
}

.flex {
  display: flex;
  gap: var(--space-px4);
  flex-wrap: wrap;
}
```

## Documentation Best Practices

### 24. Document Custom Decisions
**Rule:** If deviating from design system, document why.

```css
/* ✅ Good: Documented deviation */
.special-case {
  /* Using custom spacing because of specific UX requirement
     Issue: https://github.com/... */
  padding: 13px;
  margin: 25px;
}
```

### 25. Comment Complex Components
**Rule:** Explain non-obvious design decisions.

```jsx
// ✅ Good: Clear comments
function DataTable() {
  return (
    <table
      role="grid"
      aria-label="Sortable data table"
      // Using role="grid" instead of table for better keyboard support
      // See: accessibility.md > Semantic HTML
    >
      {/* ... */}
    </table>
  );
}
```

## Quality Assurance Checklist

Before shipping:

- [ ] Using tokens for all colors/spacing/typography?
- [ ] Dark mode tested and looks good?
- [ ] Focus indicators visible on all interactive elements?
- [ ] Hover states clear?
- [ ] Disabled states obvious?
- [ ] Color contrast WCAG AA minimum?
- [ ] Keyboard navigation works?
- [ ] Forms properly labeled?
- [ ] Images have alt text?
- [ ] No hardcoded colors/spacing?
- [ ] Responsive design tested (mobile, tablet, desktop)?
- [ ] Touch targets 44px minimum?
- [ ] Loading states shown?
- [ ] Error messages helpful?
- [ ] No unnecessary animations?
- [ ] RTL preparation (logical properties)?
- [ ] Localization ready?
- [ ] Design validator passes?

## When in Doubt

1. **Check design-tokens.md** - Token specifications
2. **Check design-patterns.md** - Common patterns
3. **Check accessibility.md** - Accessibility requirements
4. **Check dark-mode.md** - Dark mode implementation
5. **Run design validator** - Check for consistency issues
6. **Test in both light/dark modes** - Always test both
7. **Test keyboard navigation** - Always test accessibility
8. **Ask design team** - When unsure about visual decisions
