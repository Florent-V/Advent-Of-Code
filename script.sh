#!/bin/bash

# Assurez-vous que la variable SESSION_MONSITE_ID est définie
if [ -z "$AOC_ID" ]; then
  echo "La variable d'environnement SESSION_MONSITE_ID n'est pas définie"
  exit 1
fi

echo $AOC_ID

# Faites la requête cURL en utilisant la variable d'environnement
curl -X GET \
     -b "session=$AOC_ID" \
     https://adventofcode.com/2023/day/13/input
