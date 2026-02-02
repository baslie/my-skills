# Mobile Components

Mobile-specific patterns with `wire-*` color palette.

---

## Bottom Navigation

```html
<nav class="fixed bottom-0 left-0 right-0 bg-wire-bg border-t border-wire-border z-50 md:hidden">
  <div class="flex justify-around items-center py-2">
    <a href="#" class="flex flex-col items-center gap-1 px-3 py-2 text-wire-dark">
      <svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24">
        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 12l2-2m0 0l7-7 7 7M5 10v10a1 1 0 001 1h3m10-11l2 2m-2-2v10a1 1 0 01-1 1h-3m-6 0a1 1 0 001-1v-4a1 1 0 011-1h2a1 1 0 011 1v4a1 1 0 001 1m-6 0h6"/>
      </svg>
      <span class="text-xs font-medium">Home</span>
    </a>
    <a href="#" class="flex flex-col items-center gap-1 px-3 py-2 text-wire-muted hover:text-wire-text transition-colors">
      <svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24">
        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M21 21l-6-6m2-5a7 7 0 11-14 0 7 7 0 0114 0z"/>
      </svg>
      <span class="text-xs">Search</span>
    </a>
    <a href="#" class="flex flex-col items-center gap-1 px-3 py-2 text-wire-muted hover:text-wire-text transition-colors">
      <svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24">
        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 17h5l-1.405-1.405A2.032 2.032 0 0118 14.158V11a6.002 6.002 0 00-4-5.659V5a2 2 0 10-4 0v.341C7.67 6.165 6 8.388 6 11v3.159c0 .538-.214 1.055-.595 1.436L4 17h5m6 0v1a3 3 0 11-6 0v-1m6 0H9"/>
      </svg>
      <span class="text-xs">Alerts</span>
    </a>
    <a href="#" class="flex flex-col items-center gap-1 px-3 py-2 text-wire-muted hover:text-wire-text transition-colors">
      <svg class="w-6 h-6" fill="currentColor" viewBox="0 0 24 24">
        <path d="M12 12c2.21 0 4-1.79 4-4s-1.79-4-4-4-4 1.79-4 4 1.79 4 4 4zm0 2c-2.67 0-8 1.34-8 4v2h16v-2c0-2.66-5.33-4-8-4z"/>
      </svg>
      <span class="text-xs">Profile</span>
    </a>
  </div>
</nav>
<!-- Add padding to body: pb-16 -->
```

---

## Mobile Card

```html
<!-- Compact mobile card for lists -->
<div class="bg-wire-bg border border-wire-border rounded-wire p-3 flex items-center gap-3">
  <!-- Thumbnail -->
  <div class="w-12 h-12 bg-wire-surface border border-wire-border border-dashed rounded-wire flex-shrink-0 flex items-center justify-center">
    <svg class="w-5 h-5 text-wire-muted" fill="currentColor" viewBox="0 0 24 24">
      <path d="M21 19V5c0-1.1-.9-2-2-2H5c-1.1 0-2 .9-2 2v14c0 1.1.9 2 2 2h14c1.1 0 2-.9 2-2zM8.5 13.5l2.5 3.01L14.5 12l4.5 6H5l3.5-4.5z"/>
    </svg>
  </div>
  <!-- Content -->
  <div class="flex-1 min-w-0">
    <h4 class="text-sm font-medium text-wire-dark truncate">Item title</h4>
    <p class="text-xs text-wire-muted truncate">Short description text</p>
  </div>
  <!-- Action -->
  <button class="p-2 text-wire-muted hover:text-wire-text transition-colors flex-shrink-0">
    <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
      <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 5l7 7-7 7"/>
    </svg>
  </button>
</div>
```

---

## Mobile Card List

