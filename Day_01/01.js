const fs = require('fs');

// Remplacez 'chemin/vers/votre/fichier.txt' par le chemin réel de votre fichier texte
const cheminFichier = 'input_01.txt';

// Lecture du fichier
fs.readFile(cheminFichier, 'utf8', (err, data) => {
    if (err) {
        console.error('Erreur de lecture du fichier :', err);
        return;
    }

    // Séparation des lignes du fichier en un tableau
    const lignes = data.split('\n');

    // Affichage du tableau
    //console.log('Tableau de lignes du fichier :', lignes);

    let somme = 0;
    for (let i = 0; i < lignes.length; i++) {
        //console.log("ligne: ", lignes[i]);
        try {
          let firstDigit = lignes[i].match(/\d/)[0];
          let lastDigit = lignes[i].match(/\d/g).pop();
          let digit = parseInt(`${firstDigit}${lastDigit}`)
          somme += digit;
        } catch (e) {
          console.log(somme);
        }

    }
    console.log("somme chiffre: ", somme);



});

