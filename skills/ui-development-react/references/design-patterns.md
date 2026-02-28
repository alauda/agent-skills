# ACP Design Patterns

Visual and structural patterns used consistently throughout ACP interfaces.

## Card Pattern

Cards are the fundamental building block of ACP interfaces. They organize content into discrete, contained units.

### Anatomy
- **Background**: White (#ffffff light) or #2d3748 (dark)
- **Border**: 1px solid #cbd7e0 (light) or #4b5563 (dark)
- **Border Radius**: 8px (md)
- **Padding**: 16px (px4)
- **Shadow**: Subtle shadow for depth

### Variants

#### Info Card
Used for informational content, alerts, and guidance.
- **Background**: #e3f2fd (light) or #1e3a8a (dark)
- **Border**: #90caf9 (light) or #60a5fa (dark)
- **Text Color**: Adjust for readability

**Example Use Cases:**
- Monitor alerts
- Key information boxes
- System status updates
- Guidance and tips

#### Success Card
Used for completion states, confirmations, and successful operations.
- **Background**: #d7f5e9 (light) or #064e3b (dark)
- **Border**: #4caf50 (light) or #10b981 (dark)
- **Icon**: Green check mark

**Example Use Cases:**
- Operation completed
- Deployment successful
- Investigation resolved
- Action confirmed

#### Process Card
Used for workflow states, processing steps, and ongoing operations.
- **Background**: #e8f2ff (light) or #1e40af (dark)
- **Border**: #2196f3 (light) or #3b82f6 (dark)
- **Icon**: Process indicator (clock, spinner)

**Example Use Cases:**
- Runbook execution steps
- Memory collection progress
- Investigation in progress
- Data processing

#### Teal Card
Used for hypothesis investigation and analysis states.
- **Background**: #e0f2f1 (light) or #134e4a (dark)
- **Border**: #4db6ac (light) or #14b8a6 (dark)

**Example Use Cases:**
- Hypothesis investigation
- Analysis results
- Validation steps
- RCA findings

## Color Usage Guidelines

### Blue (Info)
**When to use:** Informational content, status updates, guidance
**Why:** Blue encourages reading and attention without alarm
**Semantic meaning:** "This is informational"

### Green (Success)
**When to use:** Completion, confirmation, successful operations
**Why:** Green = "action completed successfully"
**Semantic meaning:** "Operation successful"

### Teal (Process)
**When to use:** Investigation steps, workflow states, pending operations
**Why:** Teal indicates "something is being processed or analyzed"
**Semantic meaning:** "Analysis/processing in progress"

### Orange (Warning) - Reserved
**When to use:** Warnings, cautions requiring attention
**Semantic meaning:** "Attention required, not critical"
**Status:** Not currently in active use, reserved for future

### Red (Error) - Reserved
**When to use:** Critical errors, failures
**Semantic meaning:** "Critical failure, action required"
**Status:** Not currently in active use, reserved for future

## Layout Patterns

### Standard 3-Column Layout
Standard layout for dashboard-like interfaces.

```
┌─────────────────────────────────────────────┐
│ HEADER / CHROME (24px height)               │
├─────────┬─────────────────────────────────┤
│ SIDEBAR │ MAIN CONTENT                    │
│ 280px   │ Flexible width                  │
│         │                                 │
│         │                                 │
└─────────┴─────────────────────────────────┘
```

**Components:**
- **Header**: Navigation, title, global actions
- **Left Sidebar**: Navigation, filters, guidance
- **Content Area**: Main content

### 2-Column Layout with Right Panel
For details-heavy interfaces.

```
┌───────────────────────────────┬─────────┐
│ HEADER                        │         │
├───────────────────────────────┤ DETAIL  │
│ MAIN CONTENT                  │ PANEL   │
│                               │ 280px   │
└───────────────────────────────┴─────────┘
```

### Responsive Behavior

| Breakpoint | Width | Behavior |
|-----------|-------|----------|
| Mobile | < 768px | Stack vertically, hide/collapse sidebars |
| Tablet | 768px - 1024px | Collapse sidebar to icon-only |
| Desktop | > 1024px | Full layout with sidebars visible |

## Component Patterns

### Status Indicators

#### Success Badge
- **Background**: #d7f5e9 (light) or #064e3b (dark)
- **Text**: #4caf50 (light) or #10b981 (dark)
- **Icon**: Green checkmark
- **Usage**: Completed items, successful states

#### Warning Badge
- **Background**: #fff3cd (light)
- **Text**: #856404 (light)
- **Icon**: Exclamation mark
- **Usage**: Items requiring attention

#### Error Badge
- **Background**: #f8d7da (light)
- **Text**: #721c24 (light)
- **Icon**: Red X mark
- **Usage**: Failed items, errors

#### Info Badge
- **Background**: #e3f2fd (light) or #1e3a8a (dark)
- **Text**: #90caf9 (light) or #60a5fa (dark)
- **Icon**: Information mark
- **Usage**: Informational items

### Interactive States

#### Default State
- Normal colors as defined in palette
- No hover effect
- Full opacity (100%)

#### Hover State
- 1 shade darker (slightly more saturated)
- Slight shadow increase
- Cursor changes to pointer
- 200ms transition

#### Active/Pressed State
- 2 shades darker
- Strong shadow
- Potentially different layout (button press effect)
- Immediate response (0ms transition)

#### Disabled State
- Gray background (#cbd7e0 light, #555d6f dark)
- Gray border
- 50% opacity text
- No pointer cursor
- No hover effects

#### Focus State
- Clear focus ring (2px border)
- Use info border color for consistency
- Visible on all interactive elements
- Important for accessibility

### Data Display Patterns

#### Table Header
- **Background**: Primary background color (#f4f6f8 light)
- **Font Weight**: Semibold (600)
- **Border Bottom**: Primary border color
- **Padding**: 12px vertical, 16px horizontal

#### Table Row - Alternate
- **Background**: Alternating white and #fafafa (light)
- **Hover**: #eef4ff highlight
- **Border**: Subtle line between rows

#### Metrics Display
- **Title**: Secondary text color, smaller font
- **Value**: Primary text, larger font, semibold
- **Unit**: Tertiary text, smaller font
- **Trend**: Green (up/good), red (down/bad)

## Spacing Patterns

### Component Padding
- **Small elements**: 8px (2 units)
- **Standard**: 12px - 16px (3-4 units)
- **Large**: 20px - 24px (5-6 units)

### Margin Relationships
- **Between sections**: 24px - 32px
- **Between components**: 16px
- **Between card/element rows**: 12px

### Gaps in Grids/Flexbox
- **Tight**: 8px
- **Standard**: 16px
- **Loose**: 24px

## Typography Hierarchy

### Page Structure

```
Page Title              32px / bold / primary text
└─ Section Heading     24px / semibold / primary text
   └─ Subsection      20px / semibold / primary text
      └─ Body Text    16px / normal / primary text
         └─ Helper    14px / normal / secondary text
         └─ Small     12px / normal / tertiary text
```

### Visual Weight
- **Heavy**: Use 700 weight + larger size for emphasis
- **Medium**: Use 600 weight for section headings
- **Light**: Use 400 weight for body text
- **Never mix**: Avoid mixing too many weights

## Localization Patterns

### Language Support
- **English**: Primary language
- **Chinese**: Full UI localization

### Text Expansion
- Chinese is more compact than English
- Plan layout for 30% text expansion
- Use flexible/wrapping layouts when possible

### Line Height Adjustment
- **English**: 1.5 line height
- **Chinese**: 1.6-1.8 line height (more spacing needed)

## Animation Patterns

### Standard Transition
All color and position changes:
```css
transition: all 300ms ease-in-out;
```

### Quick Interactions
Micro-interactions (hover, focus):
```css
transition: all 200ms ease-in-out;
```

### Complex Animations
Page transitions, complex sequences:
```css
animation-duration: 500ms;
animation-timing-function: ease-in-out;
```

### Avoid
- Animations longer than 500ms
- Bounce/elastic easing (too playful)
- Multiple simultaneous animations (cluttered feel)

## Accessibility Patterns

### Color Combinations
Always pair text with sufficient contrast:

**Light Mode:**
- Primary text (#1a202c) on white (#ffffff): 18:1 ratio ✅
- Primary text on info bg (#e3f2fd): 10:1 ratio ✅

**Dark Mode:**
- Primary text (#f3f4f6) on dark bg (#1a1a1a): 15:1 ratio ✅
- Primary text on info bg (#1e3a8a): 11:1 ratio ✅

### Keyboard Navigation
- All interactive elements must be keyboard accessible
- Focus indicators must be visible
- Tab order follows logical reading order

### Screen Reader Support
- Use semantic HTML (`<button>`, `<a>`, form elements)
- Provide meaningful alt text for icons
- Use `aria-label` for interactive elements when needed
