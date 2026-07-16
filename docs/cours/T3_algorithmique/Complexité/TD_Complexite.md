# <center><div class = "titre5"> TP : Complexité algorithmique </div></center>

__Objectif :__ Dans ce TP, nous allons vérifier expérimentalement les complexités qui ont été abordées dans la leçon.
<span style="display: block; margin: 12px 0 0 0;">Pour cela nous allons mesurer des temps d'exécution de divers algorithmes.</span>
<span style="display: block; margin: 3px 0 0 0;">Il va falloir observer le temps d'exécution en fonction de la taille des données en entrée.</span>

## <div class = "encadré2_TP">Mesurer le temps d'exécution d'une portion de code</div>

La librairie `#!python timeit` permet de mesurer le temps d'exécution d'un code Python. Pour cela, le code doit être répété un grand nombre de fois pour avoir une mesure pertinente. C'est ce que fait la librairie `#!python timeit` : répéter le code pour mesurer son temps d'exécution.
<span style="display: block; margin: 3px 0 0 0;">On utilise alors la classe `#!python Timer` de cette librairie :</span>

!!! exemple "__Exemple__"
    ```python
    from timeit import Timer

    t = Timer('sin(1.2)', setup='from math import sin')
    # Création d'un objet de type timeit.Timer
    ```

    On obtient dans la console :
    ```pycon
    >>> t
    <timeit.Timer object at 0x00000205CF7C7590>
    ```

Le constructeur de cette classe prend comme premier argument le fragment de code dont on souhaite mesurer le temps.
<span style="display: block; margin: 3px 0 0 0;">Le deuxième argument : `#!python setup` est un fragment de code exécuté une seule fois.</span>

Ensuite, on invoque la méthode `#!python repeat` de cette classe `#!python Timer` qui va mesurer le temps d'exécution comme le montre l'exemple suivant :

!!! exemple "__Exemple__"
    ```python
    temps = min(t.repeat(repeat=1000, number=1)) 
    # répète sin(1.2) 1000 fois et prend le plus petit temps d'execution
    ```
    
    On obtient dans la console :
    ```pycon
    >>> temps
    6.999471224844456e-07
    ```

`#!python t.repeat(repeat=1000, number=1)` est la répétition du code spécifié dans `#!python t`, le code est exécuté `#!python repeat` (ici 1000) fois.
<span style="display: block; margin: 3px 0 0 0;">Nous prendrons la valeur minimale des temps obtenus.</span>

