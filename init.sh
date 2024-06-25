#!/bin/bash

# Fonction pour vérifier si une entrée est un nombre valide pour l'année
is_valid_year() {
    [[ $1 =~ ^[0-9]+$ ]] && [ $1 -gt 0 ]
}

# Fonction pour vérifier si une entrée est un nombre valide pour le jour
is_valid_day() {
    [[ $1 =~ ^[0-9]+$ ]] && [ $1 -ge 1 ] && [ $1 -le 25 ]
}

# Demande à l'utilisateur d'entrer une année valide
while true; do
    read -p "Veuillez entrer une année : " year
    if is_valid_year $year; then
        break
    else
        echo "Année invalide. Veuillez réessayer."
    fi
done

# Demande à l'utilisateur d'entrer un jour valide
while true; do
    read -p "Veuillez entrer un jour (1-25) : " day
    if is_valid_day $day; then
        day_padded=$(printf "%02d" $day)
        break
    else
        echo "Jour invalide. Veuillez réessayer."
    fi
done

# Vérifie que la variable d'environnement AOC_ID est définie
if [ -z "$AOC_ID" ]; then
    echo "La variable d'environnement AOC_ID n'est pas définie"
    exit 1
fi

# URL de la requête
url="https://adventofcode.com/${year}/day/${day}/input"
cookies="session=$AOC_ID"

# Effectue la requête HTTP avec curl
response=$(curl -s -w "%{http_code}" -b "$cookies" "$url")
http_code=$(tail -n1 <<< "$response")
body=$(sed '$ d' <<< "$response")

# Vérifie le code de réponse HTTP
if [ "$http_code" -ne 200 ]; then
    echo "Erreur lors de la requête : $http_code"
    exit 1
fi

# Crée le répertoire pour stocker les fichiers
directory="${year}/Day-${day_padded}"
mkdir -p "$directory"

# Contenu du fichier main.py
main_py_content='if __name__ == "__main__":
    part_01()
    part_02()
'

# Écrit le fichier main.py
echo "$main_py_content" > "$directory/main.py"

# Écrit le fichier data.txt avec le contenu de la réponse
echo "$body" > "$directory/data.txt"

echo "Fichiers créés dans $directory"
