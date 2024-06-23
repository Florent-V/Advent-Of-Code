import sys
import math

steps = ['seed-to-soil', 'soil-to-fertilizer', 'fertilizer-to-water', 'water-to-light', 'light-to-temperature', 'temperature-to-humidity', 'humidity-to-location']

def read_file(file):
    # Dictionnaire pour stocker les lignes de chaque partie
    sections = {}
    seeds = []
    # Initialiser la variable nom_partie
    nom_partie = None
    # Lire le fichier ligne par ligne
    with open(file, 'r') as fichier:
        for ligne in fichier:
            
            # Supprimer les espaces inutiles en début et fin de ligne
            ligne = ligne.strip()
            if ligne.startswith('seeds:'):
                seeds = [int(chiffre) for chiffre in ligne.replace('seeds:', '').split()]
            # Vérifier si la ligne est une nouvelle partie
            elif ligne.endswith(' map:'):
                # Nouvelle partie détectée
                nom_partie = ligne.replace(' map:', '')
                sections[nom_partie] = []
            elif nom_partie is not None and ligne != '':
                # Ajouter la ligne à la partie courante
                sections[nom_partie].append([int(chiffre) for chiffre in ligne.split()])
    return seeds, sections

def sort_section(sections):
    for section in sections:
        sections[section].sort(key=lambda x: x[1])
    return sections

def find_correspondance(number, section):
    #print(f'number: {number}, section: {section} ')
    for elt in section:
        if (number >= elt[1]) and (number < (elt[1] + elt[2])):
            return number + (elt[0]-elt[1])
    return number

def calculate_location(seed, sections):
    steps = ['seed-to-soil', 'soil-to-fertilizer', 'fertilizer-to-water', 'water-to-light', 'light-to-temperature', 'temperature-to-humidity', 'humidity-to-location']
    for step in steps:
        #print(f'{step}: {seed}')
        seed = find_correspondance(seed, sections[step])
        #print(f'correspondance: {seed}')
    #print(f'Location: {seed}')
    return seed

    

def main():
    seeds, sections = read_file(sys.argv[1]) if len(sys.argv) > 1 else read_file('input_light.txt')
    #print(seeds)
    #print(sections)
    sections = sort_section(sections)
    for section in sections:
        print(section)
        for elt in sections[section]:
            print(elt)
    print(sections)
    #print('Sorted')
    # for section in sections:
    #     print(section)
    #     for elt in sections[section]:
    #         print(elt)
    #shortest_location = math.inf
    # for seed in seeds:
    #     #print(f'Seed: {seed}')
    #     location = calculate_location(seed, sections)
    #     if location < shortest_location:
    #         shortest_location = location
    # print('shortest_location_1', shortest_location)
    # shortest_location = math.inf
    # for i in range(0, len(seeds), 2):
    #     for j in range(seeds[i],seeds[i]+seeds[i+1]):
    #         location = calculate_location(j, sections)
    #         print(f'Seed: {j}, location: {location}')
    #         if location < shortest_location:
    #             shortest_location = location
    # print('shortest_location_2', shortest_location)


    
    


    



if __name__ == "__main__":
    main()
   