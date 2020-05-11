# SudokuSolver

A Sudoku solver module written in Python.

## Acceptable sudoku formats
The acceptable formats are as follows:

* A 2D-Array that contains 9 rows which each contain 9 numbers. Where each row corresponds to a row on the sudoku board and each number in the row corresponds to a number in the row on the sudoku board.
* A 1D-Array that contains 81 numbers. Where every 9 numbers in the array correspond to a row of numbers on the sudoku board.
## Usage
### Demo
```python
import solver

# Create a Solver instance - by default it solves the sudoku upon instantiation
solver = solver.Solver(sudoku_array_goes_here)

# Prints a 'pretty' version of the solved sudoku
solver.print()
```
For more check example.py 
## Documentation
The Solver class has the following methods: 
`.solve()`,`.print()`,`.returnAsArray()`.

When invoked `Solver.solve()` will attempt to solve the sudoku given.

When invoked `Solver.print()` will print out a sudoku grid.

When invoked `Solver.returnAsArray()` will return the sudoku as a 2D-array.

### Exceptions

* If the sudoku is unsolvable a `UnsolvableSudoku` exception is thrown. 
* If the sudoku is already solved a `SudokuSolved` exception is thrown.
* If the sudoku is of an invalid format a `InvalidSudoku` exception is thrown.

