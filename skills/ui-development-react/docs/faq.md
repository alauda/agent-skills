# ACP Design System - Frequently Asked Questions

Common questions about using ACP design tokens and visual identity.

## Getting Started

### Q: Where do I start with design tokens?
**A:** Start with Quick Start Guide (`docs/quick-start.md`):
1. Choose your integration method (CSS, TypeScript, Tailwind, or JSON)
2. Copy the appropriate token files to your project
3. Replace hardcoded colors/spacing with tokens
4. Test in both light and dark modes

### Q: Which token file should I use?
**A:** Choose based on your project:
- **CSS Projects:** Use `design-tokens.css`
- **React/Next.js:** Use `design-tokens.ts` with styled-components or CSS-in-JS
- **Next.js with Tailwind:** Use `tailwind.config.js`
- **Design Tools:** Use `design-tokens.json`
- **CSS Modules:** Use `colors.module.css`

### Q: Do I need to install anything?
**A:** No! Just copy the token files to your project and import/link them. No npm packages required.

### Q: How do I enable dark mode?
**A:** Automatic! Just import `design-tokens.css` or use CSS variables. Dark mode automatically:
- Respects system preference (`@media (prefers-color-scheme: dark)`)
- Works with `.dark` class for manual toggle
- No additional setup needed

## Colors & Styling

### Q: Can I create custom colors?
**A:** Not without design team approval. The current palette covers all common use cases.

**If you need a custom color:**
1. Contact the design team
2. Explain the use case
3. They'll either find an existing token or add a new one

**Never hardcode colors** like `#ff6b6b` - always use tokens.

### Q: Why do I have to use tokens?
**A:** Design tokens ensure:
- **Consistency** - All UIs look the same
- **Maintainability** - One place to change colors
- **Accessibility** - Tokens are WCAG AA compliant
- **Dark Mode** - Automatic color switching
- **Scalability** - Easy to update company-wide

### Q: What if the color looks wrong in my design?
**A:** Before changing colors:
1. Check contrast ratio (should be 4.5:1+)
2. Test in both light and dark modes
3. Verify you're using the right token for the context
4. Ask design team if unsure

**Most "wrong looking" colors are actually right** - they're designed for accessibility.

