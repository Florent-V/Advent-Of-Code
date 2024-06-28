import sys
import time
from Utils.CalculateDuration import CalculateDuration
from itertools import combinations, permutations, combinations_with_replacement
import re


def read_file(file):
    with open(file, "r") as f:
        return f.read().split("\n")


def part_1():
    pass


def part_2():
    pass


def main():
    chrono = CalculateDuration()
    part_1()
    # lines = read_file(sys.argv[1]) if len(sys.argv) > 1 else read_file('input_light.txt')
    chrono.calculate()
    chrono.start_time = time.time()
    part_2()
    chrono.calculate()


if __name__ == "__main__":
    main()
