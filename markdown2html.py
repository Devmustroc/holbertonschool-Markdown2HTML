#!/usr/bin/python3
"""Converts markdown to html"""
import sys
import os
import markdown


if __name__ == "__main__":
    """
    This script converts a Markdown file to HTML.

    Usage: ./markdown2html.py <input_file> <output_file>

    The first argument is the path to the input Markdown file, and the second argument
    is the path to the output HTML file. If the input file does not exist, an error
    message will be printed to STDERR and the script will exit with a status code of 1.

    Example usage:

        ./markdown2html.py README.md README.html
    """

    # Check that the correct number of command line arguments are provided
    if len(sys.argv) < 3:
        print("Usage: ./markdown2html.py README.md README.html", file=sys.stderr)
        sys.exit(1)

    # Get the input and output file paths from the command line arguments
    input_file, output_file = sys.argv[1], sys.argv[2]

    # Check that the input file exists
    if not os.path.exists(input_file):
        print(f"Missing {input_file}", file=sys.stderr)
        sys.exit(1)

    # Convert the Markdown text to HTML
    with open(input_file) as f:
        html_text = markdown.markdown(f.read())

    # Write the HTML text to the output file
    with open(output_file, "w") as f:
        f.write(html_text)

    # Exit with a status code of 0 to indicate success
    sys.exit(0)