### Q: How do I pick the right color for my component?
**A:** Use this guide:
- **Blue (#90caf9):** Information, alerts, guidance, status updates
- **Green (#4caf50):** Success, completion, confirmations
- **Teal (#4db6ac):** Processing, investigation, workflow states
- **Gray (#cbd7e0):** Borders, dividers, inactive elements

**Rule:** Choose the color that matches the semantic meaning, not the visual preference.

## Spacing & Typography

### Q: Can I use custom spacing values?
**A:** No. Always use the spacing scale:
4px, 8px, 12px, 16px, 20px, 24px, 32px, 48px, 64px

**Why?** Consistent spacing creates visual harmony and professional appearance.

### Q: What font should I use?
**A:** Always use the system font stack:
```
-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto,
'Helvetica Neue', Arial, sans-serif
```

**Why?** Fast, readable, works across all platforms, includes Chinese support.

### Q: Can I use custom font sizes?
**A:** No. Use the provided sizes:
xs, sm, base, lg, xl, 2xl, 3xl, 4xl

**If you need a different size:**
- Probably using wrong heading level
- Check typography hierarchy again
- Contact design team if genuinely different use case

### Q: How do I adjust line height for Chinese text?
**A:** Use `--line-height-loose` (1.8) instead of `--line-height-normal` (1.5):

```css
.english { line-height: var(--line-height-normal); }
.chinese { line-height: var(--line-height-loose); }
```

## Dark Mode

### Q: How do I test dark mode?
**A:**
1. **System preference:** Go to OS settings and enable dark mode
2. **Manual toggle:** Add `.dark` class to `<html>`
3. **DevTools:** Chrome DevTools > Rendering > Emulate CSS media feature

### Q: Dark mode looks broken, what do I do?
**A:**
1. **Check imports:** Make sure `design-tokens.css` is imported
2. **Verify CSS variables:** Use Chrome DevTools to check variable values
3. **Test contrast:** Make sure text is light on dark backgrounds
4. **Common issue:** Using hardcoded colors that don't switch

### Q: Can I customize dark mode colors?
**A:** No. Dark mode colors are carefully chosen for:
- WCAG AA compliance
- Reduced eye strain
- Professional appearance
- Consistency across ACP

**If colors look wrong in dark mode:**
1. Check you're using tokens (not hardcoded colors)
2. Verify contrast ratio (4.5:1+)
3. Test with actual system dark mode
4. Contact design team

### Q: How do I support dark mode without media queries?
**A:** Add `.dark` class to element or use class-based toggle:

```jsx
// Manual dark mode with class
<div className={isDark ? 'dark' : ''}>
  {/* Dark mode content */}
</div>

<style>
:root { --color-bg: #ffffff; }
.dark { --color-bg: #1a1a1a; }
</style>
```

## Design Patterns & Components

### Q: Should I use the card pattern?
**A:** Yes, for almost all content containers. Cards:
- Organize information clearly
- Create visual hierarchy
- Are easy to scan
- Work well in both light and dark modes

### Q: How do I style a success button?
**A:** Use the success token:

```css
.btn-success {
  background-color: var(--color-success-border);
  color: white;
  border: 1px solid var(--color-success-border);
}

.btn-success:hover {
  background-color: var(--color-success-dark);
}
```

### Q: How do I create focus indicators?
**A:** Always show a visible focus state:

```css
button:focus {
  outline: 2px solid var(--color-info-border);
  outline-offset: 2px;
}
```

Never do `outline: none` - breaks keyboard navigation.

### Q: How do I disable a button?
**A:** Use clear disabled styling:

```css
button:disabled {
  background-color: var(--color-borders-primary);
  color: var(--color-text-disabled);
  cursor: not-allowed;
  opacity: 0.6;
}
```

## Accessibility

### Q: Do I need to worry about accessibility?
**A:** Yes! All components must be:
- Keyboard navigable
- Screen reader friendly
- WCAG AA compliant
- Tested with real users

The design system helps with colors, but **you're responsible for structure**.

### Q: How do I check color contrast?
**A:**
1. **WebAIM Checker:** https://webaim.org/resources/contrastchecker/
2. **Chrome DevTools:** Inspect > Styles > Click color swatch
3. **WAVE Extension:** Browser accessibility auditor

**Requirement:** 4.5:1 for normal text, 3:1 for large text

### Q: How do I make forms accessible?
**A:** Always label inputs:

```html
<!-- Good -->
<label for="email">Email Address</label>
<input id="email" type="email" required>

<!-- Bad - no label -->
<input type="email" placeholder="Email">
```

### Q: How do I handle images?
**A:** Always include alt text:

```html
<!-- Good - meaningful images -->
<img src="chart.png" alt="Monthly revenue chart showing 20% increase">

<!-- Good - decorative images -->
<img src="decoration.png" alt="">

<!-- Bad - no alt text -->
<img src="chart.png">
```

## Localization

### Q: How do I support Chinese?
**A:**
1. Use system font stack (already supports Chinese)
2. Increase line height to 1.6-1.8 for Chinese text
3. Plan for 30% text expansion
4. Test with actual Chinese content

**Important:** Punctuation is different in Chinese. Use proper CJK punctuation.

### Q: How do I handle text expansion?
**A:** Never use fixed widths:

```css
/* Bad */
.label { width: 100px; }

/* Good */
.label { max-width: 100%; flex-wrap: wrap; }
```

### Q: Do I need to support right-to-left (RTL)?
**A:** Not yet. But prepare by using logical CSS properties:

```css
/* Prepare for future RTL support */
.sidebar {
  margin-inline-start: 1rem;   /* Left in LTR, right in RTL */
  padding-inline-end: 1rem;    /* Right in LTR, left in RTL */
}
```

## Design Validator

### Q: How do I run the design validator?
**A:**
```bash
python3 .claude/skills/ui-development/scripts/design-validator.py \
  audit --path=src --mode=light
```

**What it checks:**
- Hardcoded colors (should use tokens)
- Non-standard spacing values
- Non-standard border radius values

### Q: What if the validator reports errors?
**A:**
1. Replace hardcoded colors with tokens
2. Use spacing from the scale (4px, 8px, 12px, etc.)
3. Use radius tokens (4px, 8px, 12px, 16px)
4. Run validator again to verify

### Q: Can I ignore validator warnings?
**A:** No. Validator warnings indicate:
- Design inconsistency
- Likely accessibility issues
- Maintenance problems

**Fix all warnings before shipping.**

## Extending the Design System

### Q: How do I add a new token?
**A:**
1. Discuss with design team
2. Add to `design-tokens.json`
3. Run converter script to update exports
4. Commit to repo
5. Document in `reference/design-tokens.md`

**Don't add tokens without consensus** - defeats the purpose of design system.

### Q: Can I create component variants?
**A:** Yes! But use tokens consistently:

```css
.card { padding: var(--space-px4); }
.card-small { padding: var(--space-px2); }
.card-large { padding: var(--space-px8); }
```

All padding values should be from the scale.

### Q: How do I modify an existing token?
**A:** Contact the design team. Changing tokens affects:
- All components using that token
- Consistency across products
- Dark mode colors
- Accessibility compliance

**Changes must be coordinated company-wide.**

## Troubleshooting

### Q: Colors look wrong in production
**A:**
1. Check tokens are properly imported
2. Verify CSS/JS bundle includes token files
3. Clear browser cache
4. Test in different browser

### Q: Dark mode not working
**A:**
1. Check `@media (prefers-color-scheme: dark)` is working
2. Verify system dark mode is enabled
3. Check DevTools > Rendering > emulate CSS media
4. Make sure using CSS variables (not hardcoded colors)

### Q: Spacing looks inconsistent
**A:**
1. Check using spacing tokens (not hardcoded pixels)
2. Verify scaling is consistent across components
3. Compare with other ACP interfaces
4. Use design validator to audit code

### Q: Text doesn't look right in dark mode
**A:**
1. Check contrast ratio (4.5:1+)
2. Verify using proper text color token
3. Test with actual dark background
4. May need to adjust line height

### Q: Performance is slow with tokens
**A:**
1. CSS variables have minimal performance impact
2. Make sure not recreating tokens on every render
3. Check for excessive re-renders in JavaScript
4. Profile in Chrome DevTools

## Getting Help

### Q: Where can I ask questions?
**A:**
1. Check FAQ (you're reading it!)
2. Review relevant documentation:
   - `quick-start.md` - Getting started
   - `design-tokens.md` - Token reference
   - `design-patterns.md` - Common patterns
   - `accessibility.md` - Accessibility requirements
   - `dark-mode.md` - Dark mode guide
3. Contact design systems team

### Q: How do I report design system issues?
**A:**
1. Describe the issue clearly
2. Include screenshots or code example
3. Specify light/dark mode
4. Include browser/OS information
5. Contact design team

### Q: I found a bug in a token file
**A:**
1. Report to design team immediately
2. Include specific token and issue
3. Provide test case
4. Document temporary workaround if needed

### Q: Can I suggest a new feature?
**A:** Yes! But first:
1. Check if existing token/pattern solves it
2. Discuss with team if unclear
3. Propose addition to design system
4. Get team buy-in before implementation

## Pro Tips

### Tip 1: Use CSS variables for simple projects
CSS variables are the simplest way to get started with tokens.

### Tip 2: Combine with Tailwind for larger projects
Tailwind + ACP tokens = powerful, scalable styling.

### Tip 3: Test dark mode early
Don't wait until the end. Test dark mode throughout development.

### Tip 4: Use design validator regularly
Run validator early and often to catch issues.

### Tip 5: Document deviations
If you must deviate, document why and plan to standardize.

## Quick Links

- **Token Reference:** `reference/design-tokens.md`
- **Design Patterns:** `reference/design-patterns.md`
- **Guidelines:** `reference/guidelines.md`
- **Accessibility:** `reference/accessibility.md`
- **Dark Mode:** `reference/dark-mode.md`
- **Quick Start:** `docs/quick-start.md`
- **Token Usage:** `docs/token-usage.md`
- **Best Practices:** `docs/best-practices.md`
- **Visual Identity:** `docs/visual-identity.md`

---

**Still have questions?** Contact the design systems team or create an issue in the repository.
