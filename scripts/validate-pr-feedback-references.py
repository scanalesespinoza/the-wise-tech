#!/usr/bin/env python3
"""
Falla si el cuerpo del PR declara la sección 'Human Feedback References'
pero no contiene al menos un #issue o el texto 'N/A'.
Evita PRs sin vínculo al circuito de feedback cuando aplica.
"""
import os
import re
import sys

def main():
    body = os.environ.get("PR_BODY","")
    if "Human Feedback References" not in body:
        print("No PR body provided or section missing; skipping.")
        return
    refs = re.findall(r"#\d+", body)
    if not refs and "N/A" not in body:
        print("PR feedback references missing: add at least one #issue or 'N/A'.")
        sys.exit(1)
    print("PR feedback references OK.")

if __name__ == "__main__":
    main()
