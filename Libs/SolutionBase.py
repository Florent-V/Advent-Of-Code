from abc import ABC, abstractmethod
from Utils.FileHandler import FileHandler as File
from Utils.CalculateDuration import CalculateDuration

class SolutionBase(ABC):
    
    def __init__(self, directory, day=1, year=2023, all=False):
        self.directory = directory
        self.day = day
        self.year = year
        self.input_file = "input.txt" if all else "input_light.txt"
        self.content = self.get_input()
        self.lines = self.get_input_lines()

    def get_input(self):
        content = File.read_file(self.directory, self.input_file)
        self.content = content
        return content
    
    def get_input_lines(self):
        return self.content.split("\n")
    
    def run(self, func):
        if func in ["part_1", "part_2, solve, solve_both"]:
            print(f"Running this {func} is not allowed. Please use the --solve argument instead.")
            return
        function_to_call = getattr(self, func)
        function_to_call()
    
    def solve(self, part_number):
        func = getattr(self, f"part_{part_number}")
        chrono = CalculateDuration()
        print(f"Résultat Partie {part_number}: {func(self.lines)}")
        duration = chrono.calculate()
        print(f"Durée d'exécution Partie {part_number}: {self.format_duration(duration)}")
    
    def format_duration(self, duration):
        units = ["s", "ms", "µs", "ns"]
        i = 0
        while duration < 1 and i < len(units):
            duration *= 1000
            i += 1
        return f"{duration:.2e} {units[i]}"
    
    def solve_both(self):
      self.solve(1)
      self.solve(2)

    def main(self):
      print('Hello !')
      print(f"Les arguments de cette classe sont : {self.directory}, {self.day}, {self.year}, {self.input_file}, {self.content}")

    # @abstractmethod
    # def get_solution(self):
    #     pass



 