#!/usr/bin/python3
""" N- Queens backTracing """
import sys


if len(sys.argv) < 2:
    print("Usage: nqueens N")
    sys.exit(1)
try:
    N = int(sys.argv[1])
except Exception:
    print("N must be a number")
    sys.exit(1)
if N < 4:
    print("N must be at least 4")
    sys.exit(1)

board = [[0 for i in range(N)] for j in range(N)]


def is_safe(row, col):
    """ Check if placing on cell i, j is OK"""
    for i in range(N):
        if board[row][i] == 1 or board[i][col] == 1:
            return False
    x = row - 1
    y = col + 1
    while x >= 0 and y <= N - 1:
        if board[x][y] == 1:
            return False
        x -= 1
        y += 1
    x = row - 1
    y = col - 1
    while x >= 0 and y >= 0:
        if board[x][y] == 1:
            return False
        x -= 1
        y -= 1
    return True


def NQueen(row, n):
    """ main nqueen backtracking algorithm"""
    if n == 0:
        return True
    for j in range(N):
        if is_safe(row, j):
            board[row][j] = 1
            if NQueen(row + 1, n - 1):
                return True
            board[row][j] = 0
    return False


def _print(grid):
    """ print solution board"""
    solution = []
    for i in range(N):
        for j in range(N):
            if grid[i][j]:
                solution.append([i, j])
    print(solution)


def reset_board():
    """ reset board """
    global board
    board = [[0 for _ in range(N)] for _ in range(N)]


for i in range(N):
    reset_board()
    board[0][i] = 1
    if NQueen(1, N - 1):
        _print(board)
