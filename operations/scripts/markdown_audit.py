#!/usr/bin/env python3
"""Audit Markdown files for metadata coverage and broken links."""

from __future__ import annotations

import csv
import os
import re
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable, List, Optional, Sequence

import markdown
import requests
from git import Repo
from github import Github, GithubException
from markdown.extensions.meta import MetaExtension
from xml.etree import ElementTree as ET

REPO_ROOT = Path(__file__).resolve().parents[2]
TARGET_DIRS = (
    REPO_ROOT / "knowledge",
    REPO_ROOT / "experience",
    REPO_ROOT / "implementation",
)
OUTPUT_PATH = REPO_ROOT / "audit.csv"
HTTP_TIMEOUT = 8
USER_AGENT = "wise-tech-md-audit/1.0"


@dataclass
class AuditRow:
    path: Path
    title: str
    last_modified: str
    broken_links: int
    metadata_ok: bool


def split_front_matter(text: str) -> tuple[str, str]:
    if text.startswith("---\n"):
        parts = text.split("\n")
        for idx in range(1, len(parts)):
            if parts[idx].strip() == "---":
                front = "\n".join(parts[: idx + 1]) + "\n"
                body = "\n".join(parts[idx + 1 :])
                return front, body
    return "", text


def extract_title(front_matter: str, body: str, path: Path) -> str:
    title = None
    if front_matter:
        for line in front_matter.splitlines():
            if line.lower().startswith("title:"):
                title = line.split(":", 1)[1].strip().strip('"')
                if title:
                    break
    if not title:
        match = re.search(r"^#\s+(.+)", body, re.MULTILINE)
        if match:
            title = match.group(1).strip()
    if not title:
        title = path.stem.replace("-", " ").strip().title() or path.name
    return title


def has_metadata_block(body: str) -> bool:
    snippet = body.lstrip().splitlines()[:4]
    return any("> **Propósito:**" in line for line in snippet)


def markdown_to_links(text: str) -> Sequence[str]:
    front_matter, body = split_front_matter(text)
    clean_body = body.strip()
    html = markdown.markdown(clean_body, extensions=[MetaExtension()])
    wrapped = f"<div>{html}</div>"
    links: List[str] = []
    try:
        root = ET.fromstring(wrapped)
    except ET.ParseError:
        return links
    for anchor in root.iter("a"):
        href = anchor.attrib.get("href", "")
        if href.startswith("http://") or href.startswith("https://"):
            links.append(href)
    return links


def normalize_url(url: str) -> str:
    clean = url.split("#", 1)[0]
    return clean.rstrip("/ ")


def should_skip_link(url: str) -> bool:
    lowered = url.lower()
    return any(
        prefix in lowered
        for prefix in ("localhost", "127.0.0.1", "0.0.0.0", "file://", "mailto:")
    )


def check_link(url: str, cache: dict[str, bool]) -> bool:
    normalized = normalize_url(url)
    if not normalized or should_skip_link(normalized):
        return True
    if normalized in cache:
        return cache[normalized]
    headers = {"User-Agent": USER_AGENT}
    try:
        response = requests.head(
            normalized, allow_redirects=True, timeout=HTTP_TIMEOUT, headers=headers
        )
        status = response.status_code
        if status >= 400 or status == 405:
            response = requests.get(
                normalized, allow_redirects=True, timeout=HTTP_TIMEOUT, headers=headers
            )
            status = response.status_code
        ok = status < 400
    except requests.RequestException:
        ok = False
    cache[normalized] = ok
    return ok


def get_last_modified(repo: Repo, path: Path) -> str:
    rel_path = os.path.relpath(path, repo.working_tree_dir)
    try:
        return repo.git.log("-1", "--format=%cs", "--", rel_path)
    except Exception:
        return "N/A"


def discover_repo_slug(repo: Repo) -> Optional[str]:
    try:
        remote_url = next(repo.remote().urls)
    except Exception:
        return None
    if remote_url.startswith("git@github.com:"):
        return remote_url.split(":", 1)[1].rstrip(".git")
    if remote_url.startswith("https://github.com/"):
        return remote_url.split("github.com/", 1)[1].rstrip(".git")
    return None


def announce_repo(repo: Repo) -> None:
    token = os.getenv("GITHUB_TOKEN")
    slug = discover_repo_slug(repo)
    if not token or not slug:
        print("⚠️  No GitHub token or slug detected; continuing with local data only.")
        return
    try:
        gh_repo = Github(token).get_repo(slug)
    except GithubException as exc:  # pragma: no cover
        print(f"⚠️  Unable to reach GitHub repo {slug}: {exc}")
        return
    print(
        f"ℹ️  Connected to GitHub repo {gh_repo.full_name} (default branch: {gh_repo.default_branch})."
    )


def iter_markdown_files() -> Iterable[Path]:
    for base in TARGET_DIRS:
        if not base.exists():
            continue
        yield from sorted(base.rglob("*.md"))


def run_audit() -> None:
    repo = Repo(REPO_ROOT)
    announce_repo(repo)
    cache: dict[str, bool] = {}
    rows: List[AuditRow] = []
    for path in iter_markdown_files():
        text = path.read_text(encoding="utf-8")
        front_matter, body = split_front_matter(text)
        title = extract_title(front_matter, body, path)
        metadata_ok = has_metadata_block(body)
        broken = 0
        for link in markdown_to_links(text):
            if not check_link(link, cache):
                broken += 1
        last_modified = get_last_modified(repo, path)
        rows.append(
            AuditRow(
                path=path.relative_to(REPO_ROOT),
                title=title,
                last_modified=last_modified,
                broken_links=broken,
                metadata_ok=metadata_ok,
            )
        )
    with OUTPUT_PATH.open("w", encoding="utf-8", newline="") as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(
            ["path", "title", "last_modified", "broken_links", "metadata_ok"]
        )
        for row in rows:
            writer.writerow(
                [
                    row.path.as_posix(),
                    row.title,
                    row.last_modified,
                    row.broken_links,
                    "yes" if row.metadata_ok else "no",
                ]
            )
    flagged = [row for row in rows if not row.metadata_ok or row.broken_links > 3]
    print(f"Audit completed for {len(rows)} documents. Flagged: {len(flagged)}.")
    if flagged:
        for row in flagged:
            print(
                f" - {row.path}: metadata={'ok' if row.metadata_ok else 'missing'}, broken_links={row.broken_links}"
            )


if __name__ == "__main__":
    run_audit()
