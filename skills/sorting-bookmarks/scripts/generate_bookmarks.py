"""
Generate a sorted HTML bookmarks file from analysis data and category mapping.
Reads bookmarks_analysis.json and categories_mapping.json,
creates a NETSCAPE-Bookmark-file-1 HTML with the new category structure.
"""

import argparse
import json
import sys
import os
from html import escape
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8", errors="replace")
sys.stderr.reconfigure(encoding="utf-8", errors="replace")
os.environ["PYTHONIOENCODING"] = "utf-8"


def load_json(filepath: str) -> dict:
    """Load a JSON file."""
    return json.loads(Path(filepath).read_text(encoding="utf-8"))


def sort_key(text: str) -> str:
    """Sort key: strip leading special chars, lowercase."""
    clean = text.lstrip("[]()")
    return clean.lower()


def build_url_index(analysis: dict) -> dict[str, dict]:
    """Build URL -> bookmark data index from analysis."""
    index = {}
    for bm in analysis["bookmarks"]:
        url = bm["url"]
        title = bm.get("original_title", "") or bm.get("crawled_title", "") or url
        index[url] = {"url": url, "title": title}
    return index


def generate_html(categories: dict, url_index: dict, root_folder: str) -> str:
    """Generate NETSCAPE-Bookmark-file-1 HTML."""
    lines = []
    lines.append("<!DOCTYPE NETSCAPE-Bookmark-file-1>")
    lines.append("<!-- This is an automatically generated file.")
    lines.append("     It will be read and overwritten.")
    lines.append("     DO NOT EDIT! -->")
    lines.append(
        '<META HTTP-EQUIV="Content-Type" CONTENT="text/html; charset=UTF-8">'
    )
    lines.append("<TITLE>Bookmarks</TITLE>")
    lines.append("<H1>Bookmarks</H1>")
    lines.append("<DL><p>")

    # Root folder
    lines.append(f"    <DT><H3>{escape(root_folder)}</H3>")
    lines.append("    <DL><p>")

    # Sort categories alphabetically
    sorted_categories = sorted(categories.keys(), key=sort_key)

    for cat_name in sorted_categories:
        urls = categories[cat_name]
        bookmarks = []
        for url in urls:
            if url in url_index:
                bookmarks.append(url_index[url])
            else:
                bookmarks.append({"url": url, "title": url})

        # Sort bookmarks within category by title
        bookmarks.sort(key=lambda b: sort_key(b["title"]))

        lines.append(f"        <DT><H3>{escape(cat_name)}</H3>")
        lines.append("        <DL><p>")

        for bm in bookmarks:
            escaped_url = escape(bm["url"], quote=True)
            escaped_title = escape(bm["title"])
            lines.append(
                f'            <DT><A HREF="{escaped_url}">{escaped_title}</A>'
            )

        lines.append("        </DL><p>")

    lines.append("    </DL><p>")
    lines.append("</DL><p>")

    return "\n".join(lines)


def main():
    parser = argparse.ArgumentParser(
        description="Generate sorted HTML bookmarks from analysis and category mapping."
    )
    parser.add_argument(
        "--analysis",
        required=True,
        help="Path to bookmarks_analysis.json",
    )
    parser.add_argument(
        "--mapping",
        required=True,
        help="Path to categories_mapping.json",
    )
    parser.add_argument(
        "--output",
        default="bookmarks_sorted.html",
        help="Output HTML file (default: bookmarks_sorted.html)",
    )
    parser.add_argument(
        "--root-folder",
        default=None,
        help="Root folder name in output HTML (default: taken from analysis target_folder)",
    )
    args = parser.parse_args()

    print(f"Loading {args.analysis}...")
    analysis = load_json(args.analysis)

    print(f"Loading {args.mapping}...")
    mapping = load_json(args.mapping)

    categories = mapping["categories"]

    # Determine root folder name
    root_folder = args.root_folder
    if not root_folder:
        root_folder = analysis.get("target_folder", "Bookmarks")
    print(f"Root folder: {root_folder}")

    # Build URL index
    url_index = build_url_index(analysis)

    # Validate mapping completeness
    mapped_urls = set()
    for urls in categories.values():
        mapped_urls.update(urls)

    analysis_urls = {bm["url"] for bm in analysis["bookmarks"]}
    missing = analysis_urls - mapped_urls
    extra = mapped_urls - analysis_urls

    if missing:
        print(
            f"\nWARNING: {len(missing)} URLs from analysis are not in any category:"
        )
        for url in sorted(missing):
            title = url_index.get(url, {}).get("title", "?")
            print(f"  - {title[:80]}")

    if extra:
        print(f"\nWARNING: {len(extra)} URLs in mapping are not in analysis:")
        for url in sorted(extra):
            print(f"  - {url[:80]}")

    # Stats
    total_bookmarks = sum(len(urls) for urls in categories.values())
    print(f"\nCategories: {len(categories)}")
    print(f"Total bookmarks in mapping: {total_bookmarks}")
    print(f"Bookmarks in analysis: {len(analysis['bookmarks'])}")

    # Generate HTML
    html = generate_html(categories, url_index, root_folder)

    Path(args.output).write_text(html, encoding="utf-8")
    print(f"\nFile saved: {args.output}")

    # Print structure
    print(f"\nStructure of '{root_folder}':")
    sorted_cats = sorted(categories.keys(), key=sort_key)
    for cat in sorted_cats:
        count = len(categories[cat])
        print(f"  {cat} ({count})")


if __name__ == "__main__":
    main()
