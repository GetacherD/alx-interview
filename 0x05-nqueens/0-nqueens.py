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

    def NQueen(col):
        """ main nqueen backtracking algorithm"""
        row = 1
        placed = False
        prev = col
        col = 0
        global board
        board[0][prev] = 1
        while True:
            for i in range(col, N):
                if is_safe(row, i):
                    board[row][i] = 1
                    prev = i
                    placed = True
                    break
            if placed:
                col = 0
                if row == N - 1:
                    return board
                row += 1
                placed = False
            else:
                col = prev + 1
                row -= 1
                board[row][prev] = 0
                placed = False
                for k in range(N):
                    if board[row - 1][k]:
                        prev = k
            if row < 1:
                return []
            if row >= N:
                return []

    def reset():
        global board
        board = [[0 for i in range(N)] for j in range(N)]
    for i in range(N):
        candidate = NQueen(i)
        data = []
        if candidate:
            for k in range(N):
                for m in range(N):
                    if candidate[k][m]:
                        data.append([k, m])
        if data:
            print(data)
        reset()
