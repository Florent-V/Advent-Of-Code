"""
This module contains utility functions that are used in the project.
"""
import re
from itertools import product

def find_matches_with_positions(pattern, text):
  """
  Find all matches of a pattern in a text and return a list of tuples
  containing the matched text, start position and end position of each match.
  """
  matches = []
  for match in re.finditer(pattern, text):
      start_pos = match.start()
      end_pos = match.end()
      matched_text = match.group()
      matches.append((matched_text, start_pos, end_pos))
  return matches

def search_item_in_matrix_around(matrix, i, j, match_func):
  """
  Search for an item in the 2x2 matrix around the given position (i, j).
  Return the position of the match if found, otherwise return None.
  """
  for di, dj in product((-1, 0, 1), repeat=2):
    si = i + di
    sj = j + dj

    if 0 <= si < len(matrix) and 0 <= sj < len(matrix[si]) and match_func(matrix[si][sj]):
          return (si, sj)
    
def matrix_shape(matrix):
  """
  Return the shape of a matrix as a tuple (number of rows, number of columns).
  """
  return len(matrix), len(matrix[0])


def transpose_matrix(matrix):
  """
  Transpose a matrix.
  """
  return [''.join(i) for i in zip(*matrix)]