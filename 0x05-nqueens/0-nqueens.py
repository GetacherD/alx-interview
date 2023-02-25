#!/usr/bin/python3
""" N- Queens backTracing """
import sys


if __name__ == "__main__":

    if len(sys.argv) < 2 or len(sys.argv) > 2:
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
        for i in range(row):
            if board[i][col]:
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

    sol = []

    def NQueen(i, j, n):
        """ main nqueen backtracking algorithm"""
        global board
        if n == 0:
            cand = []
            for row in range(N):
                for col in range(N):
                    if board[row][col]:
                        cand.append([row, col])
            print(cand)
            cand = []
            return True
        if j >= N:
            return False
        if is_safe(i, j):
            board[i][j] = 1
            if NQueen(i + 1, 0, n - 1):
                board[i][j] = 0
                NQueen(i, j + 1, n)
            else:
                board[i][j] = 0
                NQueen(i, j + 1, n)
        else:
            NQueen(i, j + 1, n)

    def reset():
        global board
        board = [[0 for i in range(N)] for j in range(N)]
    NQueen(0, 0, N)
