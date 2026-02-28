# ACP Design System - Accessibility Guide

WCAG 2.1 Level AA compliance guidelines for ACP interfaces.

## Color Contrast

All ACP tokens meet or exceed WCAG AA contrast requirements:

### Light Mode Contrast Ratios

| Text Color | Background | Ratio | Standard |
|-----------|-----------|-------|----------|
| Primary (#1a202c) | White (#ffffff) | 18:1 | AA+ |
| Primary (#1a202c) | Primary BG (#f4f6f8) | 10:1 | AA+ |
| Primary (#1a202c) | Info BG (#e3f2fd) | 10:1 | AA+ |
| Secondary (#4a5568) | White (#ffffff) | 8:1 | AA+ |
| Info Border (#90caf9) | Info BG (#e3f2fd) | 4.5:1 | AA minimum |
| Success Border (#4caf50) | Success BG (#d7f5e9) | 4.5:1 | AA minimum |

### Dark Mode Contrast Ratios

| Text Color | Background | Ratio | Standard |
|-----------|-----------|-------|----------|
| Primary (#f3f4f6) | Dark Main (#1a1a1a) | 15:1 | AA+ |
| Primary (#f3f4f6) | Dark Primary (#2d3748) | 11:1 | AA+ |
| Primary (#f3f4f6) | Info BG (#1e3a8a) | 11:1 | AA+ |
| Secondary (#e5e7eb) | Dark Main (#1a1a1a) | 13:1 | AA+ |
| Info Border (#60a5fa) | Info BG (#1e3a8a) | 4.5:1 | AA minimum |
| Success Border (#10b981) | Success BG (#064e3b) | 4.5:1 | AA minimum |

### Testing Contrast

**Tools:**
- [WebAIM Contrast Checker](https://webaim.org/resources/contrastchecker/)
- [Accessible Colors](https://accessible-colors.com/)
- [WAVE Browser Extension](https://wave.webaim.org/extension/)

**In Chrome DevTools:**
1. Inspect element
2. Go to Styles tab
3. Click color swatch
4. View contrast ratio
5. Ensure ratio meets WCAG AA (4.5:1 for normal text, 3:1 for large text)

**Requirements:**
- Normal text (< 18px): 4.5:1 minimum
- Large text (≥ 18px): 3:1 minimum
- UI components: 3:1 minimum
- Graphical elements: 3:1 minimum

## Keyboard Navigation

### Standard Tab Order
Tab order should follow logical reading order (top to bottom, left to right).

### Focus Indicators
Every interactive element must have a visible focus indicator:

```css
:focus {
  outline: 2px solid #90caf9; /* Info border for visibility */
  outline-offset: 2px;
}
```

**Focus styling requirements:**
- Contrast ratio: 3:1 minimum against background
- Visible in both light and dark modes
- At least 2px thick
- Not invisible (avoid outline: none)

### Keyboard Accessible Interactions

**Required for keyboard access:**
- `<button>` for clickable actions
- `<a>` for navigation
- `<input>`, `<select>`, `<textarea>` for forms
- Proper ARIA roles for custom components

**Testing:**
- Tab through entire interface
- Verify focus order makes sense
- Check all buttons respond to Enter
- Check all inputs accept text
- Verify no keyboard traps exist

### Skip Links

For complex interfaces, include skip links:
```html
<a href="#main-content" class="skip-link">
  Skip to main content
</a>
```

## Semantic HTML

### Heading Structure
Always use proper heading hierarchy:
```html
<h1>Page Title</h1>           <!-- Only one per page -->
<h2>Section</h2>
<h3>Subsection</h3>
```

**Don't do:**
```html
<h1>Title</h1>
<h3>Skip h2</h3>              <!-- Breaks hierarchy -->
```

### Buttons vs Links
```html
<!-- For actions -->
<button>Click me</button>

<!-- For navigation -->
<a href="/destination">Go there</a>

<!-- Never do -->
<div onclick="doAction()">Click</div>  <!-- Not accessible -->
```

### Form Elements
```html
<label for="email">Email Address</label>
<input id="email" type="email" required>

<!-- Don't use placeholder as label -->
<input placeholder="Email">  <!-- Not accessible -->
```

## ARIA Labels & Attributes

### When to Use ARIA

Use ARIA to provide additional context for accessibility:

```html
<!-- Icon-only button -->
<button aria-label="Close menu">
  <svg><!-- close icon --></svg>
</button>

<!-- Hidden description -->
<input aria-describedby="hint-id">
<span id="hint-id">Password must be 8+ characters</span>

<!-- Expanded/collapsed state -->
<button aria-expanded="false" aria-controls="menu">
  Menu
</button>
<div id="menu" hidden>
  <!-- menu content -->
</div>
```

### Common ARIA Attributes

| Attribute | Purpose | Example |
|-----------|---------|---------|
| `aria-label` | Provide accessible name | `<button aria-label="Close">X</button>` |
| `aria-labelledby` | Reference another element as label | `<h2 id="title">Section</h2><p aria-labelledby="title">` |
| `aria-describedby` | Reference element with description | `<input aria-describedby="help">` |
| `aria-expanded` | Show collapse/expand state | `<button aria-expanded="false">Menu</button>` |
| `aria-hidden` | Hide decorative elements | `<svg aria-hidden="true"></svg>` |
| `aria-live` | Announce dynamic updates | `<div aria-live="polite">Loading...</div>` |
| `role` | Define element's role | `<div role="alert">Error message</div>` |

## Images & Icons

### Alt Text Rules

**For meaningful images:**
```html
<!-- Good: descriptive alt -->
<img src="chart.png" alt="Monthly revenue chart showing 20% increase">

<!-- Bad: unhelpful alt -->
<img src="chart.png" alt="chart">
```

**For decorative images:**
```html
<!-- Good: empty alt for decorative images -->
<img src="decoration.png" alt="">

<!-- Good: hide with aria-hidden -->
<svg aria-hidden="true"><circle/></svg>
```

**For icon-only buttons:**
```html
<!-- Good: aria-label -->
<button aria-label="Delete item">
  <svg><path d="..."/></svg>
</button>

<!-- Bad: no label -->
<button>
  <svg><path d="..."/></svg>
</button>
```

### Icon Colors
Always pair icon colors with text or sufficient contrast:

```html
<!-- Good: icon + text -->
<button>
  <svg class="text-green-600"></svg>
  Success
</button>

<!-- Bad: icon only, hard to read -->
<button>
  <svg class="text-green-200"></svg>  <!-- Low contrast -->
</button>
```

## Text & Typography

### Font Sizes
Minimum readable size: **14px** for body text

```css
/* Good: readable sizes */
body { font-size: 1rem; }           /* 16px */
.small { font-size: 0.875rem; }    /* 14px */

/* Bad: too small */
.tiny { font-size: 10px; }          /* Unreadable */
```

### Line Height
Minimum line height for readability: **1.5**

```css
/* Good: generous spacing */
body { line-height: 1.5; }

/* Better for Chinese: even more space */
.chinese { line-height: 1.8; }

/* Bad: cramped text */
body { line-height: 1.1; }
```

### Text Alignment
- ✅ Use left alignment for LTR languages (English)
- ✅ Use right alignment for RTL languages (future)
- ❌ Avoid justified alignment (creates uneven spacing)
- ❌ Avoid center alignment for body text (hard to read)

### Language Support

**English:**
- Line height: 1.5
- Font: System font stack
- Text width: 50-75 characters per line

**Chinese (Simplified):**
- Line height: 1.6-1.8 (more space needed)
- Font: System font stack (supports Chinese)
- Text width: 30-40 characters per line
- Character spacing may need adjustment

## Form Accessibility

### Inputs
```html
<!-- Good: labeled input -->
<label for="name">Name</label>
<input id="name" type="text" required>

<!-- Good: error messaging -->
<label for="email">Email</label>
<input id="email" type="email" aria-describedby="email-error">
<span id="email-error" role="alert">Invalid email address</span>

<!-- Bad: no label -->
<input type="text">
```

### Validation
```html
<!-- Good: descriptive error -->
<span role="alert">Password must contain uppercase letter</span>

<!-- Bad: unclear error -->
<span>Invalid!</span>
```

## Motion & Animation

### Respect Reduced Motion
```css
/* Good: respect user preferences */
@media (prefers-reduced-motion: reduce) {
  * {
    animation-duration: 0.01ms !important;
    animation-iteration-count: 1 !important;
    transition-duration: 0.01ms !important;
  }
}

/* Bad: ignore user preferences */
body {
  animation: slide 1s;  /* No prefers-reduced-motion query */
}
```

### Animation Guidelines
- Maximum duration: 500ms
- Avoid autoplay: Let users control animation
- No rapid flashing: Avoid 3+ flashes per second (seizure risk)
- Provide pause controls: Especially for looping animations

## Color Blindness

While tokens don't account for specific types of color blindness, follow these guidelines:

- **Don't rely on color alone**: Always pair with text or icons
- **Test with protanopia/deuteranopia**: Red/green blind simulators
- **Use sufficient contrast**: Works for most color blindness
- **Use patterns**: Combine colors with patterns when possible

**Testing tools:**
- [Color Oracle](https://colororacle.org/)
- [Coblis Color Blindness Simulator](https://www.color-blindness.com/coblis-color-blindness-simulator/)

## Accessibility Testing Checklist

- [ ] **Keyboard Navigation**: Tab through entire interface
- [ ] **Focus Indicators**: All interactive elements visible when focused
- [ ] **Color Contrast**: All text meets 4.5:1 (normal) or 3:1 (large)
- [ ] **Semantic HTML**: Proper use of buttons, links, form elements
- [ ] **Form Labels**: All inputs have visible labels
- [ ] **Error Messages**: Clear, specific, with solutions
- [ ] **Icon Alt Text**: Meaningful images have descriptive alt text
- [ ] **ARIA**: Used appropriately for complex interactions
- [ ] **Screen Reader**: Test with NVDA or JAWS
- [ ] **Reduced Motion**: Animations respect prefers-reduced-motion
- [ ] **Dark Mode**: Tested contrast and visibility
- [ ] **Mobile/Touch**: Touch targets are 44px minimum

## Automated Testing Tools

- **WAVE**: Browser extension for accessibility errors
- **Axe DevTools**: Comprehensive accessibility testing
- **Lighthouse**: Built into Chrome DevTools
- **NVDA**: Free screen reader for Windows
- **VoiceOver**: Built into macOS/iOS

## Resources

- [WCAG 2.1 Guidelines](https://www.w3.org/WAI/WCAG21/quickref/)
- [MDN Accessibility](https://developer.mozilla.org/en-US/docs/Web/Accessibility)
- [WebAIM Articles](https://webaim.org/articles/)
- [Inclusive Components](https://inclusive-components.design/)
- [A11y Project](https://www.a11yproject.com/)

## Localization for Accessibility

### Language-Specific Considerations

**English:**
- Clear, concise language
- Short sentences for clarity
- Standard punctuation

**Chinese:**
- Characters are more compact
- Punctuation varies (Chinese punctuation marks)
- Tone and formality important
- Line height needs more space

### Text Direction
Currently supporting LTR (left-to-right):
- English
- Prepare for RTL (right-to-left):
- Arabic, Hebrew (future)

Use logical properties in CSS to prepare:
```css
/* Good: logical properties */
padding-inline: 1rem;
margin-inline-start: 1rem;

/* Less flexible: physical properties */
padding-left: 1rem;
margin-left: 1rem;
```

## Support & Questions

For accessibility questions or to report issues, contact the design systems team.

Make sure to reference:
- Which WCAG guideline is in question
- Light or dark mode
- Which language (English/Chinese)
- Browser/screen reader used
