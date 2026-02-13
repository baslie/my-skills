# UI State Components

Loading, empty, and progress states with `wire-*` color palette.

## Contents

- [Spinners](#spinners)
  - [Simple Spinner](#simple-spinner)
  - [Spinner with Text](#spinner-with-text)
  - [Large Centered Spinner](#large-centered-spinner)
- [Skeleton Loaders](#skeleton-loaders)
  - [Text Skeleton](#text-skeleton)
  - [Card Skeleton](#card-skeleton)
  - [Avatar + Text Skeleton](#avatar--text-skeleton)
  - [Table Skeleton](#table-skeleton)
- [Empty State](#empty-state)
- [Progress Bars](#progress-bars)
  - [Simple Progress Bar](#simple-progress-bar)
  - [Progress Bar with Label](#progress-bar-with-label)
  - [Steps Progress](#steps-progress)
  - [Circular Progress (CSS)](#circular-progress-css)
- [Badges / Tags](#badges--tags)
  - [Default Badge](#default-badge)
  - [Status Badges](#status-badges)
- [Pagination](#pagination)
- [Utility Icons](#utility-icons)

---

## Spinners

### Simple Spinner

```html
<div class="w-6 h-6 border-2 border-wire-border border-t-wire-dark rounded-full animate-spin"></div>
```

### Spinner with Text

```html
<div class="flex items-center gap-2">
  <div class="w-5 h-5 border-2 border-wire-border border-t-wire-dark rounded-full animate-spin"></div>
  <span class="text-sm text-wire-muted">Loading...</span>
</div>
```

### Large Centered Spinner

```html
<div class="flex items-center justify-center py-12">
  <div class="w-8 h-8 border-2 border-wire-border border-t-wire-dark rounded-full animate-spin"></div>
</div>
```

---

## Skeleton Loaders

### Text Skeleton

```html
<div class="animate-pulse space-y-2">
  <div class="h-4 bg-wire-surface rounded w-3/4"></div>
  <div class="h-4 bg-wire-surface rounded w-full"></div>
  <div class="h-4 bg-wire-surface rounded w-5/6"></div>
</div>
```

### Card Skeleton

```html
<div class="animate-pulse bg-wire-bg border border-wire-border rounded-wire p-4 space-y-4">
  <div class="h-32 bg-wire-surface rounded-wire"></div>
  <div class="h-4 bg-wire-surface rounded w-2/3"></div>
  <div class="h-4 bg-wire-surface rounded w-full"></div>
  <div class="h-8 bg-wire-surface rounded w-24"></div>
</div>
```

### Avatar + Text Skeleton

```html
<div class="animate-pulse flex items-center gap-3">
  <div class="w-10 h-10 bg-wire-surface rounded-full"></div>
  <div class="space-y-2 flex-1">
    <div class="h-4 bg-wire-surface rounded w-1/4"></div>
    <div class="h-3 bg-wire-surface rounded w-1/2"></div>
  </div>
</div>
```

### Table Skeleton

```html
<div class="animate-pulse border border-wire-border rounded-wire overflow-hidden">
  <div class="bg-wire-surface h-12"></div>
  <div class="divide-y divide-wire-border">
    <div class="h-14 bg-wire-bg"></div>
    <div class="h-14 bg-wire-bg"></div>
    <div class="h-14 bg-wire-bg"></div>
  </div>
</div>
```

---

## Empty State

```html
<div class="flex flex-col items-center justify-center py-12 px-4 text-center">
  <div class="w-16 h-16 bg-wire-surface border border-wire-border rounded-full flex items-center justify-center mb-4">
    <svg class="w-8 h-8 text-wire-muted" fill="none" stroke="currentColor" viewBox="0 0 24 24">
      <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M20 13V6a2 2 0 00-2-2H6a2 2 0 00-2 2v7m16 0v5a2 2 0 01-2 2H6a2 2 0 01-2-2v-5m16 0h-2.586a1 1 0 00-.707.293l-2.414 2.414a1 1 0 01-.707.293h-3.172a1 1 0 01-.707-.293l-2.414-2.414A1 1 0 006.586 13H4"/>
    </svg>
  </div>
  <h3 class="text-lg font-medium text-wire-dark mb-2">No items yet</h3>
  <p class="text-wire-muted text-sm mb-4 max-w-sm">Get started by creating your first item. It only takes a few seconds.</p>
  <button class="px-4 py-2 bg-wire-dark text-white rounded-wire hover:bg-wire-text transition-colors">
    Create item
  </button>
</div>
```

---

## Progress Bars

### Simple Progress Bar

```html
<div class="w-full bg-wire-surface rounded-full h-2">
  <div class="bg-wire-dark h-2 rounded-full" style="width: 65%"></div>
</div>
```

### Progress Bar with Label

```html
<div class="space-y-2">
  <div class="flex justify-between text-sm">
    <span class="text-wire-text">Progress</span>
    <span class="text-wire-muted">65%</span>
  </div>
  <div class="w-full bg-wire-surface rounded-full h-2">
    <div class="bg-wire-dark h-2 rounded-full" style="width: 65%"></div>
  </div>
</div>
```

### Steps Progress

```html
<div class="flex items-center gap-2">
  <div class="flex-1 h-1 bg-wire-dark rounded-full"></div>
  <div class="flex-1 h-1 bg-wire-dark rounded-full"></div>
  <div class="flex-1 h-1 bg-wire-surface rounded-full"></div>
  <div class="flex-1 h-1 bg-wire-surface rounded-full"></div>
</div>
```

### Circular Progress (CSS)

```html
<div class="relative w-16 h-16">
  <svg class="w-16 h-16 transform -rotate-90">
    <circle cx="32" cy="32" r="28" stroke-width="4" fill="none" class="stroke-wire-surface"></circle>
    <circle cx="32" cy="32" r="28" stroke-width="4" fill="none" class="stroke-wire-dark" stroke-dasharray="175.9" stroke-dashoffset="44" stroke-linecap="round"></circle>
  </svg>
  <span class="absolute inset-0 flex items-center justify-center text-sm font-medium text-wire-dark">75%</span>
</div>
```

---

## Badges / Tags

### Default Badge

```html
<span class="inline-flex items-center px-2 py-1 text-xs font-medium bg-wire-surface text-wire-text rounded-full">
  Default
</span>
```

### Status Badges

```html
<!-- Active/New -->
<span class="inline-flex items-center px-2 py-1 text-xs font-medium bg-wire-dark text-white rounded-full">
  New
</span>

<!-- Inactive -->
<span class="inline-flex items-center px-2 py-1 text-xs font-medium border border-wire-border text-wire-muted rounded-full">
  Inactive
</span>

<!-- With dot indicator -->
<span class="inline-flex items-center gap-1 px-2 py-1 text-xs font-medium bg-wire-surface text-wire-text rounded-full">
  <span class="w-1.5 h-1.5 bg-wire-dark rounded-full"></span>
  Active
</span>
```

---

## Pagination

```html
<nav class="flex items-center gap-1">
  <button class="px-3 py-2 text-sm text-wire-muted hover:text-wire-text hover:bg-wire-surface rounded-wire transition-colors disabled:opacity-50" disabled>
    <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
      <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 19l-7-7 7-7"/>
    </svg>
  </button>
  <button class="px-3 py-2 text-sm bg-wire-dark text-white rounded-wire">1</button>
  <button class="px-3 py-2 text-sm text-wire-text hover:bg-wire-surface rounded-wire transition-colors">2</button>
  <button class="px-3 py-2 text-sm text-wire-text hover:bg-wire-surface rounded-wire transition-colors">3</button>
  <span class="px-2 text-wire-muted">...</span>
  <button class="px-3 py-2 text-sm text-wire-text hover:bg-wire-surface rounded-wire transition-colors">10</button>
  <button class="px-3 py-2 text-sm text-wire-muted hover:text-wire-text hover:bg-wire-surface rounded-wire transition-colors">
    <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
      <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 5l7 7-7 7"/>
    </svg>
  </button>
</nav>
```

---

## Utility Icons

### Image Icon
```html
<svg class="w-6 h-6" fill="currentColor" viewBox="0 0 24 24">
  <path d="M21 19V5c0-1.1-.9-2-2-2H5c-1.1 0-2 .9-2 2v14c0 1.1.9 2 2 2h14c1.1 0 2-.9 2-2zM8.5 13.5l2.5 3.01L14.5 12l4.5 6H5l3.5-4.5z"/>
</svg>
```

### User Icon
```html
<svg class="w-6 h-6" fill="currentColor" viewBox="0 0 24 24">
  <path d="M12 12c2.21 0 4-1.79 4-4s-1.79-4-4-4-4 1.79-4 4 1.79 4 4 4zm0 2c-2.67 0-8 1.34-8 4v2h16v-2c0-2.66-5.33-4-8-4z"/>
</svg>
```

### Check Icon
```html
<svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24">
  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7"/>
</svg>
```

### Menu Icon (Hamburger)
```html
<svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24">
  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 6h16M4 12h16M4 18h16"/>
</svg>
```

### Close Icon
```html
<svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24">
  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12"/>
</svg>
```

### Arrow Right Icon
```html
<svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24">
  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 5l7 7-7 7"/>
</svg>
```
