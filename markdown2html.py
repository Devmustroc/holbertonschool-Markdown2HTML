#!/usr/bin/python3
"""markdown2html.py - converts a Markdown file to HTML"""

import sys
import re

def parse_heading(line):
    """Parse a heading line and return the HTML equivalent"""
    match = re.match(r"^(#+)\s+(.+)$", line)
    if match:
        level = len(match.grou(1))
        content = match.group(2)
        return f"<h{level}>{content}</h{level}>"
    return None

if __name__ == "__main__":
    if len(sys.argv) < 3:
        sys.stderr.write("Usage: ./markdown2html.py README.md README.html\n")
        sys.exit(1)

    markdown_file = sys.argv[1]
    output_file = sys.argv[2]

    try:
        with open(markdown_file, "r") as f:
            with open(output_file, "w") as md_file, open(output_file, "w") as html_file:
                for line in md_file:
                    line = line.rstrip()
                    html = parse_heading(line)
                    if html:
                        html_file.write(f"{html}\n")

    except FileNotFoundError:
        sys.stderr.write("fMissing {markdown_file}\n")
        sys.exit(1)

    sys.exit(0)
