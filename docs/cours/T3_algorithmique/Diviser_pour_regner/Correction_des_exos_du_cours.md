# <center><div class = "titre2"> Correction de l'exercice du cours </div></center>

<div class="list1_1" markdown="1">

1. Il est utile de se rappeler que la parité d'un nombre se teste en comparant son reste dans la division entière par 2 avec 0. Il faut par ailleurs prendre garde à utiliser des divisions entières lorsque `#!python a` décroît, pour préserver son type entier.
```python
def exp_rap(a, n):
    if n == 0:
        return 1
    if n % 2 == 0:
        return exp_rap(a * a, n // 2)
    return a * exp_rap(a * a, (n - 1) // 2)
    
```
2. Les appels récursifs sont simulés à l'aide d'une boucle. Celle-ci est du type <span style="font-family: 'Trebuchet MS';font-weight: bold">while</span> car nous ne connaissons pas le nombre explicite de répétitions nécessaires pour finir le calcul, mais connaissons une condition d'arrêt. Un certain nombre de variables doivent être créées, elles serviront à retenir les valeurs courantes des variables du problème. `#!python a` et `#!python n` verront leur valeur évoluer et de nouvelles variables `#!python aloc` et `#!python nloc` contenant leurs valeurs sont nécessaires. Une variable stockant le résultat en cours des calculs, `#!python res`, est également nécessaire.
```python
def expo_rapide(a, n):
    aloc = a
    nloc = n
    res = 1
    while nloc > 0:
        if nloc % 2 == 0:
            aloc = aloc * aloc
            nloc = nloc // 2
        else:
            res = res * aloc
            aloc = aloc * aloc
            nloc = (nloc -1) // 2
    return res
    
```

</div>
