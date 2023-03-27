#!/usr/bin/pyhton3
"""
Converts a markdown file to html
"""
import sys
import os
import markdown

# Check for correct number of arguments
if len(sys.argv) < 3:
    print("Usage: markdown2html.py README.md README.html")
    sys.exit(1)

# Check if file exists
inputFile = sys.argv[1]
outputFile = sys.argv[2]

# Check if file exists
if not os.path.exists(inputFile):
    print(f"Usage: ./markdown2html.py README.md README.html")
    sys.exit(1)

# Convert markdown to html
with open(inputFile) as f:
    html_txt = markdown.markdown(f.read())
# Write html to file
with open(outputFile, "w") as f:
    f.write(html_txt)
# Exit
sys.exit(0)
