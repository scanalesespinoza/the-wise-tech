#!/usr/bin/env python3
"""Fail when user-facing strings are not wrapped for translation."""

from __future__ import annotations

import ast
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[2]
TARGET_FILES = [REPO_ROOT / "operations" / "scripts" / "translation_status.py"]


class I18NVisitor(ast.NodeVisitor):
    def __init__(self, *, source_lines: list[str]) -> None:
        self.errors: list[tuple[int, str]] = []
        self._stack: list[ast.AST] = []
        self._source_lines = source_lines

    def visit_Constant(self, node: ast.Constant) -> None:  # pragma: no cover - small utility
        if not isinstance(node.value, str):
            return
        if self._is_docstring(node):
            return
        if self._has_ignore_comment(node.lineno):
            return
        if not self._looks_user_facing(node.value):
            return
        if self._is_translated(node):
            return
        self.errors.append((node.lineno, node.value.strip()))

    def generic_visit(self, node: ast.AST) -> None:  # pragma: no cover - traversal support
        self._stack.append(node)
        super().generic_visit(node)
        self._stack.pop()

    def _parent(self) -> ast.AST | None:
        return self._stack[-1] if self._stack else None

    def _grandparent(self) -> ast.AST | None:
        return self._stack[-2] if len(self._stack) >= 2 else None

    def _is_docstring(self, node: ast.Constant) -> bool:
        parent = self._parent()
        grandparent = self._grandparent()
        if isinstance(parent, (ast.Module, ast.FunctionDef, ast.AsyncFunctionDef, ast.ClassDef)):
            return bool(parent.body and parent.body[0] is node)
        if (
            isinstance(parent, ast.Expr)
            and isinstance(grandparent, (ast.Module, ast.FunctionDef, ast.AsyncFunctionDef, ast.ClassDef))
        ):
            return bool(grandparent.body and grandparent.body[0] is parent)
        return False

    def _has_ignore_comment(self, lineno: int) -> bool:
        if lineno - 1 >= len(self._source_lines):
            return False
        return "i18n: ignore" in self._source_lines[lineno - 1]

    def _looks_user_facing(self, value: str) -> bool:
        return value.count(" ") >= 1 and any(char.isalpha() for char in value)

    def _is_translated(self, node: ast.Constant) -> bool:
        parent = self._parent()
        if isinstance(parent, ast.Call):
            func = parent.func
            if isinstance(func, ast.Name) and func.id in {"_", "gettext"}:
                return True
            if isinstance(func, ast.Attribute) and func.attr == "gettext":
                return True
        return False


def lint_file(path: Path) -> list[tuple[int, str]]:
    tree = ast.parse(path.read_text(encoding="utf-8"))
    visitor = I18NVisitor(source_lines=path.read_text(encoding="utf-8").splitlines())
    visitor.visit(tree)
    return visitor.errors


def main() -> int:
    failed: list[str] = []
    for file_path in TARGET_FILES:
        errors = lint_file(file_path)
        if errors:
            for lineno, text in errors:
                failed.append(f"{file_path}:{lineno}: non-localized string -> {text}")
    if failed:
        for message in failed:
            print(message)
        return 1
    print("i18n lint passed ✅")
    return 0


if __name__ == "__main__":  # pragma: no cover - CLI entry point
    sys.exit(main())
