from Libs.SolutionBase import SolutionBase
from Libs.Parsers import parse_block_matrice_string_to_list
from Libs.Utils import transpose_matrix

class Solution(SolutionBase):

  def find_horizontal_symetric_basic(self, matrice):
      for i in range(len(matrice)-1):
          if matrice[i] == matrice[i+1]:
              j=1
              while i-j >= 0 and i+1+j < len(matrice) and matrice[i-j] == matrice[i+1+j]:
                  j+=1
              if  i-j < 0 or i+1+j >= len(matrice):
                  return i+1
      return False
  
  def find_vertical_symetric(self, matrice, func, nb_diff=None):
      transposee = transpose_matrix(matrice)
      return func(transposee, nb_diff) if nb_diff else func(transposee)
  
  def count_differences(self, line1, line2):
    """Compare deux lignes et retourne le nombre de différences."""
    return sum(1 for a, b in zip(line1, line2) if a != b)
  

  def find_horizontal_symetric(self, matrice, diff_max=0):
      liste = []
      for i in range(len(matrice)-1):
          j=0
          nb_diff = 0
          while i-j >= 0 and i+1+j < len(matrice) and  nb_diff <= diff_max:
              nb_diff += self.count_differences(matrice[i-j], matrice[i+1+j])
              j+=1
          if  (i-j < 0 or i+1+j >= len(matrice)) and nb_diff <= diff_max:
              liste.append(i+1)
      return liste
  
  def part_1(self, lines):
    """returns the solution for part_a"""
    all_matrices = parse_block_matrice_string_to_list(lines)
    sum = 0
    for index, matrice in enumerate(all_matrices):
        V_sym = self.find_vertical_symetric(matrice, self.find_horizontal_symetric_basic)
        if V_sym:
            sum += V_sym
        else:
            H_sym = self.find_horizontal_symetric_basic(matrice)
            if H_sym:
                sum += (H_sym)*100
            else:
                print('#######CAREFULL############## no sym in matrice number :', index)
    return sum

  def part_2(self, lines):
    """returns the solution for part_b"""
    all_matrices = parse_block_matrice_string_to_list(lines)
    liste_sym_1, liste_sym_2 = [], []
    for index, matrice in enumerate(all_matrices):
        temp_1, temp_2 = [], []
        H_sym_1 = self.find_horizontal_symetric(matrice)
        temp_1 += [(index, 'H', sym) for sym in H_sym_1 if H_sym_1]

        H_sym_2 = self.find_horizontal_symetric(matrice, 1)
        temp_2 += [(index, 'H', sym) for sym in H_sym_2 if H_sym_2]

        V_sym_1 = self.find_vertical_symetric(matrice, self.find_horizontal_symetric)
        temp_1 += [(index, 'V', sym) for sym in V_sym_1 if V_sym_1]

        V_sym_2 = self.find_vertical_symetric(matrice, self.find_horizontal_symetric, 1)
        temp_2 += [(index, 'V', sym) for sym in V_sym_2 if V_sym_2]

        if len(temp_2) != 2:
            print('#######CAREFULL############## index', index, temp_2)
            return
        liste_sym_1 += temp_1
        liste_sym_2 += temp_2
    bilan = (set(liste_sym_2) - set(liste_sym_1))
    return sum([elt[2]*100 if elt[1] == 'H' else elt[2] for elt in bilan])
