import sys
import os
import time
# Get and add the Tools directory to sys.path
# current_dir = os.path.dirname(os.path.abspath(__file__))
# tools_dir = os.path.abspath(os.path.join(current_dir, '..', '..', 'Tools'))
# sys.path.append(tools_dir)
from Tools.PuzzleReader import PuzzleReader
from Tools.CalculateDuration import CalculateDuration


def get_file():
    file_name = sys.argv[1] if len(sys.argv) > 1 else 'input_light.txt'
    print(f"file_name: {file_name}")
    return PuzzleReader(file_name, os.path.dirname(os.path.abspath(__file__))).read_file()

def _get_sum(in_str):
    return int(in_str[0] + in_str[-1])


def _get_num(in_line):
    res = ""
    for _ in in_line:
        if _ in {"1", "2", "3", "4", "5", "6", "7", "8", "9", "0"}:
            res += _
    return _get_sum(res)

def _get_num_b(in_line):
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
    return _get_sum(res)


def part_1(lines):
    """returns the solution for part_a"""
    return sum(_get_num(_) for _ in lines)
  


def part_2(lines):
    """returns the solution for part_b"""
    return sum(_get_num_b(_) for _ in lines)



def main():
    lines = get_file()
    chrono = CalculateDuration()
    print(f"Résultat Partie 1: {part_1(lines)}")
    chrono.calculate()
    print(f"Durée d'exécution Partie 1: {chrono.duration:.2e} sec")
    chrono.start_time = time.time()
    print(f"Résultat Partie 2: {part_2(lines)}")
    chrono.calculate()
    print(f"Durée d'exécution Partie 2: {chrono.duration:.2e} sec")


if __name__ == "__main__":
    main()
