# ACP Design Guidelines

Design do's and don'ts for maintaining ACP visual consistency.

## DO's ✅

### Color Usage
- ✅ **Use design tokens** for all colors
- ✅ **Use semantic color names**: "Use the success background color" instead of "#d7f5e9"
- ✅ **Match our blue palette** for info states
- ✅ **Use green for success** completion, confirmations
- ✅ **Use teal for process** states and workflows
- ✅ **Test colors in both light and dark modes**
- ✅ **Verify WCAG AA contrast** for all text

### Spacing
- ✅ **Use spacing tokens** for all padding, margin, gap
- ✅ **Maintain 10px grid system** alignment
- ✅ **Be consistent** with spacing relationships
- ✅ **Use white space** to create hierarchy and breathing room
- ✅ **Plan for text expansion** (30% for English, even more for Chinese)

### Typography
- ✅ **Use system fonts** for performance and native look
- ✅ **Follow heading hierarchy** (h1, h2, h3, etc.)
- ✅ **Use semibold (600)** for interactive elements and emphasis
- ✅ **Use line heights** appropriate to language (1.5 for English, 1.6-1.8 for Chinese)
- ✅ **Increase line height** for readability in dark mode

### Components
- ✅ **Use card pattern** for content containers
- ✅ **Include subtle shadows** for depth
- ✅ **Use border-radius tokens** (4px, 8px, 12px, 16px)
- ✅ **Show focus indicators** for keyboard navigation
- ✅ **Provide hover states** for interactive elements
- ✅ **Use disabled state** for unavailable actions

### Interactions
- ✅ **Include transitions** (200-300ms) for visual feedback
- ✅ **Use ease-in-out** timing function
- ✅ **Show loading states** for long operations
- ✅ **Provide success/error feedback** for user actions
- ✅ **Test keyboard navigation** thoroughly

### Accessibility
- ✅ **Verify color contrast** (4.5:1 for normal text)
- ✅ **Include alt text** for meaningful images
- ✅ **Use semantic HTML** for structure
- ✅ **Provide clear labels** for form inputs
- ✅ **Make interactive elements obvious** (buttons, links)
- ✅ **Support keyboard navigation** for all features
- ✅ **Test with screen readers** during development

### Localization
- ✅ **Support English and Chinese** from the start
- ✅ **Use flexible layouts** that accommodate text expansion
- ✅ **Adjust line heights** for Chinese text
- ✅ **Test with Chinese text** early in development
- ✅ **Use language-appropriate fonts** (system fonts work well)

## DON'Ts ❌

### Color Usage
- ❌ **Don't use hardcoded colors** (#d7f5e9, #90caf9, etc.)
- ❌ **Don't create new colors** without design team approval
- ❌ **Don't use arbitrary colors** for emphasis
- ❌ **Don't ignore dark mode** - test colors in dark mode
- ❌ **Don't use color alone** for meaning (add icons/text)
- ❌ **Don't use low-contrast text** (fails WCAG AA)

### Spacing
- ❌ **Don't use arbitrary spacing values** (13px, 25px, etc.)
- ❌ **Don't break the 10px grid** system without reason
- ❌ **Don't create inconsistent** spacing relationships
- ❌ **Don't use padding instead of margin** to fake hierarchy
- ❌ **Don't ignore responsive spacing** - adjust for mobile

### Typography
- ❌ **Don't use web fonts** without performance testing
- ❌ **Don't skip heading hierarchy** (no h1 to h3 jump)
- ❌ **Don't use all caps** for body text
- ❌ **Don't use multiple font sizes** randomly
- ❌ **Don't ignore line height** - too small or too large
- ❌ **Don't use justified text** without good reason

### Components
- ❌ **Don't create new component patterns** without design discussion
- ❌ **Don't use hardcoded values** for radius/shadows
- ❌ **Don't skip focus states** for keyboard users
- ❌ **Don't hide hover states** - users expect visual feedback
- ❌ **Don't use inconsistent** component styling
- ❌ **Don't forget disabled states** for conditional actions

