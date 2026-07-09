# <center><div class = "titre7">Fonction : decode()</div></center>

<div class="para">Objectif principal</div>

Réaliser une fonction qui à partir du texte compressé avec le dictionnaire d’encodage optimal d’Huffman (chaine de caractères composée de `#!python 0` et de `#!python 1`), reconstitue le texte source non compressé.

<div class="para">Rendu / Evaluation</div>

La fonction, une fois achevée, servira de brique de base au programme de compression de Huffman que l’ensemble de la classe codera. Tout le monde compte sur vous !!!
<span style="display: block; margin: 10px 0 0 0;">Votre fonction doit être fonctionnelle, optimale, et son codage doit respecter les bonnes pratiques de programmation telles que CamelCase, ou <a href="https://fr.wikipedia.org/wiki/Snake_case" target="_blank">Snake_case</a>.</span>
<span style="display: block; margin: 10px 0 0 0;">A l’issu, __votre groupe passera à l’oral au tableau__ afin d’expliquer concrètement le déroulement de l’exécution de votre fonction. Le vocabulaire employé, la perspicacité, et le niveau de compréhension seront des critères d’évaluation.</span> 

__La durée de la prestation orale est fixée à 5 min.__ 

<div class="para">Cahier des charges de la fonction</div>

Fichier à compléter :  

```python
from binaryTree import Arbre as BT
from fct_huffman_tree import huffman_tree
from fct_sequence_to_occurrences import sequence_to_occurrences


def decode(encoded_source, tree):
    """
    Rôle: Décode la suite codée de 0 et 1 et obtient le texte

    Parameters
    ----------
    encoded_source: (str) la chaîne binaire à décoder
    tree: (arbre) l'arbre de Huffman du codage utilisé

    Returns
    -------
    (str) le message source décodé

    """

    pass

```

<div class="para">Commandes utiles / Aide</div>

La fonction doit lire dans l’ordre les `#!python 0` et `#!python 1` du texte compressé, et en même temps (en partant de la racine) parcourir l’arbre de Huffman.
<span style="display: block; margin: 10px 0 0 0;">Lorsque l’on est sur une feuille, alors on lit le caractère qu’elle contient.</span>
<span style="display: block; margin: 10px 0 0 0;">On se replace ensuite à la racine tout en continuant à parcourir le texte compressé.</span>  

Principe de ce que fait dans l’ordre la fonction :
<div class="couleur_puce28" markdown="1">

* Tant que l’on n’a pas parcouru entièrement le texte compressé (chaine de `#!python 0` et de `#!python 1`) :

</div>
<div class="couleur_puce28etoi_decal" markdown="1">

* Si on lit un `#!python 0` et que le noeud en cours n’est pas une feuille alors on part dans le fils gauche.
* Si on lit un `#!python 1` et que le noeud en cours n’est pas une feuille alors on part dans le fils droit.
* Si le noeud en cours est une feuille, alors on lit le caractère étiqueté dans ce noeud que l’on ajoute au texte décodé, puis on se replace à la racine de l’arbre.

</div>

<div class="para">Tests</div>

```python

# ----------------------------
#       TEST
# ----------------------------

occ = sequence_to_occurrences('rechercher')     # nécessaire uniquement pour le test de la fonction
arbre_Huffman = huffman_tree(occ)                # nécessaire uniquement pour le test de la fonction
texte_compresse = "11100100101101001011"
assert decode(texte_compresse, arbre_Huffman) == 'rechercher', "Erreur"

occ = sequence_to_occurrences('i love coding')     # nécessaire uniquement pour le test de la fonction
arbre_Huffman = huffman_tree(occ)                # nécessaire uniquement pour le test de la fonction
texte_compresse = "0010101010001110110101110110011000011111110"
assert decode(texte_compresse, arbre_Huffman) == 'i love coding', "Erreur"

```