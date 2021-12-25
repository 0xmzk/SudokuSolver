import solver

# Acceptable format type 1
example_sudoku = [
    [9, 0, 0, 0, 5, 0, 0, 0, 2],
    [0, 0, 8, 6, 0, 3, 0, 5, 0],
    [1, 5, 0, 9, 2, 0, 0, 0, 4],
    [0, 8, 6, 0, 0, 0, 0, 0, 0],
    [4, 0, 2, 8, 3, 7, 6, 0, 5],
    [0, 0, 0, 0, 0, 0, 2, 8, 0],
    [6, 0, 0, 0, 7, 9, 0, 2, 8],
    [0, 9, 0, 5, 0, 4, 3, 0, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 7],
]

# Acceptable format type 2
example_sudoku2 = [9, 0, 0, 0, 5, 0, 0, 0, 2, 0, 0, 8, 6, 0, 3, 0, 5, 0, 1, 5, 0, 9, 2, 0, 0, 0, 4, 0, 8, 6, 0, 0, 0, 0,
                   0, 0, 4, 0, 2, 8, 3, 7, 6, 0, 5, 0, 0, 0, 0, 0, 0, 2, 8, 0, 6, 0, 0, 0, 7, 9, 0, 2, 8, 0, 9, 0, 5, 0,
                   4, 3, 0, 0, 8, 0, 0, 0, 6, 0, 0, 0, 7]

# Example 1
# Create a Solver instance - by default it solves the sudoku upon instantiation
s = solver.Solver(example_sudoku)

# Prints a 'pretty' version of the solved sudoku
s.print()

# Example 2 (auto-solve disabled)
# Create a Solver instance - this time the sudoku will not be solved upon instantiation
s = solver.Solver(example_sudoku, auto_solve=False)

# Call the solve function to solve the sudoku
s.solve()

# Returns the solved sudoku as an 2D-array (structure of format type 1)
print(s.returnAs2DArray())


