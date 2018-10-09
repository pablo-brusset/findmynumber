import math


# f(x) = 2 * x * pi
def calculer_circonference(rayon_cercle):
    circonference = rayon_cercle * 2 * math.pi

    return circonference


# f(x) = pi * x²
def calculer_aire(rayon_cercle):
    aire = math.pi * math.pow(rayon_cercle, 2)

    return aire


# f(x) = 4/3 * pi * x^3
def calculer_volume(rayon_cercle):
    volume = 4/3 * math.pi * math.pow(rayon_cercle, 3)

    return volume


print('Que voulez-vous calculer ?')
print('1. Circonférence')
print('2. Aire')
print('3. Volume')
choix = input()

donnee = int(input('Quel est le rayon ? (en cm)'))

if choix == '1':
    resultat = calculer_circonference(donnee)
    print('La circonférence est', resultat, 'cm.')
elif choix == '2':
    resultat = calculer_aire(donnee)
    print('L\'aire est', resultat, 'cm.')
elif choix == '3':
    resultat = calculer_volume(donnee)
    print('Le volume est', resultat, 'cm.')
