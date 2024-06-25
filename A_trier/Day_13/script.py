import sys
from itertools import combinations, permutations, combinations_with_replacement
import time
import re

def read_file(file):
    with open(file, "r") as f:
        return f.read().split("\n")

def format_data(lines):
    matrice = []
    all_matrices = []
    for line in lines:
        if line:
            matrice.append(line)
        else:
            all_matrices.append(matrice)
            matrice = []
    all_matrices.append(matrice)
    return all_matrices

def find_horizontal_symetric(matrice):
    for i in range(len(matrice)-1):
        if matrice[i] == matrice[i+1]:
            #print('test symetric line', i)
            j=1
            isSymetric = True
            while i-j >= 0 and i+1+j < len(matrice):
                #print(f'symetric line{i-j}', matrice[i-j])
                #print(f'symetric line{i+1+j}', matrice[i+1+j])
                if matrice[i-j] != matrice[i+1+j]:
                    isSymetric = False
                    break
                j+=1
            if isSymetric:
                #print('symetric line', i)
                return i+1
    return False

def find_vertical_symetric(matrice):
    colonnes = zip(*matrice)
    transposee = [''.join(i) for i in colonnes]
    return find_horizontal_symetric(transposee)

def find_horizontal_symetric_2(matrice):
    liste = []
    for i in range(len(matrice)-1):
        if matrice[i] == matrice[i+1] or ont_une_seule_difference(matrice[i], matrice[i+1]):
            #print('test symetric line', i)
            nb_diff = 0
            if ont_une_seule_difference(matrice[i], matrice[i+1]):
                nb_diff += 1
                #print('une diff', nb_diff)
            j=1
            isSymetric = True
            while i-j >= 0 and i+1+j < len(matrice):
                #print(f'symetric line{i-j}', matrice[i-j])
                #print(f'symetric line{i+1+j}', matrice[i+1+j])
                if matrice[i-j] == matrice[i+1+j] or ont_une_seule_difference(matrice[i-j], matrice[i+1+j]):
                    if ont_une_seule_difference(matrice[i-j], matrice[i+1+j]):
                        nb_diff += 1
                        #print('plus une diff', nb_diff)
                    if nb_diff > 2:
                      isSymetric = False
                      break
                else:
                    isSymetric = False
                    break
                j+=1
            if isSymetric:
                #print('symetric line', i)
                liste.append(i+1)
    if len(liste) > 0:
        return liste
    return False

def find_vertical_symetric_2(matrice):
    # print('matrice')
    # for i in matrice:
    #     print(i)
    colonnes = zip(*matrice)
    transposee = [''.join(i) for i in colonnes]
    # print('transposee')
    # for i in transposee:
    #     print(i)
    return find_horizontal_symetric_2(transposee)


def ont_une_seule_difference(str1, str2):
    return sum(c1 != c2 for c1, c2 in zip(str1, str2)) == 1

def part_1(all_matrices):
    sum = 0
    liste = []
    for index, matrice in enumerate(all_matrices):
        V_sym = find_vertical_symetric(matrice)
        if V_sym:
            #print('V_sym', V_sym, 'index, ', index)
            liste.append((index, 'V', V_sym))
            sum += V_sym
        else:
            H_sym = find_horizontal_symetric(matrice)
            if H_sym:
                #print('H_sym', H_sym, 'index, ', index)
                liste.append((index, 'H', H_sym))
                sum += (H_sym)*100
            else:
                print('#######CAREFULL############## no sym in matrice number :', index)
    print('sum part 1', sum)
    print('Nombre de symétrie part 1:', len(liste))
    return liste

def part_2(all_matrices):
    liste = []
    for index, matrice in enumerate(all_matrices):
        temp = []
        H_sym = find_horizontal_symetric_2(matrice)
        #print('H_sym', H_sym)
        if H_sym:
            for sym in H_sym:
                #print('H_sym', sym, 'index, ', index)
                temp.append((index, 'H', sym))
        V_sym = find_vertical_symetric_2(matrice)
        #print('V_sym', V_sym)
        if V_sym:
            for sym in V_sym:
                #print('V_sym', sym, 'index, ', index)
                temp.append((index, 'V', sym))
        if len(temp) != 2:
            print('#######CAREFULL############## index', index, temp)
            return
        liste+=temp
    print('Nombre de symétrie part 2:', len(liste))
    return liste

def main():
    now = time.time()
    lines = read_file(sys.argv[1]) if len(sys.argv) > 1 else read_file('input_light.txt')
    #print('lines', lines)
    all_matrices = format_data(lines)
    print('number all_matrices', len(all_matrices))
    sym_part_1 = part_1(all_matrices)
    sym_part_2 = part_2(all_matrices)

    listefinale = []
    for i in sym_part_2:
        if i not in sym_part_1:
            listefinale.append(i)
    print(len(listefinale))
    sum = 0
    for elt in listefinale:
        if elt[1] == 'H':
            sum += elt[2]*100
        elif elt[1] == 'V':
            sum += elt[2]
    print(sum)
    

    # print(all_matrices[19])
    # for i in all_matrices[19]:
    #     print(i)
        
        
        #find_vertical_symetric(matrice)








    print('script execution time', time.time() - now)
    

    



if __name__ == "__main__":
    main()
   