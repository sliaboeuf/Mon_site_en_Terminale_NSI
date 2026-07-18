# <center><div class = "titre2"> Correction des exercices sur la portée des variables</div></center>

### <div class = "encadré_exo"> __Correction de l'exercice 1__ </div>

Il y a 3 variables qui interviennent dans la fonction `#!python f` :
<div class="couleur_puce14" markdown="1">

 * `#!python a` qui a une portée globale (puisque déclarée en tant que telle dans la fonction)
 * `#!python b` qui a elle aussi une portée globale (puisqu'elle n'est pas redéclarée dans la fonction)
 * `#!python c` qui a une portée locale (puisqu'elle est déclarée dans la fonction)

</div>

!!! a-retenir "__A retenir__"
	__La déclaration locale est prioritaire sur la déclaration globale__.  
	Autrement dit :  
	<div class="couleur_puce20" markdown="1">

	* Si une variable globale est redéclarée à l'intérieur d'un sous-programme alors c'est la déclaration locale qui l'emporte (c'est le cas de la variable `#!python c` de cet exercice), sauf s'il est précisé qu'elle doit rester globale (comme pour la variable `#!python a` de cet exercice).
	* Si une variable globale est utilisée à l'intérieur d'un sous-programme dans lequel elle n'est pas redéclarée, c'est la déclaration globale qui est prise en compte (c'est la cas de la variable `#!python b` de cet exercice).

	</div>

### <div class = "encadré_exo"> __Correction de l'exercice 2__ </div>
Dans le premier programme, la valeur de la variable `#!python b` est modifiée après l'appel `#!python f(a)` puisque `#!python b` est déclarée en tant que variable globale. On a `#!python b = 4` avant cet appel et `#!python b  = 10` après.  
<span style="display: block; margin: 8px 0 0 0;"> Dans le second programme, la variable `#!python b` qui se trouve dans le corps de la fonction `#!python f` est locale à cette fonction donc la valeur de la variable globale `#!python b` ne s'en trouve pas modifiée.</span>

### <div class = "encadré_exo"> __Correction de l'exercice 3__ </div>

Il faut commencer par évaluer `#!python f(6)` : la variable `#!python v` est locale à `#!python f`, l'appel `#!python f(6)` renvoie donc `#!python g(6) + 1` au programme principal. 
<span style="display: block; margin: 8px 0 0 0;">Il s'agit ensuite d'évaluer l'appel `#!python g(6)` : `#!python v` est déclarée en tant que variable globale et prend pour valeur `#!python 1000`. L'appel `#!python g(6)` renvoie alors `#!python 12` au programme principal.</span>
<span style="display: block; margin: 8px 0 0 0;">Ainsi `#!python f(6)` vaut donc `#!python 12 + 1 = 13`.</span>
<span style="display: block; margin: 8px 0 0 0;">On ajoute alors `#!python v` qui vaut à présent `#!python 1000` et `#!python a` qui vaut `#!python 3`.</span>
<span style="display: block; margin: 8px 0 0 0;">Le programme affiche donc `#!python 1016`.</span>


