RIGHT = 0
LEFT = 1
DOWN = 2
UP = 3

deltas = [(1, 0), (-1, 0), (0, 1), (0, -1)]

splitters = {"|": {LEFT: [UP, DOWN], RIGHT: [UP, DOWN], UP: [UP], DOWN: [DOWN]},
             "-": {UP: [LEFT, RIGHT], DOWN: [LEFT, RIGHT], LEFT: [LEFT], RIGHT: [RIGHT]}}
mirrors = {"\\": {RIGHT: DOWN, LEFT: UP, DOWN: RIGHT, UP: LEFT},
           "/": {RIGHT: UP, LEFT: DOWN, DOWN: LEFT, UP: RIGHT}}


def parse(lines):
    grid = {}
    for y, line in enumerate(lines):
        for x, c in enumerate(line):
            grid[(x, y)] = c
    width = len(lines[0])
    height = len(lines)
    return grid, height, width


def count_max_visited(starting_positions, grid):
    max_visited = 0
    for starting_position in starting_positions:
        beams = [starting_position]
        visited_bitmasks = {k: 0 for k in grid.keys()}
        while beams:
            new_beams = []
            for (pos, delta) in beams:
                pos = (pos[0] + delta[0], pos[1] + delta[1])
                if pos in grid:
                    direction = deltas.index(delta)
                    visited_bitmask = visited_bitmasks[pos]
                    if visited_bitmask & (1 << direction) == 0:
                        visited_bitmasks[pos] = visited_bitmask | (1 << direction)
                        cell = grid[pos]
                        if cell == ".":
                            new_beams.append((pos, delta))
                        elif cell in mirrors:
                            delta = deltas[mirrors[cell][direction]]
                            new_beams.append((pos, delta))
                        elif cell in splitters:
                            new_dirs = splitters[cell][direction]
                            for new_dir in new_dirs:
                                new_beams.append((pos, deltas[new_dir]))
            beams = new_beams
        max_visited = max(max_visited, sum((1 for v in visited_bitmasks.values() if v > 0)))

    return max_visited


def part1(lines):
    grid, height, width = parse(lines)

    starting_positions = [((-1, 0), (1, 0))]
    return count_max_visited(starting_positions, grid)


def part2(lines):
    grid, height, width = parse(lines)

    starting_positions = []
    for x in range(width):
        starting_positions.append(((x, -1), deltas[DOWN]))
        starting_positions.append(((x, height), deltas[UP]))
    for y in range(height):
        starting_positions.append(((-1, y), deltas[RIGHT]))
        starting_positions.append(((width, y), deltas[LEFT]))

    return count_max_visited(starting_positions, grid)


if __name__ == "__main__":
    lines = open("input.txt", "r").read().strip().splitlines()
    print(part1(lines))
    print(part2(lines))