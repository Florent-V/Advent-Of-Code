import sys
from itertools import combinations, permutations, combinations_with_replacement
import time
import re

def read_file(file):
    with open(file, "r") as f:
        return f.read().split("\n")

def format_data(lines):
    matrice = []
    for line in lines:
        if line:
            matrice.append(list(line))
    return matrice

def part_1(matrice):
    matrice = roll_O_To_North(matrice)
    print()
    for line in matrice:
        print(line)
    prod = 0
    for i in range(len(matrice)):
        nb_O = matrice[i].count('O')
        prod += nb_O * (len(matrice)-i)
    print('prod', prod)

def roll_O_To_North(matrice):
    for i in range(1, len(matrice)):
        for j in range(len(matrice[i])):
            if matrice[i][j] == 'O':
                #print('matrice[i][j]', i, j)
                new_line = i-1
                while new_line >= 0:
                    if matrice[new_line][j] == 'O' or matrice[new_line][j] == '#':
                        matrice[i][j] = '.'
                        matrice[new_line+1][j] = 'O'
                        new_line = -1
                    elif new_line == 0:
                        matrice[i][j] = '.'
                        matrice[0][j] = 'O'
                        new_line = -1
                    else:
                        new_line -= 1
    return matrice

def roll_O_To_South(matrice):
    for i in range(len(matrice)-1, -1, -1):
        for j in range(len(matrice[i])):
            if matrice[i][j] == 'O':
                #print('matrice[i][j]', i, j)
                new_line = i+1
                while new_line < len(matrice):
                    if matrice[new_line][j] == 'O' or matrice[new_line][j] == '#':
                        matrice[i][j] = '.'
                        matrice[new_line-1][j] = 'O'
                        new_line = len(matrice)
                    elif new_line == len(matrice)-1:
                        matrice[i][j] = '.'
                        matrice[len(matrice)-1][j] = 'O'
                        new_line = len(matrice)
                    else:
                        new_line += 1
    return matrice

def roll_O_To_East(matrice):
    for i in range(len(matrice)):
        for j in range(len(matrice[i])-1, -1, -1):
            if matrice[i][j] == 'O':
                #print('matrice[i][j]', i, j)
                new_line = j+1
                while new_line < len(matrice[i]):
                    if matrice[i][new_line] == 'O' or matrice[i][new_line] == '#':
                        matrice[i][j] = '.'
                        matrice[i][new_line-1] = 'O'
                        new_line = len(matrice[i])
                    elif new_line == len(matrice[i])-1:
                        matrice[i][j] = '.'
                        matrice[i][len(matrice[i])-1] = 'O'
                        new_line = len(matrice[i])
                    else:
                        new_line += 1
    return matrice

def roll_O_To_West(matrice):
    for i in range(len(matrice)):
        for j in range(len(matrice[i])):
            if matrice[i][j] == 'O':
                #print('matrice[i][j]', i, j)
                new_line = j-1
                while new_line >= 0:
                    if matrice[i][new_line] == 'O' or matrice[i][new_line] == '#':
                        matrice[i][j] = '.'
                        matrice[i][new_line+1] = 'O'
                        new_line = -1
                    elif new_line == 0:
                        matrice[i][j] = '.'
                        matrice[i][0] = 'O'
                        new_line = -1
                    else:
                        new_line -= 1
    return matrice

def part_2(matrice):
    list_prod=[]
    for i in range(1000):
        #print('Step', i+1)
        matrice = roll_O_To_North(matrice)
        matrice = roll_O_To_West(matrice)
        matrice = roll_O_To_South(matrice)
        matrice = roll_O_To_East(matrice)
        prod = 0
        for i in range(len(matrice)):
            nb_O = matrice[i].count('O')
            prod += nb_O * (len(matrice)-i)
        #print('prod', prod)
        list_prod.append(prod)
        # for line in matrice:
        #   print(''.join(line))
    print()
    #print(list_prod)
    for i in range(len(list_prod)):
      debut_periode = i  # Indice à partir duquel la périodicité commence
      motif_periodique = trouver_motif_periodique(list_prod, debut_periode)
      if motif_periodique:
        print('debut_periode', debut_periode)
        print('longueur_periodicite', len(motif_periodique))
        print("Motif Périodique:", motif_periodique)
        break

      


    
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

    if len(liste[debut_periode:debut_periode + longueur_periodicite]) != len(sous_liste):
        return liste[debut_periode:debut_periode + longueur_periodicite]
    return False

def main():
    now = time.time()
    lines = read_file(sys.argv[1]) if len(sys.argv) > 1 else read_file('input_light.txt')
    matrice = format_data(lines)
    for line in matrice:
        print(''.join(line))
    #part_1(matrice)
    part_2(matrice)


    print('script execution time', time.time() - now)
    

    



if __name__ == "__main__":
    main()
   