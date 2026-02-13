# Interactive Components

Alpine.js-powered interactive components with `wire-*` color palette.

---

## Modal / Dialog

```html
<div x-data="{ open: false }">
  <!-- Trigger button -->
  <button @click="open = true" class="px-4 py-2 bg-wire-dark text-white rounded-wire hover:bg-wire-text transition-colors">
    Open Modal
  </button>

  <!-- Modal overlay -->
  <div x-show="open" x-transition:enter="transition ease-out duration-200" x-transition:enter-start="opacity-0" x-transition:enter-end="opacity-100" x-transition:leave="transition ease-in duration-150" x-transition:leave-start="opacity-100" x-transition:leave-end="opacity-0" class="fixed inset-0 bg-wire-dark/50 z-50 flex items-center justify-center p-4" @click.self="open = false">
    <!-- Modal content -->
    <div x-show="open" x-transition:enter="transition ease-out duration-200" x-transition:enter-start="opacity-0 scale-95" x-transition:enter-end="opacity-100 scale-100" x-transition:leave="transition ease-in duration-150" x-transition:leave-start="opacity-100 scale-100" x-transition:leave-end="opacity-0 scale-95" class="bg-wire-bg border border-wire-border rounded-wire p-6 w-full max-w-md shadow-lg">
      <div class="flex items-center justify-between mb-4">
        <h3 class="text-lg font-semibold text-wire-dark">Modal Title</h3>
        <button @click="open = false" class="text-wire-muted hover:text-wire-text transition-colors">
          <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12"/>
          </svg>
        </button>
      </div>
      <p class="text-wire-muted mb-6">Modal content goes here. This is a simple dialog box.</p>
      <div class="flex justify-end gap-2">
        <button @click="open = false" class="px-4 py-2 border border-wire-border text-wire-text rounded-wire hover:bg-wire-surface transition-colors">
          Cancel
        </button>
        <button @click="open = false" class="px-4 py-2 bg-wire-dark text-white rounded-wire hover:bg-wire-text transition-colors">
          Confirm
        </button>
      </div>
    </div>
  </div>
</div>
```

---

## Dropdown Menu

```html
<div x-data="{ open: false }" class="relative">
  <button @click="open = !open" class="px-4 py-2 border border-wire-border text-wire-text rounded-wire hover:bg-wire-surface transition-colors flex items-center gap-2">
    Options
    <svg class="w-4 h-4" :class="{ 'rotate-180': open }" fill="none" stroke="currentColor" viewBox="0 0 24 24">
      <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 9l-7 7-7-7"/>
    </svg>
  </button>

  <div x-show="open" x-transition @click.outside="open = false" class="absolute top-full left-0 mt-1 w-48 bg-wire-bg border border-wire-border rounded-wire shadow-lg z-10">
    <a href="#" class="block px-4 py-2 text-sm text-wire-text hover:bg-wire-surface transition-colors">Option 1</a>
    <a href="#" class="block px-4 py-2 text-sm text-wire-text hover:bg-wire-surface transition-colors">Option 2</a>
    <a href="#" class="block px-4 py-2 text-sm text-wire-text hover:bg-wire-surface transition-colors">Option 3</a>
    <div class="border-t border-wire-border"></div>
    <a href="#" class="block px-4 py-2 text-sm text-wire-muted hover:bg-wire-surface transition-colors">Logout</a>
  </div>
</div>
```

---

## Tabs

