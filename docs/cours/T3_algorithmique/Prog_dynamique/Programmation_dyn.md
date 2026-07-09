# <center><div class = "titre1">Vers la programmation dynamique</div></center>

Nous prolongeons la méthode générale "diviser pour régner" (<span style="font-family: 'Trebuchet MS';font-weight: bold">DR</span>) implémentée grâce à la récursivité en systématisant la démarche de mémoïsation, puis en allant plus loin pour compléter encore ces algorithmes lorsqu'ils ne sont pas efficaces.

## <div class = "encadré2">De l'approche DR à la programmation dynamique (DP)</div>
<div class="couleur_puce13" markdown="1">

* Dans l'approche __diviser pour régner__ (<span style="font-family: 'Trebuchet MS';font-weight: bold">DR</span>) appliquée sur les exemples de tri fusion ou de la recherche dichotomique, nous avons utilisé comme outils la récursivité et la création de sous-problèmes indépendants dont la résolution permet de traiter le problème initial.
* Cette approche est améliorée par la technique de la mémoïsation. Dans l'approche de la __programmation dynamique__ (<span style="font-family: 'Trebuchet MS';font-weight: bold">DP</span>), les sous-problèmes se recoupent parfois et sont réutilisés dans la résolution de plusieurs problèmes différents.

</div>

## <div class = "encadré2">Mémoïsation d'une fonction quelconque</div>
Reprenons l'exemple de la suite de Fibonacci :

```python
def fibo_rec(n):
    memo_fibo = {}
    def fib(n):
        if n in memo_fibo:
            return memo_fibo[n]
        if n < 2:
            memo_fibo[n] = n
        else:
            memo_fibo[n] = fib(n-1) + fib(n-2)
        return memo_fibo[n]
    return fib(n)

```

Et rappelons que l'arbre des appels correpondant au lancement de `#!python fibo_rec(5)` est :
<span style="display:block; margin: 25px 0px 0px 0px;">

![](images/Fibo2.png){ .image width=60%}

</span>
<div class="couleur_puce13" markdown="1">

* Les méthodes vues à ce stade sont de type <span style="font-family: 'Trebuchet MS';font-weight: bold">DR</span> "__*top-down*__" ou "*haut-bas*". La mémoïsation constitue l'un des outils de base de la programmation dynamique, <span style="font-family: 'Trebuchet MS';font-weight: bold">DP</span>.

</div>

## <div class = "encadré2">Démarche "bas vers haut"</div>
<div class="couleur_puce13" markdown="1">

* La démarche inverse de type itérative "__*bottom-up*__", du bas vers le haut, est également possible, par exemple pour `#!python fibo` :
```python
def fibo_bas_haut(n):
    liste = [0] * (n+1)
    liste[1] = 1
    for i in range(2, n+1):
        liste[i] = liste[i-1] + liste[i-2]
    return liste[n]

```

</div>

!!! book1 "Mot clé"
    Dans une forme itérative "__*bottom-up*__", on résout d'abord les sous-problèmes de "petite taille" puis ceux de la taille intermédiaire... jusqu'à la taille voulue. On stocke les résultats partiels dans un tableau ou un dictionnaire comme dans la mémoïsation.
<div class="couleur_puce13" markdown="1">

* Les performances sont semblables à celles de la fonction mémoïsée, une exécution en temps linéaire, proportionnel à $~n$, et une occupation mémoire de taille $~n$.
