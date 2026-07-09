# <center><div class = "titre2"> Exercices </div></center>
  
### <div class = "encadré_exo">__Exercice 1 : Découvrir les décorateurs de fonction Python__</div>
Dans cet exercice, nous allons découvrir la notion de <a href="https://python.doctor/page-decorateurs-decorator-python-cours-debutants" target="_blank">__décorateur Python__</a> qui se prête bien à l'utilisation de la mémoïsation.
<span style="display:block; margin: 5px 0px 0px 0px;">
L'idée de base des décorateurs Python est simplement de passer une fonction en paramètre d'une autre fonction et d'y ajouter des pré et post traitements lors d'un appel à cette fonction, tout cela avec une syntaxe facile à utiliser. 
<div class="list1_1" markdown="1">

1. Voici un exemple simple.

</div>
<div class="list1_a" markdown="1">

1. Prenons une fonction que l'on souhaite décorer sans la modifier :
```python
def une_fonction_intouchable():
    print("je suis une fonction intouchable, ne me modifiez pas !")
    
``` 
Que donne l'appel `#!python une_fonction_intouchable()` ?
2. Décorons maintenant cette fonction :
```python
def decorateur_magique(fonction_a_decorer):
    # Le décorateur définit une fonction interne : le wrapper
    # le wrapper (emballage) enrobe la fonction originale
    # On peut ainsi ainsi exécuter du code avant et après celui-ci
    def wrapper_autour_de_la_fonction_originale():
        # code que l'on souhaite exécuter avant la fonction d'origine
        print("Avant que la fonction ne s'exécute.")

        # Appel de la fonction
        fonction_a_decorer()

        # Mettre ici le code que l'on souhaite exécuter après la fonction d'origine
        print("Après que la fonction se soit exécutée.")

    return wrapper_autour_de_la_fonction_originale
   
``` 
Est-ce que `#!python fonction_a_decorer` a été exécutée à ce stade ?
3. Si on passe `#!python une_fonction_intouchable` à ce décorateur, que se passe-t-il ?
```python
fonction_decoree = decorateur_magique(une_fonction_intouchable)
fonction_decoree()
    
``` 

</div>
<div class="list1_2" markdown="1">

2. On définit maintenant la fonction `#!python fonction_intouchable` avec un décorateur Python :
```python
@decorateur_magique
def fonction_intouchable():
    print("Ne me touchez pas !")

```

</div>
<div class="list1_a" markdown="1">

1. Que provoque l'appel à `#!python fonction_intouchable()` ?
2. A quelle instruction correspond donc `#!python @decorateur_magique` ?
3. Quel est le nom de `#!python fonction_intouchable` à présent (obtenu à l'aide l'instruction `#!python fonction_intouchable.__name__`) ?
4. Réécrire le décorateur `#!python decorateur_magique` en utilisant le décorateur `#!python @wraps` (étudier sa documentation → <a href="https://docs.python.org/fr/3/library/functools.html" target="_blank">ici</a> ) afin de remédier à ce changement de nom et de documentation.

</div>
<div class="list1_3" markdown="1">

3. Utilisons les connaissances acquises à la question <span style="color : rgb(251, 152, 83); font-weight: bold;">2.</span> pour réaliser un décorateur qui va chronométrer une fonction quelconque à un argument.  
Nous allons utiliser `#!python perf_counter_ns` du module <span style="font-family: 'Trebuchet MS';font-weight: bold">time</span> comme chronomètre (consulter sa documentation → <a href="https://docs.python.org/fr/3/library/time.html" target="_blank">ici</a> )
<span style="display:block; margin: 5px 0px 0px 0px;">
L'idée est de noter le temps avant l'appel de la fonction, d'appeler la fonction, de renoter le temps, puis d'afficher la différence des 2 temps mémorisés.</span>
<span style="display:block; margin: 5px 0px 0px 0px;">
Implémenter ce nouveau décorateur en l'appelant `#!python chrono`. Il faut qu'après l'avoir défini, par exemple, l'appel à :</span>
```python
@chrono
def boucle(n):
    for i in range(n):
        pass

boucle(10000)

```
affiche le temps pris par cette fonction sur la valeur 10 000.

</div>
<div class="list1_4" markdown="1">

4. Expliquer la deuxième version ci-dessous du décorateur `#!python chrono`. Qu'apporte-t-elle de plus ?
```python
from time import perf_counter_ns as now
from functools import wraps

def chrono2(f):
    @wraps(f)
    def my_f(*args, **kwargs):
        t0 = now()
        v = f(*args, **kwargs)
        t1 = now()
        print(t1 - t0, "ns")
        return v
    return my_f

@chrono2
def boucle2(n, autre=100):
    for i in range(n*autre):
        pass

# appel à boucle2
boucle2(100, autre = 50)

```

</div>
<center>
[Correction de l'exercice :material-cursor-default-click:](Correction.md#correction-de-lexercice-1){:target="_blank" .md-button}
</center>

### <div class = "encadré_exo">__Exercice 2 : décorateurs et mémoïsation__</div>

Il existe dans Python un décorateur de mémoïsation : `#!python lru_cache` dans le module <span style="font-family: 'Trebuchet MS';font-weight: bold">functools</span> que nous pouvons directement utiliser. Ce décorateur met en place une mémoïsation pour la fonction décorée.
<div class="list1_1" markdown="1">

1. On utilise ce décorateur pour définir une fonction `#!python fibonacci` :
```python
from functools import lru_cache
@lru_cache(maxsize=None)
def fibonacci(n):
    if n < 2:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

```

</div>
<div class="list1_a" markdown="1">

1. Taper ce code et invoquer `#!python fibonacci(37)`.
2. Il est possible de mieux comprendre le mécanisme de cache en invoquant `#!python fibonacci.cache_info()`. Comment interpréter sa réponse ?
3. Comparer avec la version récursive non mémoïsée (sans le décorateur en changeant son nom en `#!python fibo`)

</div>
<div class="list1_2" markdown="1">

2. On souhaite écrire un décorateur Python `#!python @memoise` qui garde toutes les valeurs déjà calculées en cache dans un dictionnaire. Construire la fonction `#!python memoise` suivant le modèle de la fonction `#!python chrono2` rencontrée dans le précédent exercice.
3. En utilisant ce décorateur `#!python @chrono2`, comparer les performances de :

</div>
<div class="couleur_puce14_decal" markdown="1">

* La version classique récursive de `#!python fibo`.
* La version mémoïsée avec le décorateur `#!python @memoise`.
* La version mémoïsée avec `#!python @lru_cache`.
* La version itérative bottom-up de Fibonacci.

</div>

!!! ampoule "__Conseils__"
    On peut empiler les décorateurs comme par exemple :

    ```python
    @chrono2
    @lru_cache(maxsize=None)
    def fibonacci(n):
        if n < 2:
            return n
        return fibonacci(n - 1) + fibonacci(n - 2)

    ```
    Attention ! Pour les fonctions récursives, chaque appel est ainsi chronométré.
    <span style="display:block; margin: 10px 0px 20px 0px;">Les affichages de temps se feront donc à chaque appel. Parmi tous les affichages, lequel devra-t-on retenir dans ce cas ?</span>
     
<center>
[Correction de l'exercice :material-cursor-default-click:](Correction.md#correction-de-lexercice-2){:target="_blank" .md-button}
</center>

