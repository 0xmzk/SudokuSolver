import copy

import numpy as np
import numpy.typing as npt


class UnsolvableSudoku(Exception):
    def __str__(self):
        return "The sudoku cannot be solved."


class InvalidSudoku(Exception):
    def __str__(self):
        return "The sudoku format is invalid."


class SudokuSolved(Exception):
    def __str__(self):
        return "The sudoku format is already solved."


class Solver:
    def __init__(self, sudoku, auto_solve=True):
        """
        :param sudoku: The array of numbers from the sudoku puzzle.
        :param auto_solve: Decides whether to solve straight away or wait for solve()
        to be invoked.

        There are two acceptable formats for the sudoku parameter that the Solver
        works with (see below).

        A 2D-Array of 9x9 shape.

        A 1D-Array of 1x81 shape.
        """

        self.sudoku = self.__formatSudoku(copy.deepcopy(sudoku))
        if auto_solve:
            self.solve()

    def returnAs2DArray(self) -> npt.ArrayLike:
        """
        Returns sudoku as a 9x9 array
        :return:
        """
        return self.sudoku

    def print(self):
        """
        Pretty prints current sudoku.
        """
        s = "-" * 23 + "\n"
        for y in range(len(self.sudoku)):
            for x in range(len(self.sudoku[y])):
                s += str(self.sudoku[y][x]) + " "
                if x == 2 or x == 5:
                    s += " | "
                elif x == 8:
                    s += "\n"
            if y == 2 or y == 5 or y == 8:
                s += "-" * 23 + "\n"
        print(s)

    def solve(self):
        # Entry function into recursive solving algorithm
        if self.__isSolved():
            raise SudokuSolved
        self.__solve(self.sudoku)
        if not self.__isSolved():
            raise UnsolvableSudoku

    def __solve(self, sudoku):
        """
        :param sudoku:
        :return: True, sudoku is solved; False, sudoku is not solved.
        """
        if self.__isSolved():
            return True
        for y in range(0, 9):
            for x in range(0, 9):
                # 0, indicated an empty space.
                if sudoku[y][x] == 0:
                    for number_try in range(1, 10):
                        if self.__isValid(number_try, x, y):
                            sudoku[y][x] = number_try
                            if self.__solve(sudoku):
                                return True
                            sudoku[y][x] = 0
                    return False

    @staticmethod
    def __determineBox(x: int, y: int) -> []:
        """
        Function determines the box which given x, y positions lie.
        The function returns a 1D list.
        :param x: x cord
        :param y: y cord
        :return: 1D List, x-max cord at idx 0, y-max cord at idx 1
        """

        def determinePositionInArray(n: int):
            if n in [0, 1, 2]:
                return 1
            elif n in [3, 4, 5]:
                return 2
            elif n in [6, 7, 8]:
                return 3

        return [determinePositionInArray(x) * 3, determinePositionInArray(y) * 3]


    def __isValid(self, number, x, y):
        """
        Function checks whether given number make the sudoku valid.
        :param number:
        :param x: x-position in the sudoku (2D-array column index)
        :param y: y-position in the sudoku (2D-array row index)
        :return:
        """
        # Check if given number is already present in current row.
        if number in self.sudoku[y]:
            return False

        # Check if given number is already present in current column.
        for row in self.sudoku:
            if number == row[x]:
                return False

        # # Check if given number is present in 3x3 section (box) of sudoku
        box_x_y = self.__determineBox(x, y)

        # Iterate from y_max - 3 to y_max
        for y1 in range(box_x_y[1] - 3, box_x_y[1]):
            # Iterate from x_max -3 to x_max
            for x1 in range(box_x_y[0] - 3, box_x_y[0]):
                # Skip comparing the element to itself
                if (y1 == y) & (x1 == x):
                    continue
                if number == self.sudoku[y1][x1]:
                    return False

        return True

    def __isSolved(self):
        """
        Checks if current sudoku is solved.

        :return: True if solved, else False
        """
        for y in range(0, 9):
            for x in range(0, 9):
                if self.sudoku[y][x] == 0:
                    return False
        return True

    @staticmethod
    def format1Dto2DArray(array: npt.ArrayLike) -> npt.ArrayLike:
        """Reshapes a 1d array into a 2d array"""
        return np.reshape(array, (9, 9))

    def __formatSudoku(self, sudoku: list) -> npt.ArrayLike:
        """
        Function formats given sudoku (list) as a 2D (9x9) array that the program can work with
        :param sudoku: one of the two acceptable format types.
        :return: (9x9) numpy array
        """
        formatted_sudoku = np.array(sudoku)
        # Data type validation
        # Check if all elements are integers
        if not formatted_sudoku.dtype == int:
            raise InvalidSudoku
        # Data range validation
        if not ((formatted_sudoku >= 0) & (formatted_sudoku <= 9)).all():
            raise InvalidSudoku

        # Case 1, format type 2 (1x81 array)
        if len(formatted_sudoku) == 81:
            formatted_sudoku = self.format1Dto2DArray(sudoku)
        # Case 2, format type 1 (9x9 array)
        if not formatted_sudoku.shape == (9, 9):
            raise InvalidSudoku

        return formatted_sudoku
