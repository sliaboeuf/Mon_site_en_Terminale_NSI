# <center><div class = "titre3_bis">Correction de l'exercice</div> </center>

```python
import random

class Domino :

    def __init__(self, ptg, ptd):
        """ Constructeur """
        self.__coteGauche = ptg
        self.__coteDroit = ptd

    def AfficherDomino(self):
        """ Affiche les 2 faces d'un domino """
        affichageGauche = self.__coteGauche
        affichageDroit = self.__coteDroit
        if self.__coteGauche == 0:
            affichageGauche = " "

        if self.__coteDroit == 0:
            affichageDroit = " "

        if self.EstDouble():
            print("−−−−−")
            print("⎢",affichageGauche,"⎥")
            print("−−−−−")
            print("⎢",affichageDroit,"⎥")
            print("−−−−−")
        else :
            print("−−−−−−−−−")
            print("⎢",affichageGauche,"⎥",affichageDroit,"⎥")
            print("−−−−−−−−−")

    def NbPoints(self):
        """ Retourne la somme des points présents sur les deux côtés"""
        return self.__coteGauche + self.__coteDroit

    def EstBlanc (self):
        """ Teste si le domino possède un blanc """
        return (self.__coteGauche == 0 or self.__coteDroit == 0)

    def EstDouble(self):
        """ Teste si le domino est double """
        return self.__coteGauche == self.__coteDroit

class JeuDeDomino :

    def __CreerJeu(self):
        """ Pour créer un jeu de 28 pièces toutes différentes """
        jeu = []
        for i in range (7):
            for j in range (i+1):
                jeu.append(Domino(i,j))
        return jeu

    def __init__(self):
        """ Constructeur """
        self.__jeu = self.__CreerJeu()
        self.__nbPieces = 28
        self.__jeuJoueur = []

    def Melanger(self):
        """ Melange aléatoirement le jeu de dominos """
        random.shuffle(self.__jeu)

    def AfficherJeu(self):
        """ Affiche toutes les pièces du jeu ou la pioche s'il y a eu distribution """
        for elt in self.__jeu :
            elt.AfficherDomino()

    def AfficherJeuJoueur(self):
        """ Affiche toutes les pièces distribuées au joueur en cours ainsi que ses points """
        nbDominosBlancs = 0
        nbDominosDoubles = 0
        nbPoints = 0
        for elt in self.__jeuJoueur :
            elt.AfficherDomino()
            nbPoints += elt.NbPoints()
            if elt.EstBlanc() :
                nbDominosBlancs += 1
            if elt.EstDouble() :
                nbDominosDoubles += 1
        print(nbPoints,"points possibles dont :",nbDominosBlancs," blancs et",nbDominosDoubles,"doubles")
        print("-----------------------------------")

    def Distribuer(self, nbJoueur):
        """ Extrait des dominos du jeu pour un joueur et retourne une liste de 6 ou 7 dominos """
        self.__jeuJoueur = []
        if nbJoueur == 2 :
            nbDomino = 7
        else :
            nbDomino = 6
        for i in range (nbDomino):
            dom = self.__jeu.pop(0)
            self.__jeuJoueur.append(dom)
            self.__nbPieces -=1
        return self.__jeuJoueur
      
monjeu = JeuDeDomino()
monjeu.Melanger()

monjeu.Distribuer(2)
monjeu.AfficherJeuJoueur()


monjeu.Distribuer(2)
monjeu.AfficherJeuJoueur()

monjeu.AfficherJeu()
``` 