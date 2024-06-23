def fusionner_en_alternance(list1, list2):
    fusion = []
    min_len = min(len(list1), len(list2))

    for i in range(min_len):
        fusion.append(list1[i])
        fusion.append(list2[i])

    # Ajouter les éléments restants de la liste la plus longue
    fusion.extend(list1[min_len:])
    fusion.extend(list2[min_len:])

    return fusion

# Exemple d'utilisation
liste1 = [1, 2, 3, 4]
liste2 = ['a', 'b', 'c', 'd']

resultat = fusionner_en_alternance(liste1, liste2)
print(resultat)


def fusionner_en_alternance_variable(list1, list2):
    fusion = []

    for i in range(len(list1)):
        fusion.append(list1[i])
        if i < len(list2):
            fusion.append(list2[i])

    # Ajouter les éléments restants de la liste la plus longue
    # fusion.extend(list1[len(list2):])
    # fusion.extend(list2[len(list1):])

    return fusion

# Exemple d'utilisation
liste1 = [1, 2, 3, 4, 5]
liste2 = ['a', 'b', 'c', 'd']

resultat = fusionner_en_alternance_variable(liste1, liste2)
print(resultat)
