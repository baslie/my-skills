# Table Components

Ready-to-use table components with `wire-*` color palette.

## Contents

- [Simple Table](#simple-table)
- [Data Table with Actions](#data-table-with-actions)
- [Table with Pagination](#table-with-pagination)

---

## Simple Table

```html
<div class="border border-wire-border rounded-wire overflow-hidden">
  <table class="w-full">
    <thead class="bg-wire-surface">
      <tr>
        <th class="px-4 py-3 text-left text-sm font-medium text-wire-dark">Column</th>
        <th class="px-4 py-3 text-left text-sm font-medium text-wire-dark">Column</th>
        <th class="px-4 py-3 text-left text-sm font-medium text-wire-dark">Column</th>
      </tr>
    </thead>
    <tbody class="divide-y divide-wire-border">
      <tr class="hover:bg-wire-surface transition-colors">
        <td class="px-4 py-3 text-sm text-wire-text">Data</td>
        <td class="px-4 py-3 text-sm text-wire-text">Data</td>
        <td class="px-4 py-3 text-sm text-wire-text">Data</td>
      </tr>
      <tr class="hover:bg-wire-surface transition-colors">
        <td class="px-4 py-3 text-sm text-wire-text">Data</td>
        <td class="px-4 py-3 text-sm text-wire-text">Data</td>
        <td class="px-4 py-3 text-sm text-wire-text">Data</td>
      </tr>
    </tbody>
  </table>
</div>
```

---

## Data Table with Actions

```html
<div class="border border-wire-border rounded-wire overflow-hidden">
  <table class="w-full">
    <thead class="bg-wire-surface">
      <tr>
        <th class="px-4 py-3 text-left text-sm font-medium text-wire-dark">
          <label class="flex items-center">
            <input type="checkbox" class="w-4 h-4 border border-wire-border rounded accent-wire-dark">
          </label>
        </th>
        <th class="px-4 py-3 text-left text-sm font-medium text-wire-dark">Name</th>
        <th class="px-4 py-3 text-left text-sm font-medium text-wire-dark">Email</th>
        <th class="px-4 py-3 text-left text-sm font-medium text-wire-dark">Status</th>
        <th class="px-4 py-3 text-left text-sm font-medium text-wire-dark">Actions</th>
      </tr>
    </thead>
    <tbody class="divide-y divide-wire-border">
      <tr class="hover:bg-wire-surface transition-colors">
        <td class="px-4 py-3">
          <label class="flex items-center">
            <input type="checkbox" class="w-4 h-4 border border-wire-border rounded accent-wire-dark">
          </label>
        </td>
        <td class="px-4 py-3">
          <div class="flex items-center gap-3">
            <div class="w-8 h-8 bg-wire-surface border border-wire-border rounded-full flex items-center justify-center">
              <svg class="w-4 h-4 text-wire-muted" fill="currentColor" viewBox="0 0 24 24">
                <path d="M12 12c2.21 0 4-1.79 4-4s-1.79-4-4-4-4 1.79-4 4 1.79 4 4 4zm0 2c-2.67 0-8 1.34-8 4v2h16v-2c0-2.66-5.33-4-8-4z"/>
              </svg>
            </div>
            <span class="text-sm text-wire-text">John Doe</span>
          </div>
        </td>
        <td class="px-4 py-3 text-sm text-wire-muted">john@example.com</td>
        <td class="px-4 py-3">
          <span class="inline-flex items-center gap-1 px-2 py-1 text-xs font-medium bg-wire-surface text-wire-text rounded-full">
            <span class="w-1.5 h-1.5 bg-wire-dark rounded-full"></span>
            Active
          </span>
        </td>
        <td class="px-4 py-3">
          <div class="flex items-center gap-2">
            <button class="p-1 text-wire-muted hover:text-wire-text transition-colors">
              <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15.232 5.232l3.536 3.536m-2.036-5.036a2.5 2.5 0 113.536 3.536L6.5 21.036H3v-3.572L16.732 3.732z"/>
              </svg>
            </button>
            <button class="p-1 text-wire-muted hover:text-wire-text transition-colors">
              <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 7l-.867 12.142A2 2 0 0116.138 21H7.862a2 2 0 01-1.995-1.858L5 7m5 4v6m4-6v6m1-10V4a1 1 0 00-1-1h-4a1 1 0 00-1 1v3M4 7h16"/>
              </svg>
            </button>
          </div>
        </td>
      </tr>
      <tr class="hover:bg-wire-surface transition-colors">
        <td class="px-4 py-3">
          <label class="flex items-center">
            <input type="checkbox" class="w-4 h-4 border border-wire-border rounded accent-wire-dark">
          </label>
        </td>
        <td class="px-4 py-3">
          <div class="flex items-center gap-3">
            <div class="w-8 h-8 bg-wire-surface border border-wire-border rounded-full flex items-center justify-center">
              <svg class="w-4 h-4 text-wire-muted" fill="currentColor" viewBox="0 0 24 24">
                <path d="M12 12c2.21 0 4-1.79 4-4s-1.79-4-4-4-4 1.79-4 4 1.79 4 4 4zm0 2c-2.67 0-8 1.34-8 4v2h16v-2c0-2.66-5.33-4-8-4z"/>
              </svg>
            </div>
            <span class="text-sm text-wire-text">Jane Smith</span>
          </div>
        </td>
        <td class="px-4 py-3 text-sm text-wire-muted">jane@example.com</td>
        <td class="px-4 py-3">
          <span class="inline-flex items-center px-2 py-1 text-xs font-medium border border-wire-border text-wire-muted rounded-full">
            Inactive
          </span>
        </td>
        <td class="px-4 py-3">
          <div class="flex items-center gap-2">
            <button class="p-1 text-wire-muted hover:text-wire-text transition-colors">
              <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15.232 5.232l3.536 3.536m-2.036-5.036a2.5 2.5 0 113.536 3.536L6.5 21.036H3v-3.572L16.732 3.732z"/>
              </svg>
            </button>
            <button class="p-1 text-wire-muted hover:text-wire-text transition-colors">
              <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 7l-.867 12.142A2 2 0 0116.138 21H7.862a2 2 0 01-1.995-1.858L5 7m5 4v6m4-6v6m1-10V4a1 1 0 00-1-1h-4a1 1 0 00-1 1v3M4 7h16"/>
              </svg>
            </button>
          </div>
        </td>
      </tr>
    </tbody>
  </table>
</div>
```

---

## Table with Pagination

```html
<div class="space-y-4">
  <!-- Table -->
  <div class="border border-wire-border rounded-wire overflow-hidden">
    <table class="w-full">
      <thead class="bg-wire-surface">
        <tr>
          <th class="px-4 py-3 text-left text-sm font-medium text-wire-dark">Column</th>
          <th class="px-4 py-3 text-left text-sm font-medium text-wire-dark">Column</th>
          <th class="px-4 py-3 text-left text-sm font-medium text-wire-dark">Column</th>
        </tr>
      </thead>
      <tbody class="divide-y divide-wire-border">
        <tr class="hover:bg-wire-surface transition-colors">
          <td class="px-4 py-3 text-sm text-wire-text">Data</td>
          <td class="px-4 py-3 text-sm text-wire-text">Data</td>
          <td class="px-4 py-3 text-sm text-wire-text">Data</td>
        </tr>
      </tbody>
    </table>
  </div>

  <!-- Pagination -->
  <div class="flex items-center justify-between">
    <p class="text-sm text-wire-muted">Showing 1-10 of 100 results</p>
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
  </div>
</div>
```
