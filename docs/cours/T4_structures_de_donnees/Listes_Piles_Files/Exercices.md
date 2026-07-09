# <center><div class = "titre2"> Exercices </div></center>

!!! tip "__Remarques__"
	Dans tous les exercices qui suivent :
	<div class = "couleur_puce36">

	* Lorsqu'on donne la liste des éléments d'une pile ou d'une file, l'élément situé le plus à droite de cette liste correspond à l'élément inséré en dernier (donc en sommet de pile ou en queue de file).
	* On n’utilisera que l’interface fournie par les classes `#!python Pile` et `#!python File` et pas les opérateurs spécifiques aux listes.

	</div>

### <div class = "encadré_exo"> __Exercice 1__ </div>
<div class="list1_1" markdown="1">

1. Ecrire une fonction qui renvoie le $n$-ième élément d’une pile. 
<span style="display: block; margin: 3px 0 0 0;">On s’assurera que la pile, en sortie, contient toujours les mêmes éléments. (Indication : on pourra utiliser une deuxième pile).
<span style="display: block; margin: 3px 0 0 0;">On prévoira le cas où la pile n’est pas de taille suffisante pour qu’un tel élément existe.</span>
2. Ecrire une fonction qui recherche un élément dans une pile. 
<span style="display: block; margin: 3px 0 0 0;">Cette fonction booléenne renverra `#!python True` ou `#!python False` suivant que l'élément est présent ou non dans la pile.</span>
<span style="display: block; margin: 3px 0 0 0;">On s’assurera que la pile, en sortie, contient toujours les mêmes éléments.</span>
3. Ecrire une fonction qui concatène deux piles dans une troisième pile, autrement dit qui renvoie une pile constituée des éléments des 2 piles entrées en paramètres de la fonction, ces deux piles contenant les mêmes éléments en sortie.
4. Ecrire une fonction qui prend une pile non vide en argument et place l’élément situé à son sommet tout au fond de la pile, en conservant l’ordre des autres éléments.

