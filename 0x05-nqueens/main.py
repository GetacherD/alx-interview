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

    sol = []

    def NQueen(c):
        """ main nqueen backtracking algorithm"""
        row = 0
        col = 0
        safe = False
        global board
        while True:
            print(f"trying for ({row}, {col}", end="\t")
            for i in range(col, N):
                print("try for col=", i, "row=", row)
                if is_safe(row, i):
                    board[row][i] = 1
                    safe = True
                    break
                    print(f"Safe placed @t ({row}, {col}", end="")
            if safe:
                row += 1
                col = 0
            if not safe:
                safe = False
                print(f"back Trackin ({row}, {col}", end="\t")
                while True:
                    row -= 1
                    print(f"back Trackin to ({row}, {col}", end="\t")
                    for i in range(N):
                        if board[row][i]:
                            board[row][i] = 0
                            col = i + 1
                            print(
                                f"prev queen found at  ({row}, {col - 1}", end="\t")
                            break
                    if row == 0 and col >= N:
                        print(f"No Solution", end="\t")
                        return []
                    elif row and col < N:
                        board[row][col] = 1
                        col = 0
                        break
            if row == N - 1:
                print(board)
                return board
    print(NQueen(2))
