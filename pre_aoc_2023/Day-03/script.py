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


def part_1(lines):
    pass


def part_2(lines):
    pass


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
