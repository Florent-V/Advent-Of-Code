import os
import requests

def get_session_id():
    session_id = os.getenv("AOC_ID")
    if not session_id:
        raise ValueError("La variable d'environnement SESSION_MONSITE_ID n'est pas définie")
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
          "https://adventofcode.com/2023/day/13/input"

    url = f"https://adventofcode.com/{year}/day/{day}/input"
    cookies = {'session': session_id}
    print(f"Téléchargement de l'input depuis {url}...")
    print(f"Session ID : {session_id}")
    response = requests.get(url, cookies=cookies)
    print(response)
    # if response.status_code != 200:
    #     print(f"Erreur lors de la requête : {response.status_code}")
    #     return

    directory = f"{year}/Day-{day_padded}"
    os.makedirs(directory, exist_ok=True)

    main_py_content = '''if __name__ == "__main__":
    part_01()
    part_02()
'''

    with open(f"{directory}/main.py", "w") as f:
        f.write(main_py_content)

    with open(f"{directory}/data.txt", "w") as f:
        f.write("coucou")

    print(f"Fichiers créés dans {directory}")

if __name__ == "__main__":
    main()
