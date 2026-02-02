# Content Components

Ready-to-use content blocks with `wire-*` color palette.

## Contents

- [Hero Sections](#hero-sections)
  - [Hero with Image Right](#hero-with-image-right)
  - [Hero Centered Minimal](#hero-centered-minimal)
  - [Hero with Signup Form](#hero-with-signup-form)
- [Cards](#cards)
  - [Basic Card](#basic-card)
  - [Card Grid (3 columns)](#card-grid-3-columns)
- [Placeholders](#placeholders)
  - [Image Placeholder](#image-placeholder)
  - [Avatar Placeholder](#avatar-placeholder)
- [Testimonial](#testimonial)
- [Pricing Card](#pricing-card)
- [FAQ Accordion (Pure CSS)](#faq-accordion-pure-css)
- [Layout Patterns](#layout-patterns)
  - [Container with Max Width](#container-with-max-width)
  - [Section with Background](#section-with-background)
  - [Dashboard Layout (Sidebar + Main)](#dashboard-layout-sidebar--main)

---

## Hero Sections

### Hero with Image Right

```html
<section class="py-16 md:py-24">
  <div class="max-w-6xl mx-auto px-4">
    <div class="grid md:grid-cols-2 gap-12 items-center">
      <div class="space-y-6">
        <h1 class="text-4xl md:text-5xl font-bold text-wire-dark leading-tight">
          Main headline goes here
        </h1>
        <p class="text-lg text-wire-muted">
          Supporting text that explains the value proposition.
        </p>
        <div class="flex flex-wrap gap-3">
          <button class="px-6 py-3 bg-wire-dark text-white rounded-wire hover:bg-wire-text transition-colors">
            Primary action
          </button>
          <button class="px-6 py-3 border border-wire-border text-wire-text rounded-wire hover:bg-wire-surface transition-colors">
            Secondary action
          </button>
        </div>
      </div>
      <div class="bg-wire-surface border border-wire-border border-dashed rounded-wire aspect-video flex items-center justify-center">
        <svg class="w-16 h-16 text-wire-muted" fill="currentColor" viewBox="0 0 24 24">
          <path d="M21 19V5c0-1.1-.9-2-2-2H5c-1.1 0-2 .9-2 2v14c0 1.1.9 2 2 2h14c1.1 0 2-.9 2-2zM8.5 13.5l2.5 3.01L14.5 12l4.5 6H5l3.5-4.5z"/>
        </svg>
      </div>
    </div>
  </div>
</section>
```

### Hero Centered Minimal

```html
<section class="py-24 md:py-32 text-center">
  <div class="max-w-3xl mx-auto px-4 space-y-6">
    <h1 class="text-4xl md:text-6xl font-bold text-wire-dark">
      Headline here
    </h1>
    <p class="text-xl text-wire-muted">
      Supporting text that explains the value proposition in one or two sentences.
    </p>
    <div class="flex justify-center gap-4">
      <button class="px-8 py-3 bg-wire-dark text-white rounded-wire hover:bg-wire-text transition-colors">
        Get started
      </button>
    </div>
  </div>
</section>
```

### Hero with Signup Form

```html
<section class="py-16 md:py-24">
  <div class="max-w-6xl mx-auto px-4">
    <div class="grid md:grid-cols-2 gap-12 items-center">
      <div class="space-y-6">
        <h1 class="text-4xl md:text-5xl font-bold text-wire-dark leading-tight">
          Headline goes here
        </h1>
        <p class="text-lg text-wire-muted">
          Brief description of the offer.
        </p>
      </div>
      <div class="bg-wire-surface border border-wire-border rounded-wire p-6 space-y-4">
        <h2 class="text-xl font-semibold text-wire-dark">Sign up free</h2>
        <input type="email" placeholder="Email address" class="w-full px-4 py-3 border border-wire-border rounded-wire bg-wire-bg text-wire-text placeholder:text-wire-muted focus:outline-none focus:border-wire-muted">
        <input type="password" placeholder="Password" class="w-full px-4 py-3 border border-wire-border rounded-wire bg-wire-bg text-wire-text placeholder:text-wire-muted focus:outline-none focus:border-wire-muted">
        <button class="w-full px-4 py-3 bg-wire-dark text-white rounded-wire hover:bg-wire-text transition-colors">
          Create account
        </button>
        <p class="text-sm text-wire-muted text-center">
          Already have an account? <a href="#" class="text-wire-text hover:underline">Log in</a>
        </p>
      </div>
    </div>
  </div>
</section>
```

---

## Cards

### Basic Card

```html
<div class="bg-wire-surface border border-wire-border rounded-wire p-6 space-y-4">
  <h3 class="text-lg font-semibold text-wire-dark">Card title</h3>
  <p class="text-wire-muted text-sm">Card description text goes here.</p>
</div>
```

### Card Grid (3 columns)

```html
<div class="grid md:grid-cols-3 gap-6">
  <div class="bg-wire-surface border border-wire-border rounded-wire p-6 space-y-4">
    <div class="w-12 h-12 bg-wire-bg border border-wire-border rounded-wire flex items-center justify-center">
      <svg class="w-6 h-6 text-wire-muted" fill="none" stroke="currentColor" viewBox="0 0 24 24">
        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13 10V3L4 14h7v7l9-11h-7z"/>
      </svg>
    </div>
    <h3 class="text-lg font-semibold text-wire-dark">Feature</h3>
    <p class="text-wire-muted text-sm">Description text.</p>
  </div>
  <!-- Repeat for more cards -->
</div>
```

---

## Placeholders

### Image Placeholder

```html
<div class="bg-wire-surface border border-wire-border border-dashed rounded-wire aspect-video flex items-center justify-center">
  <svg class="w-12 h-12 text-wire-muted" fill="currentColor" viewBox="0 0 24 24">
    <path d="M21 19V5c0-1.1-.9-2-2-2H5c-1.1 0-2 .9-2 2v14c0 1.1.9 2 2 2h14c1.1 0 2-.9 2-2zM8.5 13.5l2.5 3.01L14.5 12l4.5 6H5l3.5-4.5z"/>
  </svg>
</div>
```

### Avatar Placeholder

```html
<div class="w-12 h-12 bg-wire-surface border border-wire-border rounded-full flex items-center justify-center">
  <svg class="w-6 h-6 text-wire-muted" fill="currentColor" viewBox="0 0 24 24">
    <path d="M12 12c2.21 0 4-1.79 4-4s-1.79-4-4-4-4 1.79-4 4 1.79 4 4 4zm0 2c-2.67 0-8 1.34-8 4v2h16v-2c0-2.66-5.33-4-8-4z"/>
  </svg>
</div>
```

---

## Testimonial

```html
<div class="bg-wire-surface border border-wire-border rounded-wire p-6 space-y-4">
  <p class="text-wire-text italic">"Quote text goes here. Keep it brief and impactful."</p>
  <div class="flex items-center gap-3">
    <div class="w-10 h-10 bg-wire-border rounded-full"></div>
    <div>
      <p class="text-sm font-medium text-wire-dark">Name</p>
      <p class="text-sm text-wire-muted">Title, Company</p>
    </div>
  </div>
</div>
```

---

## Pricing Card

```html
<div class="bg-wire-bg border border-wire-border rounded-wire p-6 space-y-6">
  <div>
    <h3 class="text-lg font-semibold text-wire-dark">Plan name</h3>
    <p class="text-wire-muted text-sm">Brief description</p>
  </div>
  <div class="flex items-baseline gap-1">
    <span class="text-4xl font-bold text-wire-dark">$29</span>
    <span class="text-wire-muted">/month</span>
  </div>
  <ul class="space-y-3 text-sm">
    <li class="flex items-center gap-2 text-wire-text">
      <svg class="w-5 h-5 text-wire-muted" fill="none" stroke="currentColor" viewBox="0 0 24 24">
        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7"/>
      </svg>
      Feature one
    </li>
    <li class="flex items-center gap-2 text-wire-text">
      <svg class="w-5 h-5 text-wire-muted" fill="none" stroke="currentColor" viewBox="0 0 24 24">
        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7"/>
      </svg>
      Feature two
    </li>
  </ul>
  <button class="w-full px-4 py-2 bg-wire-dark text-white rounded-wire hover:bg-wire-text transition-colors">
    Choose plan
  </button>
</div>
```

---

## FAQ Accordion (Pure CSS)

```html
<div class="space-y-2">
  <details class="border border-wire-border rounded-wire">
    <summary class="px-4 py-3 cursor-pointer text-wire-dark font-medium hover:bg-wire-surface transition-colors">
      Question one?
    </summary>
    <div class="px-4 pb-4 text-wire-muted text-sm">
      Answer text goes here.
    </div>
  </details>
  <details class="border border-wire-border rounded-wire">
    <summary class="px-4 py-3 cursor-pointer text-wire-dark font-medium hover:bg-wire-surface transition-colors">
      Question two?
    </summary>
    <div class="px-4 pb-4 text-wire-muted text-sm">
      Answer text goes here.
    </div>
  </details>
</div>
```

---

## Layout Patterns

### Container with Max Width

```html
<div class="max-w-6xl mx-auto px-4">
  <!-- Content -->
</div>
```

### Section with Background

```html
<section class="py-16 bg-wire-surface">
  <div class="max-w-6xl mx-auto px-4">
    <!-- Content -->
  </div>
</section>
```

### Dashboard Layout (Sidebar + Main)

```html
<div class="flex min-h-screen">
  <!-- Sidebar -->
  <aside class="w-64 border-r border-wire-border bg-wire-bg p-4">
    <!-- Sidebar content -->
  </aside>

  <!-- Main content -->
  <main class="flex-1 p-6 bg-wire-surface">
    <!-- Page content -->
  </main>
</div>
```
