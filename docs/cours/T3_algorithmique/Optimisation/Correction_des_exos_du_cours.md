---
password: "corr_Optimisation"
---

# <center><div class = "titre2"> Correction des exercices du cours </div></center>

### <div class = "encadré_exo">__Correction de l'exercice 1__</div>
<div class = "list1_1" markdown="1">

1.  Une chaîne de caractères se construit en partant d'une chaîne `#!python s` vide et en accumulant dans `#!python s`, à l'intérieur d'une boucle, les caractères lus au fur et à mesure.
```python
def miroir(ch):
    s = ""
    for i in range(len(ch) - 1, -1, -1):
        # on parcourt les indice à l'envers
        s += ch[i]
    return s
```
Une autre solution, élégante, utilise le fait que lire de droite à gauche et écrire de gauche à droite (ce qu'on a fait au-dessus) donne le même résultat que lire de gauche à droite et écrire de droite à gauche :
```python
def miroir(ch):
    s = ""
    for c in ch:
        s = c + s
    return s
```
2. <span style="color: #f36379; font-weight: bold; margin: 0px 10px 0px 0px;">a.</span>  
Une fonction récursive utilisant le *slicing* peut être écrite en tenant compte de la méthodologie habituelle : le cas de base est celui d'une chaîne vide et comme une chaîne doit être renvoyée par cette fonction, nous restons cohérents en renvoyant une chaîne vide dans ce cas.
```python
def mir(ch):
    if ch == "":
        return ""
    return mir(ch[1:]) + ch[0]
```
<span style="color: #f36379; font-weight: bold; margin: 0px 10px 0px 0px;">b.</span>  
Le *slicing* a un coût qui ne peut être négligé. Celui-ci est de la taille de la chaîne slicée. Cela donne la relation de récurrence $T(n)=T(n-1)+n$, ce qui donne $~T(n)=\mathcal{O}(n^2)$.
3. <span style="color: #f36379; font-weight: bold; margin: 0px 10px 0px 0px;">a.</span>  
Pour éviter de slicer à chaque appel récursif, il est nécessaire de retenir combien de caractères ont déjà été mis dans la chaîne inversée. Cela donne :
```python
def miroir(ch):
    def mir(ch, i):
        if i == 0:
            return ch[0]
        else:
            return ch[i] + mir(ch, i - 1)
    return mir(ch, len(ch) - 1)
```
<span style="color: #f36379; font-weight: bold; margin: 0px 10px 0px 0px;">b.</span> On a désormais la relation de récurrence $T(n)=T(n-1)+1$ et donc une complexité linéaire.
4. On utilise la définition d'un palindrome :
```python
def palindrome(ch):
    return ch == miroir(ch)
```

</div>

### <div class = "encadré_exo">__Correction de l'exercice 2__</div>
<div class="list1_1" markdown="1">

1. Une écriture naïve récursive du calcul de $~u_{n}~$ est :
```python
def tribo(n):
    if n == 0:
        return 0
    if n == 1 or n == 2:
        return 1
    return tribo(n - 1) + tribo(n - 2) + tribo(n - 3)
```
Si cette fonction calcule effectivement $~u_{n}$, son efficacité est désastreuse. En effet, les seuls cas de base sont évalués à 1, ce qui signifie qu'il y a au moins autant d'appels à la fonction `#!python tribo(n)` que ce que vaut `#!python tribo(n)`. Comme sa valeur a une croissance au moins exponentielle, la complexité de l'algorithme l'est également.
2. Une écriture itérative du calcul de $~u_{n}~$ utilise trois variables auxiliaires `#!python u`, `#!python v` et `#!python w` qui stockent initialement les valeurs de $~u_0~$, $~u_1~$ et $~u_2~$ puis, à chaque itération de la boucle, les valeurs de $~u_{n}~$, $~u_{n+1}~$ et $~u_{n+2}~$ :
```python
def tribo(n):
    u, v, w = 0, 1, 1
    for i in range(n - 2):
        u, v, w = v, w, u + v + w
    return w
```
3. La solution efficace récursive fait appel à une technique de mémoïsation. Les valeurs de $~u_{n}~$ déjà calculées sont stockés dans un dictionnaire :
```python
def tribo(n):
    memo_tribo = {}
    def trib(n):
        if n in memo_tribo:
            return memo_tribo[n]
        if n == 0:
            memo_tribo[n] = 0
        elif n == 1 or n == 2:
            memo_tribo[n] = 1
        else :
            memo_tribo[n] = trib(n-1) + trib(n-2) + trib(n-3)
        return memo_tribo[n]
    return trib(n)
```

</div>