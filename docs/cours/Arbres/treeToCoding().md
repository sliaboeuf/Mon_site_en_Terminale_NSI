# <center><div class = "titre12">Fonction : treeToCoding()</div></center>

<div class="para">Objectif principal</div>

Réaliser la fonction qui génère la table de codage. Cette table contient le code optimal, selon l’algorithme de Huffman, de chacun des caractères du fichier source à compresser.

<div class="para">Rendu / Evaluation</div>

La fonction, une fois achevée, servira de brique de base au programme de compression de Huffman que l’ensemble de la classe codera. Tout le monde compte sur vous !!!  

Votre fonction doit être fonctionnelle, optimale, et son codage doit respecter les bonnes pratiques de programmation telles que CamelCase, ou <a href="https://fr.wikipedia.org/wiki/Snake_case" target="_blank">Snake_case</a>.  

A l’issu, __votre groupe passera à l’oral au tableau__ afin d’expliquer concrètement le déroulement de l’exécution de votre fonction. Le vocabulaire employé, la perspicacité, et le niveau de compréhension seront des critères d’évaluation.  

__La durée de la prestation orale est fixée à 5 min.__ 

<div class="para">Cahier des charges de la fonction</div>

Fichier à compléter :  

```python
from binaryTree import Arbre as BT
from fct_huffmanTree import huffmanTree
from fct_sequenceToOccurrences import sequenceToOccurrences


def treeToCoding(arbre_huff, dicCodeCarac = {}, codeEnConstruction = []):
    """
    Rôle: cette fonction récursive construit le dictionnaire de codage.

    Exemple de retour : {'a': 0, 't': 10, 'r': 11}

    Parameters
    ----------
    arbre_huff : (arbre) arbre de Huffman

    Returns
    -------
    (dict) dictionnaire donnant pour chaque caractère le code de Huffman à utiliser

    """

    pass

```

<div class="para">Commandes utiles / Aide</div>

Principe de ce que fait dans l’ordre la fonction :
<div class="couleur_puce16" markdown="1">

* Si le noeud est une feuille, alors on est arrivé en bout de branche sur un caractère, on affecte le symbole construit à ce <span class="decal5">caractère.</span>
* Ajout d’un `#!python '0'` au code en construction.
* Exécution de la fonction (récursion) pour explorer le fils gauche.
* Suppression d’un `#!python '0'` au code de construction puisque l’on remonte depuis un fils gauche.
* Ajout d’un `#!python '1'` au code en construction.
* Exécution de la fonction (récursion) pour explorer le fils droit.
* Suppression d’un `#!python '1'` au code de construction puisque l’on remonte depuis un fils droit.
* Renvoie du dictionnaire d’encodage des caractères.

</div>
<div class="para">Tests</div>

```python

# ----------------------------
#       TEST
# ----------------------------

occurrences = sequenceToOccurrences('bienvenue')
arbreHuffman = huffmanTree(occurrences)
tableCodage = treeToCoding(arbreHuffman)

assert tableCodage == {'i': '000', 'b': '001', 'u': '010', 'v': '011', 'n': '10', 'e': '11'}, 'Erreur'                         

```