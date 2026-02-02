#!/usr/bin/env python3
"""
Wireframe Validator
Validates wireframe HTML files against wireframe-builder standards.

Usage:
    python validate-wireframe.py <path-to-wireframe.html>

Checks:
    - Wire palette: Only wire-* colors used
    - Responsive: md: breakpoints present
    - Hover states: hover: classes on interactive elements
    - Semantic HTML: header, main, footer present
    - Section comments: <!-- ===== --> markers
"""

import sys
import re
from pathlib import Path


class WireframeValidator:
    def __init__(self, filepath: str):
        self.filepath = Path(filepath)
        self.content = ""
        self.errors = []
        self.warnings = []
        self.passed = []

    def load(self) -> bool:
        """Load the HTML file."""
        if not self.filepath.exists():
            print(f"Error: File not found: {self.filepath}")
            return False

        if not self.filepath.suffix.lower() == '.html':
            print(f"Error: File must be an HTML file: {self.filepath}")
            return False

        self.content = self.filepath.read_text(encoding='utf-8')
        return True

    def check_wire_palette(self) -> None:
        """Check that only wire-* colors are used."""
        # Common Tailwind color patterns that should NOT be used
        forbidden_colors = [
            r'(?:bg|text|border|ring|from|to|via)-(?:red|orange|amber|yellow|lime|green|emerald|teal|cyan|sky|blue|indigo|violet|purple|fuchsia|pink|rose|slate|gray|zinc|neutral|stone)-\d+',
            r'(?:bg|text|border)-(?:black|white)(?!\s)',  # Allow bg-white if part of template
        ]

        issues = []
        for pattern in forbidden_colors:
            matches = re.findall(pattern, self.content)
            if matches:
                issues.extend(matches[:5])  # Limit to first 5 matches

        # Check for wire-* colors usage
        wire_usage = re.findall(r'wire-(?:bg|surface|border|muted|text|dark)', self.content)

        if issues:
            self.errors.append(f"Non-wire colors found: {', '.join(set(issues))}")
        elif wire_usage:
            self.passed.append("Wire palette: OK (only wire-* colors used)")
        else:
            self.warnings.append("No wire-* colors detected - is this a wireframe?")

    def check_responsive(self) -> None:
        """Check for responsive breakpoints."""
        md_breakpoints = re.findall(r'md:', self.content)
        lg_breakpoints = re.findall(r'lg:', self.content)

        if md_breakpoints or lg_breakpoints:
            self.passed.append(f"Responsive: OK (md: {len(md_breakpoints)}, lg: {len(lg_breakpoints)} breakpoints)")
        else:
            self.warnings.append("No responsive breakpoints (md:, lg:) found")

    def check_hover_states(self) -> None:
        """Check for hover states on interactive elements."""
        # Check for hover: classes
        hover_classes = re.findall(r'hover:[a-z-]+', self.content)

        # Check for buttons and links
        buttons = len(re.findall(r'<button', self.content))
        links = len(re.findall(r'<a\s+href', self.content))

        if hover_classes:
            self.passed.append(f"Hover states: OK ({len(hover_classes)} hover: classes found)")
        elif buttons > 0 or links > 0:
            self.warnings.append(f"No hover: classes found ({buttons} buttons, {links} links detected)")
        else:
            self.passed.append("Hover states: N/A (no interactive elements)")

    def check_semantic_html(self) -> None:
        """Check for semantic HTML elements."""
        semantic_elements = {
            'header': bool(re.search(r'<header[\s>]', self.content)),
            'main': bool(re.search(r'<main[\s>]', self.content)),
            'footer': bool(re.search(r'<footer[\s>]', self.content)),
            'section': bool(re.search(r'<section[\s>]', self.content)),
            'nav': bool(re.search(r'<nav[\s>]', self.content)),
        }

        present = [k for k, v in semantic_elements.items() if v]
        missing = [k for k, v in semantic_elements.items() if not v and k in ['header', 'main', 'footer']]

        if missing:
            self.warnings.append(f"Missing semantic elements: {', '.join(missing)}")
        else:
            self.passed.append(f"Semantic HTML: OK ({', '.join(present)} present)")

    def check_section_comments(self) -> None:
        """Check for section comment markers."""
        comments = re.findall(r'<!--\s*=+\s*\w+', self.content)

        if comments:
            self.passed.append(f"Section comments: OK ({len(comments)} markers found)")
        else:
            self.warnings.append("No section comments found (<!-- ===== SECTION ===== -->)")

    def check_template_structure(self) -> None:
        """Check for proper HTML structure."""
        checks = {
            'DOCTYPE': bool(re.search(r'<!DOCTYPE\s+html>', self.content, re.I)),
            'viewport meta': bool(re.search(r'<meta[^>]*viewport', self.content)),
            'Tailwind CSS': bool(re.search(r'tailwindcss|tailwind\.config', self.content)),
            'wire-* config': bool(re.search(r"wire:\s*\{", self.content)),
        }

        missing = [k for k, v in checks.items() if not v]

        if missing:
            self.warnings.append(f"Template issues: missing {', '.join(missing)}")
        else:
            self.passed.append("Template structure: OK")

    def check_alpine_js(self) -> None:
        """Check Alpine.js usage if interactive components are present."""
        has_alpine = bool(re.search(r'alpinejs|x-data', self.content))
        uses_alpine_directives = bool(re.search(r'x-show|x-on|@click|x-transition', self.content))

        if uses_alpine_directives and not has_alpine:
            self.errors.append("Alpine.js directives used but Alpine not included")
        elif has_alpine:
            self.passed.append("Alpine.js: OK (included)")

    def validate(self) -> bool:
        """Run all validation checks."""
        if not self.load():
            return False

        self.check_wire_palette()
        self.check_responsive()
        self.check_hover_states()
        self.check_semantic_html()
        self.check_section_comments()
        self.check_template_structure()
        self.check_alpine_js()

        return len(self.errors) == 0

    def report(self) -> None:
        """Print validation report."""
        print(f"\nValidating: {self.filepath.name}")
        print("=" * 50)

        for msg in self.passed:
            print(f"[OK] {msg}")

        for msg in self.warnings:
            print(f"[!] Warning: {msg}")

        for msg in self.errors:
            print(f"[X] Error: {msg}")

        print()
        if self.errors:
            print(f"Result: FAILED ({len(self.errors)} errors, {len(self.warnings)} warnings)")
        elif self.warnings:
            print(f"Result: PASSED with warnings ({len(self.warnings)} warnings)")
        else:
            print("Result: PASSED")


def main():
    if len(sys.argv) < 2:
        print("Usage: python validate-wireframe.py <path-to-wireframe.html>")
        print("\nExample:")
        print("  python validate-wireframe.py wireframes/user-profile.html")
        sys.exit(1)

    filepath = sys.argv[1]
    validator = WireframeValidator(filepath)
    success = validator.validate()
    validator.report()

    sys.exit(0 if success else 1)


if __name__ == "__main__":
    main()
