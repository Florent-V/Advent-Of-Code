import sys
import re
from string import punctuation

def read_file(file):
    with open(file, "r") as f:
        return f.read().split("\n")
    
def extraire_nombres(texte):
    nombres = re.findall(r'\d+', texte)
    return [nombre for nombre in nombres]




def main():
    lines = read_file(sys.argv[1]) if len(sys.argv) > 1 else read_file('input_light.txt')
    # Initialiser le dictionnaire de résultats
    print(lines)
    # Extraire les nombres de chaque ligne et stocker dans le dictionnaire
    for i, line in enumerate(lines):
        numbers = extraire_nombres(line)
        for number in numbers:
            x_1 = line.find(number)
            x_2 = x_1 + len(number)
            print(x_1, x_2)
    



if __name__ == "__main__":
    main()
   