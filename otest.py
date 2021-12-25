from timeit import timeit

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


def approach_1(number=9, x=1):
    for row in example_sudoku:
        if number == row[x]:
            return False


def approach_2(number=9, x=1, s=example_sudoku):
    if number in [row[x] for row in s]:
        return False


a1 = timeit("approach_1(9,1)", number=1000, globals=globals())
print(a1)
a2 = timeit("approach_2(9,1, example_sudoku)", number=1000, globals=globals())
print(a2)

if a1 < a2:
    print("Approach 1 is faster")
else:
    print("Approach 2 is faster")

