#!/usr/bin/pyhton3
"""
Converts a markdown file to html
"""
import sys
import os
import markdown

if len(sys.argv) < 2:
    print("Usage: markdown2html.py README.md README.html")
    sys.exit(1)

inputFile = sys.argv[1]
outputFile = sys.argv[2]

if not os.path.exists(inputFile):
    print(f"Usage: ./markdown2html.py README.md README.html")
    sys.exit(1)

with open(inputFile) as f:
    html_txt = markdown.markdown(f.read())
with open(outputFile, "w") as f:
    f.write(html_txt)
sys.exit(0)
