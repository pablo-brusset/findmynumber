from random import randrange

continuer = True

recommencer = True
while recommencer:

    nombre_a_trouver = randrange(101)
    # On choisit un nombre entre 1 et 100 au hasard et on le met dans nombre_a_trouver.
    print('L\'ordinateur à choisi')

    trouve = False
    while not trouve:

        nombre_utilisateur = -1
        while nombre_utilisateur < 0:

            nombre_utilisateur = input('Choisir un nombre ? ')

            print('L\'utilisateur a choisi', nombre_utilisateur)
            try:
                nombre_utilisateur = int(nombre_utilisateur)
            except ValueError:
                nombre_utilisateur = -1

            if nombre_utilisateur < 0:
                print('Erreur, choisir un nouveau nombre supérieur à 0')

        if nombre_utilisateur < nombre_a_trouver:
            print('C\'est plus')
        elif nombre_utilisateur > nombre_a_trouver:
            print('C\'est moins')
        else:
            print('C\'est gagné, bravo !')
            trouve = True

    reponse = input('Recommencer ? o/N ')
    # On demande a l'utilisateur si il veut rejouer un partie.
    if reponse == 'o' or reponse == 'O' or reponse == 'y' or reponse == 'Y':
        recommencer = True
    else:
        recommencer = False
