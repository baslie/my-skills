---
name: wireframe-builder
description: |
  Generate lo-fi wireframes as single HTML files with Tailwind CSS.
  Use when user asks to: create wireframe, sketch page layout, prototype UI,
  design page structure, visualize interface concept, build mockup, or plan
  website/app layout. Supports: landing pages, dashboards, forms, e-commerce,
  admin panels, mobile screens, etc.
---

# Wireframe Builder

Generate lo-fi wireframes as single HTML files using Tailwind CSS with a grayscale `wire-*` palette.

## Quick Start

1. Analyze user's prompt or document to understand requirements
2. Determine sections, components, and layout from context
3. Copy template from `assets/template.html`
4. Pick components from `references/components.md`
5. Suggest filename and ask for confirmation
6. Create `wireframes/` folder if needed
7. Save to `wireframes/[confirmed-name].html`

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

## HTML Template Structure

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Wireframe - [Page Name]</title>
  <script src="https://cdn.tailwindcss.com"></script>
  <script>
    tailwind.config = {
      theme: {
        extend: {
          colors: {
            wire: {
              bg: 'hsl(0 0% 100%)',
              surface: 'hsl(0 0% 96%)',
              border: 'hsl(0 0% 88%)',
              muted: 'hsl(0 0% 62%)',
              text: 'hsl(0 0% 26%)',
              dark: 'hsl(0 0% 13%)',
            }
          },
          borderRadius: {
            wire: '0.375rem',
          }
        }
      }
    }
  </script>
  <style type="text/tailwindcss">
    @layer base {
      body {
        @apply bg-wire-bg text-wire-text;
        font-family: system-ui, -apple-system, sans-serif;
      }
    }
  </style>
</head>
<body class="min-h-screen">
  <!-- ========== SECTION NAME ========== -->
  <!-- Content here -->
</body>
</html>
```

## Design Tokens

| Token | Class | Hex | Purpose |
|-------|-------|-----|---------|
| `wire-bg` | `bg-wire-bg` | #ffffff | Page background |
| `wire-surface` | `bg-wire-surface` | #f5f5f5 | Card/section bg |
| `wire-border` | `border-wire-border` | #e0e0e0 | Borders |
| `wire-muted` | `text-wire-muted` | #9e9e9e | Placeholder, icons |
| `wire-text` | `text-wire-text` | #424242 | Body text |
| `wire-dark` | `bg-wire-dark` | #212121 | Headings, primary buttons |

## Core Components

### Image Placeholder
```html
<div class="bg-wire-surface border border-wire-border border-dashed rounded-wire aspect-video flex items-center justify-center">
  <svg class="w-12 h-12 text-wire-muted" fill="currentColor" viewBox="0 0 24 24">
    <path d="M21 19V5c0-1.1-.9-2-2-2H5c-1.1 0-2 .9-2 2v14c0 1.1.9 2 2 2h14c1.1 0 2-.9 2-2zM8.5 13.5l2.5 3.01L14.5 12l4.5 6H5l3.5-4.5z"/>
  </svg>
</div>
```

### Primary Button
```html
<button class="px-4 py-2 bg-wire-dark text-white rounded-wire hover:bg-wire-text transition-colors">
  Button
</button>
```

### Secondary Button
```html
<button class="px-4 py-2 border border-wire-border text-wire-text rounded-wire hover:bg-wire-surface transition-colors">
  Secondary
</button>
```

### Card
```html
<div class="bg-wire-surface border border-wire-border rounded-wire p-4 space-y-3">
  <!-- content -->
</div>
```

### Input
```html
<input type="text" placeholder="Placeholder..."
  class="w-full px-3 py-2 border border-wire-border rounded-wire bg-wire-bg text-wire-text placeholder:text-wire-muted focus:outline-none focus:border-wire-muted">
```

## Interactivity

Use CSS-only where possible:
- Hover: `hover:bg-wire-surface`, `hover:border-wire-muted`
- Focus: `focus:border-wire-muted focus:outline-none`
- Transitions: `transition-colors`
- Accordion: `<details>` / `<summary>` elements

## Layout Patterns

### Container
```html
<div class="max-w-6xl mx-auto px-4">
  <!-- content -->
</div>
```

### Section with Background
```html
<section class="py-16 bg-wire-surface">
  <div class="max-w-6xl mx-auto px-4">
    <!-- content -->
  </div>
</section>
```

### Dashboard (Sidebar + Main)
```html
<div class="flex min-h-screen">
  <aside class="w-64 border-r border-wire-border bg-wire-bg p-4">
    <!-- sidebar -->
  </aside>
  <main class="flex-1 p-6 bg-wire-surface">
    <!-- content -->
  </main>
</div>
```

## Responsive Design

- Mobile-first: start with single column
- Use `md:` breakpoint for tablet/desktop
- Grid: `grid md:grid-cols-2 lg:grid-cols-3 gap-6`
- Hide on mobile: `hidden md:flex`
- Show on mobile: `md:hidden`

## Generation Checklist

- [ ] Use `wire-*` palette only (grayscale)
- [ ] Add HTML comments for sections: `<!-- ===== HEADER ===== -->`
- [ ] Include hover states on interactive elements
- [ ] Make layout responsive with `md:` breakpoints
- [ ] Use semantic HTML (`<header>`, `<main>`, `<section>`, `<footer>`)
- [ ] Test: open in browser, resize to 375px width

## Component Reference

See `references/components.md` for full component library:
- Navigation (header, sidebar, breadcrumbs)
- Hero sections (with image, centered, with form)
- Content (cards, testimonials, pricing, FAQ)
- Forms (login, signup, contact, search)
- Footer (simple, multi-column)
- Tables
- Utility icons (SVG)

## File Naming & Storage

### Output Directory
All wireframes save to `wireframes/` in project root:
```
project/
└── wireframes/
    ├── user-profile.html
    ├── checkout-flow.html
    └── admin-users.html
```

### Naming Convention
Generate kebab-case names from content (2-4 words):
- User profile page → `user-profile.html`
- Product checkout → `checkout-flow.html`
- Admin user list → `admin-users.html`

### Confirmation Flow
Always confirm before saving:
> "I'll save this as `wireframes/user-profile.html`. Is this name okay?"

Use user's preferred name if they suggest one.
