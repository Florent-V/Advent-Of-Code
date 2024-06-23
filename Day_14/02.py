ma_liste = [100865, 100609, 100323, 100128, 100011, 99944, 99932, 99894, 99898, 99867, 99777, 99712, 99599, 99512, 99441, 99354, 99300, 99259, 99219, 99170, 99143, 99108, 99096, 99049, 98987, 98936, 98869, 98780, 98671, 98591, 98518, 98439, 98370, 98291, 98222, 98173, 98096, 98029, 97957, 97883, 97805, 97713, 97618, 97541, 97491, 97428, 97349, 97275, 97204, 97129, 97058, 96984, 96908, 96841, 96759, 96687, 96612, 96531, 96451, 96403, 96329, 96263, 96215, 96148, 96114, 96087, 96062, 96068, 96071, 96067, 96057, 96054, 96048, 96050, 96054, 96058, 96063, 96071, 96075, 96082, 96082, 96070, 96066, 96062, 96066, 96068, 96072, 96087, 96093, 96112, 96133, 96146, 96162, 96165, 96153, 96141, 96124, 96105, 96094, 96097]

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

debut_periode = 4  # Indice à partir duquel la périodicité commence
for i in range(100):
    debut_periode = i  # Indice à partir duquel la périodicité commence
    motif_periodique = trouver_motif_periodique(ma_liste, debut_periode)
    print("Motif Périodique:", motif_periodique)
    

motif_periodique = trouver_motif_periodique(ma_liste, debut_periode)
print("Motif Périodique:", motif_periodique)