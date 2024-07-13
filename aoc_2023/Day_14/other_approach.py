import sys
from itertools import count
import time

def read_file(file):
    with open(file, "r") as f:
        return f.read().split("\n")
    
def format_data(lines):
    matrice = []
    for line in lines:
        if line:
            matrice.append(list(line))
    return matrice

def matrix_shape(matrix):
  return len(matrix), len(matrix[0])

def roll(grid, H, W):
    target = dict(grid)
    for x in range(W):
        stop = 0
        for y in range(H):
            match grid[x, y]:
                case "#":
                    stop = y + 1
                case "O":
                    if y > stop:
                        target[x, y] = "."
                        target[x, stop] = "O"
                    stop += 1
    return target

def get_load(grid, H, W):
    load = 0
    for x in range(W):
        for y in range(H):
            if grid[x, y] == "O":
                load += H - y
    return load

def rotate(grid, H):
    return {(H - y - 1, x): c for (x, y), c in grid.items()}

def part_1(lines):
    H, W = matrix_shape(lines)
    grid = {(x, y): c for y, line in enumerate(lines) for x, c in enumerate(line)}
    grid = roll(grid, H, W)
    return get_load(grid, H, W)


def part_2(lines):
    H, W = matrix_shape(lines)
    grid = {(x, y): c for y, line in enumerate(lines) for x, c in enumerate(line)}
    states = [grid]
    for i in count(1):
        grid = roll(grid, H, W)  # north
        grid = rotate(grid, H)
        grid = roll(grid, W, H)  # west
        grid = rotate(grid, W)
        grid = roll(grid, H, W)  # south
        grid = rotate(grid, H)
        grid = roll(grid, W, H)  # east
        grid = rotate(grid, W)

        if grid in states:
            j = states.index(grid)  # loop found
            k = (1000000000 - j) % (i - j) + j
            return get_load(states[k], H, W)

        states.append(grid)


def main():
    now = time.time()
    lines = read_file(sys.argv[1]) if len(sys.argv) > 1 else read_file('input_light.txt')
    print('Result Partie 1 :', part_1(lines))
    print('Result Partie 2 :', part_2(lines))
    print('script execution time', time.time() - now)


if __name__ == "__main__":
    main()
   