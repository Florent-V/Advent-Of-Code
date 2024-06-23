import sys
from itertools import combinations, permutations, combinations_with_replacement
import time
import re

def read_file(file):
    with open(file, "r") as f:
        return f.read().split("\n")

def format_data(lines):
    data = []
    for line in lines:
        data.append([[int(i) for i in x.split(',')] for x in line.split('~')])
    data.sort(key=lambda x: int(x[0][2]))
    return data

def create_3d_matrice(x, y, z):
    return [[[0 for _ in range(x+1)] for _ in range(y+1)] for _ in range(z+1)]

def set_brick(matrice, brique, value):
    debut_brique = [coor for coor in brique[0]]
    fin_brique = [coor for coor in brique[1]]

    for z in range(debut_brique[2], fin_brique[2] + 1):
        for y in range(debut_brique[1], fin_brique[1] + 1):
            for x in range(debut_brique[0], fin_brique[0] + 1):
                matrice[z][y][x] = value
    return matrice

def placer_briques_dans_matrice(coordonnees_briques):
    # Trouver les valeurs maximales de x, y et z parmi toutes les coordonnées
    max_x = max(int(coor[0]) for brique in coordonnees_briques for coor in brique)
    max_y = max(int(coor[1]) for brique in coordonnees_briques for coor in brique)
    max_z = max(int(coor[2]) for brique in coordonnees_briques for coor in brique)

    print(max_x, max_y, max_z)

    # Initialiser la matrice avec des zéros
    # matrice = []
    # for z in range(max_z+1):
    #     matrice2D = []
    #     for y in range(max_y+1):
    #         matrice2D.append([0 for _ in range(max_x+1)])
    #     matrice.append(matrice2D)
    # print('dimensions', len(matrice), len(matrice[0]), len(matrice[0][0]))

    matrice = create_3d_matrice(x=max_x, y=max_y, z=max_z)

    # Placer les briques dans la matrice
    for brique in coordonnees_briques:
        matrice = set_brick(matrice, brique, 1)
    # for plan in matrice:
    #   for line in plan:
    #       print(''.join(str(x) for x in line))
    #   print()
    return matrice


def verifier_surface_disponible(matrice, brique, z):
    # Extraire les coordonnées des deux points opposés du rectangle
    x1, y1, z1 = brique[0]
    x2, y2, z2 = brique[1]

    # print('z', z)
    if z < 1:
        return False

    # Vérifier si la surface du rectangle est disponible
    for x in range(x1, x2 + 1):
        for y in range(y1, y2 + 1):
            if matrice[z][y][x] != 0:
                # print('not free')
                return False  # La surface n'est pas disponible
    #print('free')
    return True  # La surface est disponible


def descendre_brique_dun_etage(matrice, brique):
    
    debut_brique = [coor for coor in brique[0]]

    if verifier_surface_disponible(matrice, brique, debut_brique[2] - 1):
        matrice = set_brick(matrice, brique, 0)
        brique[0][2] -= 1
        brique[1][2] -= 1
        matrice = set_brick(matrice, brique, 1)
        descendre_brique_dun_etage(matrice, brique)

    return matrice, brique

def test_safety(matrice, bricks):
    b = bricks.pop(0)
    matrice = set_brick(matrice, b, 0)
    for brick in bricks:
        if verifier_surface_disponible(matrice, brick, brick[0][2] - 1):
            print('not safe')
            matrice = set_brick(matrice, b, 1)
            return False
    print('safe')
    matrice = set_brick(matrice, b, 1)
    return True

    

#def part_1(matrice):
#def part_2(matrice):

def main():
    now = time.time()
    lines = read_file(sys.argv[1]) if len(sys.argv) > 1 else read_file('input_light.txt')
    bricks = format_data(lines)
    print(bricks)
    matrice = placer_briques_dans_matrice(bricks)
    for i in range(len(bricks)):
        matrice, bricks[i] = descendre_brique_dun_etage(matrice, bricks[i])
    # for plan in matrice:
    #   for line in plan:
    #       print(''.join(str(x) for x in line))
    #   print()
    print(bricks)
    nb = 0
    while len(bricks) > 0:
        nb += test_safety(matrice, bricks)
    print(nb)
        








    # delete_bricks = bricks.pop(0)
    # print(delete_bricks)
    # matrice = set_brick(matrice, delete_bricks, 0)
    # for b in bricks:
    #     print(verifier_surface_disponible(matrice, b, b[0][2] - 1))
    # matrice = set_brick(matrice, delete_bricks, 1)

    # delete_bricks = bricks.pop(0)
    # print(delete_bricks)
    # matrice = set_brick(matrice, delete_bricks, 0)
    # for b in bricks:
    #     print(verifier_surface_disponible(matrice, b, b[0][2] - 1))
    # matrice = set_brick(matrice, delete_bricks, 1)

  




    print('script execution time', time.time() - now)
    

    



if __name__ == "__main__":
    main()

