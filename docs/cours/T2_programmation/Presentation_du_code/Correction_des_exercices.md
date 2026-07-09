# <center><div class = "titre2">Correction des exercices</div> </center>

### <div class = "encadré_exo"> __Correction de l'exercice 1__ </div>
<div class = "list1_1" markdown="1">

1. La fonction `#!python ma_fonction(n)` renvoie une liste de 100 entiers choisis aléatoirement entre 1 et 100000 et précise pour chaque entier s'il est premier ou non.
2. Ce code ne vérifie pas les recommandations de la PEP8, voici ce qui n'a pas été respecté :
```c
==============================================================================
SUBMITTED CODE
------------------------------------------------------------------------------
from random import *

def ma_fonction(n):
    if n < 2:
        return False
    fact = 2
    while fact * fact <= n:
        if n % fact == 0:
            return False
        else:
            fact += 1
    return True

for loop in range(100):
    n = randint(1, 100000)
    print(n, ma_fonction(n))

==============================================================================

==============================================================================
8 STYLE ISSUES FOUND
-----------------------------------------------------------------------------
ISSUE 1
Line 1 - Issue code: D100
Module (the term for the Python file) should have a docstring.
Add a docstring to your module.
A docstring is a special comment at the top of your module that briefly explains the purpose of the module. It should have 3 sets of quotes to start and finish the comment.
For example:
"""This file calculates required dietary requirements for kiwis.
-----------------------------------------------------------------------------
ISSUE 2
Line 1 - Issue code: F403
'from random import *' used; unable to detect undefined names

-----------------------------------------------------------------------------
ISSUE 3
Line 3 - Issue code: D103
This function should have a docstring.
Add a docstring to your function.
A docstring is a special comment at the top of your module that briefly explains the purpose of the function. It should have 3 sets of quotes to start and finish the comment.
For example:
def get_waypoint_latlng(number):
    """Return the latitude and longitude values of the waypoint."""
-----------------------------------------------------------------------------
ISSUE 4
Line 3 - Issue code: E302
Two blank lines are expected before and after each function or class.
Ensure there are two blank lines before and after each function and class.
-----------------------------------------------------------------------------
ISSUE 5
Line 4 - Issue code: E225
Line is missing whitespace around an operator.
Ensure there is one space before and after all operators.
-----------------------------------------------------------------------------
ISSUE 6
Line 8 - Issue code: E221
Line has multiple spaces before an operator.
Remove any extra spaces that appear before the operator on this line.
-----------------------------------------------------------------------------
ISSUE 7
Line 14 - Issue code: E305
Functions and classes should have two blank lines after them.
Ensure that functions and classes should have two blank lines after them.
-----------------------------------------------------------------------------
ISSUE 8
Line 15 - Issue code: F405
'randint' may be undefined, or defined from star imports: random

==============================================================================
```
3. Les docstrings seront étudiées dans le paragraphe "Prototyper une fonction".
```python
from random import randint


def ma_fonction(n):
    if n < 2:
        return False
    fact = 2
    while fact * fact <= n:
        if n % fact == 0:
            return False
        else:
            fact += 1
    return True


for loop in range(100):
    n = randint(1, 100000)
    print(n, ma_fonction(n))

```

</div>

### <div class = "encadré_exo"> __Correction de l'exercice 2__ </div>

En tapant `#!python help(ajout)`, on obtient :

```pycon
>>> help(ajout)
Help on function ajout in module __main__:

ajout(a, b)
    La somme de deux nombres.
    
    Renvoie la somme des deux nombres donnés en argument
    
    Parameters
    ----------
    a : int ou float
        première valeur à ajouter
    b : int ou float
        deuxième valeur à ajouter
    
    Returns
    -------
    int or float
        La somme des deux arguments de la fonction
```

### <div class = "encadré_exo"> __Correction de l'exercice 3__ </div>

Voici un code possible :

```python
def liste_diviseurs_entier(n):
    """La liste des diviseurs d'un nombre.

    Renvoie la liste des diviseurs d'un nombre donné en argument

    Parameters
    ----------
    n : int 
        Nombre dont on veut connaitre la liste des diviseurs

    Returns
    -------
    list 
        La liste des diviseurs de l'argument de la fonction
    """
    diviseurs = []
    
    for i in range(1, n+1):
        if n % i == 0:
            diviseurs.append(i)

    return diviseurs   

```

