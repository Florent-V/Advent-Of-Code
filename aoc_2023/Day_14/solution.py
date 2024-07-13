from Libs.SolutionBase import SolutionBase
from Libs.Parsers import parse_matrice_string_to_list
from itertools import count
from copy import deepcopy

class Solution(SolutionBase):

  def roll_O_To_North(self, matrice):
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
  
  def roll_O_To_South(self, matrice):
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

  def roll_O_To_East(self, matrice):
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

  def roll_O_To_West(self, matrice):
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
  
  def get_load(self, matrice):
    load = 0
    for i in range(len(matrice)):
        nb_O = matrice[i].count('O')
        load += nb_O * (len(matrice)-i)
    return load
  
  def part_1(self, lines):
    """returns the solution for part_a"""
    matrice = parse_matrice_string_to_list(lines)
    self.roll_O_To_North(matrice)
    return self.get_load(matrice)
    pass

  def part_2(self, lines):
    """returns the solution for part_b"""
    matrice = parse_matrice_string_to_list(lines)
    grids = [deepcopy(matrice)]
    for i in count(1):
      self.roll_O_To_North(matrice)
      self.roll_O_To_West(matrice)
      self.roll_O_To_South(matrice)
      self.roll_O_To_East(matrice)

      if matrice in grids:
          index = grids.index(matrice)
          k = (1000000000 - index) % (i - index) + index
          return self.get_load(grids[k])
      
      grids.append(deepcopy(matrice))


