#!/usr/bin/python3
""" function that prints a text with new lines """


def text_indentation(text):
    """Prints the given text with two newlines after each sentence-ending punctuation.

    Args:
        text (str): The text to be printed.

    Raises:
        TypeError: If `text` is not a string.

    Returns:
        None
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    # Initialize a variable to keep track of the characters printed in the current line
    chars_in_line = 0

    for char in text:
        # If the current character is a sentence-ending punctuation, print two newlines
        # and reset the `chars_in_line` counter
        if char in ['.', '?', ':']:
            print('\n\n', end='')
            chars_in_line = 0
        # If the current character is not a whitespace, print it and increment the
        # `chars_in_line` counter
        elif not char.isspace():
            print(char, end='')
            chars_in_line += 1
        # If the current character is a whitespace, print it only if it is not the first
        # character in a new line
        elif chars_in_line > 0:
            print(char, end='')
