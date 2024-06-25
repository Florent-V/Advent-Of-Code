import heapq

def heuristic(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def find_path(matrix):
    start = (0, 0)  # Position de départ (coin supérieur gauche)
    end = (12, 13)  # Position de fin (coin inférieur droit)

    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    def cost(current, next):
        return int(matrix[next[0]][next[1]])

    heap = [(0, start)]
    heapq.heapify(heap)

    cost_so_far = {start: 0}

    while heap:
        current_cost, current_pos = heapq.heappop(heap)

        if current_pos == end:
            break

        for dir in directions:
            next_pos = (current_pos[0] + dir[0], current_pos[1] + dir[1])

            if 0 <= next_pos[0] < len(matrix) and 0 <= next_pos[1] < len(matrix[0]):
                new_cost = cost_so_far[current_pos] + cost(current_pos, next_pos)

                if new_cost <= 3 and (next_pos not in cost_so_far or new_cost < cost_so_far[next_pos]):
                    cost_so_far[next_pos] = new_cost
                    priority = new_cost + heuristic(end, next_pos)
                    heapq.heappush(heap, (priority, next_pos))
    print(cost_so_far)
    return cost_so_far[end]

# Votre matrice
matrix = [
    "2413432311323",
    "3215453535623",
    "3255245654254",
    "3446585845452",
    "4546657867536",
    "1438598798454",
    "4457876987766",
    "3637877979653",
    "4654967986887",
    "4564679986453",
    "1224686865563",
    "2546548887735",
    "4322674655533"
]

result = find_path(matrix)
print(f"La somme minimale est : {result}")
