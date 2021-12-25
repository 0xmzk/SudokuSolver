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

        A 2D-Array that contains 9 rows which each contain 9 numbers. Each row corresponds
        to a row on the sudoku board and each number in the row corresponds to a
        number in the row on the sudoku board.

        A 1D-Array that contains 81 numbers. Every 9 numbers in the array correspond
        to a row of numbers on the sudoku board.
        """

        self.sudoku = self.__formatSudoku(copy.deepcopy(sudoku))
        if auto_solve:
            self.solve()

    def returnAs2DArray(self):
        return self.sudoku

    def print(self):
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
        if self.__isSolved():
            raise SudokuSolved
        self.__solve(self.sudoku)
        if not self.__isSolved():
            raise UnsolvableSudoku
        return True

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
                    for numberTry in range(1, 10):
                        if self.__isValid(numberTry, x, y):
                            sudoku[y][x] = numberTry
                            if self.__solve(sudoku):
                                return True
                            sudoku[y][x] = 0
                    return False

    @staticmethod
    def __determineQuadrant(n):
        if 9 / (n + 1) >= 3:
            # first third of the array
            return 1
        elif 9 / (n + 1) >= 1.5:
            # second third of the array
            return 2
        else:
            # last third of the array
            return 3

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

        square_location = [self.__determineQuadrant(x) * 3, self.__determineQuadrant(y) * 3]
        for y in range(square_location[1] - 3, square_location[1]):
            for x in range(square_location[0] - 3, square_location[0]):
                if number == self.sudoku[y][x]:
                    return False

        return True

    def __isSolved(self):
        for y in range(0, 9):
            for x in range(0, 9):
                if self.sudoku[y][x] == 0:
                    return False
        return True

    @DeprecationWarning
    def __toMatrix(self):
        matrix = [
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0]
        ]
        for y in range(9):
            for x in range(9):
                matrix[y][x] = self.sudoku[0]
                del self.sudoku[0]
        self.sudoku = matrix

    @DeprecationWarning
    def __valueValidation(self, x):
        if type(x) != int:
            # check if value in cell is a int
            return False
        elif x > 9 or x < 0:
            # check if the value in the cell is between 0-9
            return False
        return True

    def _isValidFormatPlacement(self, number, x, y):
        if number == 0:
            return True

        if self.sudoku[y].count(number) > 1:
            return False

        count = 0
        for row in self.sudoku:
            if number == row[x]:
                count += 1
        if count > 1:
            return False

        count = 0
        square_location = [self.__determineQuadrant(x) * 3, self.__determineQuadrant(y) * 3]
        for y in range(square_location[1] - 3, square_location[1]):
            for x in range(square_location[0] - 3, square_location[0]):
                if number == self.sudoku[y][x]:
                    count += 1
        if count > 1:
            return False

        return True

    @staticmethod
    def __format1Dto2DArray(array: npt.ArrayLike) -> npt.ArrayLike:
        return np.reshape(array, (9, 9))

    def __formatSudoku(self, sudoku: list) -> npt.ArrayLike:
        """
        Function formats given sudoku (list) as a 2D (9x9) array that the program can work with
        :param sudoku: one of the two acceptable format types.
        :return:
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
            formatted_sudoku = self.__format1Dto2DArray(sudoku)
        # Case 2, format type 1 (9x9 array)
        if not formatted_sudoku.shape == (9, 9):
            raise InvalidSudoku

        return formatted_sudoku

    def __isValidFormat(self):
        if len(self.sudoku) == 81:
            # if length is 81 then it could be a 1d array of 81 numbers
            for number in self.sudoku:
                if not self.__valueValidation(number):
                    return False
            # if the 1d array passes all the checks then convert it into a 2d array
            self.__toMatrix()
        elif len(self.sudoku) == 9:
            # if length is 9 then it could be a 2d array of 9 rows containing 9 numbers each
            # check if it is a valid matrix
            for y in range(9):
                for x in range(9):
                    if not self.__valueValidation(self.sudoku[y][x]):
                        return False
                    if not self._isValidFormatPlacement(self.sudoku[y][x], x, y):
                        # check if the numbers already present abide by the rules
                        return False
        else:
            return False
        return True
