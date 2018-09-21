from random import randrange

recommencer = True

continuer = True

while recommencer:
    nombre_a_trouver = randrange(101)
    # On choisit un nombre entre 1 et 100 au hasard et on le met dans nombre_a_trouver.
    print('L\'ordinateur a choisi')

    trouve = False

    while not trouve:
        nombre_utilisateur = input('choisir un nombre ? ')
        # On récupère une chaine de caractères
        nombre_utilisateur = int(nombre_utilisateur)
        print('L\'utilisateur a choisi', nombre_utilisateur)

        if nombre_utilisateur < nombre_a_trouver:
            print('C\'est plus')
        elif nombre_utilisateur > nombre_a_trouver:
            print('C\'est moins')
        else:
            print('C\'est gagné, bravo !')
            trouve = True

    # On demande a l'utilisateur si il veut rejouer un partie.
    reponse = input('Recommencer ? o/N ')
    if reponse == 'o' or reponse == 'O' or reponse == 'y' or reponse == 'Y':
        recommencer = True
    else:
        recommencer = False
