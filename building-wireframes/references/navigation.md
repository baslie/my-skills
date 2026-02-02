# Navigation Components

Ready-to-use navigation components with `wire-*` color palette.

## Contents

- [Header with Logo + Nav + CTA](#header-with-logo--nav--cta)
- [Sidebar Navigation](#sidebar-navigation)
- [Breadcrumbs](#breadcrumbs)
- [Hamburger Menu (Mobile Navigation)](#hamburger-menu-mobile-navigation)
- [Simple Footer](#simple-footer)
- [Multi-column Footer](#multi-column-footer)

---

## Header with Logo + Nav + CTA

```html
<header class="border-b border-wire-border bg-wire-bg sticky top-0 z-50">
  <div class="max-w-6xl mx-auto px-4 py-4 flex items-center justify-between">
    <!-- Logo -->
    <div class="flex items-center gap-2">
      <div class="w-8 h-8 bg-wire-dark rounded-wire"></div>
      <span class="font-semibold text-wire-dark">Brand</span>
    </div>

    <!-- Navigation -->
    <nav class="hidden md:flex items-center gap-6">
      <a href="#" class="text-wire-text hover:text-wire-dark transition-colors">Link</a>
      <a href="#" class="text-wire-text hover:text-wire-dark transition-colors">Link</a>
      <a href="#" class="text-wire-text hover:text-wire-dark transition-colors">Link</a>
    </nav>

    <!-- CTA -->
    <button class="px-4 py-2 bg-wire-dark text-white rounded-wire hover:bg-wire-text transition-colors">
      Action
    </button>
  </div>
</header>
```

---

## Sidebar Navigation

```html
<aside class="w-64 border-r border-wire-border bg-wire-bg min-h-screen p-4">
  <!-- Logo -->
  <div class="flex items-center gap-2 mb-8">
    <div class="w-8 h-8 bg-wire-dark rounded-wire"></div>
    <span class="font-semibold text-wire-dark">Brand</span>
  </div>

  <!-- Nav items -->
  <nav class="space-y-1">
    <a href="#" class="flex items-center gap-3 px-3 py-2 rounded-wire bg-wire-surface text-wire-dark">
      <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 12l2-2m0 0l7-7 7 7M5 10v10a1 1 0 001 1h3m10-11l2 2m-2-2v10a1 1 0 01-1 1h-3m-6 0a1 1 0 001-1v-4a1 1 0 011-1h2a1 1 0 011 1v4a1 1 0 001 1m-6 0h6"/>
      </svg>
      Dashboard
    </a>
    <a href="#" class="flex items-center gap-3 px-3 py-2 rounded-wire text-wire-muted hover:bg-wire-surface hover:text-wire-text transition-colors">
      <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 4.354a4 4 0 110 5.292M15 21H3v-1a6 6 0 0112 0v1zm0 0h6v-1a6 6 0 00-9-5.197M13 7a4 4 0 11-8 0 4 4 0 018 0z"/>
      </svg>
      Users
    </a>
    <a href="#" class="flex items-center gap-3 px-3 py-2 rounded-wire text-wire-muted hover:bg-wire-surface hover:text-wire-text transition-colors">
      <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M10.325 4.317c.426-1.756 2.924-1.756 3.35 0a1.724 1.724 0 002.573 1.066c1.543-.94 3.31.826 2.37 2.37a1.724 1.724 0 001.065 2.572c1.756.426 1.756 2.924 0 3.35a1.724 1.724 0 00-1.066 2.573c.94 1.543-.826 3.31-2.37 2.37a1.724 1.724 0 00-2.572 1.065c-.426 1.756-2.924 1.756-3.35 0a1.724 1.724 0 00-2.573-1.066c-1.543.94-3.31-.826-2.37-2.37a1.724 1.724 0 00-1.065-2.572c-1.756-.426-1.756-2.924 0-3.35a1.724 1.724 0 001.066-2.573c-.94-1.543.826-3.31 2.37-2.37.996.608 2.296.07 2.572-1.065z"/>
        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 12a3 3 0 11-6 0 3 3 0 016 0z"/>
      </svg>
      Settings
    </a>
  </nav>
</aside>
```

---

## Breadcrumbs

```html
<nav class="flex items-center gap-2 text-sm text-wire-muted">
  <a href="#" class="hover:text-wire-text transition-colors">Home</a>
  <span>/</span>
  <a href="#" class="hover:text-wire-text transition-colors">Products</a>
  <span>/</span>
  <span class="text-wire-text">Current page</span>
</nav>
```

---

## Hamburger Menu (Mobile Navigation)

```html
<div x-data="{ open: false }">
  <!-- Header with hamburger -->
  <header class="border-b border-wire-border bg-wire-bg sticky top-0 z-50">
    <div class="max-w-6xl mx-auto px-4 py-4 flex items-center justify-between">
      <!-- Logo -->
      <div class="flex items-center gap-2">
        <div class="w-8 h-8 bg-wire-dark rounded-wire"></div>
        <span class="font-semibold text-wire-dark">Brand</span>
      </div>

      <!-- Desktop nav -->
      <nav class="hidden md:flex items-center gap-6">
        <a href="#" class="text-wire-text hover:text-wire-dark transition-colors">Link</a>
        <a href="#" class="text-wire-text hover:text-wire-dark transition-colors">Link</a>
        <a href="#" class="text-wire-text hover:text-wire-dark transition-colors">Link</a>
      </nav>

      <!-- Hamburger button (mobile) -->
      <button @click="open = !open" class="md:hidden p-2 text-wire-text hover:text-wire-dark transition-colors">
        <svg x-show="!open" class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24">
          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 6h16M4 12h16M4 18h16"/>
        </svg>
        <svg x-show="open" class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24">
          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12"/>
        </svg>
      </button>
    </div>
  </header>

  <!-- Mobile menu overlay -->
  <div x-show="open" x-transition:enter="transition ease-out duration-200" x-transition:enter-start="opacity-0" x-transition:enter-end="opacity-100" x-transition:leave="transition ease-in duration-150" x-transition:leave-start="opacity-100" x-transition:leave-end="opacity-0" class="fixed inset-0 bg-wire-dark/50 z-40 md:hidden" @click="open = false">
  </div>

  <!-- Mobile menu slide-in -->
  <div x-show="open" x-transition:enter="transition ease-out duration-200" x-transition:enter-start="-translate-x-full" x-transition:enter-end="translate-x-0" x-transition:leave="transition ease-in duration-150" x-transition:leave-start="translate-x-0" x-transition:leave-end="-translate-x-full" class="fixed top-0 left-0 bottom-0 w-64 bg-wire-bg border-r border-wire-border z-50 md:hidden">
    <div class="p-4">
      <div class="flex items-center justify-between mb-8">
        <div class="flex items-center gap-2">
          <div class="w-8 h-8 bg-wire-dark rounded-wire"></div>
          <span class="font-semibold text-wire-dark">Brand</span>
        </div>
        <button @click="open = false" class="p-2 text-wire-muted hover:text-wire-text transition-colors">
          <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12"/>
          </svg>
        </button>
      </div>
      <nav class="space-y-2">
        <a href="#" class="block px-3 py-2 text-wire-text hover:bg-wire-surface rounded-wire transition-colors">Link 1</a>
        <a href="#" class="block px-3 py-2 text-wire-text hover:bg-wire-surface rounded-wire transition-colors">Link 2</a>
        <a href="#" class="block px-3 py-2 text-wire-text hover:bg-wire-surface rounded-wire transition-colors">Link 3</a>
      </nav>
    </div>
  </div>
</div>
```

---

## Simple Footer

```html
<footer class="border-t border-wire-border py-8">
  <div class="max-w-6xl mx-auto px-4 flex flex-col md:flex-row justify-between items-center gap-4">
    <div class="flex items-center gap-2">
      <div class="w-6 h-6 bg-wire-dark rounded"></div>
      <span class="font-semibold text-wire-dark">Brand</span>
    </div>
    <p class="text-sm text-wire-muted">&copy; <span x-data x-text="new Date().getFullYear()"></span> Brand. All rights reserved.</p>
  </div>
</footer>
```

---

## Multi-column Footer

```html
<footer class="border-t border-wire-border py-12">
  <div class="max-w-6xl mx-auto px-4">
    <div class="grid md:grid-cols-4 gap-8 mb-8">
      <div class="space-y-4">
        <div class="flex items-center gap-2">
          <div class="w-8 h-8 bg-wire-dark rounded-wire"></div>
          <span class="font-semibold text-wire-dark">Brand</span>
        </div>
        <p class="text-sm text-wire-muted">Brief description.</p>
      </div>
      <div>
        <h4 class="font-semibold text-wire-dark mb-4">Column 1</h4>
        <ul class="space-y-2 text-sm text-wire-muted">
          <li><a href="#" class="hover:text-wire-text">Link</a></li>
          <li><a href="#" class="hover:text-wire-text">Link</a></li>
        </ul>
      </div>
      <div>
        <h4 class="font-semibold text-wire-dark mb-4">Column 2</h4>
        <ul class="space-y-2 text-sm text-wire-muted">
          <li><a href="#" class="hover:text-wire-text">Link</a></li>
          <li><a href="#" class="hover:text-wire-text">Link</a></li>
        </ul>
      </div>
      <div>
        <h4 class="font-semibold text-wire-dark mb-4">Column 3</h4>
        <ul class="space-y-2 text-sm text-wire-muted">
          <li><a href="#" class="hover:text-wire-text">Link</a></li>
          <li><a href="#" class="hover:text-wire-text">Link</a></li>
        </ul>
      </div>
    </div>
    <div class="pt-8 border-t border-wire-border text-center text-sm text-wire-muted">
      &copy; <span x-data x-text="new Date().getFullYear()"></span> Brand. All rights reserved.
    </div>
  </div>
</footer>
```