</div>
<center>
[Correction de l'exercice 1 :material-cursor-default-click:](Correction.md#correction-de-lexercice-1){:target="_blank" .md-button}
</center>

### <div class = "encadré_exo"> __Exercice 2__ </div>

On se donne une pile `#!python P1` contenant des entiers positifs.
<div class="list1_1" markdown="1">

1. Ecrire une fonction qui déplace les entiers de `#!python P1` dans une pile `#!python P2` de façon à avoir dans `#!python P2` tous les nombres pairs en dessous des nombres impairs.
2. Ecrire une fonction qui copie dans `#!python P2` les nombres pairs contenus dans `#!python P1`. 
<span style="display: block; margin: 3px 0 0 0em;">Le contenu de `#!python P1` après exécution de la fonction doit être identique à celui avant exécution.</span> 
<span style="display: block; margin: 3px 0 0 0em;">Les nombres pairs de `#!python P2` doivent être dans l'ordre où ils apparaissent dans `#!python P1`.</span>

</div>

<center>
[Correction de l'exercice 2 :material-cursor-default-click:](Correction.md#correction-de-lexercice-2){:target="_blank" .md-button}
</center>

### <div class = "encadré_exo"> __Exercice 3__ </div>
__Inversion d'une file en utilisant une pile.__
<div></div>
Le but de cet exercice est d’écrire en Python une procédure qui inverse une file d'éléments qui lui est passée en paramètre.
<span style="display: block; margin: 3px 0 0 0;">On demande de ne pas utiliser de tableau ou de liste de travail pour effectuer l'inversion, mais d'utiliser plutôt une pile.</span>
<span style="display: block; margin: 3px 0 0 0;">Il existe en effet une méthode très simple pour inverser une file en utilisant une pile.</span>

<center>
[Correction de l'exercice 3 :material-cursor-default-click:](Correction.md#correction-de-lexercice-3){:target="_blank" .md-button}
</center>

### <div class = "encadré_exo"> __Exercice 4__ </div>

Un problème fréquent pour les compilateurs et les traitements de textes est de déterminer si les parenthèses d’une chaîne de caractères sont équilibrées et proprement incluses les unes dans les autres.  
<span style="display: block; margin: 8px 0 0 0;">On désire donc écrire une fonction qui teste la validité du parenthésage d’une expression :</span>
<div class = "couleur_puce19" markdown="1">

* On considère que les expressions suivantes sont valides : `#!python "()"`, `#!python "[([bonjour+]essai)7plus- ]"`.
* Alors que les suivantes ne le sont pas : `#!python "("`, `#!python ")("`, `#!python "4(essai]"`.

</div>

Notre but est donc d’évaluer la validité d’une expression en ne considérant que ses parenthèses et ses crochets. On suppose que l’expression à tester est dans une chaîne de caractères, dont on peut ignorer tous les caractères autres que `#!python ‘(’`, `#!python ‘[’`, `#!python ’]’` et `#!python ‘)’`.  
<span style="display: block; margin: 8px 0 0 0;">Écrire en Python la fonction `valide` qui renvoie `#!python True` si l’expression passée en paramètre est valide, `#!python False` sinon.</span>

<center>
[Correction de l'exercice 4 :material-cursor-default-click:](Correction.md#correction-de-lexercice-4){:target="_blank" .md-button}
</center>

### <div class = "encadré_exo"> __Exercice 5__ </div>
<div class="list1_1" markdown="1">

1. Écrire une fonction `#!python melange(P1, P2)` qui prend en argument deux piles `#!python P1` et `#!python P2` et qui mélange leurs éléments dans une troisième pile `#!python P3` de la façon suivante : tant qu’une pile au moins n’est pas vide, on retire aléatoirement un élément du sommet d’une des deux piles et on l’empile sur `#!python P3`. La fonction renvoie `#!python P3`.
</div>
<div class = "decal1" markdown="1">

!!! tip "__Remarque__"
	A l’issue du mélange, les deux piles `#!python P1` et `#!python P2` sont vides.

</div>
<div class="list1_2" markdown="1">

2. Écrire une fonction `#!python couper(P)` qui prend une pile `#!python P` et qui retire de son sommet `#!python k` éléments qui sont replacés dans une autre pile `#!python autre_P`. `#!python k` est un nombre tiré au hasard et si `#!python k` est supérieur au nombre d’éléments de `#!python P`, on retire simplement tous les éléments de `#!python P`.
<span style="display: block; margin: 8px 0 0 0;">Par exemple, si `#!python P` contient les nombres `#!python 1, 2, 3, 4, 5` et si `#!python k = 2`, alors `#!python autre_P` contient les nombres `#!python 5, 4`.</span>
La fonction renvoie `#!python autre_P`.
3. __Tour de magie de Gilbreath__.

</div>
<div class="list1_a" markdown="1">

1. Construire une liste de `#!python n` cartes, par exemple `#!python [9, 10, "reine", "roi", "as"]`.
2. Empiler `K` fois cette liste de `#!python n` cartes dans une pile `#!python P`.
3. Couper alors cette pile avec la fonction `#!python couper`, puis mélanger les deux piles obtenues avec la fonction `#!python melange`.
<span style="display: block; margin: 5px 0 0 0;">On observe alors que la pile finale est constituée de `#!python K` blocs contenant toutes les `#!python n` cartes de la liste initiale (même si ces dernières peuvent apparaître dans un ordre différent au sein de chaque bloc).</span>

</div>

<center>
[Correction de l'exercice 5 :material-cursor-default-click:](Correction.md#correction-de-lexercice-5){:target="_blank" .md-button}
</center>

### <div class = "encadré_exo"> __Exercice 6__ </div>

Un palindrome est une chaîne de caractères qui se lit de la même manière de gauche à droite et de droite à gauche.
<span style="display: block; margin: 5px 0 0 0;">En utilisant une pile et une file, écrire un programme qui détermine si une chaîne de caractères est un palindrome.</span>
<span style="display: block; margin: 5px 0 0 0;">On veillera à ce que la chaîne de caractères passée en argument de la fonction ne sera parcourue qu’une seule fois. L’algorithme doit donner en sortie `#!python True` ou `#!python False` selon le cas.</span>

<center>
[Correction de l'exercice 6 :material-cursor-default-click:](Correction.md#correction-de-lexercice-6){:target="_blank" .md-button}
</center>

### <div class = "encadré_exo"> __Exercice 7__ </div>
<div class="list1_1" markdown="1">

1. Montrer comment implémenter une file à l'aide de deux piles. L'implémentation se limitera ici à un constructeur, à la méthode d'affichage et aux méthodes `#!python enfiler` et `#!python defiler`.
2. Montrer comment implémenter une pile à l'aide de deux files. L'implémentation se limitera ici à un constructeur, à la méthode d'affichage et aux méthodes `#!python empiler` et `#!python depiler`.

</div>

<center>
[Correction de l'exercice 7 :material-cursor-default-click:](Correction.md#correction-de-lexercice-7){:target="_blank" .md-button}
</center>
