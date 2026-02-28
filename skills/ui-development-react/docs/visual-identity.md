# ACP Brand Visual Identity

Brand identity and visual standards for Alauda Container Platform.

## Brand Overview

**Alauda Container Platform (ACP)** is a professional, enterprise-focused platform for container orchestration and Kubernetes management.

**Visual Characteristics:**
- Professional & Trustworthy
- Modern & Efficient
- Clear & Transparent
- Scalable & Reliable

## Color Philosophy

### Primary Color: Blue (#90caf9)
**Meaning:** Trust, professionalism, clarity

**Usage:**
- Information states
- Interactive elements
- Guidance and tips
- Status indicators

**When blue is right:**
- User needs information
- Setting expectations
- Providing guidance
- Non-critical status

### Success Color: Green (#4caf50)
**Meaning:** Success, completion, confirmation

**Usage:**
- Successful operations
- Completed tasks
- Confirmations
- Positive status

**When green is right:**
- Operation completed
- Task succeeded
- Action confirmed
- Goal achieved

### Process Color: Teal (#4db6ac)
**Meaning:** Processing, investigation, workflow

**Usage:**
- Workflow states
- Investigation steps
- Processing indicators
- Active operations

**When teal is right:**
- Something is being analyzed
- Workflow in progress
- Investigation ongoing
- Data processing

### Neutral Colors: Gray (#cbd7e0)
**Meaning:** Separation, structure, stability

**Usage:**
- Borders and dividers
- Inactive elements
- Structural elements
- Subtle backgrounds

## Palette at a Glance

### Light Mode
```
Primary Background: #f4f6f8 (Soft gray-blue)
├─ Panel Background: #eef4ff (Lighter blue)
├─ Content Background: #ffffff (Pure white)
└─ Alternate: #fafafa (Very light gray)

Text Colors:
├─ Primary: #1a202c (Dark blue-gray)
├─ Secondary: #4a5568 (Medium gray)
├─ Tertiary: #718096 (Light gray)
└─ Disabled: #cbd5e0 (Very light gray)

Status Colors:
├─ Info: #e3f2fd bg / #90caf9 border
├─ Success: #d7f5e9 bg / #4caf50 border
├─ Process: #e8f2ff bg / #2196f3 border
└─ Teal: #e0f2f1 bg / #4db6ac border
```

### Dark Mode
```
Primary Background: #2d3748 (Dark gray-blue)
├─ Panel Background: #1e3a5f (Darker blue)
├─ Content Background: #1a1a1a (Near black)
└─ Alternate: #2d3748 (Same as primary)

Text Colors:
├─ Primary: #f3f4f6 (Near white)
├─ Secondary: #e5e7eb (Light gray)
├─ Tertiary: #d1d5db (Medium gray)
└─ Disabled: #9ca3af (Darker gray)

Status Colors:
├─ Info: #1e3a8a bg / #60a5fa border
├─ Success: #064e3b bg / #10b981 border
├─ Process: #1e40af bg / #3b82f6 border
└─ Teal: #134e4a bg / #14b8a6 border
```

## Visual Hierarchy

### Information Hierarchy Through Color

**Primary Information** (Dark, main text)
- Critical information
- Key data
- Main content

**Secondary Information** (Medium gray text)
- Supporting information
- Labels
- Explanations

**Tertiary Information** (Light gray text)
- Hints
- Help text
- Supplementary details

**Inactive/Disabled** (Very light gray)
- Unavailable options
- Disabled states
- Placeholder text

### Information Hierarchy Through Size

```
Page Title:        32px / Bold (700)
Section Title:     24px / Semibold (600)
Subsection:        20px / Semibold (600)
Body Text:         16px / Normal (400)
Small Text:        14px / Normal (400)
Tiny Text:         12px / Normal (400)
```

## Spacing & Rhythm

### 10px Grid System

The visual rhythm of ACP is based on a **10px grid unit**:

```
Padding/Margin scales:
4px   (1/3 unit)   - Minimal spacing
8px   (4/5 unit)   - Small gaps
12px  (1.2 units)  - Comfortable spacing
16px  (1.6 units)  - Standard padding
24px  (2.4 units)  - Large spacing
32px  (3.2 units)  - Section spacing
48px  (4.8 units)  - Major gaps
64px  (6.4 units)  - Page breaks
```

**Visual Effect:**
- Creates visual breathing room
- Maintains consistent relationships
- Scales well across screen sizes
- Professional, organized appearance

## Component Style Guidelines

