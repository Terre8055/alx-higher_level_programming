#!/usr/bin/python3
import sys

def nqueens(N):
    """ solve the N queens puzzle """
    if not isinstance(N, int):
        print("N must be a number")
        sys.exit(1)
    if N < 4:
        print("N must be at least 4")
        sys.exit(1)
    board = [-1] * N
    queens(N, board, 0)

def queens(N, board, row):
    """ recursive function to place queens on the board """
    if row == N:
        print_board(board)
        return
    for col in range(N):
        if is_valid(board, row, col):
            board[row] = col
            queens(N, board, row+1)

def is_valid(board, row, col):
    """ check if the given position is valid """
    for i in range(row):
        if board[i] == col or \
           board[i] - i == col - row or \
           board[i] + i == col + row:
            return False
    return True

def print_board(board):
    """ print the board """
    for row in range(len(board)):
        line = ""
        for col in range(len(board)):
            if col == board[row]:
                line += "Q "
            else:
                line += ". "
        print(line)
    print()

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    try:
        N = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)
    nqueens(N)

