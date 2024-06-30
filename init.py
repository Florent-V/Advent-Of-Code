import os
from Utils.Puzzle import ExtractPuzzle
from Utils.FileHandler import FileHandler


def get_session_id():
    session_id = os.getenv("AOC_ID")
    if not session_id:
        raise ValueError("La variable d'environnement AOC_ID n'est pas définie")
    return session_id


def get_valid_input(prompt, validation_fn):
    while True:
        value = input(prompt)
        if validation_fn(value):
            return value
        print("Entrée invalide. Veuillez réessayer.")


def is_valid_year(year):
    return year.isdigit() and int(year) > 0


def is_valid_day(day):
    return day.isdigit() and 1 <= int(day) <= 25


def main():
    session_id = get_session_id()
    year = get_valid_input("Veuillez entrer une année : ", is_valid_year)
    day = get_valid_input("Veuillez entrer un jour (1-25) : ", is_valid_day)
    day_padded = f"{int(day):02d}"
    directory = f"{year}/Day-{day_padded}"

    extract_puzzle = ExtractPuzzle(session_id, year, day)
    puzzle = extract_puzzle.download_puzzle()

    file_handler = FileHandler(directory, "input.txt", puzzle)
    file_handler.write_file()

    puzzle_light = extract_puzzle.download_puzzle_light()
    file_handler.reinitialise(directory, "input_light.txt", puzzle_light)
    file_handler.write_file()

    file_handler.copy_file("bootstrap.py", f"{directory}/script.py")

    return



if __name__ == "__main__":
    main()
