#!/usr/bin/env python3
import os
import re
import sys

MD_LINK = re.compile(r"\[[^\]]+\]\((?P<url>[^\s)]+)\)")
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))


def is_internal(path: str) -> bool:
    return not (
        path.startswith("http://")
        or path.startswith("https://")
        or path.startswith("#")
    )


def normalize(path: str, base: str) -> str:
    if path.startswith("#"):
        return ""  # anchors dentro del mismo archivo: ignorar aquí
    clean_path = path.split("#", 1)[0]
    if not clean_path:
        return ""
    abs_path = os.path.normpath(os.path.join(base, clean_path))
    return abs_path


def check_markdown(md_file: str) -> list[tuple[str, str]]:
    errors = []
    base = os.path.dirname(md_file)
    with open(md_file, "r", encoding="utf-8", errors="ignore") as f:
        for line in f:
            for m in MD_LINK.finditer(line):
                url = m.group("url")
                if is_internal(url):
                    target = normalize(url, base)
                    if target and not os.path.exists(target):
                        errors.append((md_file, url))
    return errors


def collect_md_files(root: str) -> list[str]:
    result = []
    for dirpath, _, filenames in os.walk(root):
        for fn in filenames:
            if fn.lower().endswith(".md"):
                result.append(os.path.join(dirpath, fn))
    return result


def main():
    md_files = collect_md_files(ROOT)
    failures = []
    for f in md_files:
        failures.extend(check_markdown(f))
    if failures:
        print("Broken internal links found:")
        for src, url in failures:
            print(f" - {src} -> {url}")
        sys.exit(1)
    print("All internal markdown links OK.")


if __name__ == "__main__":
    main()
