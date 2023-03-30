#!/usr/bin/python3
"""markdown2html.py - converts a Markdown file to HTML"""

import sys

if __name__ == "__main__":
    if len(sys.argv) < 3:
        sys.stderr.write("Usage: ./markdown2html.py README.md README.html\n")
        sys.exit(1)

    markdown_file = sys.argv[1]
    output_file = sys.argv[2]

    try:
        with open(markdown_file, 'r') as f:
            pass
    except FileNotFoundError:
        sys.stderr.write("fMissing {markdown_file}\n")
        sys.exit(1)

    sys.exit(0)
