def trouver_chemins_possibles(chemins, depart, arrivee, chemin_actuel=None):
    if chemin_actuel is None:
        chemin_actuel = []

    chemins_possibles = []

    for sous_chemin in chemins:
        if sous_chemin['start'] == depart and sous_chemin['end'] not in chemin_actuel:
            nouveau_chemin = chemin_actuel + [sous_chemin['start'], sous_chemin['end']]
            nouveaux_chemins = trouver_chemins_possibles(chemins, sous_chemin['end'], arrivee, nouveau_chemin)
            chemins_possibles.extend(nouveaux_chemins)
        elif sous_chemin['end'] == depart and sous_chemin['start'] not in chemin_actuel:
            nouveau_chemin = chemin_actuel + [sous_chemin['end'], sous_chemin['start']]
            nouveaux_chemins = trouver_chemins_possibles(chemins, sous_chemin['start'], arrivee, nouveau_chemin)
            chemins_possibles.extend(nouveaux_chemins)

    if not chemin_actuel:  # Ajouter le chemin initial à la première itération
        chemins_possibles.append(chemin_actuel)

    # Filtrer les chemins qui atteignent l'arrivée
    chemins_possibles = [chemin for chemin in chemins_possibles if chemin[-1] == arrivee]

    return chemins_possibles

# Exemple d'utilisation :
# Exemple d'utilisation :
chemins_exemple = [
    {'start': (0, 1), 'end': (5, 3), 'step': 15},
    {'start': (3, 11), 'end': (13, 13), 'step': 24},
    {'start': (3, 11), 'end': (11, 21), 'step': 30},
    {'start': (3, 11), 'end': (5, 3), 'step': 22},
    {'start': (5, 3), 'end': (13, 5), 'step': 22},
    {'start': (11, 21), 'end': (19, 19), 'step': 10},
    {'start': (11, 21), 'end': (13, 13), 'step': 18},
    {'start': (13, 5), 'end': (19, 13), 'step': 38},
    {'start': (13, 5), 'end': (13, 13), 'step': 12},
    {'start': (13, 13), 'end': (19, 13), 'step': 10},
    {'start': (19, 13), 'end': (19, 19), 'step': 10},
    {'start': (19, 19), 'end': (22, 21), 'step': 5},
]

depart = (0, 1)
arrivee = (22, 21)

tous_les_chemins = trouver_chemins_possibles(chemins_exemple, depart, arrivee)

for chemin in tous_les_chemins:
    print(chemin)
