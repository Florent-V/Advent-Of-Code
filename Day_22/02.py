

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

def verifier_surface_disponible(matrice, brique, z):
    # Extraire les coordonnées des deux points opposés du rectangle
    x1, y1, z1 = brique[0]
    x2, y2, z2 = brique[1]

    print('z', z)
    if z < 1:
        return False

    # Vérifier si la surface du rectangle est disponible
    for x in range(x1, x2 + 1):
        for y in range(y1, y2 + 1):
            if matrice[z][y][x] != 0:
                print('not free')
                return False  # La surface n'est pas disponible
    print('free')
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

matrice = create_3d_matrice(7,7,7)

matrice[1][3][3] = 3

print(len(matrice), len(matrice[0]), len(matrice[0][0]))

brique = [[2, 2, 3], [4, 4, 5]]
brique2 = [[0, 0, 5], [1, 2, 6]]

# matrice = set_brick(matrice, brique, 1)
# matrice = set_brick(matrice, brique2, 2)
for plan in matrice:
    for line in plan:
        print(''.join(str(x) for x in line))
    print()

matrice, brique = descendre_brique_dun_etage(matrice, brique)
matrice, brique2 = descendre_brique_dun_etage(matrice, brique2)

print('brique1', brique)
print('brique2', brique2)

print(brique)
for plan in matrice:
    for line in plan:
        print(''.join(str(x) for x in line))
    print()

