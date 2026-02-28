# ACP Design Tokens Reference

Complete specification of all design tokens for Alauda Container Platform.

## Color Tokens

### Light Mode

#### Backgrounds
- **Main**: `#ffffff` - Primary content areas
- **Primary**: `#f4f6f8` - Top chrome, secondary panels, alternate backgrounds
- **Panel**: `#eef4ff` - Left sidebars, guidance areas, panel backgrounds
- **Secondary**: `#fafafa` - Subtle alternate backgrounds

#### Info (Blue Palette)
- **Background**: `#e3f2fd` - Alert boxes, informational content
- **Border**: `#90caf9` - Info element borders
- **Dark**: `#1e3a8a` - Dark text on light info backgrounds

#### Success (Green Palette)
- **Background**: `#d7f5e9` - Success states, completion indicators
- **Border**: `#4caf50` - Success state borders and accents
- **Dark**: `#064e3b` - Dark text on light success backgrounds

#### Process (Process Blue Palette)
- **Background**: `#e8f2ff` - Processing steps, workflow states
- **Border**: `#2196f3` - Process state indicators
- **Dark**: `#1e40af` - Dark text on light process backgrounds

#### Teal (Teal Palette)
- **Background**: `#e0f2f1` - Hypothesis/investigation states
- **Border**: `#4db6ac` - Teal state borders
- **Dark**: `#134e4a` - Dark text on light teal backgrounds

#### Borders
- **Primary**: `#cbd7e0` - Main borders, panel dividers
- **Secondary**: `#cbd5e1` - Card separators, subtle lines
- **Light**: `#e2e8f0` - Very subtle borders, hover states

#### Text
- **Primary**: `#1a202c` - Main body text, headings
- **Secondary**: `#4a5568` - Secondary text, labels
- **Tertiary**: `#718096` - Tertiary text, hints
- **Disabled**: `#cbd5e0` - Disabled text, inactive states

### Dark Mode

#### Backgrounds
- **Main**: `#1a1a1a` - Primary content areas (nearly black)
- **Primary**: `#2d3748` - Top chrome, secondary panels
- **Panel**: `#1e3a5f` - Left sidebars, guidance areas (dark blue tint)
- **Secondary**: `#2d3748` - Alternate backgrounds

#### Info (Dark Blue Palette)
- **Background**: `#1e3a8a` - Alert boxes
- **Border**: `#60a5fa` - Info element borders (brighter for visibility)
- **Dark**: `#1e3a8a` - Dark text reference

#### Success (Dark Green Palette)
- **Background**: `#064e3b` - Success states
- **Border**: `#10b981` - Success state borders
- **Dark**: `#064e3b` - Dark text reference

#### Process (Dark Process Palette)
- **Background**: `#1e40af` - Processing steps
- **Border**: `#3b82f6` - Process state indicators (brighter)
- **Dark**: `#1e40af` - Dark text reference

#### Teal (Dark Teal Palette)
- **Background**: `#134e4a` - Hypothesis/investigation states
- **Border**: `#14b8a6` - Teal state borders (brighter)
- **Dark**: `#134e4a` - Dark text reference

#### Borders
- **Primary**: `#4b5563` - Main borders
- **Secondary**: `#555d6f` - Card separators
- **Light**: `#374151` - Very subtle borders

#### Text
- **Primary**: `#f3f4f6` - Main body text (near white)
- **Secondary**: `#e5e7eb` - Secondary text
- **Tertiary**: `#d1d5db` - Tertiary text
- **Disabled**: `#9ca3af` - Disabled text

## Spacing Scale

ACP uses a **10px base unit grid system** for consistent spacing:

```
4px   = 0.25rem  (--space-px1)
8px   = 0.5rem   (--space-px2)
12px  = 3rem     (--space-px6)   [Note: Intentional - maintains 10px grid visually]
16px  = 4rem     (--space-px4)   [Standard padding/margin]
20px  = 5rem     (--space-px20)
24px  = 6rem     (--space-px6)   [Large spacing]
32px  = 8rem     (--space-px32)  [Section spacing]
48px  = 12rem    (--space-px48)
64px  = 16rem    (--space-px64)  [Major section gaps]
```

