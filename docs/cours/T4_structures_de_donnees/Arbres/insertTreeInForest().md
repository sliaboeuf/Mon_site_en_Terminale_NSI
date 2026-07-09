# <center><div class = "titre7">Fonction : insert_tree_in_forest()</div></center>

<div class="para">Objectif principal</div>

Réaliser une fonction qui insère un arbre binaire dans une forêt d’arbres binaire (qui est en fait une liste d’arbres). L’arbre est inséré à la première position qui maintient la forêt rangée en ordre décroissant.

<div class="para">Rendu / Evaluation</div>

La fonction, une fois achevée, servira de brique de base au programme de compression de Huffman que l’ensemble de la classe codera. Tout le monde compte sur vous !!!  
<span style="display: block; margin: 10px 0 0 0;">Votre fonction doit être fonctionnelle, optimale, et son codage doit respecter les bonnes pratiques de programmation telles que CamelCase, ou <a href="https://fr.wikipedia.org/wiki/Snake_case" target="_blank">Snake_case</a>.</span>
<span style="display: block; margin: 10px 0 0 0;">A l’issu, __votre groupe passera à l’oral au tableau__ afin d’expliquer concrètement le déroulement de l’exécution de votre fonction. Le vocabulaire employé, la perspicacité, et le niveau de compréhension seront des critères d’évaluation.</span>

__La durée de la prestation orale est fixée à 5 min.__ 

<div class="para">Cahier des charges de la fonction</div>

Fichier à compléter :  

```python
from binaryTree import Arbre as BT
from fct_weight_tree import weight_tree

def insert_tree_in_forest(arbre, foret):
    """
    Rôle: cette fonction insère un arbre supplémentaire dans la forêt de manière à ce que l'ordre de poids décroissant des arbres soit respecté.

    Parameters
    ----------
    arbre : Objet de la class Arbre importée via le module binaryTree
    foret: Une liste d'arbres

    Returns
    -------
    Une liste d'arbres dans lequel l'arbre a été inséré.
    """

    pass

```

<div class="para">Commandes utiles / Aide</div>

Méthode <a href= "https://docs.python.org/fr/3/tutorial/datastructures.html?highlight=insert" target="_blank">insert</a>.

<div class="para">Tests</div>

```python

# ----------------------------
#       TEST
# ----------------------------

def affiche_foret():
    for arbre in foret:
        print(arbre.cle(), end=' ')
    print()

foret=[]                                # Création d'une foret vide
foret.append(BT(("a", 3)))              # Ajoute à la foret un arbre binaire (sommet) avec le symbole et sa fréquence dans le texte
foret.append(BT(("b", 1)))              # Ajoute à la foret un arbre binaire (sommet) avec le symbole et sa fréquence dans le texte
arbre3 = BT(("c", 1))                   # Création d'un arbre binaire
arbre4 = BT(("d", 5))                   # Création d'un arbre binaire


affiche_foret()                          # Renvoie ('a', 3) ('b', 1)
insert_tree_in_forest(arbre3, foret)     # Appel de la fonction pour insérer l'arbre 3 dans la foret
affiche_foret()                          # Renvoie ('a', 3) ('b', 1) ('c', 1)
insert_tree_in_forest(arbre4, foret)     # Appel de la fonction pour insérer l'arbre 4 dans la foret
affiche_foret()                          # Renvoie ('d', 5) ('a', 3) ('b', 1) ('c', 1)

```