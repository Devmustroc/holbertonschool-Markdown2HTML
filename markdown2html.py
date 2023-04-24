#!/usr/bin/python3
"""markdown2html.py - converts a Markdown file to HTML"""

from sys import argv, stderr, exit
import os


def input_check():
    """Checks input"""
    if len(argv) != 3:  # check for correct number of arguments
        print("Usage: ./markdown2html.py README.md README.html", file=stderr)  # print error
        exit(1)  # exit
    if not os.path.exists(argv[1]):  # check if file exists
        print("Missing {}".format(argv[1]), file=stderr)  # print error
        exit(1)  # exit


def file_to_array():
    """Converts file to array"""
    with open(argv[1], 'r') as file:  # open file
        array = [line for line in file]  # create array
    return array  # return array


def array_parser(array):
    """Parses array"""
    result = ""  # result string
    i = 0  # index
    while i < len(array):  # loop through array
        if '#' in array[i]:  # if line is a header
            h_level = array[i].count('#')  # count number of #
            text = array[i].strip('#\n').strip()  # get text
            html = f"<h{h_level}>{text}</h{h_level}>"  # create html
            result += html + "\n"  # add to result
        i += 1
    return result


def file_writer(result, html_file):
    """Writes result to file"""
    with open(argv[2], 'w') as file:  # open file
        file.write(result)  # write result
    exit(0)  # exit


def main():  # main function
    """Main function"""
    input_check()  # check input
    array = file_to_array()  # convert file to array
    text = array_parser(array)
    file_writer(text, argv[2])  # parse array


if __name__ == "__main__":  # if file is run directly
    main()  # run main function
