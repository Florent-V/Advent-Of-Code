def construire_table_prefixe(motif):
    m = len(motif)
    table_prefixe = [0] * m
    longueur_prefixe = 0

    for i in range(1, m):
        while longueur_prefixe > 0 and motif[i] != motif[longueur_prefixe]:
            longueur_prefixe = table_prefixe[longueur_prefixe - 1]

        if motif[i] == motif[longueur_prefixe]:
            longueur_prefixe += 1

        table_prefixe[i] = longueur_prefixe

    return table_prefixe

def trouver_motif_periodique(liste, debut_periode):
    sous_liste = liste[debut_periode:]
    table_prefixe = construire_table_prefixe(sous_liste)

    longueur_periodicite = len(sous_liste) - table_prefixe[-1]

    print(len(liste[debut_periode:debut_periode + longueur_periodicite]))
    print(len(sous_liste))

    return liste[debut_periode:debut_periode + longueur_periodicite]

# Exemple d'utilisation
ma_liste = [1, 2, 3, 1, 2, 3, 1, 2, 3, 4, 5, 3, 1, 2, 3, 4, 5, 3, 1, 2, 3, 4, 5, 3, 1, 2, 3, 4, 5, 3, 1, 2, 3, 4, 5]

debut_periode = 4  # Indice à partir duquel la périodicité commence

motif_periodique = trouver_motif_periodique(ma_liste, debut_periode)
print("Motif Périodique:", motif_periodique)
