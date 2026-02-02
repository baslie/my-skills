---
name: wireframe-builder
description: |
  Generates lo-fi wireframes as single HTML files with Tailwind CSS and Alpine.js.
  Triggers when user asks to: create wireframe, sketch page layout, prototype UI,
  design page structure, visualize interface concept, build mockup, or plan
  website/app layout. Supports: landing pages, dashboards, forms, e-commerce,
  admin panels, mobile screens, etc.
argument-hint: "[page description or PRD document]"
allowed-tools: Bash(python:*), Read, Write
---

# Wireframe Builder

Generate lo-fi wireframes as single HTML files using Tailwind CSS with a grayscale `wire-*` palette.

## Quick Start

1. Analyze user's prompt or document to understand requirements
2. Determine sections, components, and layout from context
3. Copy template from `assets/template.html`
4. Pick components from `references/` files
5. Suggest filename and ask for confirmation
6. Create `wireframes/` folder if needed
7. Save to `wireframes/[confirmed-name].html`
8. Validate: `python scripts/validate-wireframe.py wireframes/[name].html`
9. Open in browser: `python scripts/open-wireframe.py wireframes/[name].html`

## Context Analysis

### Input Sources
The skill works with any input that describes what to build:
- **Direct prompt**: "Create a user profile page with settings"
- **Text document**: PRD, user story, feature spec, design brief, notes
- **Reference**: Description of existing page or competitor

### Automatic Understanding
Analyze the input to identify:
- Page purpose and main functionality
- Required sections and their hierarchy
- Key UI elements (forms, tables, lists, cards)
- User actions and flows
- Implicit mobile requirements

### Minimal Questions
Only ask when context is genuinely ambiguous:
- "Should I include [specific element] mentioned in the doc?"
- "The document describes two flows. Which is primary?"

**Never ask about predefined categories** (SaaS, corporate, landing, etc.)
The wireframe structure emerges from the actual requirements.

## Document Processing

When user provides a document (PRD, spec, user story, notes, any text):

1. **Read the document** completely
2. **Extract requirements**:
   - Main purpose of the page
   - User actions and flows
   - Data to display (lists, tables, forms)
   - Navigation needs
   - Mentioned UI elements
3. **Map to components**:
   - Forms mentioned → form components
   - Lists/data → tables, cards, grids
   - Actions → buttons, CTAs
   - Media references → image placeholders
4. **Build wireframe** matching the document's intent

## HTML Template

Copy the template from `assets/template.html` as your starting point.

The template includes:
- Tailwind CSS with `wire-*` color tokens
- Alpine.js for interactive components
- Base styles and responsive meta tags

## Design Tokens

| Token | Class | Hex | Purpose |
|-------|-------|-----|---------|
| `wire-bg` | `bg-wire-bg` | #ffffff | Page background |
| `wire-surface` | `bg-wire-surface` | #f5f5f5 | Card/section bg |
| `wire-border` | `border-wire-border` | #e0e0e0 | Borders |
| `wire-muted` | `text-wire-muted` | #9e9e9e | Placeholder, icons |
| `wire-text` | `text-wire-text` | #424242 | Body text |
| `wire-dark` | `bg-wire-dark` | #212121 | Headings, primary buttons |

## Component Reference

See `references/components.md` for the full index, or jump to specific categories:

- **[Navigation](references/navigation.md)**: Header, sidebar, breadcrumbs, hamburger menu, footer
- **[Content](references/content.md)**: Hero sections, cards, testimonials, pricing, FAQ, layouts
- **[Forms](references/forms.md)**: Inputs, buttons, login, search, contact forms
- **[Tables](references/tables.md)**: Simple table, data tables with actions, pagination
- **[Interactive](references/interactive.md)**: Modal, dropdown, tabs, toast (Alpine.js)
- **[Mobile](references/mobile.md)**: Bottom nav, mobile cards, swipeable carousel
- **[States](references/states.md)**: Spinner, skeleton, empty state, progress, badges, icons

## Interactivity

### CSS-only (preferred)
- Hover: `hover:bg-wire-surface`, `hover:border-wire-muted`
- Focus: `focus:border-wire-muted focus:outline-none`
- Transitions: `transition-colors`
- Accordion: `<details>` / `<summary>` elements

### Alpine.js (when needed)
- Modals and dialogs (open/close state)
- Dropdown menus (click outside to close)
- Tabs (switching active tab)
- Mobile hamburger menu (toggle visibility)
- Toast notifications (auto-dismiss)

Basic pattern:
```html
<div x-data="{ open: false }">
  <button @click="open = !open">Toggle</button>
  <div x-show="open" x-transition>Content</div>
</div>
```

## Responsive Design

- Mobile-first: start with single column
- Use `md:` breakpoint for tablet/desktop
- Grid: `grid md:grid-cols-2 lg:grid-cols-3 gap-6`
- Hide on mobile: `hidden md:flex`
- Show on mobile: `md:hidden`

## Generation Checklist

```
- [ ] Analyzed user input
- [ ] Determined sections and components
- [ ] Created responsive layout
- [ ] Added hover states
- [ ] Used wire-* palette only
- [ ] Added HTML section comments (<!-- ===== SECTION ===== -->)
- [ ] Tested at 375px width
```

## Examples

See `examples/` directory for ready-to-use wireframe templates:
- `landing-page.html` — Basic marketing page (header, hero, features, CTA, footer)
- `dashboard.html` — Admin panel with sidebar navigation
- `login-form.html` — Authentication page

## File Naming & Storage

### Output Directory
All wireframes save to `wireframes/` in project root.

### Naming Convention
Generate kebab-case names from content (2-4 words):
- User profile page → `user-profile.html`
- Product checkout → `checkout-flow.html`
- Admin user list → `admin-users.html`

### Confirmation Flow
Always confirm before saving:
> "I'll save this as `wireframes/user-profile.html`. Is this name okay?"

## Verification

After generating a wireframe:

1. **Validate**: `python scripts/validate-wireframe.py wireframes/[name].html`
2. **Open**: `python scripts/open-wireframe.py wireframes/[name].html`
3. **Check**:
   - All requested sections present
   - Responsive at 375px width
   - Hover states work
   - Only `wire-*` colors used
   - Semantic HTML used
