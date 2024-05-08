N = int(input())
queen = "Q"
empty = "-"
solutions = []

def isSafe(board, row, col):
    for p in range(N):
        if board[row][p] == queen or board[p][col] == queen:
            return False
    for n in range(N):
        for m in range(N):
            if row + col == n + m or row - col == n - m:
                if board[n][m] == queen:
                    return False
    return True

def nqueen():
    global solutions
    stack = []  # Using a stack for DFS
    stack.append(([[empty] * N for _ in range(N)], 0))  # Initial state with an empty board
    while stack:
        board, row = stack.pop()
        if row == N:
            solutions.append(board[:])
            continue
        for col in range(N):
            if isSafe(board, row, col):
                new_board = [row[:] for row in board]
                new_board[row][col] = queen
                stack.append((new_board, row + 1))

nqueen()

def printBoard(board):
    for row in board:
        print(" ".join(row))

for solution in solutions:
    printBoard(solution)
    print()

print("Total solutions:", len(solutions))
