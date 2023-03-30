#!/usr/bin/python3
"""markdown2html.py - converts a Markdown file to HTML"""

import sys
import re


def parse_headings(ln):
    """Parses a ln of Markdown for headings and returns the corresponding HTML"""
    match = re.match(r'^(#{1,6})\s+(.*)', ln)
    if match:
        level = len(match.group(1))
        content = match.group(2)
        return "<h{0}>{1}</h{0}>".format(level, content)
    return None


if __name__ == "__main__":
    if len(sys.argv) < 3:
        sys.stderr.write("Usage: ./markdown2html.py README.md README.html\n")
        sys.exit(1)

    markdown_file = sys.argv[1]
    output_file = sys.argv[2]

    try:
        with open(markdown_file, "r") as f:
            with open(markdown_file, 'r') as md_file, open(output_file, 'w') as html_file:
                for line in md_file:
                    line = line.rstrip()
                    html = parse_headings(line)
                    if html:
                        html_file.write(html + '\n')

    except FileNotFoundError:
        sys.stderr.write("fMissing {markdown_file}\n")
        sys.exit(1)

    sys.exit(0)
