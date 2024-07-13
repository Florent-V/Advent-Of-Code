from itertools import groupby

def parse_matrice_string_to_list(lines):
  """
  Parse a string representing a matrix to a list of lists.
  """
  return [list(line) for line in lines]

def parse_matrice_string_to_int_list(lines):
  """
  Parse a string representing a matrix to a list of lists.
  """
  return [[int(i) for i in line.split()] for line in lines]

def parse_matrice_string_to_list(lines):
  """
  Parse a string representing a matrix to a list of lists.
  """
  return [list(line) for line in lines]

def parse_block_matrice_string_to_list(lines):
  """
  Parse a string representing a block matrix to a list of lists.
  """
  return [list(group) for k, group in groupby(lines, key=bool) if k]