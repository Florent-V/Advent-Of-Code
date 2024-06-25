points = [
    (0, 0), (0, 1), (0, 2), (0, 3), (0, 4), (0, 5),
    (0, 6), (1, 6), (2, 6), (3, 6), (4, 6), (5, 6),
    (5, 5), (5, 4), (6, 4), (7, 4), (7, 5), (7, 6),
    (8, 6), (9, 6), (9, 5), (9, 4), (9, 3), (9, 2),
    (9, 1), (8, 1), (7, 1), (7, 0), (6, 0), (5, 0),
    (5, 1), (5, 2), (4, 2), (3, 2), (2, 2), (2, 1),
    (2, 0), (1, 0), (0, 0)
]

# Utiliser un dictionnaire pour compter le nombre d'occurrences de chaque point
point_counts = {}
for point in points:
    point_counts[point] = point_counts.get(point, 0) + 1

# Filtrer les points qui n'apparaissent qu'une seule fois (les sommets)
vertices = [point for point, count in point_counts.items() if count == 1]

print(vertices)
