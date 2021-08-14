matrix = [
    [1, 0, 0, 0, 0, 0],
    [0, 1, 0, 1, 1, 1],
    [0, 0, 1, 0, 1, 0],
    [1, 1, 0, 0, 1, 0],
    [1, 0, 1, 1, 0, 0],
    [1, 0, 0, 0, 0, 1]
]


def superalgo(x, y, matrix):
    matrix[x][y] = 2
    for pos in {"x", "y"}:
        for rng in {-1, 1}:
            if pos == "x" and 0 <= x + rng < len(matrix):
                if matrix[x + rng][y] == 1:
                    matrix = superalgo(x + rng, y, matrix)
            elif pos == "y" and 0 <= y + rng < len(matrix[1]):
                if matrix[x][y + rng] == 1:
                    matrix = superalgo(x, y + rng, matrix)
    return matrix


def rmisland(matrix):
    for x in range(len(matrix)):
        for y in range(len(matrix[x])):
            if x == 0 or x == len(matrix) - 1 or y == 0 or y == len(matrix[x]) - 1:
                if matrix[x][y] == 1:
                    matrix = superalgo(x, y, matrix)

    for x in range(len(matrix)):
        for y in range(len(matrix[x])):
            if matrix[x][y] == 1:
                matrix[x][y] = 0
            if matrix[x][y] == 2:
                matrix[x][y] = 1

    return matrix


matrix = rmisland(matrix)
for x in matrix:
    print(x)