```html
<div class="space-y-2 p-4">
  <!-- Mobile card -->
  <div class="bg-wire-bg border border-wire-border rounded-wire p-3 flex items-center gap-3">
    <div class="w-12 h-12 bg-wire-surface border border-wire-border border-dashed rounded-wire flex-shrink-0 flex items-center justify-center">
      <svg class="w-5 h-5 text-wire-muted" fill="currentColor" viewBox="0 0 24 24">
        <path d="M21 19V5c0-1.1-.9-2-2-2H5c-1.1 0-2 .9-2 2v14c0 1.1.9 2 2 2h14c1.1 0 2-.9 2-2zM8.5 13.5l2.5 3.01L14.5 12l4.5 6H5l3.5-4.5z"/>
      </svg>
    </div>
    <div class="flex-1 min-w-0">
      <h4 class="text-sm font-medium text-wire-dark truncate">Item one</h4>
      <p class="text-xs text-wire-muted truncate">Description text</p>
    </div>
    <button class="p-2 text-wire-muted hover:text-wire-text transition-colors flex-shrink-0">
      <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 5l7 7-7 7"/>
      </svg>
    </button>
  </div>

  <!-- Mobile card -->
  <div class="bg-wire-bg border border-wire-border rounded-wire p-3 flex items-center gap-3">
    <div class="w-12 h-12 bg-wire-surface border border-wire-border border-dashed rounded-wire flex-shrink-0 flex items-center justify-center">
      <svg class="w-5 h-5 text-wire-muted" fill="currentColor" viewBox="0 0 24 24">
        <path d="M21 19V5c0-1.1-.9-2-2-2H5c-1.1 0-2 .9-2 2v14c0 1.1.9 2 2 2h14c1.1 0 2-.9 2-2zM8.5 13.5l2.5 3.01L14.5 12l4.5 6H5l3.5-4.5z"/>
      </svg>
    </div>
    <div class="flex-1 min-w-0">
      <h4 class="text-sm font-medium text-wire-dark truncate">Item two</h4>
      <p class="text-xs text-wire-muted truncate">Description text</p>
    </div>
    <button class="p-2 text-wire-muted hover:text-wire-text transition-colors flex-shrink-0">
      <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 5l7 7-7 7"/>
      </svg>
    </button>
  </div>
</div>
```

---

## Mobile Header with Hamburger

See [navigation.md](navigation.md) for the complete Hamburger Menu component with slide-in navigation.

---

## Swipeable Card (Touch-friendly)

```html
<div class="overflow-x-auto pb-4 -mx-4 px-4">
  <div class="flex gap-4" style="width: max-content;">
    <!-- Card 1 -->
    <div class="w-64 flex-shrink-0 bg-wire-surface border border-wire-border rounded-wire p-4 space-y-3">
      <div class="aspect-video bg-wire-bg border border-wire-border border-dashed rounded-wire flex items-center justify-center">
        <svg class="w-8 h-8 text-wire-muted" fill="currentColor" viewBox="0 0 24 24">
          <path d="M21 19V5c0-1.1-.9-2-2-2H5c-1.1 0-2 .9-2 2v14c0 1.1.9 2 2 2h14c1.1 0 2-.9 2-2zM8.5 13.5l2.5 3.01L14.5 12l4.5 6H5l3.5-4.5z"/>
        </svg>
      </div>
      <h4 class="text-sm font-medium text-wire-dark">Card title</h4>
      <p class="text-xs text-wire-muted">Description text</p>
    </div>

    <!-- Card 2 -->
    <div class="w-64 flex-shrink-0 bg-wire-surface border border-wire-border rounded-wire p-4 space-y-3">
      <div class="aspect-video bg-wire-bg border border-wire-border border-dashed rounded-wire flex items-center justify-center">
        <svg class="w-8 h-8 text-wire-muted" fill="currentColor" viewBox="0 0 24 24">
          <path d="M21 19V5c0-1.1-.9-2-2-2H5c-1.1 0-2 .9-2 2v14c0 1.1.9 2 2 2h14c1.1 0 2-.9 2-2zM8.5 13.5l2.5 3.01L14.5 12l4.5 6H5l3.5-4.5z"/>
        </svg>
      </div>
      <h4 class="text-sm font-medium text-wire-dark">Card title</h4>
      <p class="text-xs text-wire-muted">Description text</p>
    </div>

    <!-- Card 3 -->
    <div class="w-64 flex-shrink-0 bg-wire-surface border border-wire-border rounded-wire p-4 space-y-3">
      <div class="aspect-video bg-wire-bg border border-wire-border border-dashed rounded-wire flex items-center justify-center">
        <svg class="w-8 h-8 text-wire-muted" fill="currentColor" viewBox="0 0 24 24">
          <path d="M21 19V5c0-1.1-.9-2-2-2H5c-1.1 0-2 .9-2 2v14c0 1.1.9 2 2 2h14c1.1 0 2-.9 2-2zM8.5 13.5l2.5 3.01L14.5 12l4.5 6H5l3.5-4.5z"/>
        </svg>
      </div>
      <h4 class="text-sm font-medium text-wire-dark">Card title</h4>
      <p class="text-xs text-wire-muted">Description text</p>
    </div>
  </div>
</div>
```