???+ exercice2 "Exercice 1"
    On veut vérifier que passer à 10000 exécutions ne change pas beaucoup le temps d'exécution moyen.
    <span style="display: block; margin: 8px 0 0 0;">Compléter alors le code suivant :</span>
    ```python
    from timeit import Timer 

    t = Timer('sin(1.2)', setup='from math import sin')
    # CODE A COMPLETER

    # répète sin(1.2) 10000 fois et prend le plus petit temps d'execution
    ```
    <center>
    [Correction de l'exercice 1 :material-cursor-default-click:](Correction des exos du TP.md#correction-de-lexercice-1){:target="_blank" .md-button}
    </center>

Testons la vitesse de la fonction `#!python max` qui renvoie le maximum d'une liste.
<span style="display: block; margin: 8px 0 0 0;">Nous allons afficher le temps mis par la fonction `#!python max` sur une liste de 50 nombres aléatoires.</span>

```python
from timeit import Timer

# On configure la liste utilisée (ce code sera exécuté une seule fois.)
setup = '''
from random import randint
L = [randint(1, 100) for i in range(50)]
'''

# Mesure du temps
t = Timer('max(L)', setup=setup)
temps = min(t.repeat(repeat=10000, number=1))
print(temps)
```

???+ exercice2 "Exercice 2"
    <div class = "list7_1">

    1. Afficher le temps mis par la fonction `#!python max` sur une liste de 500 nombres aléatoires.  
    ```python
    # CODE A COMPLETER

    # Affiche le temps d'éxécution sur une liste de 500 éléments.
    ```
    2. Lors du passage d'une liste de 50 éléments à 500 éléments, par combien le temps a-t-il été multiplié ?
    3. Pourquoi est-ce cohérent avec le cours ?  
    </div>
    <center>
    [Correction de l'exercice 2 :material-cursor-default-click:](Correction des exos du TP.md#correction-de-lexercice-2){:target="_blank" .md-button}
    </center>

## <div class = "encadré2_TP">Mesurer le temps d'une fonction à plusieurs paramètres</div>

Pour mesurer le temps d'exécution d'une fonction `#!python f`, il faut la passer en argument à `#!python Timer` avec ses arguments.
<span style="display: block; margin: 8px 0 0 0;">Il y a plusieurs méthodes. La plus simple est de faire appel à la méthode `#!python partial` de la librairie de programmation fonctionnelle `#!python functools` qui permet de transformer la fonction `#!python f` et ses paramètres en une nouvelle fonction avec moins de paramètres.</span>
<span style="display: block; margin: 8px 0 0 0;">Dans l'exemple, on transforme l'addition en une addition avec la constante `#!python 2`.</span>

```python
from functools import partial

def addition(x, y):
    return x + y

add2 = partial(addition, y=2)
# add2 est une fonction d'un seul paramètre (qui est x ici).
```

On obtient dans la console :
```pycon
>>> add2(4)
6
```

Au moyen de `#!python partial`, on peut fournir une fonction à `#!python Timer`.
<span style="display: block; margin: 3px 0 0 0;">On construit alors une liste des mesures du temps d'exécution.</span>

```python
# On va stocker les temps d'exécution dans la liste temps
temps = []
for i in range(5):
    # Pour chaque valeur i de 0 à 4 on exécute add2(i) puis on mesure le temps moyen d'exécution
    mesure = Timer(partial(add2, i))
    t = min(mesure.repeat(repeat=10000, number=1))
    # on ajoute ce temps à la liste temps
    temps.append(t)
    
print(temps)
# Constatez alors que la liste temps est constituée de 5 temps d'exécution relativement proches.
```

## <div class = "encadré2_TP">Application au calcul de moyenne</div>

???+ exercice2 "Exercice 3"
    Compléter ci-dessous le code de la fonction `#!python moyenne` :
    ```python
    def moyenne(L:list) -> float:
    """
    Entrée : L liste de flottants
    Sortie : un flottant qui est la moyenne de la liste L
    """
    # CODE A COMPLETER
    ```

    On testera sa fonction à l'aide du bout de code suivant :
    ```python
    # Tests de la fonction moyenne
    assert moyenne([1, 2, 3, 4]) == 2.5
    assert moyenne([1, 2, 3, 4, 5, 6]) == 3.5
    ```
    <center>
    [Correction de l'exercice 3 :material-cursor-default-click:](Correction des exos du TP.md#correction-de-lexercice-3){:target="_blank" .md-button}
    </center>

On construit maintenant une liste `#!python L` de 100 entiers tirés au hasard entre 1 et 10 000 et on effectue différentes mesures en fonction de la taille des entrées :

```python
from random import randint

# Première mesure avec une liste de taille 100
L1 = [randint(1, 10000) for i in range(100)]
mesure1 = Timer(partial(moyenne, L1))
t1 = min(mesure1.repeat(repeat=10000, number=1))
print(t1)

# Seconde mesure avec une liste de taille 1000
L2 = [randint(1, 10000) for i in range(1000)]
mesure2 = Timer(partial(moyenne, L2))
t2 = min(mesure2.repeat(repeat=10000, number=1))
print(t2)

# Troisième mesure avec une liste de taille 10000
L3 = [randint(1, 10000) for i in range(10000)]
mesure3 = Timer(partial(moyenne, L3))
t3 = min(mesure3.repeat(repeat=10000, number=1))
print(t3)
```

???+ exercice2 "Exercice 4"
    Coder la fonction `#!python randlist` ayant :
    <div class = "couleur_puce21">

    * en entrée : un entier `#!python n` ;
    * en sortie : une liste de taille `#!python n` constituée d'entiers aléatoires entre 1 et 100.
    </div>

    ```python
    def randlist(n:int) -> list:
    ###################
    # Votre code ici  #
    ###################
    ```
    <center>
    [Correction de l'exercice 4 :material-cursor-default-click:](Correction des exos du TP.md#correction-de-lexercice-4){:target="_blank" .md-button}
    </center>

Ci-dessous, nous allons constituer deux listes `#!python x` et `#!python y` contenant respectivement :
<div class = "couleur_puce22" markdown="1">

* La taille des données en entrée (ici la longueur de la liste).
* Le temps d'exécution de la fonction `#!python moyenne` sur ces entrées.
</div>

Bien prendre le temps de chercher à comprendre ce que fait chaque instruction avant d'exécuter le code.

```python
x, y = [], []
for i in range(1, 1000, 10):
    mesure = Timer(partial(moyenne, randlist(i)))
    t = min(mesure.repeat(repeat=100, number=1))
    x.append(i)
    y.append(t)
    
# Combien de fois la fonction moyenne est-elle appelée dans un tour de boucle ?
```

Et ci-dessous, voici le code permettant d'afficher la courbe de `#!python y` en fonction de `#!python x`, c'est-à-dire le temps d'exécution en fonction de la taille des entrées.
<span style="display: block; margin: 8px 0 0 0;">Il faudra sans doute l'adapter à d'autres exemples pour la suite de ce TP. Encore une fois, prendre le temps de bien comprendre ce que font les instructions.</span>

```python
# Exécutez deux fois ce code si le graphique ne s'affiche pas.
import matplotlib.pyplot as plt
plt.rcParams.update({'font.size': 12})
fig = plt.figure(figsize=(10, 10))
plt.plot(x, y, marker='o',label='Moyenne de liste')
plt.xlabel('taille n')
plt.ylabel('temps de calcul en secondes [s]')
plt.legend(loc='upper left')
plt.grid()
plt.show()
```

???+ exercice2 "Exercice 5"
    <div class = "list7_1">

    1. Que peut-on dire de la représentation graphique de cette fonction ?
    2. Expliquer pourquoi cela est cohérent avec le cours.
    </div>
    <center>
    [Correction de l'exercice 5 :material-cursor-default-click:](Correction des exos du TP.md#correction-de-lexercice-5){:target="_blank" .md-button}
    </center>

## <div class = "encadré2_TP">Parcours séquentiel d'une liste de listes</div>

Dans cette partie, nous allons analyser la vitesse d'exécution d'un code qui parcourt une liste de listes.

???+ exercice2 "Exercice 6"
    <div class = "list7_1">

    1. Coder une fonction `#!python randlistlist` ayant :
    </div>
    
    <div class = "couleur_puce21_decal">

    * en entrée : un entier `#!python n` ;
    * en sortie : une liste de listes de taille `#!python n × n` constituée d'entiers aléatoires entre 1 et 100.
    </div>
    <div class = "decal1"> 
    ```python
    def randlistlist(n:int) -> list:
    ###################
    # Votre code ici  #
    ###################
    
    # Tests de la fonction
    t = randlistlist(10)
    assert (len(t), len(t[0])) == (10, 10)
    ```
    </div>

    <div class = "list7_2">

    2. Coder une fonction `#!python double` ayant :
    </div>
    
    <div class = "couleur_puce21_decal">

    * en entrée : une liste `#!python L` de listes de taille `#!python n × n`;
    * en sortie : une liste de listes de taille `#!python n × n` constituée des doubles des éléments de `#!python L`.
    </div>
    <div class = "decal1"> 
    ```python
    def double(L:list) -> list:
    """
    L est une liste de liste d'entiers
    """
    ###################
    # Votre code ici  #
    ###################
    
    # Test de la fonction
    L = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    assert double(L) == [[2, 4, 6], [8, 10, 12], [14, 16, 18]]
    ```
    </div>
    <center>
    [Correction de l'exercice 6 :material-cursor-default-click:](Correction des exos du TP.md#correction-de-lexercice-6){:target="_blank" .md-button}
    </center>

Ci-dessous, nous allons constituer deux listes `#!python x` et `#!python y` contenant respectivement :
<div class = "couleur_puce22" markdown="1">

* La taille des données en entrée.
* Le temps d'exécution de la fonction `#!python double` sur ces entrées.
</div>

Prendre le temps de chercher à comprendre ce que fait chaque instruction avant d'exécuter le code.

```python
x, y = [], []
for i in range(1, 100, 10):
    mesure = Timer(partial(double, randlistlist(i)))
    t = min(mesure.repeat(repeat=100, number=1))
    x.append(i)
    y.append(t)

import matplotlib.pyplot as plt
plt.rcParams.update({'font.size': 12})
fig = plt.figure(figsize=(10, 10))
plt.plot(x,y,marker='o', label='Parcours de listes de listes')
plt.xlabel('taille n')
plt.ylabel('temps de calcul en secondes [s]')
plt.legend(loc='upper left')
plt.grid()
plt.show()
```

???+ exercice2 "Exercice 7"
    <div class = "list7_1">

    1. Que peut-on dire de la représentation graphique de cette fonction ?
    2. Expliquer pourquoi cela est cohérent avec le cours.
    
    </div>
    <center>
    [Correction de l'exercice 7 :material-cursor-default-click:](Correction des exos du TP.md#correction-de-lexercice-7){:target="_blank" .md-button}
    </center>

## <div class = "encadré2_TP">Algorithmes de recherche dans une liste triée</div>

Dans cette partie, nous allons comparer deux algorithmes de recherche dans des listes : un algorithme "naïf" et l'algorithme de dichotomie.

### <div class = "encadré3_TP">Algorithme naïf</div>

???+ exercice2 "Exercice 8"
    <div class = "list7_1">

    1. Coder une fonction `#!python gene_liste_triee` ayant :
    
    </div>
    <div class = "couleur_puce21_decal">

    * en entrée : un entier `#!python n` positif ;
    * en sortie : une liste de taille `#!python n` de nombres aléatoires (entre 1 et 100) __triée dans l'or
    dre croissant__.
    
    </div>
    <div class = "decal1">
    
    !!! remarque "__Remarque__"
        le code `#!python L.sort()` permet de trier une liste `#!python L` en place (c'est à dire que `#!python L` sera triée sans avoir besoin de réaliser une affectation).
   
    ```python
    def gene_liste_triee(n:int) -> list:
    """
    Entrée : n est un entier, c'est la taille de la liste en sortie
    Sortie : L est une liste d'entiers positifs triée par ordre croissant.
    """
    ###################
    # Votre code ici  #
    ###################
    ```
    </div>

    <div class = "list7_2">

    2. Coder une fonction `#!python recherche_naïve` ayant :
    </div>
    
    <div class = "couleur_puce21_decal">

    * en entrée : une liste `#!python L` de taille `#!python n` triée dans l'ordre croissant et `#!python c` un entier ;
    * en sortie : un booléen indiquant si l'élément `#!python c` est dans la liste `#!python L`.
    
    </div>
    <div class = "decal1">
    ```python
    def recherche_naïve(L:list, c:int) -> bool:
    """
    Entrée : L est une liste d'entiers positifs triée par ordre croissant et c est un entier
    Sortie : un booléen qui indique si c est dans la liste L
    """
    ###################
    # Votre code ici  #
    ###################

    L = [2, 3, 5, 7, 11, 13, 17, 19, 23]
    assert recherche_naïve(L, 23) == True
    assert recherche_naïve(L, 25) == False
    assert recherche_naïve(L, 0) == False
    ```
    </div>
    <div class = "list7_3">

    3. Dans cette question, nous allons constituer deux listes `#!python x` et `#!python y` contenant respectivement :
    </div>

    <div class = "couleur_puce21_decal">

    * La taille des données en entrée (ici la longueur de la liste).
    * Le temps d'exécution de la fonction `#!python recherche_naïve` sur ces entrées.
    
    </div>
    <div class = "decal1">
    Prendre le temps de chercher à comprendre ce que fait chaque instruction avant d'exécuter le code.
    ```python
    x,y = [],[]
    for i in range(1, 1000, 10):
        mesure = Timer(partial(recherche_naïve, gene_liste_triee(i), 42))
        t = min(mesure.repeat(repeat=100, number=1))
        x.append(i)
        y.append(t)

    plt.rcParams.update({'font.size': 12})
    fig = plt.figure(figsize=(10, 10))
    plt.plot(x, y, '-bo', label='Recherche naïve')
    plt.xlabel('taille n')
    plt.ylabel('temps de calcul en secondes [s]')
    plt.legend(loc='upper left')
    plt.grid()
    plt.show()
    ```
    </div>
    <center>
    [Correction de l'exercice 8 :material-cursor-default-click:](Correction des exos du TP.md#correction-de-lexercice-8){:target="_blank" .md-button}
    </center>

### <div class = "encadré3_TP">Algorithme de dichotomie</div>

???+ exercice2 "Exercice 9"
    <div class = "list7_1">

    1. Coder l'algorithme de recherche dichotomique comme vu en cours.
    
    </div>
    <div class = "decal1">
    ```python
    def recherche_dichotomique(L:list, c:float) -> bool:
    """
    L est une liste triée dans l'odre croissant
    Retourne un booléen indiquant si l'élément c est dans la liste L
    """
    ###################
    # Votre code ici  #
    ###################
    
    L = [2, 3, 5, 7, 11, 13, 17, 19, 23]
    assert recherche_dichotomique(L, 23) == True
    assert recherche_dichotomique(L, 25) == False
    assert recherche_dichotomique(L, 0) == False
    ```    
    </div>

    <div class = "list7_2">

    2. Dans cette question, nous allons constituer deux listes `#!python x` et `#!python z` contenant respectivement :
    </div>

    <div class = "couleur_puce21_decal">

    * La taille des données en entrée (ici la longueur de la liste).
    * Le temps d'exécution de la fonction `#!python recherche_dichotomique` sur ces entrées.
    </div>
    <div class = "decal1">
    Prendre le temps de chercher à comprendre ce que fait chaque instruction avant d'exécuter le code.
    ```python
    x, z = [], []
    for i in range(1, 1000, 10):
        testTimer = Timer(partial(recherche_dichotomique, gene_liste_triee(i), 42))
        t = min(testTimer.repeat(repeat=10000, number=1))
        x.append(i)
        z.append(t)
    
    plt.rcParams.update({'font.size': 12})
    fig = plt.figure(figsize=(10, 10))
    plt.plot(x,z,'--ro',label='Recherche dichotomique')
    plt.xlabel('taille n')
    plt.ylabel('temps de calcul en secondes [s]')
    plt.legend(loc='upper left')
    plt.grid()
    plt.show()
    ```
    </div>
    <center>
    [Correction de l'exercice 9 :material-cursor-default-click:](Correction des exos du TP.md#correction-de-lexercice-9){:target="_blank" .md-button}
    </center>

### <div class = "encadré3_TP">Comparaison des deux algorithmes</div>

Affichons le temps d'exécution sur un même graphique.

```python
plt.rcParams.update({'font.size': 12})
fig = plt.figure(figsize=(10, 10))
plt.plot(x, y, '--bo', label='Recherche naïve')
plt.plot(x, z, '--ro', label='Recherche dichotomique')
plt.xlabel('taille n')
plt.ylabel('temps de calcul en secondes [s]')
plt.legend(loc='upper left')
plt.grid()
plt.show()
```

???+ exercice2 "Exercice 10"
    <div class = "list7_1">

    1. Que constate-t-on ? 
    2. Est-ce cohérent avec la leçon, pourquoi ?
    </div>
    <center>
    [Correction de l'exercice 10 :material-cursor-default-click:](Correction des exos du TP.md#correction-de-lexercice-10){:target="_blank" .md-button}
    </center>






