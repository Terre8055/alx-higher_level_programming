#!/usr/bin/python3
"""Defines a text file-reading function."""


def read_file(filename=""):
        '''
        function to read the contents of a file
        @r - read
        @filename - relative path to file
        @encoding - parse file in utf-8 encoding
        '''

        with open(filename, mode='r', encoding='utf-8') as f:
        print(f.read(), end="")
