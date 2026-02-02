# Form Components

Ready-to-use form elements with `wire-*` color palette.

---

## Input Fields

### Basic Input

```html
<input type="text" placeholder="Placeholder..."
  class="w-full px-4 py-2 border border-wire-border rounded-wire bg-wire-bg text-wire-text placeholder:text-wire-muted focus:outline-none focus:border-wire-muted">
```

### Input with Label

```html
<div class="space-y-2">
  <label class="text-sm font-medium text-wire-dark">Label</label>
  <input type="text" placeholder="Placeholder..."
    class="w-full px-4 py-2 border border-wire-border rounded-wire bg-wire-bg text-wire-text placeholder:text-wire-muted focus:outline-none focus:border-wire-muted">
</div>
```

### Textarea

```html
<textarea rows="4" placeholder="Message..."
  class="w-full px-4 py-2 border border-wire-border rounded-wire bg-wire-bg text-wire-text placeholder:text-wire-muted focus:outline-none focus:border-wire-muted resize-none"></textarea>
```

### Select

```html
<select class="w-full px-4 py-2 border border-wire-border rounded-wire bg-wire-bg text-wire-text focus:outline-none focus:border-wire-muted">
  <option value="">Select option...</option>
  <option value="1">Option 1</option>
  <option value="2">Option 2</option>
</select>
```

### Checkbox

```html
<label class="flex items-center gap-2 cursor-pointer">
  <input type="checkbox" class="w-4 h-4 border border-wire-border rounded accent-wire-dark">
  <span class="text-sm text-wire-text">Checkbox label</span>
</label>
```

---

## Buttons

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

### Ghost Button

```html
<button class="px-4 py-2 text-wire-text hover:text-wire-dark hover:bg-wire-surface rounded-wire transition-colors">
  Ghost
</button>
```

### Button Group

```html
<div class="flex gap-2">
  <button class="px-4 py-2 bg-wire-dark text-white rounded-wire hover:bg-wire-text transition-colors">Primary</button>
  <button class="px-4 py-2 border border-wire-border text-wire-text rounded-wire hover:bg-wire-surface transition-colors">Secondary</button>
</div>
```

---

## Complete Forms

### Login Form

```html
<div class="max-w-sm mx-auto bg-wire-surface border border-wire-border rounded-wire p-6 space-y-4">
  <h2 class="text-xl font-semibold text-wire-dark text-center">Log in</h2>
  <div class="space-y-2">
    <label class="text-sm font-medium text-wire-dark">Email</label>
    <input type="email" placeholder="you@example.com"
      class="w-full px-4 py-2 border border-wire-border rounded-wire bg-wire-bg text-wire-text placeholder:text-wire-muted focus:outline-none focus:border-wire-muted">
  </div>
  <div class="space-y-2">
    <label class="text-sm font-medium text-wire-dark">Password</label>
    <input type="password" placeholder="********"
      class="w-full px-4 py-2 border border-wire-border rounded-wire bg-wire-bg text-wire-text placeholder:text-wire-muted focus:outline-none focus:border-wire-muted">
  </div>
  <button class="w-full px-4 py-2 bg-wire-dark text-white rounded-wire hover:bg-wire-text transition-colors">
    Log in
  </button>
  <p class="text-sm text-wire-muted text-center">
    Don't have an account? <a href="#" class="text-wire-text hover:underline">Sign up</a>
  </p>
</div>
```

### Search Bar

```html
<div class="flex gap-2">
  <input type="search" placeholder="Search..."
    class="flex-1 px-4 py-2 border border-wire-border rounded-wire bg-wire-bg text-wire-text placeholder:text-wire-muted focus:outline-none focus:border-wire-muted">
  <button class="px-4 py-2 bg-wire-dark text-white rounded-wire hover:bg-wire-text transition-colors">
    Search
  </button>
</div>
```

### Contact Form

```html
<div class="max-w-md mx-auto bg-wire-surface border border-wire-border rounded-wire p-6 space-y-4">
  <h2 class="text-xl font-semibold text-wire-dark">Contact us</h2>
  <div class="space-y-2">
    <label class="text-sm font-medium text-wire-dark">Name</label>
    <input type="text" placeholder="Your name"
      class="w-full px-4 py-2 border border-wire-border rounded-wire bg-wire-bg text-wire-text placeholder:text-wire-muted focus:outline-none focus:border-wire-muted">
  </div>
  <div class="space-y-2">
    <label class="text-sm font-medium text-wire-dark">Email</label>
    <input type="email" placeholder="you@example.com"
      class="w-full px-4 py-2 border border-wire-border rounded-wire bg-wire-bg text-wire-text placeholder:text-wire-muted focus:outline-none focus:border-wire-muted">
  </div>
  <div class="space-y-2">
    <label class="text-sm font-medium text-wire-dark">Message</label>
    <textarea rows="4" placeholder="How can we help?"
      class="w-full px-4 py-2 border border-wire-border rounded-wire bg-wire-bg text-wire-text placeholder:text-wire-muted focus:outline-none focus:border-wire-muted resize-none"></textarea>
  </div>
  <button class="w-full px-4 py-2 bg-wire-dark text-white rounded-wire hover:bg-wire-text transition-colors">
    Send message
  </button>
</div>
```