### Cards
- **Background:** White (#ffffff) or dark equivalent
- **Border:** Subtle 1px border (#cbd7e0)
- **Radius:** 8px (medium)
- **Padding:** 16px (standard)
- **Shadow:** Subtle (0 1px 2px rgba(0,0,0,0.05))

**Purpose:** Contains related information in a cohesive unit

### Buttons
- **Style:** Solid fill, not outlined
- **Padding:** 8px horizontal, 12px vertical minimum
- **Radius:** 8px (medium)
- **Text:** Medium weight (500)
- **Hover:** Darker shade + shadow increase
- **Focus:** 2px border with info color

**Purpose:** Clear, actionable elements

### Forms
- **Inputs:** White background, subtle border
- **Border Color:** Primary border (#cbd7e0)
- **Radius:** 4px (subtle)
- **Padding:** 8-12px
- **Focus State:** Info border color + background hint

**Purpose:** Clear, organized data entry

### Tables
- **Header:** Primary background (#f4f6f8)
- **Rows:** Alternating white and #fafafa
- **Borders:** Secondary color, subtle
- **Hover:** Info background tint

**Purpose:** Organize large data sets

## Typography System

### Font Selection
**Primary Font:** System fonts
```
-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto,
'Helvetica Neue', Arial, sans-serif
```

**Why system fonts?**
- Fast loading (no network request)
- Native appearance on each platform
- Excellent readability
- Professional look
- Full character support (including Chinese)

### Font Weight Usage

**700 Bold:** Main headings, high emphasis
**600 Semibold:** Subheadings, interactive elements
**500 Medium:** Buttons, labels, emphasis
**400 Normal:** Body text, default

### Line Height Strategy

**Headings:** 1.1-1.2 (tight, no extra space)
**Body Text:** 1.5 (comfortable reading)
**Chinese Text:** 1.6-1.8 (more space needed)
**Accessibility:** 1.6+ (more generous spacing)

## Visual Consistency

### Do's ✅
- Use the blue palette for information and status
- Use green for success and completion
- Use teal for processes and investigation
- Maintain 16px standard padding
- Use card pattern consistently
- Test in both light and dark modes

### Don'ts ❌
- Create new colors without approval
- Mix multiple color palettes
- Use arbitrary spacing values
- Ignore dark mode
- Use decorative shadows
- Overuse animations

## Real-World Examples

### Information Alert
**When to use:** Sharing important information with users

```
┌─────────────────────────────────────┐
│ ℹ️  Key Information                  │  Blue background (#e3f2fd)
│                                     │  Blue border (#90caf9)
│ This feature requires upgrade to    │  Dark text for readability
│ version 4.1 or higher.              │  Subtle shadow
└─────────────────────────────────────┘
```

### Success Confirmation
**When to use:** Confirming that an action completed successfully

```
┌─────────────────────────────────────┐
│ ✓ Deployment Successful             │  Green background (#d7f5e9)
│                                     │  Green border (#4caf50)
│ Your application is now running     │  Dark text for readability
│ on cluster-01.                      │  Subtle shadow
└─────────────────────────────────────┘
```

### Processing Step
**When to use:** Indicating an operation is in progress

```
┌─────────────────────────────────────┐
│ ↻ Analyzing Metrics                 │  Blue background (#e8f2ff)
│                                     │  Blue border (#2196f3)
│ Collecting performance data...      │  Dark text for readability
│ Estimated time: 30 seconds          │  Loading indicator
└─────────────────────────────────────┘
```

### Investigation Finding
**When to use:** Displaying analysis results

```
┌─────────────────────────────────────┐
│ ⚙️  Hypothesis Investigation         │  Teal background (#e0f2f1)
│                                     │  Teal border (#4db6ac)
│ Investigating: High API latency     │  Dark text for readability
│ Status: 45% complete                │  Progress indicator
└─────────────────────────────────────┘
```

## Localization Visual Considerations

### English Layout
- Compact text (words are short)
- Single line fits more text
- Standard line height (1.5)
- Left-aligned (LTR)

### Chinese Layout
- More compact characters (but need more space)
- Fewer characters per line
- Increased line height (1.6-1.8)
- Left-aligned (LTR)

**Key differences:**
- Chinese text needs 30% more vertical space
- Characters are denser, need more breathing room
- Punctuation marks are different
- Text direction remains LTR

## Accessibility Visual Standards

### Color Contrast
All text meets or exceeds WCAG AA:
- Normal text: 4.5:1 ratio minimum
- Large text: 3:1 ratio minimum
- Borders: 3:1 ratio minimum

### Focus Indicators
- 2px solid border with info border color
- 2px outline offset
- Visible in both light and dark modes
- Never removed (no `outline: none`)

### Interactive Element Sizing
- Minimum 44px height for buttons
- Minimum 44x44px for touch targets
- Adequate spacing between interactive elements

## Design System Evolution

This visual identity is based on:
- Real screenshots from ACP 4.0
- User testing and feedback
- WCAG AA accessibility standards
- Modern design best practices

**Principles guiding evolution:**
1. **Consistency** - Maintain visual cohesion
2. **Accessibility** - Serve all users
3. **Scalability** - Work at all sizes
4. **Efficiency** - Use tokens, not custom values
5. **Localization** - Support multiple languages

## When to Break the Rules

Only in exceptional circumstances, and with:
1. Design team discussion
2. Clear business justification
3. Accessibility review
4. Documentation
5. Plan to standardize later

Example: Custom data visualization might use different colors for specific data types (as long as WCAG AA contrast is maintained).

## Resources

- **Tokens:** See `design-tokens.md` for exact values
- **Patterns:** See `design-patterns.md` for usage patterns
- **Accessibility:** See `accessibility.md` for compliance requirements
- **Dark Mode:** See `dark-mode.md` for implementation
- **Guidelines:** See `guidelines.md` for do's and don'ts

## Summary

ACP's visual identity is:
- **Professional:** Blue palette conveys trust
- **Clear:** Simple colors with semantic meaning
- **Accessible:** WCAG AA contrast throughout
- **Scalable:** 10px grid system adapts to all sizes
- **Localized:** Supports English and Chinese
- **Modern:** System fonts and contemporary design
- **Consistent:** Design tokens ensure uniformity

Use these standards to create interfaces that feel cohesive, professional, and trustworthy.
