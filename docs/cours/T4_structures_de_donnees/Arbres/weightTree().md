# <center><div class = "titre7">Fonction : weight_tree()</div></center>

<div class="para">Objectif principal</div>

Réaliser une fonction qui renvoie le poids d’un arbre, c’est-à-dire dans notre cas le poids étiqueté dans le sommet de l’arbre (qui est aussi la somme des poids étiquetés dans les feuilles).

<div class="para">Rendu / Evaluation</div>

La fonction, une fois achevée, servira de brique de base au programme de compression de Huffman que l’ensemble de la classe codera. Tout le monde compte sur vous !!!  
<span style="display: block; margin: 10px 0 0 0;">Votre fonction doit être fonctionnelle, optimale, et son codage doit respecter les bonnes pratiques de programmation telles que CamelCase, ou <a href="https://fr.wikipedia.org/wiki/Snake_case" target="_blank">Snake_case</a>.</span>
<span style="display: block; margin: 10px 0 0 0;">A l’issu, __votre groupe passera à l’oral au tableau__ afin d’expliquer concrètement le déroulement de l’exécution de votre fonction. Le vocabulaire employé, la perspicacité, et le niveau de compréhension seront des critères d’évaluation.</span>

__La durée de la prestation orale est fixée à 5 min.__ 

<div class="para">Cahier des charges de la fonction</div>

Fichier à compléter :  

```python
from binaryTree import Arbre as BT

def weight_tree(arbre):
    """
    Rôle: Donne le poids d'un arbre non vide : le poids de la racine, soit la somme des poids des feuilles.

    Parameters
    ----------
    arbre : Objet de la class Arbre importée via le module binaryTree

    Returns
    -------
    nombre entier si occurrences, float de 0 à 100 si %
    """

    pass

```

<div class="para">Commandes utiles / Aide</div>

Le module `binaryTree` qui se trouve [ici](fichiers/binaryTree.zip).

<div class="para">Tests</div>

```python
# ----------------------------
#       TEST
# ----------------------------

arbre1 = BT(("c", 2))         # Création d'un arbre binaire
arbre2 = BT(("d", 11.26))     # Création d'un arbre binaire

assert weight_tree(arbre1) == 2, "erreur"
assert weight_tree(arbre2) == 11.26, "erreur"

```