### <div class = "encadré_exo"> __Correction de l'exercice 4__ </div>

En tapant `help(fibo)`, voilà ce que l'on obtient :

```pycon
>>> help(fibo)
Help on module fibo:

NAME
    fibo - Module fibo relatif à la création de nombres de Fibionacci

DESCRIPTION
    Pour rappel, la suite de Fibonacci est une suite d_entiers dans laquelle chaque terme est la somme
    des deux termes qui le précèdent.(voir: https://fr.wikipedia.org/wiki/Suite_de_Fibonacci)
    
    Ce module présente deux fonctions:
    
    - fib_print: affiche les nombres de Fibionacii
    - fib_to_array: renvoie la liste des nombres de Fibionacci

FUNCTIONS
    fib_print(n)
        Affiche les nombres de Fibonacci
        
        Arguments
        ---------
        n: int
            dernier rang de la suite de Fibonacci affichée
    
    fib_to_array(n)
        Renvoie la liste des nombres de Fibonacci
        
        Arguments
        ---------
        n: int
            dernier rang de la suite de Fibonacci renvoyée dans la liste
        
        Returns
        -------
        list
            La liste des nombres de Fibonacci jusqu_au rang n

FILE
    f:\nsi\tnsi\mon_cours\presentation_du_code._modularite._validation_d_un_programme\fibo.py


```

### <div class = "encadré_exo"> __Correction de l'exercice 5__ </div>
<div class = "list1_1" markdown="1">

1. Les 2 conditions implicites au bon fonctionnement de cette fonction sont :

</div>
<div class="couleur_puce14_decal" markdown="1">

* le paramètre `#!python lst` de la fonction doit être de type liste. 
* Cette liste ne doit pas être vide (sans quoi `#!python len[0]` va déclencher une erreur).

</div>
<div class = "list1_2" markdown="1">

2. </div>
<div class="decal1" markdown="1">
```python
def minimum_liste(lst):
    """Renvoie la minimum d'une liste

    Arguments
    ---------
    lst: liste
        Une liste non vide d'entiers ou de flottants

    Returns
    -------
    float
        Le minimum des éléments de cette liste
    """

    assert type(lst) == list, "L'argument de la fonction doit être une liste !"
    assert len(lst) > 0, "La liste ne doit pas être vide !"

    longueur = len(lst)
    mini = lst[0]
    i = 1
    while i < longueur:
        if lst[i] < mini:
            mini = lst[i]
        i += 1
    return mini
```
</div>


### <div class = "encadré_exo"> __Correction de l'exercice 6__ </div>
<div class = "list1_1" markdown="1">
        
1. Si le fichier `#!python "test.txt"` n'existe pas, Python "plante" et affiche le message suivant :
<span style="display: block; margin: 8px 0 0 0;">
```pycon
Traceback (most recent call last):
  File "<tmp 2>", line 1, in <module>
    f = open("test.txt","r")
OSError: [Errno 22] Invalid argument: 'test.txt'
```
</span>
2. Voici un code possible :
<span style="display: block; margin: 8px 0 0 0;">
```python
def ouverture_fichier_lecture(nom_fich):
    erreur = ""
    f = None
    try:
        f = open(nom_fich, "r")
    except OSError:
        erreur = "fichier non trouvé"
    return(f, erreur)

```
</span>

</div>

### <div class = "encadré_exo"> __Correction de l'exercice 7__ </div>

Voici un code possible :
```python
import doctest


def rendu_pieces(somme, S):
    """Renvoie la liste des pièces rendues sur un montant donné

    Arguments
    ---------
    somme: int
        Le montant à rendre
    S : list
        La liste des pièces à disposition

    Returns
    -------
    list
        La décomposition, si possible, du montant à rendre à
        l'aide des pièces disponibles

    >>> rendu_pieces(19, (500, 200, 100, 50, 20, 10, 5, 2, 1))
    [10, 5, 2, 2]

    >>> rendu_pieces(19, (500, 200, 100, 50, 20, 10, 5))
    'rendu impossible'

    """

    ind, pieces_rendues = 0, []
    while somme != 0:
        while S[ind] <= somme:
            pieces_rendues.append(S[ind])
            somme -= S[ind]
        if somme != 0:
            if ind == len(S) - 1:
                return "rendu impossible"
            else:
                ind += 1
    return pieces_rendues

doctest.testmod()

```

