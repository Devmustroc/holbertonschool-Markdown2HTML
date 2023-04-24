#!/usr/bin/python3
"""markdown2html.py - converts a Markdown file to HTML"""
import os
import sys


def input_check():
    """Checks if the input file exists"""
    if len(sys.argv) < 3:
        print("Usage: ./markdown2html.py README.md README.html", file=sys.stderr)
        exit(1)
    if not os.path.exists(sys.argv[1]):
        print("Missing {}".format(sys.argv[1]), file=sys.stderr)
        exit(1)


def file_to_array():
    """Reads the file and returns an array"""
    with open(sys.argv[1], 'r') as f:
        lines = [f.readlines()]
    return lines


def array_parser(lines):
    """Parses the array and returns a new array"""
    result = ""
    i = 0

    while i < len(lines):
        if "#" in lines[i]:
            result += "<h{}>{}</h{}>".format(lines[i].count("#"), lines[i].replace("#", "").strip(),
                                             lines[i].count("#"))
        elif "-" in lines[i]:
            result += "<ul>\n"
            while "-" in lines[i]:
                result += "<li>{}</li>\n".format(lines[i].replace("-", "").strip())
                i += 1
            result += "</ul>\n"
        else:
            result += "<p>{}</p>\n".format(lines[i].strip())
        i += 1
    return result


def file_writer(result, file):
    """Writes the result to the output file"""
    with open(sys.argv[2], 'w') as f:
        f.write(result)
    exit(0)


def main():
    """Main function"""
    input_check()
    array = file_to_array()
    text = array_parser(array)
    file_writer(text, sys.argv[2])


if __name__ == "__main__":
    main()
