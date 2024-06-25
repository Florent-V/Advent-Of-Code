import sys
import time
import heapq

def read_file(file):
    with open(file, "r") as f:
        return f.read().split("\n")

#def format_data(lines):
    
def heuristic(a, b):
    # Heuristique pour l'algorithme A* (distance de Manhattan)
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def find_path(matrix):
    start = (0, 1)  # Position de départ (coin supérieur gauche)
    end = (11, 13)  # Position de fin (coin inférieur droit)

    # Directions possibles : haut, bas, gauche, droite
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    # Fonction de coût entre deux positions voisines
    def cost(current, next):
        return int(matrix[next[0]][next[1]])

    # Initialisation de la file de priorité pour l'algorithme A*
    heap = [(0, start)]
    heapq.heapify(heap)

    # Initialisation du dictionnaire de coût
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

    return cost_so_far[end]

# Votre matrice
matrix = [
    "X413432311323",
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

def part_1(matrice):
#def part_2(matrice):

def main():
    now = time.time()
    lines = read_file(sys.argv[1]) if len(sys.argv) > 1 else read_file('input_light.txt')


    print('script execution time', time.time() - now)
    

    



if __name__ == "__main__":
    main()
   