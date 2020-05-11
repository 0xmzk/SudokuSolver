import copy


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
    def __init__(self, sudoku, autoSolve=True):
        '''
        :param sudoku: The array of numbers from the sudoku puzzle.
        :param autoSolve: Decides whether to solve straight away or wait for solve()
        to be invoked.

        There are two acceptable formats for the sudoku parameter that the Solver
        works with (see below).

        A 2D-Array that contains 9 rows which each contain 9 numbers. Each row corresponds
        to a row on the sudoku board and each number in the row corresponds to a
        number in the row on the sudoku board.

        A 1D-Array that contains 81 numbers. Every 9 numbers in the array correspond
        to a row of numbers on the sudoku board.
        '''
        self.sudoku = copy.deepcopy(sudoku)
        if autoSolve:
            self.solve()

    def returnAsArray(self):
        if self.__isValidFormat():
            return self.sudoku
        else:
            raise InvalidSudoku

    def print(self):
        if self.__isValidFormat():
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
        else:
            raise InvalidSudoku

    def solve(self):
        if self.__isValidFormat():
            if self.__isSolved():
                raise SudokuSolved
            self.__solve(self.sudoku)
            if not self.__isSolved():
                raise UnsolvableSudoku
            return True
        else:
            raise InvalidSudoku

    def __solve(self, sudoku):
        if self.__isSolved():
            return True
        for y in range(0, 9):
            for x in range(0, 9):
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
        if number in self.sudoku[y]:
            # does the number already exist in the current row?
            return False

        for row in self.sudoku:
            if number == row[x]:
                # does the number already exist in the current column?
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
