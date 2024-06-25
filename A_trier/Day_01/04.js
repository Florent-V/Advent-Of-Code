const fs = require('fs');

// Remplacez 'chemin/vers/votre/fichier.txt' par le chemin réel de votre fichier texte
const cheminFichier = 'input_01.txt';

let subStrings = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", 0, 1, 2, 3, 4, 5, 6, 7, 8, 9];
const dico = {
  one: 1,
  two: 2,
  three: 3,
  four: 4,
  five: 5,
  six: 6,
  seven:7,
  eight: 8,
  nine: 9
}
let regex = new RegExp(subStrings.join("|"), "g");

// Lecture du fichier
fs.readFile(cheminFichier, 'utf8', (err, data) => {
    if (err) {
        console.error('Erreur de lecture du fichier :', err);
        return;
    }

    // Séparation des lignes du fichier en un tableau
    const lignes = data.split('\n');

    let somme = 0;
    for (let i = 0; i < lignes.length; i++) {
        //console.log("ligne: ", lignes[i]);
        try {
          //console.log(lignes[i]);
          let matches = lignes[i].match(regex)
          console.log(matches);
          //console.log(matches[0]);
          //console.log(dico[matches[0]] ? dico[matches[0]] : matches[0])
          //afficher le dernier élément du tableau
          //console.log(matches[matches.length - 1]);
          //console.log(dico[matches[matches.length - 1]] ? dico[matches[matches.length - 1]] : matches[matches.length - 1])
          let firstDigit = dico[matches[0]] ? dico[matches[0]] : matches[0];
          console.log(firstDigit);
          let lastDigit = dico[matches[matches.length - 1]] ? dico[matches[matches.length - 1]] : matches[matches.length - 1];
          console.log(lastDigit);
          let number = parseInt(`${firstDigit}${lastDigit}`)
          console.log('number', number);
          somme += number;
        } catch (e) {
          console.log(e.message);
        }

    }
    console.log("somme chiffre: ", somme);

});

