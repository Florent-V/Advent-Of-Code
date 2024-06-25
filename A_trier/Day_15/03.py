# Votre dictionnaire initial
dico = {
    'cle1': {
        'label1': 'valeur1',
        'label2': 'valeur2'
    },
    'cle2': {
        'label1': 'valeur1',
        'label2': 'valeur2'
    }
}

# Les valeurs que vous recevez
nouvelle_cle = 'cle3'  # Imaginons que 'cle1' existe déjà
nouveau_label = 'label2'
nouvelle_valeur = 'nouvelle_valeur'

# Initialiser le dictionnaire principal et mettre à jour le label
dico.setdefault(nouvelle_cle, {})[nouveau_label] = nouvelle_valeur

# Afficher le résultat
print(dico)
