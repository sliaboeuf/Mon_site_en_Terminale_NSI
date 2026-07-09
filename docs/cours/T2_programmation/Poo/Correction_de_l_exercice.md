# <center><div class = "titre2">Correction de l'exercice</div> </center>

```python
import random

class Domino:

    def __init__(self, ptg, ptd):
        """ Constructeur """
        self.__cote_gauche = ptg
        self.__cote_droit = ptd

    def afficher_domino(self):
        """ Affiche les 2 faces d'un domino """
        affichage_gauche = self.__cote_gauche
        affichage_droit = self.__cote_droit
        if self.__cote_gauche == 0:
            affichage_gauche = " "

        if self.__cote_droit == 0:
            affichage_droit = " "

        if self.est_double():
            print("−−−−−")
            print("⎢", affichage_gauche, "⎥")
            print("−−−−−")
            print("⎢", affichage_droit, "⎥")
            print("−−−−−")
        else :
            print("−−−−−−−−−")
            print("⎢", affichage_gauche, "⎥", affichage_droit,"⎥")
            print("−−−−−−−−−")

    def nb_points(self):
        """ Retourne la somme des points présents sur les deux côtés"""
        return self.__cote_gauche + self.__cote_droit

    def est_blanc (self):
        """ Teste si le domino possède un blanc """
        return (self.__cote_gauche == 0 or self.__cote_droit == 0)

    def est_double(self):
        """ Teste si le domino est double """
        return self.__cote_gauche == self.__cote_droit

class JeuDeDomino:

    def __creer_jeu(self):
        """ Pour créer un jeu de 28 pièces toutes différentes """
        jeu = []
        for i in range (7):
            for j in range (i+1):
                jeu.append(Domino(i, j))
        return jeu

    def __init__(self):
        """ Constructeur """
        self.__jeu = self.__creer_jeu()
        self.__nb_pieces = 28
        self.__jeu_joueur = []

    def melanger(self):
        """ Melange aléatoirement le jeu de dominos """
        random.shuffle(self.__jeu)

    def afficher_jeu(self):
        """ Affiche toutes les pièces du jeu ou la pioche s'il y a eu distribution """
        for elt in self.__jeu:
            elt.afficher_domino()

    def afficher_jeu_joueur(self):
        """ Affiche toutes les pièces distribuées au joueur en cours ainsi que ses points """
        nb_dominos_blancs = 0
        nb_dominos_doubles = 0
        nb_points = 0
        for elt in self.__jeu_joueur:
            elt.afficher_domino()
            nb_points += elt.nb_points()
            if elt.est_blanc():
                nb_dominos_blancs += 1
            if elt.est_double():
                nb_dominos_doubles += 1
        print(f"{nb_points} points possibles dont : {nb_dominos_blancs} blancs et {nb_dominos_doubles} doubles")
        print("-----------------------------------")

    def distribuer(self, nb_joueur):
        """ Extrait des dominos du jeu pour un joueur et retourne une liste de 6 ou 7 dominos """
        self.__jeu_joueur = []
        if nb_joueur == 2:
            nb_domino = 7
        else :
            nb_domino = 6
        for i in range (nb_domino):
            dom = self.__jeu.pop(0)
            self.__jeu_joueur.append(dom)
            self.__nb_pieces -= 1
        return self.__jeu_joueur
      
mon_jeu = JeuDeDomino()
mon_jeu.melanger()

mon_jeu.distribuer(2)
mon_jeu.afficher_jeu_joueur()

mon_jeu.distribuer(2)
mon_jeu.afficher_jeu_joueur()

mon_jeu.afficher_jeu_joueur()
```