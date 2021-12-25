import os
import solver

# Puzzles were taken from:
# http://lipas.uwasa.fi/~timan/sudoku/

# Directories
SOLUTIONS_DIR = os.getcwd() + "\\puzzles\\solutions"
SUDOKUS_DIR = os.getcwd() + "\\puzzles\\sudokus"
PUZZLES = os.listdir(SUDOKUS_DIR)

# Counters
FAILED_COUNT = 0
PASSED_COUNT = 0
NO_OF_TESTS = len(PUZZLES)

for i in range(NO_OF_TESTS):
    file = PUZZLES[i]
    # Read sudoku puzzle file
    sudoku_file = open(f"{SUDOKUS_DIR}\\{file}", 'r')
    sudoku_puzzle = sudoku_file.read()
    sudoku_file.close()
    # Do some processing
    sudoku_puzzle = sudoku_puzzle.split("\n")
    sudoku_puzzle = sudoku_puzzle[:9]
    sudoku_puzzle = "".join(sudoku_puzzle)
    sudoku_puzzle = sudoku_puzzle.rstrip()
    sudoku_puzzle = sudoku_puzzle.replace(" ", "")
    sudoku_puzzle = [int(i) for i in sudoku_puzzle]
    # Solve the puzzle
    output = solver.Solver(sudoku_puzzle)
    output = output.returnAs2DArray()
    # Read sudoku solution file
    solution_file = open(f"{SOLUTIONS_DIR}\\{file.split('.')[0]}_s.txt", 'r')
    expected_output = solution_file.read()
    solution_file.close()
    # Do some more processing
    expected_output = expected_output.split("\n")[:11]
    del (expected_output[3])
    del (expected_output[6])
    expected_output = [i.split("=")[0] for i in expected_output]
    expected_output = [i.replace("|", "") for i in expected_output]
    expected_output = [i.replace(" ", "") for i in expected_output]
    expected_output = "".join(expected_output)
    expected_output = [int(i) for i in expected_output]
    expected_output = solver.Solver.format1Dto2DArray(expected_output)
    # Compare expected output with actual output
    comparison = (expected_output == output).all()
    if comparison:
        PASSED_COUNT += 1
    else:
        FAILED_COUNT += 1
    print(f"Test {i + 1}/{NO_OF_TESTS} | Puzzle: {file} -> {'Passed' if comparison else 'Failed'}")

print(f"\nDONE\nNSummary:\nPassed:{PASSED_COUNT}/{NO_OF_TESTS}\nFailed:{FAILED_COUNT}/{NO_OF_TESTS}")