```html
<div x-data="{ tab: 'tab1' }">
  <!-- Tab buttons -->
  <div class="flex border-b border-wire-border">
    <button @click="tab = 'tab1'" :class="tab === 'tab1' ? 'border-wire-dark text-wire-dark' : 'border-transparent text-wire-muted hover:text-wire-text'" class="px-4 py-2 border-b-2 font-medium transition-colors">
      Tab 1
    </button>
    <button @click="tab = 'tab2'" :class="tab === 'tab2' ? 'border-wire-dark text-wire-dark' : 'border-transparent text-wire-muted hover:text-wire-text'" class="px-4 py-2 border-b-2 font-medium transition-colors">
      Tab 2
    </button>
    <button @click="tab = 'tab3'" :class="tab === 'tab3' ? 'border-wire-dark text-wire-dark' : 'border-transparent text-wire-muted hover:text-wire-text'" class="px-4 py-2 border-b-2 font-medium transition-colors">
      Tab 3
    </button>
  </div>

  <!-- Tab content -->
  <div class="p-4">
    <div x-show="tab === 'tab1'" x-transition>
      <p class="text-wire-text">Content for Tab 1</p>
    </div>
    <div x-show="tab === 'tab2'" x-transition>
      <p class="text-wire-text">Content for Tab 2</p>
    </div>
    <div x-show="tab === 'tab3'" x-transition>
      <p class="text-wire-text">Content for Tab 3</p>
    </div>
  </div>
</div>
```

---

## Toast / Notification

```html
<div x-data="{ show: false, message: '' }"
     @show-toast.window="show = true; message = $event.detail.message; setTimeout(() => show = false, 3000)">

  <!-- Toast container -->
  <div x-show="show" x-transition:enter="transition ease-out duration-300" x-transition:enter-start="opacity-0 translate-y-2" x-transition:enter-end="opacity-100 translate-y-0" x-transition:leave="transition ease-in duration-200" x-transition:leave-start="opacity-100 translate-y-0" x-transition:leave-end="opacity-0 translate-y-2" class="fixed bottom-4 right-4 z-50">
    <div class="bg-wire-dark text-white px-4 py-3 rounded-wire shadow-lg flex items-center gap-3">
      <svg class="w-5 h-5 text-wire-surface" fill="none" stroke="currentColor" viewBox="0 0 24 24">
        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13 16h-1v-4h-1m1-4h.01M21 12a9 9 0 11-18 0 9 9 0 0118 0z"/>
      </svg>
      <span x-text="message">Notification message</span>
      <button @click="show = false" class="ml-2 text-wire-border hover:text-white transition-colors">
        <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12"/>
        </svg>
      </button>
    </div>
  </div>
</div>

<!-- Trigger example (place anywhere) -->
<button @click="$dispatch('show-toast', { message: 'Action completed!' })" class="px-4 py-2 bg-wire-dark text-white rounded-wire">
  Show Toast
</button>
```

---

## Accordion (Alpine.js version)

```html
<div x-data="{ openItem: null }" class="space-y-2">
  <div class="border border-wire-border rounded-wire">
    <button @click="openItem = openItem === 1 ? null : 1" class="w-full px-4 py-3 flex items-center justify-between text-left text-wire-dark font-medium hover:bg-wire-surface transition-colors">
      <span>Question one?</span>
      <svg class="w-4 h-4 transition-transform" :class="{ 'rotate-180': openItem === 1 }" fill="none" stroke="currentColor" viewBox="0 0 24 24">
        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 9l-7 7-7-7"/>
      </svg>
    </button>
    <div x-show="openItem === 1" x-collapse>
      <div class="px-4 pb-4 text-wire-muted text-sm">
        Answer text goes here.
      </div>
    </div>
  </div>

  <div class="border border-wire-border rounded-wire">
    <button @click="openItem = openItem === 2 ? null : 2" class="w-full px-4 py-3 flex items-center justify-between text-left text-wire-dark font-medium hover:bg-wire-surface transition-colors">
      <span>Question two?</span>
      <svg class="w-4 h-4 transition-transform" :class="{ 'rotate-180': openItem === 2 }" fill="none" stroke="currentColor" viewBox="0 0 24 24">
        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 9l-7 7-7-7"/>
      </svg>
    </button>
    <div x-show="openItem === 2" x-collapse>
      <div class="px-4 pb-4 text-wire-muted text-sm">
        Answer text goes here.
      </div>
    </div>
  </div>
</div>
```
