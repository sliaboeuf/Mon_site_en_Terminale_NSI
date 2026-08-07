__title__='''Generer des reptiles aléatoires dans un csv'''
__date__='''2020/03/15'''
__doc__='''
titre:   {0}
date:    {1}

Ce module génère un nombre donné de reptiles aléatoires.

Les données des reptiles :

* la longueur du corps, notée "taille"
* la largeur de la gueule, notée "gueule"
* l'espèce (parmi "alligator" et "crocodile")

Les bornes sont fictives, pas le temps d'aller chercher de vraies données.

'''.format(__title__, __date__)

import csv
import random
from pprint import pprint


DIMENSION_ANIMAUX = {
    "crocodile": {
        "taille": (3.5, 5.8),
        "gueule": (0.25, 0.5)
    },
    "alligator": {
        "taille": (2, 4),
        "gueule": (0.15, 0.3)
    }
}

FICHIER = "crocos.csv"
CHAMPS = ["espece", "taille", "gueule"]


def tirer_mesure_hasard(espece, mesure):
    '''
    retourne une dimension aléatoire entre les bornes indiquées
    dans le dictionnaire DIMENSION_ANIMAUX

    @param espece: (str) crocodile ou alligator
    @param mesure: (str) taille ou gueule
    @return: (float) arrondi à  deux chiffres après la virgule, réparti
        uniformément dans l'intervalle formé par les bornes indiquées
    '''
    return round(random.uniform(*DIMENSION_ANIMAUX[espece][mesure]), 2)


def titer_espece_hasard():
    '''
    DOC À COMPLETER
    '''
    if random.random() < 0.5:
        espece = 'crocodile'
    else:
        espece = 'alligator'
    return espece


def creer_animal():
    '''
    Crée un animal au hasard. Une chance sur deux (random() < 0.5) que ce
    soit un crocodile ou un alligator

    @return: (dict) un animal. Le dictionnaire a trois champs :
        * espece: str
        * taille: float
        * gueuel: float
    '''
    espece = titer_espece_hasard()
    taille = tirer_mesure_hasard(espece, 'taille')
    gueule = tirer_mesure_hasard(espece, 'gueule')

    animal = {
        "taille": taille,
        "gueule": gueule,
        "espece": espece,
    }
    return animal


def creer_animaux(nombre=100):
    '''
    Crée une liste d'animaux tels que décrits dans creer_animal

    @param nombre: (int) le nombre d'animaux, par défaut : 100
    @return: (list of dict) la liste de tous les animaux
    '''
    animaux = []
    for _ in range(nombre):
        animaux.append(creer_animal())
    return animaux


def creer_csv(animaux, fichier=None):
    '''
    Enregistre une liste d'animaux dans un dictionnaire
    Chaque animal est présenté par un dictionnaire, on les enregistre
    dans le csv, une ligne chacun.

    @param animaux: (list of dict) chaque animal doit respecter les contraintes
    @SE. écrit dans le fichier "crocos.csv"
    '''
    if fichier is None:
        fichier = FICHIER
    with open(fichier, 'w', newline='') as csvfile:
        champs = ['taille', 'gueule', 'espece']
        csvwriter = csv.writer(csvfile, delimiter=',')
        csvwriter = csv.DictWriter(csvfile, fieldnames=champs)
        csvwriter.writeheader()
        for animal in animaux:
            csvwriter.writerow(animal)


def main():
    '''
    Fonction qui pilote le tout.
    '''
    animaux = creer_animaux(nombre=100)
    pprint(animaux)
    creer_csv(animaux)


if __name__ == '__main__':
    main()
