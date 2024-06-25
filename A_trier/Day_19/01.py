# Exemple d'utilisation de match (à partir de Python 3.10)
def evaluer_condition(objet, step):
    operateurs = ['<', '>']
    operateur = None
    for op in operateurs:
      if op in step:
          operateur = op
          break
    if not operateur:
        return step
    
    if ':' not in step:
        print('#####################WARNING#####################')
        return step

    splitted_step = step.split(':')

    condition = splitted_step[0].split(operateur)
    cle = condition[0]
    value = int(condition[1])
    
    match operateur:
        case '<':
            return objet.get(cle, 0) < value
        case '>':
            return objet.get(cle, 0) > value
        # case '<=':
        #     return objet.get(cle, 0) <= value
        # case '>=':
        #     return objet.get(cle, 0) >= value
        # case '==':
        #     return objet.get(cle, 0) == value
        # case '!=':
        #     return objet.get(cle, 0) != value
        case _:
            raise ValueError("Opérateur de comparaison non pris en charge.")

# Exemple d'utilisation
objet = {'a': 2005, 's': 1000}
step = 's<1351:px'

resultat = evaluer_condition(objet, step)
print(resultat)  # True