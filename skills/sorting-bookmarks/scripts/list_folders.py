"""
List top-level folders from a bookmarks HTML file.
Outputs JSON with folder names, bookmark counts, and subfolder counts.
"""

import argparse
import json
import sys
from html.parser import HTMLParser
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8", errors="replace")
sys.stderr.reconfigure(encoding="utf-8", errors="replace")


class FolderHierarchyParser(HTMLParser):
    """Parse bookmarks HTML and extract folder hierarchy with stats."""

    def __init__(self):
        super().__init__()
        self.depth = 0
        self.in_h3 = False
        self.current_name = ""
        # Stack of folder info: (depth, name)
        self.folder_stack: list[tuple[int, str]] = []
        # All folders: (depth, name, bookmark_count, subfolder_count)
        self.folders: list[dict] = []
        self._folder_map: dict[int, dict] = {}  # id -> folder dict
        self._current_folder_id = -1
        self._id_counter = 0
        # Track parent-child via depth stack
        self._depth_to_folder_id: dict[int, int] = {}
        self._bookmark_counts: dict[int, int] = {}  # folder_id -> count
        self._subfolder_counts: dict[int, int] = {}  # folder_id -> count

    def handle_starttag(self, tag: str, attrs):
        tag = tag.lower()
        if tag == "dl":
            self.depth += 1
        elif tag == "h3":
            self.in_h3 = True
            self.current_name = ""
        elif tag == "a":
            # Count bookmark in current folder
            if self._current_folder_id >= 0:
                self._bookmark_counts[self._current_folder_id] = (
                    self._bookmark_counts.get(self._current_folder_id, 0) + 1
                )

    def handle_data(self, data: str):
        if self.in_h3:
            self.current_name += data

    def handle_endtag(self, tag: str):
        tag = tag.lower()
        if tag == "h3" and self.in_h3:
            self.in_h3 = False
            name = self.current_name.strip()
            folder_id = self._id_counter
            self._id_counter += 1

            folder = {"id": folder_id, "depth": self.depth, "name": name}
            self._folder_map[folder_id] = folder
            self._bookmark_counts[folder_id] = 0
            self._subfolder_counts[folder_id] = 0

            # Track parent
            parent_depth = self.depth - 1
            if parent_depth in self._depth_to_folder_id:
                parent_id = self._depth_to_folder_id[parent_depth]
                folder["parent_id"] = parent_id
                self._subfolder_counts[parent_id] = (
                    self._subfolder_counts.get(parent_id, 0) + 1
                )
            else:
                folder["parent_id"] = None

            self._depth_to_folder_id[self.depth] = folder_id
            self._current_folder_id = folder_id
            self.folders.append(folder)

        elif tag == "dl":
            # Leaving a <DL> — go back to parent folder
            if self.depth in self._depth_to_folder_id:
                parent_depth = self.depth - 1
                if parent_depth in self._depth_to_folder_id:
                    self._current_folder_id = self._depth_to_folder_id[parent_depth]
                del self._depth_to_folder_id[self.depth]
            self.depth -= 1

    def get_top_level_folders(self) -> list[dict]:
        """Return folders at depth=2 (direct children of root)."""
        root_folders = []
        for f in self.folders:
            if f["depth"] == 2:
                fid = f["id"]
                bookmarks = self._count_bookmarks_recursive(fid)
                root_folders.append(
                    {
                        "name": f["name"],
                        "bookmarks_count": bookmarks,
                        "subfolders_count": self._subfolder_counts.get(fid, 0),
                    }
                )
        return root_folders

    def _count_bookmarks_recursive(self, folder_id: int) -> int:
        """Count bookmarks in folder and all its descendants."""
        total = self._bookmark_counts.get(folder_id, 0)
        for f in self.folders:
            if f.get("parent_id") == folder_id:
                total += self._count_bookmarks_recursive(f["id"])
        return total


def main():
    parser = argparse.ArgumentParser(
        description="List top-level folders from a bookmarks HTML file."
    )
    parser.add_argument(
        "--file", required=True, help="Path to the bookmarks HTML file"
    )
    args = parser.parse_args()

    content = Path(args.file).read_text(encoding="utf-8")
    hp = FolderHierarchyParser()
    hp.feed(content)

    folders = hp.get_top_level_folders()

    output = {"source_file": args.file, "folders": folders}
    print(json.dumps(output, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
