import sys
import os
import time
# Get and add the Tools directory to sys.path
current_dir = os.path.dirname(os.path.abspath(__file__))
tools_dir = os.path.abspath(os.path.join(current_dir, '..', '..', 'Tools'))
sys.path.append(tools_dir)
from PuzzleReader import PuzzleReader
from CalculateDuration import CalculateDuration


def get_file():
    file_name = sys.argv[1] if len(sys.argv) > 1 else 'input_light.txt'
    return PuzzleReader(file_name, os.path.dirname(os.path.abspath(__file__))).read_file()


def part_1():
    pass


def part_2():
    pass


def main():
    file = get_file()
    print(file)
    chrono = CalculateDuration()
    part_1()
    # lines = read_file(sys.argv[1]) if len(sys.argv) > 1 else read_file('input_light.txt')
    chrono.calculate()
    chrono.start_time = time.time()
    part_2()
    chrono.calculate()


if __name__ == "__main__":
    main()
