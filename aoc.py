import os, argparse, importlib, subprocess, datetime, sys
from Utils.PuzzleHandler import PuzzleHandler
from Utils.FileHandler import FileHandler

def format_dir(path, year, day):
    day_padded = f"{int(day):02d}"
    return f"{path}/aoc_{year}/Day_{day_padded}"

def main():
    today = datetime.date.today()

    parser = argparse.ArgumentParser(
        prog="AOC_Runner",
        description="Advent of Code runner to init folder day, run script day, submit solution day",
        epilog="Enjoy the AOC challenge !")
    
    parser.add_argument('-y', '--year', choices=range(2015, today.year + 1), default=today.year, metavar='aoc_year_number',
                        type=int, required=False, help="Year of the AOC (for example, 2023). Required.")
    parser.add_argument('-d', '--day', choices=range(1, 25 + 1), default=today.day, metavar='aoc_day_number',
                        type=int, required=False, help="Day of the AOC (for example, 01). Required.")
    parser.add_argument('-sol', '--solve', choices=range(1, 2 + 1), metavar='part_to_solve',
                        type=int, required=False, help="Part of the puzzle to solve (1 or 2). Default is 1.")
    parser.add_argument('-exec', '--execute', metavar='function_to_execute', help='Function to execute in the solution file')
    parser.add_argument('-c', '--create', action='store_true', help='Create the folder for the day')
    parser.add_argument('-r', '--run', action='store_true', help='Run the script for the day')
    parser.add_argument('-s', '--submit', action='store_true', help='Submit the solution for the day')
    parser.add_argument('-f', '--force', action='store_true', help='Force overwrite the folder for the day')
    parser.add_argument('-a', '--all', action='store_true', help='Use the input.txt file instead of input_light.txt')
    

    args = parser.parse_args()
    print(args)
    print(args.execute)
    path = FileHandler.get_path()
    directory = format_dir(path, args.year, args.day)

    if args.create:
        print('#####################################################')
        print('Destination directory :', directory)
        if os.path.isdir(directory) and not args.force:
            raise FileExistsError(f"""The folder {directory} already exists. 
                                  Please use the -f option to force overwrite.
                                  Be careful, this will erase the existing folder.""")
        print(f"Downloading puzzle for day {args.day} of year {args.year}...")
        puzzle_handler = PuzzleHandler(args.year, args.day)
        puzzle, puzzle_light = puzzle_handler.download()
        print(f"Writing puzzle to {directory}...")
        FileHandler.write_file(directory, "input.txt", puzzle)
        FileHandler.write_file(directory, "input_light.txt", puzzle_light)
        FileHandler.copy_file("bootstrap.py", f"{directory}/solution.py")
        print("Folder created successfully. Enjoy the challenge !")

    elif args.execute:
        print('##########     EXECUTE     ##########')
        module_name = f"aoc_{args.year}.Day_{args.day:02d}.solution"
        try:
            sol = importlib.import_module(module_name).Solution(directory, args.day, args.year, args.all).run(args.execute)
        except ModuleNotFoundError:
            print(f"Impossible d'importer le module '{module_name}'")
            return
    
    elif args.solve:
        print('##########     SOLVE     ##########')
        module_name = f"aoc_{args.year}.Day_{args.day:02d}.solution"
        try:
            sol = importlib.import_module(module_name).Solution(directory, args.day, args.year, args.all)
        except ModuleNotFoundError:
            print(f"Impossible d'importer le module '{module_name}'")
            return
        sol.solve(args.solve)

    elif args.run:
        print('##########     RUN     ##########')
        module_name = f"aoc_{args.year}.Day_{args.day:02d}.solution"
        try:
            sol = importlib.import_module(module_name).Solution(directory, args.day, args.year, args.all)
        except ModuleNotFoundError:
            print(f"Impossible d'importer le module '{module_name}'")
            return
        sol.solve_both()


if __name__ == "__main__":
    main()
