# Wireframe Component Library

> **Creative Note:** This is a reference library, not a rulebook. These components are *primitives* and *patterns* — use them as inspiration, modify them freely, or invent something entirely new. The best wireframe is one that serves your specific design intent, not one that assembles pre-made blocks.
>
> Feel free to: combine patterns unexpectedly, modify proportions, ignore conventions, or create components that don't exist here.

---

Lo-fi components with `wire-*` color palette. Use as starting points, not requirements.

---

## Design Tokens

| Token | Class | Purpose |
|-------|-------|---------|
| `wire-bg` | `bg-wire-bg` | Page background (white) |
| `wire-surface` | `bg-wire-surface` | Card/section background (light gray) |
| `wire-border` | `border-wire-border` | Element borders |
| `wire-muted` | `text-wire-muted` | Placeholder text, icons |
| `wire-text` | `text-wire-text` | Body text |
| `wire-dark` | `bg-wire-dark`, `text-wire-dark` | Headings, primary buttons |

### Border Radius

| Token | Class | Value |
|-------|-------|-------|
| `wire` | `rounded-wire` | 0.375rem (6px) |

---

## Component Categories

### [Navigation](navigation.md)
- Header with logo, nav, and CTA
- Sidebar navigation
- Breadcrumbs
- Hamburger menu (mobile)
- Simple footer
- Multi-column footer

### [Content](content.md)
- Hero sections (image right, centered, with signup form)
- Cards and card grids
- Image/avatar placeholders
- Testimonials
- Pricing cards
- FAQ accordion
- Layout patterns (container, sections, dashboard)

### [Forms](forms.md)
- Input fields (basic, with label, textarea, select, checkbox)
- Buttons (primary, secondary, ghost, button group)
- Complete forms (login, search, contact)

### [Tables](tables.md)
- Simple table
- Data table with actions
- Table with pagination

### [Interactive](interactive.md)
Alpine.js-powered components:
- Modal / dialog
- Dropdown menu
- Tabs
- Toast notifications
- Accordion

### [Mobile](mobile.md)
- Bottom navigation
- Mobile cards
- Swipeable card carousel
- See also: Hamburger menu in [navigation.md](navigation.md)

### [States](states.md)
- Spinners (simple, with text, centered)
- Skeleton loaders (text, card, avatar, table)
- Empty state
- Progress bars (simple, with label, steps, circular)
- Badges / tags
- Pagination
- Utility icons (image, user, check, menu, close, arrow)
