import numpy as np

# Votre matrice
matrice = [
    [2, 4, 1, 3, 4, 3, 2, 3, 1, 1, 3, 2, 3],
    [3, 2, 1, 5, 4, 5, 3, 5, 3, 5, 6, 2, 3],
    [3, 2, 5, 5, 2, 4, 5, 6, 5, 4, 2, 5, 4],
    [3, 4, 4, 6, 5, 8, 5, 8, 4, 5, 4, 5, 2],
    [4, 5, 4, 6, 6, 5, 7, 8, 6, 7, 5, 3, 6],
    [1, 4, 3, 8, 5, 9, 8, 7, 9, 8, 4, 5, 4],
    [4, 4, 5, 7, 8, 7, 6, 9, 8, 7, 7, 6, 6],
    [3, 6, 3, 7, 8, 7, 7, 9, 7, 9, 6, 5, 3],
    [4, 6, 5, 4, 9, 6, 7, 9, 8, 8, 8, 7, 0],
    [4, 5, 6, 4, 6, 7, 9, 9, 8, 6, 8, 7, 3],
    [1, 2, 2, 4, 6, 8, 6, 8, 6, 5, 5, 6, 3],
    [2, 5, 4, 6, 5, 4, 8, 8, 8, 7, 7, 3, 5],
    [4, 3, 2, 2, 6, 7, 4, 6, 5, 5, 3, 3, 3]
]

# Convertir en numpy array pour faciliter les opérations
matrice = np.array(matrice)
print('matrice', matrice)

# Initialiser la matrice des coûts avec des infinis
couts = np.full(matrice.shape, np.inf)

# Le coût de départ est la valeur de départ
couts[0, 0] = matrice[0, 0]

# Les directions possibles : droite, bas
directions = [(0, 1), (1, 0),(-1,0),(0,-1)]
print(matrice.shape[0])
print(couts)

# Parcourir la matrice
for i in range(matrice.shape[0]):
    for j in range(matrice.shape[1]):
        # Parcourir toutes les directions possibles
        for direction in directions:
            di, dj = direction
            ni, nj = i - di, j - dj
            # Vérifier si la nouvelle position est dans la matrice
            if 0 <= ni < matrice.shape[0] and 0 <= nj < matrice.shape[1]:
                # Mettre à jour le coût si le nouveau coût est inférieur
                couts[i, j] = min(couts[i, j], couts[ni, nj] + matrice[i, j])

# Le coût minimum pour atteindre le coin inférieur droit est dans le coin inférieur droit de la matrice des coûts
cout_min = couts[-1, -1]
print('couts', couts)

print("Le coût minimum pour atteindre le coin inférieur droit est :", cout_min)
