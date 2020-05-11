# SudokuSolver

A Sudoku solver module written in Python.

# Demo 

```python
import solver

# Create a Solver instance - by default it solves the sudoku upon instantiation
solver = solver.Solver(sudoku_array_goes_here)

# Prints a 'pretty' version of the solved sudoku
solver.print()
```

Check example.py

# Documentation

## Usage

The Solver class has the following methods: 
`.solve()`,`.print()`,`.returnAsArray()`.

When invoked `Solver.solve()` will attempt to solve the sudoku given.

When invoked `Solver.print()` will print out a sudoku grid.

When invoked `Solver.returnAsArray()` will return the sudoku as a 2D-array.

## Exceptions

* If the sudoku is unsolvable a `UnsolvableSudoku` exception is thrown. 
* If the sudoku is already solved a `SudokuSolved` exception is thrown.
* If the sudoku is of an invalid format a `InvalidSudoku` exception is thrown. 

