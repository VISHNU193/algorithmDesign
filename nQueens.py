def is_safe(board, row, col, n):

    for i in range(row):
        if board[i] == col or abs(board[i] - col) == abs(i - row):
            return False
    return True

def solve_n_queens_util(board, row, n, solutions):
    if row == n:
        solutions.append(board[:])
        return

    for col in range(n):
        if is_safe(board, row, col, n):
            board[row] = col
            solve_n_queens_util(board, row + 1, n, solutions)
            board[row] = -1  # Backtrack

def solve_n_queens(n):
    board = [-1] * n  # Initialize the board with -1
    solutions = []
    solve_n_queens_util(board, 0, n, solutions)
    return solutions

def print_solutions(solutions):
    for solution in solutions:
        for row in solution:
            print('.' * row + 'Q' + '.' * (len(solution) - row - 1))
        print()


n = 4
solutions = solve_n_queens(n)
print(f"Number of solutions for {n}-Queens: {len(solutions)}")
print_solutions(solutions)
