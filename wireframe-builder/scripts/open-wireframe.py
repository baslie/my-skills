#!/usr/bin/env python3
"""
Open wireframe HTML file in the default browser.

Usage:
    python scripts/open-wireframe.py wireframes/page.html
    python scripts/open-wireframe.py  # Opens the most recent wireframe
"""

import os
import sys
import webbrowser
from pathlib import Path


def find_wireframes_dir() -> Path:
    """Find the wireframes directory relative to the script or current working directory."""
    # Try current working directory first
    cwd = Path.cwd()
    if (cwd / "wireframes").is_dir():
        return cwd / "wireframes"

    # Try relative to script location
    script_dir = Path(__file__).parent.parent
    if (script_dir / "wireframes").is_dir():
        return script_dir / "wireframes"

    return cwd / "wireframes"


def get_latest_wireframe(wireframes_dir: Path) -> Path | None:
    """Get the most recently modified HTML file in the wireframes directory."""
    if not wireframes_dir.is_dir():
        return None

    html_files = list(wireframes_dir.glob("*.html"))
    if not html_files:
        return None

    return max(html_files, key=lambda f: f.stat().st_mtime)


def open_in_browser(file_path: Path) -> None:
    """Open the file in the default browser."""
    url = file_path.as_uri()
    print(f"Opening: {file_path}")
    webbrowser.open(url)


def main() -> int:
    if len(sys.argv) > 1:
        # File path provided as argument
        file_path = Path(sys.argv[1])

        if not file_path.is_absolute():
            file_path = Path.cwd() / file_path

        if not file_path.exists():
            print(f"Error: File not found: {file_path}", file=sys.stderr)
            return 1

        if not file_path.suffix == ".html":
            print(f"Warning: File is not an HTML file: {file_path}", file=sys.stderr)
    else:
        # No argument - find the most recent wireframe
        wireframes_dir = find_wireframes_dir()
        file_path = get_latest_wireframe(wireframes_dir)

        if file_path is None:
            print(f"Error: No wireframes found in {wireframes_dir}", file=sys.stderr)
            print("Usage: python scripts/open-wireframe.py [path/to/wireframe.html]", file=sys.stderr)
            return 1

        print(f"Found latest wireframe: {file_path.name}")

    open_in_browser(file_path)
    return 0


if __name__ == "__main__":
    sys.exit(main())
