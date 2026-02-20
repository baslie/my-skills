"""
Parse bookmarks from an HTML bookmarks file (specific folder)
and crawl each URL via crawl4ai to get titles and descriptions.
Results are saved to a JSON file.
"""

import argparse
import asyncio
import json
import os
import sys
from html.parser import HTMLParser
from pathlib import Path

# Fix Windows encoding
sys.stdout.reconfigure(encoding="utf-8", errors="replace")
sys.stderr.reconfigure(encoding="utf-8", errors="replace")
os.environ["PYTHONIOENCODING"] = "utf-8"

from crawl4ai import AsyncWebCrawler, BrowserConfig, CrawlerRunConfig, CacheMode


class BookmarkParser(HTMLParser):
    """Extracts all links from a specified folder in a bookmarks file."""

    def __init__(self, target_folder: str):
        super().__init__()
        self.target_folder = target_folder
        self.bookmarks: list[dict] = []
        self.depth = 0
        self.in_target = False
        self.target_depth = 0
        self.waiting_folder_name = False
        self.waiting_link_name = False
        self.current_link: dict | None = None
        self._folder_stack: list[str] = []

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]):
        tag = tag.lower()
        attrs_dict = dict(attrs)

        if tag == "dl":
            self.depth += 1
        elif tag == "h3":
            self.waiting_folder_name = True
        elif tag == "a" and self.in_target:
            href = attrs_dict.get("href", "")
            self.current_link = {"url": href, "title": ""}
            self.waiting_link_name = True

    def handle_endtag(self, tag: str):
        tag = tag.lower()

        if tag == "dl":
            if self.in_target and self.depth == self.target_depth:
                self.in_target = False
            if self._folder_stack and self.in_target:
                self._folder_stack.pop()
            self.depth -= 1
        elif tag == "h3":
            self.waiting_folder_name = False
        elif tag == "a":
            if self.waiting_link_name and self.current_link:
                folder = self._folder_stack[-1] if self._folder_stack else "(unsorted)"
                self.current_link["folder"] = folder
                self.bookmarks.append(self.current_link)
                self.current_link = None
            self.waiting_link_name = False

    def handle_data(self, data: str):
        if self.waiting_folder_name:
            folder_name = data.strip()
            if folder_name == self.target_folder and not self.in_target:
                self.in_target = True
                self.target_depth = self.depth + 1
                self._folder_stack = []
            elif self.in_target:
                self._folder_stack.append(folder_name)
        elif self.waiting_link_name and self.current_link is not None:
            self.current_link["title"] += data


def parse_bookmarks(filepath: str, target_folder: str) -> list[dict]:
    """Parse HTML bookmarks file and return bookmarks from the target folder."""
    content = Path(filepath).read_text(encoding="utf-8")
    parser = BookmarkParser(target_folder)
    parser.feed(content)
    return parser.bookmarks


def extract_result_data(result, bookmark: dict) -> dict:
    """Extract data from a CrawlResult."""
    entry = {
        "url": result.url,
        "original_title": bookmark.get("title", ""),
        "folder": bookmark.get("folder", ""),
        "success": result.success,
    }
    if result.success:
        crawled_title = ""
        if hasattr(result, "metadata") and result.metadata:
            crawled_title = result.metadata.get("title", "")
        description = ""
        if hasattr(result, "markdown"):
            md = result.markdown
            raw = ""
            if hasattr(md, "raw_markdown"):
                raw = md.raw_markdown or ""
            elif isinstance(md, str):
                raw = md
            description = raw[:300].strip()
        entry["crawled_title"] = crawled_title
        entry["description"] = description
    else:
        entry["crawled_title"] = ""
        entry["description"] = ""
        entry["error"] = getattr(result, "error_message", "unknown error")
    return entry


async def crawl_bookmarks(bookmarks: list[dict], batch_size: int = 5) -> list[dict]:
    """Crawl each URL from the bookmarks list in batches."""
    url_to_bookmark = {b["url"]: b for b in bookmarks}
    enriched = []

    browser_config = BrowserConfig(headless=True, verbose=False)
    run_config = CrawlerRunConfig(
        cache_mode=CacheMode.BYPASS,
        page_timeout=30000,
    )

    total = len(bookmarks)
    print(f"Crawling {total} URLs in batches of {batch_size}...")

    async with AsyncWebCrawler(config=browser_config) as crawler:
        for i in range(0, total, batch_size):
            batch = bookmarks[i : i + batch_size]
            batch_urls = [b["url"] for b in batch]
            batch_num = i // batch_size + 1
            total_batches = (total + batch_size - 1) // batch_size
            print(f"  Batch {batch_num}/{total_batches} ({len(batch_urls)} URLs)...")

            results = await crawler.arun_many(
                urls=batch_urls,
                config=run_config,
            )

            for result in results:
                bm = url_to_bookmark.get(result.url, {})
                enriched.append(extract_result_data(result, bm))

            print(f"    Done: {len(results)} results")

    return enriched


async def main():
    parser = argparse.ArgumentParser(
        description="Parse bookmarks HTML and crawl URLs from a specified folder."
    )
    parser.add_argument(
        "--file", required=True, help="Path to the bookmarks HTML file"
    )
    parser.add_argument(
        "--folder", required=True, help="Name of the target folder to extract"
    )
    parser.add_argument(
        "--output",
        default="bookmarks_analysis.json",
        help="Output JSON file (default: bookmarks_analysis.json)",
    )
    parser.add_argument(
        "--batch-size",
        type=int,
        default=5,
        help="Number of URLs to crawl in each batch (default: 5)",
    )
    args = parser.parse_args()

    print(f"Parsing {args.file}...")
    bookmarks = parse_bookmarks(args.file, args.folder)
    print(f"Found {len(bookmarks)} bookmarks in folder '{args.folder}'")

    if not bookmarks:
        print(f"No bookmarks found in folder '{args.folder}'. Check the folder name.")
        sys.exit(1)

    # Deduplicate by URL (keep first occurrence)
    seen_urls: set[str] = set()
    unique_bookmarks: list[dict] = []
    duplicates: list[dict] = []
    for bm in bookmarks:
        if bm["url"] not in seen_urls:
            seen_urls.add(bm["url"])
            unique_bookmarks.append(bm)
        else:
            duplicates.append(bm)

    if duplicates:
        print(f"Found {len(duplicates)} duplicates (removed):")
        for d in duplicates:
            print(f"  - {d['title'][:60]}... [{d['folder']}]")

    print(f"Unique bookmarks to crawl: {len(unique_bookmarks)}")

    enriched = await crawl_bookmarks(unique_bookmarks, batch_size=args.batch_size)

    output = {
        "source_file": args.file,
        "target_folder": args.folder,
        "total_parsed": len(bookmarks),
        "duplicates_removed": len(duplicates),
        "unique_crawled": len(enriched),
        "bookmarks": enriched,
    }

    Path(args.output).write_text(
        json.dumps(output, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )
    print(f"\nResults saved to {args.output}")

    success_count = sum(1 for b in enriched if b["success"])
    fail_count = len(enriched) - success_count
    print(f"Success: {success_count}, Errors: {fail_count}")


if __name__ == "__main__":
    asyncio.run(main())
