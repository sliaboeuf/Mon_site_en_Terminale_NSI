# <center><div class = "titre7">Fonction : encode()</div></center>

<div class="para">Objectif principal</div>

Réaliser une fonction qui convertit le texte source, à l’aide du dictionnaire de codage optimal de Huffman, en une suite de `#!python 0` et de `#!python 1`.

<div class="para">Rendu / Evaluation</div>

La fonction, une fois achevée, servira de brique de base au programme de compression de Huffman que l’ensemble de la classe codera. Tout le monde compte sur vous !!!  
<span style="display: block; margin: 10px 0 0 0;">Votre fonction doit être fonctionnelle, optimale, et son codage doit respecter les bonnes pratiques de programmation telles que CamelCase, ou <a href="https://fr.wikipedia.org/wiki/Snake_case" target="_blank">Snake_case</a>.</span>
<span style="display: block; margin: 10px 0 0 0;">A l’issu, __votre groupe passera à l’oral au tableau__ afin d’expliquer concrètement le déroulement de l’exécution de votre fonction. Le vocabulaire employé, la perspicacité, et le niveau de compréhension seront des critères d’évaluation.</span>

__La durée de la prestation orale est fixée à 5 min.__ 

<div class="para">Cahier des charges de la fonction</div>

Fichier à compléter :  

```python
def encode(source, coding_table):
    """
    Rôle: Code le texte source en utilisant la table de Huffman

    Parameters
    ----------
    source: (str) texte source à encoder
    coding_table: (dict) une table de codage

    Returns
    -------
    (str) chaine qui contient une suite de '0' et de '1'

    """

    pass

```

<div class="para">Commandes utiles / Aide</div>

Vos connaissances actuelles suffisent à coder cette fonction.

<div class="para">Tests</div>

```python

# ----------------------------
#       TEST
# ----------------------------

texte_source = 'rechercher'
table_codage = {'h': '00', 'c': '01', 'e': '10', 'r': '11'}
assert encode(texte_source, table_codage) == "11100100101101001011", "erreur"

texte_source = 'i love coding'
table_codage = {'i': '00', 'l': '010', 'e': '0110', 'v': '0111', 'o': '100', ' ': '101', 'd': '1100', 'c': '1101', 'g': '1110', 'n': '1111'}
assert encode(texte_source, table_codage) == "0010101010001110110101110110011000011111110", "erreur"

```