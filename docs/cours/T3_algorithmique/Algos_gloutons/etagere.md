# <center><div class = "titre5">Le problème des étagères</div></center>

## <div class = "encadré2_TP">__Consigne__</div>

Une bibliothèque prévoit de refaire ses étagères.
<span style="display: block; margin: 10px 0 0 0;">Les contraintes sont les suivantes :</span>
<div class="couleur_puce22" markdown="1">

* Elle comprend une collection de `#!python n` livres `#!python b1, b2, ... , bn`.
* Chaque livre `#!python bi` a une largeur `#!python wi`.
* Les livres doivent être rangés dans l’ordre fixé (par valeur de `#!python i` croissante) sur des étagères de largueur `#!python L`.

</div>

## <div class = "encadré2_TP">__Exercice 1__</div>

**Proposer un algorithme glouton pour le rangement des étagères.**

Votre algorithme prend en paramètres une liste des livres, dont on connaît la largeur et retourne la double liste des étagères.
<span style="display: block; margin: 10px 0 0 0;">Chaque étagère contient donc différents livres.</span>
<span style="display: block; margin: 10px 0 0 0;">Par exemple avec les livres :</span>

| Livre     | 0     | 1     | 2     | 3     |
|:---------:|:-----:|:-----:|:-----:|:-----:|
| Largeur   | 4     | 6     | 2     | 3     |

et la largeur d'étagère `#!python L = 9`, on obtient : `#!python etageres = [[0], [1, 2], [3]]`
<div class="couleur_puce22" markdown="1">

* En effet, au premier étage, on peut ranger le premier livre mais pas y ajouter le second, il ne reste plus assez de place.
* Au second étage, on peut ranger le second et le troisième livre.
* Au troisième étage, on range le dernier.

</div>

## <div class = "encadré2_TP">__Exercice 2__</div>
<div class="list8_1" markdown="1">

1. Télécharger le script Python [etageres.py](scripts/etageres.py).
2. Compléter la fonction de signature `#!python generer_livres(n: int) -> list` qui prend en paramètre un nombre entier `#!python n` et renvoie une liste de `#!python n` livres dont la largeur est un entier aléatoire entre `#!python LARGEUR_MIN` et `#!python LARGEUR_MAX`.
<span style="display: block; margin: 3px 0 0 0;">N'oubliez pas de documenter la fonction.</span>
3. Télécharger le script Python [tester_etageres.py](scripts/tester_etageres.py).
<span style="display: block; margin: 3px 0 0 0;">Ce script contient des tests de vos fonctions.</span>
<span style="display: block; margin: 3px 0 0 0;">Ces tests lèvent des exceptions chaque fois qu'une condition imposée n'est pas remplie.</span>
4. Exécuter ce script. Il doit lever une exception car vous n'avez pas complété la deuxième fonction, c'est normal.
<span style="display: block; margin: 3px 0 0 0;">Par contre, le premier test doit fonctionner et vous devez lire le message : `#!python test generer_livres : ok`.</span>
5. Si le test précédent ne fonctionne pas, revenir en <span style="color: #fe6e2b;">2</span>.

</div>

## <div class = "encadré2_TP">__Exercice 3__</div>
<div class="list8_1" markdown="1">

1. Compléter la fonction de signature `#!python ranger_livres(livres: list) -> list`.
<span style="display: block; margin: 3px 0 0 0;">Elle prend en paramètre une liste de livres intitulée `livres`.</span>
<span style="display: block; margin: 3px 0 0 0;">Elle renvoie la double liste des étagères décrite plus haut.</span>
2. Exécuter à nouveau le script <span style="font-family: 'Trebuchet MS' ; font-weight: bold">tester_etageres.py</span>.
<span style="display: block; margin: 3px 0 0 0;">Cette fois vous ne devez plus avoir d'erreur du tout et vous devez lire le message `#!python test ranger_livres: ok`.</span>
3. Si vous avez encore des erreurs, revenir en <span style="color: #f3183c; font-weight: bold;">1</span>.

</div>

## <div class = "encadré2_TP">__Complément : rédiger un jeu de tests__</div>

Parmi les compétences importantes en informatique, être capable de générer
du code qui ne plante pas est fondamental.
<span style="display: block; margin: 10px 0 0 0;">Cela nécessite bien sûr une certaine maîtrise mais aussi de l'organisation. Il faut tester ses fonctions.</span>
<span style="display: block; margin: 10px 0 0 0;">Examinons ensemble le code d'un des tests utilisé plus haut.</span>

```python
def tester_generer_livres():
    nombre = 10
    livres = generer_livres(nombre)
    assert len(livres) == nombre, "le nombre de livres est incorrect"
    ...
```

Dans cette fonction on choisit un nombre arbitraire de livres (10) et on génère une liste des livres.
<span style="display: block; margin: 10px 0 0 0;">On commence par tester avec `#!python assert` qu'il y a le bon nombre de livres.</span>
<span style="display: block; margin: 10px 0 0 0;">La syntaxe est :</span>

```python
assert booleen, string
```
<div class="couleur_puce22" markdown="1">

* `#!python booleen` : le test qu'on veut réaliser, ici `#!python len(livres) == nombre`
* `#!python string` est un paramètre optionnel. C'est le message d'erreur : `#!python "le nombre de livres est incorrect"`

</div>
Lorsqu'on exécute cette fonction, on s'assure Python vérifie que le booléen est vrai. S'il est faux, il affiche un message d'erreur accompagné de la `#!python string`.
<span style="display: block; margin: 10px 0 0 0;">La suite du code est similaire, on s'assure que tous les livres ont une taille convenable.</span>
