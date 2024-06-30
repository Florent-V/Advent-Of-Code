from Libs.SolutionBase import SolutionBase

class Solution(SolutionBase):
  
  def _get_sum(self, in_str):
      return int(in_str[0] + in_str[-1])


  def _get_num(self, in_line):
      res = ""
      for _ in in_line:
          if _ in {"1", "2", "3", "4", "5", "6", "7", "8", "9", "0"}:
              res += _
      return self._get_sum(res)

  def _get_num_b(self, in_line):
      nums = {
          "1": "1",
          "2": "2",
          "3": "3",
          "4": "4",
          "5": "5",
          "6": "6",
          "7": "7",
          "8": "8",
          "9": "9",
          "one": "1",
          "two": "2",
          "three": "3",
          "four": "4",
          "five": "5",
          "six": "6",
          "seven": "7",
          "eight": "8",
          "nine": "9",
      }
      res = ""
      for cur_pos in range(len(in_line)):
          for _k, _v in nums.items():
              if in_line[cur_pos:].startswith(_k):
                  res += nums[_v]
                  break
      return self._get_sum(res)


  def part_1(self, lines):
      """returns the solution for part_a"""
      return sum(self._get_num(_) for _ in lines)
    

  def part_2(self, lines):
      """returns the solution for part_b"""
      return sum(self._get_num_b(_) for _ in lines)
