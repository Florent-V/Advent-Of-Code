import os

# Obtenir le chemin absolu du répertoire contenant le script
script_dir = os.path.dirname(os.path.abspath(__file__))

# Construire le chemin absolu vers le fichier input.txt
input_file_path = os.path.join(script_dir, "input_01.txt")

# Ouvrir et lire le fichier
with open(input_file_path) as f:
    lines = f.read().split("\n")

# Exemple d'utilisation
print(lines)