def solve_n_queens(n):
    """
    Solve the N-Queens problem using backtracking with column and diagonal hashing.
    Returns all valid board configurations.
    """
    solutions = []
    # Sets to track occupied columns and diagonals
    cols = set()
    diag1 = set()  # top-left to bottom-right diagonal (row - col)
    diag2 = set()  # top-right to bottom-left diagonal (row + col)

    board = [-1] * n  # board[row] = column where queen is placed

    def backtrack(row):
        if row == n:
            solutions.append(board[:])
            return

        for col in range(n):
            if col in cols or (row - col) in diag1 or (row + col) in diag2:
                continue

            # Place queen
            board[row] = col
            cols.add(col)
            diag1.add(row - col)
            diag2.add(row + col)

            backtrack(row + 1)

            # Remove queen (backtrack)
            cols.remove(col)
            diag1.remove(row - col)
            diag2.remove(row + col)

    backtrack(0)
    return solutions


def format_board(solution, n):
    """Convert a solution array into a visual board representation."""
    rows = []
    for row in range(n):
        line = ""
        for col in range(n):
            line += "Q " if solution[row] == col else ". "
        rows.append(line.strip())
    return "\n".join(rows)


def main():
    n = 8  # Change this to solve for any N

    print(f"Solving {n}-Queens Problem")
    print("=" * 40)

    solutions = solve_n_queens(n)

    # Print all solutions
    for i, solution in enumerate(solutions):
        print(f"\nSolution {i + 1}:")
        print(format_board(solution, n))
        print()

    # Print total count
    print("=" * 40)
    print(f"Total valid configurations for {n}-Queens: {len(solutions)}")


if __name__ == "__main__":
    main()
