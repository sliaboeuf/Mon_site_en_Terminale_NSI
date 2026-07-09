# <center><div class = "titre2"> Correction des exercices du cours </div></center>

### <div class = "encadré_exo">__Correction de l'exercice 1__</div>
<div class="list1_1" markdown="1">

1.  

</div>
<div class="list1_a" markdown="1">

1. L'affichage est :
```pycon
je suis une fonction intouchable, ne me modifiez pas !
```
2. Non, arrivés ici, la fonction `#!python fonction_a_decorer` n'a pas été exécutée. La fonction `#!python decorateur_magique` fabrique le *wrapper*, qu'elle retourne.
3. L'appel à `#!python fonction_decoree()` donne :
```pycon
Avant que la fonction ne s exécute.
je suis une fonction intouchable, ne me modifiez pas !
Après que la fonction se soit exécutée.
```

</div>
<div class="list1_2" markdown="1">

2.  

</div>
<div class="list1_a" markdown="1">

1. L'appel à `#!python fonction_intouchable()` donne :
```python
Avant que la fonction ne s exécute.
je suis une fonction intouchable, ne me modifiez pas !
Après que la fonction se soit exécutée.
```
2. `#!python @decorateur_magique` est juste un raccourci pour :
```python
fonction_intouchable = decorateur_magique(fonction_intouchable)  
```
3. `#!python fonction_intouchable()` a changé de nom dans la manoeuvre :
```python
print(fonction_intouchable.__name__)
```
donne en effet :
```pycon
wrapper_autour_de_la_fonction_originale
```
4. On peut remédier à cela grâce au décorateur `#!python @wraps` :
```python
from functools import wraps
def decorateur_magique(f):
    @wraps(f)
    def wrapper_autour_de_la_fonction_originale():
        print("Avant que la fonction ne s'exécute.")
        f()
        print("Après que la fonction se soit exécutée.")

    return wrapper_autour_de_la_fonction_originale
```
Et maintenant, le nom de la fonction décorée est cohérent avec celle de départ :
```python
@decorateur_magique
def fonction_vraiment_intouchable():
    """ Je suis vraiment intouchable !"""
    print("Ne me touchez pas !")

print(fonction_vraiment_intouchable.__name__)
```
donne :
```pycon
fonction_vraiment_intouchable  
```

</div>
<div class="list1_3" markdown="1">

3. Voici une implémentation possible du décorateur `#!python @chrono` :
```python
from time import perf_counter_ns as now

def chrono(f):
    def f_chrono(arg):
        t0 = now()
        v = f(arg)
        t1 = now()
        print(t1 - t0, "nanosecondes")
        return v
    return f_chrono
```
4. Dans cette deuxième version du décorateur `#!python chrono`, on note tout d'abord l'utilisation interne du décorateur `#!python @wraps` qui permet de ne pas modifier le nom de la fonction après décoration.  
<span style="display:block; margin: 5px 0px 0px 0px;">Pour chronométrer une fonction avec un nombre quelconque d'arguments (non nommés et nommés), en Python, on utilise :</span>

</div>
<div class="couleur_puce14_decal" markdown="1">

* Les arguments __non nommés__ qui sont récupérés et "déballés" par l'appel `#!python *args`.
* Les arguments __nommés__ récupérés et "déballés" grâce à `#!python **kargs`.

</div>
<div class="decal15" markdown="1">

!!! note1 "__A noter__"
    Ce mécanisme s'appelle *unpacking* ou "déballage" Python des listes et dictionnaires (pour plus de détail  → <a href="https://docs.python.org/3/tutorial/controlflow.html#keyword-arguments" target="_blank">ici</a>)

</div>
<div class="decal1" markdown="1">

Ici, le décorateur `#!python @chrono2` est utilisé avec une fonction `#!python boucle2` qui possède un premier argument non nommé par mot-clé et un deuxième argument nommé `#!python autre` avec une valeur par défaut de 100. L'appel à `#!python boucle2` avec tous ses arguments sera donc bien chronométré et le résultat affiché.

</div>

### <div class = "encadré_exo">__Correction de l'exercice 2__</div>
<div class="list1_1" markdown="1">

1.  

</div>
<div class="list1_a" markdown="1">

1. On obtient immédiatement `#!python fibonacci(37) = 24157817`.
2. Nous pouvons tester en invoquant `#!python fibonacci(37)` puis investiguer sur le mécanisme avec `#!python fibonacci.cache_info()` qui retourne quelque chose comme : `#!python CacheInfo(hits=35, misses=38, maxsize=None, currsize=38)`, ce qui signifie que le cache a été utilisé 35 fois, qu'il a calculé 38 nouvelles valeurs et qu'il est actuellement de taille 38.
3. Avec la version récursive classique, le calcul est beaucoup plus long !

</div>
<div class="list1_2" markdown="1">

2. Voici un décorateur de mémoïsation pour une fonction à un argument. Le cache est dans un dictionnaire Python : 
```python
from functools import wraps

def memoise(f):
    cache = {}
    @wraps(f)
    def f_memo(arg):
        if arg not in cache:
            cache[arg] = f(arg)
        return cache[arg]
    return f_memo
```
3. On décore toutes les fonctions demandées avec `#!python @chrono2` (en plus des autres décorateurs lorsqu'il y en a). Pour comparer les performances, pour les valeurs récursives, c'est la dernière valeur affichée qui sera significative car c'est celle du premier appel. C'est donc cette valeur (en ns) qui sera à comparer avec les autres.  
Si on veut éviter tous les affichages, on peut seulement décorer l'appel que nous cherchons à chronométrer comme pour la version mémoïsée avec le décorateur `#!python @memoise` :
```python
@memoise
def fibon(n):
    if n < 2:
        return n
    return fibon(n-1) + fibon(n-2)
```
On décore l'appel de `#!python fibon(37)` :
```python
@chrono2
def fibon37():
    return fibon(37)
    
```
De même, pour la version classique récursive de `#!python fibo`:
```python
def fibo_rec(n):
    if n < 2:
        return n
    return fibo_rec(n-1) + fibo_rec(n-2)
```
On décore l'appel de `#!python fibo_rec(37)` :
```python
@chrono2
def fibo_rec37():
    return fibo_rec(37)
```
Pour la version mémoïsée avec `#!python @lru_cache` :
```python
@lru_cache(maxsize = None)
def fibonacci(n):
    if n < 2:
        return n
    return fibonacci(n-1) + fibonacci(n-2)
```
On décore l'appel de `#!python fibonacci(37)` :
```python
@chrono2
def fibonacci37():
    return fibonacci(37)
```
Pour la version itérative bottom-up de Fibonacci :
```python
def fibo_bas_haut(n):
    liste = [0] * (n+1)
    liste[1] = 1
    for i in range(2, n+1):
        liste[i] = liste[i-1] + liste[i-2]
    return liste[n]
```
On décore l'appel de `#!python fibonacci(37)` :
```python
@chrono2
def fibo_bas_haut37():
    return fibo_bas_haut(37)
```
On obtient alors les différents affichages suivant :
```pycon
>>> fibon37()
3800 nanosecondes
24157817

>>> fibo_rec37()
28952723600 nanosecondes
24157817

>>> fibonacci37()
44600 nanosecondes
24157817

>>> fibo_bas_haut37()
22000 nanosecondes
24157817
```

</div>

