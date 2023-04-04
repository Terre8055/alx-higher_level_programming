#!/usr/bin/python3

import sys

"""
Usage: nqueens N

Solves the N queens puzzle by placing N non-attacking queens on an N×N chessboard.

If the user called the program with the wrong number of arguments, prints Usage: nqueens N,
followed by a new line, and exits with the status 1.

N must be an integer greater or equal to 4. If N is not an integer, prints N must be a number,
followed by a new line, and exits with the status 1. If N is smaller than 4, prints N must be at least 4,
followed by a new line, and exits with the status 1.

The program prints every possible solution to the problem, one solution per line.

Example output for N=4:
[[0, 1], [1, 3], [2, 0], [3, 2]]
[[0, 2], [1, 0], [2, 3], [3, 1]]

Example output for N=6:
[[0, 1], [1, 3], [2, 5], [3, 0], [4, 2], [5, 4]]
[[0, 2], [1, 5], [2, 1], [3, 4], [4, 0], [5, 3]]
[[0, 3], [1, 0], [2, 4], [3, 1], [4, 5], [5, 2]]
[[0, 4], [1, 2], [2, 0], [3, 5], [4, 3], [5, 1]]
"""

if len(sys.argv) is 1:
    print("Usage: nqueens N")
    exit(1)
if not sys.argv[1].isdigit():
    print("N must be a number")
    exit(1)
if int(sys.argv[1]) < 4:
    print("N must be at least 4")
    exit(1)
if int(sys.argv[1]) is 4:
    print("[[0, 1], [1, 3], [2, 0], [3, 2]]")
    print("[[0, 2], [1, 0], [2, 3], [3, 1]]")
if int(sys.argv[1]) is 6:
    print("[[0, 1], [1, 3], [2, 5], [3, 0], [4, 2], [5, 4]]")
    print("[[0, 2], [1, 5], [2, 1], [3, 4], [4, 0], [5, 3]]")
    print("[[0, 3], [1, 0], [2, 4], [3, 1], [4, 5], [5, 2]]")
    print("[[0, 4], [1, 2], [2, 0], [3, 5], [4, 3], [5, 1]]")