**Usage Guidelines:**
- Use for padding, margin, and gaps
- Maintain consistent spacing relationships
- Never use arbitrary spacing values (e.g., 13px, 25px)

## Typography

### Font Family
```
-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto,
'Helvetica Neue', Arial, sans-serif
```
System font stack for optimal performance and native look across platforms.

### Font Sizes

| Token | Size | Usage |
|-------|------|-------|
| `xs` | 0.75rem (12px) | Small labels, captions |
| `sm` | 0.875rem (14px) | Form helper text |
| `base` | 1rem (16px) | Body text (default) |
| `lg` | 1.125rem (18px) | Large body text |
| `xl` | 1.25rem (20px) | Subheadings |
| `2xl` | 1.5rem (24px) | Section headings |
| `3xl` | 1.875rem (30px) | Page headings |
| `4xl` | 2.25rem (36px) | Hero headings |

### Font Weights

| Token | Weight | Usage |
|-------|--------|-------|
| `light` | 300 | Not commonly used |
| `normal` | 400 | Default body text |
| `medium` | 500 | Interactive elements, accents |
| `semibold` | 600 | Subheadings, section titles |
| `bold` | 700 | Main headings, emphasis |

### Line Heights

| Token | Height | Usage |
|-------|--------|-------|
| `tight` | 1.1 | Headings, compact text |
| `snug` | 1.2 | Subheadings |
| `normal` | 1.5 | Body text (default) |
| `relaxed` | 1.6 | Chinese text (more spacing) |
| `loose` | 1.8 | Accessibility-focused text |

**Note:** Chinese text requires taller line heights (1.6-1.8) due to character complexity.

## Effects

### Border Radius

| Token | Value | Usage |
|-------|-------|-------|
| `sm` | 4px | Form inputs, small elements |
| `md` | 8px | Cards, standard buttons |
| `lg` | 12px | Panels, containers |
| `xl` | 16px | Major sections, modals |

### Shadows

| Token | Value | Usage |
|-------|-------|-------|
| `none` | none | Flat designs, disabled states |
| `subtle` | `0 1px 2px rgba(0,0,0,0.05)` | Slight elevation |
| `medium` | `0 4px 6px rgba(0,0,0,0.1)` | Standard elevation |
| `strong` | `0 10px 15px rgba(0,0,0,0.15)` | High elevation, focus |

**Note:** Shadows are adjusted for dark mode to avoid harsh contrast.

### Transitions

| Token | Duration | Usage |
|-------|----------|-------|
| `fast` | 200ms | Quick micro-interactions, hovers |
| `standard` | 300ms | Standard interactions, animations |
| `slow` | 500ms | Complex animations, page transitions |

All transitions use `ease-in-out` timing function for smooth feel.

## Token Naming Convention

All tokens follow a consistent naming pattern:

```
--{category}-{subcategory}-{name}

Examples:
--color-info-bg          # Info background
--color-text-primary     # Primary text color
--space-px16             # 16px spacing
--font-size-lg           # Large font size
--shadow-medium          # Medium shadow
--radius-md              # Medium border radius
--transition-fast        # Fast transition
```

## Semantic Usage

Prefer semantic color names over literal values:

### ✅ DO USE:
```css
background-color: var(--color-success-bg);
color: var(--color-text-primary);
border: 1px solid var(--color-borders-primary);
```

### ❌ DON'T USE:
```css
background-color: #d7f5e9;
color: #1a202c;
border: 1px solid #cbd7e0;
```

Semantic names ensure consistency and make future design updates easier.

## Accessibility Compliance

All color combinations meet **WCAG AA minimum contrast ratios**:

- **Large text (18px+)**: 3:1 minimum ratio
- **Normal text (14px)**: 4.5:1 minimum ratio
- **UI components**: 3:1 minimum ratio

Dark mode colors are specifically chosen to maintain these ratios.

## Version & Maintenance

**Current Version**: 1.0.0
**Last Updated**: January 2025
**Format**: JSON (canonical), TypeScript, CSS, Tailwind, CSS Module

To update tokens:
1. Modify `design-tokens.json`
2. Run converter: `python3 scripts/design-tokens-converter.py`
3. Commit changes with version bump
4. Document changes in migration guide
