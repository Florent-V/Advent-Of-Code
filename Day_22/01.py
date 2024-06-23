def verifier_surface_disponible(matrice, point1, point2):
    # Extraire les coordonnées des deux points opposés du rectangle
    x1, y1 = point1
    x2, y2 = point2

    # Déterminer les coordonnées du rectangle
    debut_x = min(x1, x2)
    fin_x = max(x1, x2)
    debut_y = min(y1, y2)
    fin_y = max(y1, y2)

    # Vérifier si la surface du rectangle est disponible
    for x in range(debut_x, fin_x + 1):
        for y in range(debut_y, fin_y + 1):
            if matrice[y][x] == 1:
                return False  # La surface n'est pas disponible

    return True  # La surface est disponible

# Exemple d'utilisation
matrice = [
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 1, 1, 0],
    [0, 0, 1, 1, 0],
    [0, 0, 0, 0, 0]
]

point1 = (3, 4)
point2 = (7, 5)

surface_disponible = verifier_surface_disponible(matrice, point1, point2)

if surface_disponible:
    print("La surface du rectangle est disponible.")
else:
    print("La surface du rectangle n'est pas disponible.")