### Interactions
- ❌ **Don't use animations longer than 500ms**
- ❌ **Don't use bounce/elastic easing** (too playful)
- ❌ **Don't animate things that shouldn't move**
- ❌ **Don't disable animations for all users** - respect prefers-reduced-motion
- ❌ **Don't skip loading states** for unclear operations

### Accessibility
- ❌ **Don't rely on color alone** for information
- ❌ **Don't create inaccessible focus states**
- ❌ **Don't use placeholder text** as labels
- ❌ **Don't create keyboard traps**
- ❌ **Don't use images of text** instead of real text
- ❌ **Don't forget ARIA labels** for complex interactions
- ❌ **Don't skip alt text** for meaningful images

### Localization
- ❌ **Don't hardcode text** - make strings translatable
- ❌ **Don't create fixed-width layouts** (breaks with expansion)
- ❌ **Don't assume English line lengths** (Chinese is different)
- ❌ **Don't test only in English** - test in Chinese too
- ❌ **Don't ignore right-to-left concerns** (prepare for future)

## Brand Voice & Tone

### Professional & Trustworthy
- Use clear, concise language
- Avoid unnecessary jargon
- Explain technical concepts simply

### Helpful & Supportive
- Provide guidance and education
- Offer clear error messages
- Give actionable feedback

### Modern & Efficient
- Design for speed and efficiency
- Respect user's time
- Make common tasks easy

### Consistent & Reliable
- Maintain visual consistency
- Use predictable patterns
- Follow design system rules

## Design System Usage

### For Developers
1. Import tokens from your preferred format
2. Use tokens in CSS, JavaScript, or styling libraries
3. Run design validator to check consistency
4. Test in both light and dark modes

### For Designers
1. Reference design-tokens.md for exact color values
2. Use the Tailwind config for web mockups
3. Follow card pattern for layouts
4. Maintain 10px spacing grid

### For Product Managers
1. Understand color meanings (blue=info, green=success, teal=process)
2. Approve new features against design system
3. Ensure consistency across products
4. Support localization from the start

## Visual Consistency Checklist

Before shipping UI:

- [ ] Using design tokens for all colors?
- [ ] Following spacing grid system?
- [ ] Proper heading hierarchy?
- [ ] Dark mode tested?
- [ ] Focus states visible?
- [ ] Hover states clear?
- [ ] Disabled states obvious?
- [ ] Color contrast WCAG AA?
- [ ] Keyboard navigation works?
- [ ] Localization ready?
- [ ] No hardcoded colors/spacing?
- [ ] Component patterns consistent?
- [ ] Responsive design tested?
- [ ] Loading states shown?
- [ ] Error messages helpful?

## When to Break the Rules

Sometimes you need to deviate from the design system. Before doing so:

1. **Discuss with design team** - Get approval
2. **Document the reason** - Why can't you use tokens?
3. **Maintain consistency** - Even if bending rules, be consistent
4. **Plan migration** - Can this be standardized later?
5. **Avoid single use cases** - If only one place needs it, find another way

## Common Mistakes to Avoid

### Mistake: Mixing multiple color palettes
❌ Bad: Info blue + Success green + Custom purple
✅ Good: Info blue + Success green + Teal process

### Mistake: Inconsistent spacing
❌ Bad: 12px padding here, 18px margin there, 20px gap elsewhere
✅ Good: Consistent use of 16px padding, 8px gaps

### Mistake: Poor contrast in dark mode
❌ Bad: Light gray text on dark background (3:1 ratio)
✅ Good: Near-white text on dark background (15:1 ratio)

### Mistake: Inaccessible focus states
❌ Bad: Blue on blue focus indicator (invisible)
✅ Good: Clear 2px border with high contrast

### Mistake: Hardcoded values
❌ Bad: `color: '#90caf9'` in component
✅ Good: `color: var(--color-info-border)` or token usage

## Questions?

Refer to:
- **Token values**: See `design-tokens.md`
- **Visual patterns**: See `design-patterns.md`
- **Accessibility**: See `accessibility.md`
- **Dark mode**: See `dark-mode.md`
- **Quick start**: See `docs/quick-start.md`
