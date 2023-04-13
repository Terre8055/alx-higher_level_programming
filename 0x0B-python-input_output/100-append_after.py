#!/usr/bin/python3
"""Search and update"""


def append_after(filename="", search_string="", new_string=""):
    """inserts a line of text to a file, after each line with empty string"""
    text = ""
    with open(filename, mode="r") as file:
        for line in file:
            text += line
            if search_string in line:
                text += new_string
    with open(filename, mode="w") as file:
        file.write(text)
