# <center><div class = "titre1">Variables locales et variables globales</div></center>

On considère le programme suivant :

```python
def fct():
    i = 5

fct()

```       

Après avoir exécuté le programme ci-dessus, si l'on détermine la valeur référencée par la variable `#!python i` en utilisant la console, nous avons droit à une erreur : 

```python
>>> i
NameError: name 'i' is not defined
```

Pourquoi cette erreur ? La variable `#!python i` est bien définie dans la fonction `#!python fct()` et la fonction `#!python fct()` est bien exécutée, où est donc le problème ?
<span style="display: block; margin: 8px 0 0 0;">En fait, la variable `#!python i` est une variable dite __locale__ : elle a été définie dans une fonction et elle "restera" dans cette fonction. Une fois que l'exécution de la fonction sera terminée, la variable `#!python i` sera "détruite" (supprimée de la mémoire). Elle n'est donc pas accessible depuis "l'extérieur" de la fonction (ce qui explique le message d'erreur que nous obtenons).</span>

??? book "__Définition__"
	Les variables définies dans une fonction sont appelées variables __locales__. Elles ne peuvent être utilisées que localement c’est-à-dire qu’à l’intérieur de la fonction qui les a définies.  
	<span style="display: block; margin: 8px 0 0 0;">Tenter d’appeler une variable locale depuis l’extérieur de la fonction qui l’a définie provoquera une erreur.</span>
	<span style="display: block; margin: 8px 0 0 0;">Cela est dû au fait que chaque fois qu’une fonction est appelée, Python réserve pour elle (dans la mémoire de l’ordinateur) un nouvel espace de noms (c’est-à-dire une sorte de dossier virtuel). Les contenus des variables locales sont stockés dans cet espace de noms qui est inaccessible depuis l’extérieur de la fonction.</span>
	<span style="display: block; margin: 8px 0 0 0;">Cet espace de noms est automatiquement détruit dès que la fonction a terminé son travail, ce qui fait que les valeurs des variables sont réinitialisées à chaque nouvel appel de fonction.</span>
	
Autre exemple de cette notion de variable locale :

```python
i = 3

def fct():
    i = 5

fct()

```      

Après avoir exécuté le programme ci-dessus, si l'on détermine la valeur référencée par la variable `#!python i`, nous obtenons :

```python
>>> i
3 
```

Cette fois pas d'erreur, mais à la fin de l'exécution de ce programme, la variable `#!python i` référence la valeur `#!python 3`. En fait dans cet exemple nous avons 2 variables `#!python i` différentes : la variable `#!python i` __globale__ (celle qui a été définie en dehors de toute fonction) et la variable `#!python i` __locale__ (celle qui a été définie dans la fonction). Ces 2 variables portent le même nom, mais sont différentes.

??? book1 "__Définition__"
	Les variables définies dans l’espace global du script, c’est-à-dire en dehors de toute fonction sont appelées des variables __globales__.  
	<span style="display: block; margin: 8px 0 0 0;">Ces variables sont accessibles (= utilisables) à travers l’ensemble du script et accessible en lecture seulement à l’intérieur des fonctions utilisées dans ce script.</span>
	<span style="display: block; margin: 8px 0 0 0;">Ainsi, une fonction va pouvoir utiliser la valeur d’une variable définie globalement mais __ne va pas pouvoir modifier sa valeur__ c’est-à-dire la redéfinir. En effet, toute variable définie dans une fonction est par définition locale ce qui fait que si on essaie de redéfinir une variable globale à l’intérieur d’une fonction, on ne fera que créer une autre variable de même nom que la variable globale qu’on souhaite redéfinir mais qui sera locale et bien distincte de cette dernière.</span>

Une variable __globale__ peut donc être "utilisée" à l'intérieur d'une fonction :
<span style="display: block; margin: 8px 0 0 0;">Analysez et testez le programme suivant :</span>

```python
i = 3

def fct():
    print(i)

fct()

```        

Quand on cherche à utiliser une variable dans une fonction, le système va d'abord chercher si cette variable se "trouve" dans l'espace local de la fonction, puis, s'il ne la trouve pas dans cet espace local, le système va aller rechercher la variable dans l'espace global. 
<span style="display: block; margin: 8px 0 0 0;">Pour le `#!python print(i)` situé dans la fonction, le système ne trouve pas de variable `#!python i` dans l'espace local de la fonction `#!python fct`, il passe donc à l'espace global et trouve la variable `#!python i` (nous avons donc `#!python 3` qui s'affiche).</span>
<span style="display: block; margin: 8px 0 0 0;">Il est important de bien comprendre que si le système avait trouvé une variable `#!python i` dans l'espace local de la fonction, la "recherche" de la variable `#!python i` se serait arrêtée là.</span>
<span style="display: block; margin: 8px 0 0 0;">Analysez et testez le programme suivant :</span>

```python
i = 3

def fct():
    i = 5
    print(i)

fct()

```    

Puis analysez et testez le programme suivant :

```python
i = 3

def fct():
    i = i + 1

fct()

```           

Nous avons une erreur :

```python
UnboundLocalError: local variable 'i' referenced before assignment
```

En effet, nous avons vu plus haut qu'on ne pouvait pas modifier la valeur d'une variable globale à l'intérieur d'une fonction.  
Pourtant, dans certaines situations, il serait utile de pouvoir modifier cette valeur depuis une fonction.
<span style="display: block; margin: 8px 0 0 0;">Cela est possible en Python, il suffit d’utiliser le mot clé `#!python global` devant le nom d’une variable globale utilisée localement afin d’indiquer à Python qu’on souhaite bien modifier le contenu de la variable globale et non pas créer une variable locale de même nom.</span>
<span style="display: block; margin: 8px 0 0 0;">Analysez le programme suivant et déterminez la valeur référencée par la variable `#!python i` en utilisant la console :</span>

```python
i = 3

def fct():
    global i
    i = i + 1

fct()

```    

En fait, l'utilisation de `#!python global` est en général une mauvaise pratique, car cette utilisation peut entrainer des "effets de bord".

??? book2 "__Définition__"
	On parle __d'effet de bord__ quand une fonction modifie l'état d'une variable globale. 

Dans notre exemple ci-dessus la fonction `#!python fct` modifie bien la valeur référencée par la variable $~$ `#!python i` : avant l'exécution de `#!python fct`, la variable `#!python i` référence la valeur `#!python 3`, après l'exécution de la fonction `#!python fct` la variable `#!python i` référence la valeur `#!python 4`. Nous avons donc bien un effet de bord.
<span style="display: block; margin: 8px 0 0 0;">Autre exemple plus "classique" (sans avoir à utiliser le `#!python global`) d'un effet de bord en Python :</span>

```python
t = [1, 2, 3]

def fct():
    t.append(4)

fct()

```        

Après avoir exécuté le programme ci-dessus, déterminez la valeur référencée par la variable `#!python t` en utilisant la console.
<span style="display: block; margin: 8px 0 0 0;">Nous avons bien ci-dessus un effet de bord puisque le tableau `#!python t` est modifié par une fonction</span>
<span style="display: block; margin: 8px 0 0 0;">Les effets de bord c'est "mal" ! Mais pourquoi est-ce "mal" ?</span>
<span style="display: block; margin: 8px 0 0 0;">Les effets de bords provoquent parfois des comportements non désirés par le programmeur (évidemment dans des programmes très complexes, pas dans des cas simplistes comme celui que nous venons de voir précédemment). Ils rendent aussi parfois les programmes difficilement lisibles (difficilement compréhensibles). À cause des effets de bord, on risque de se retrouver avec des variables qui référenceront des valeurs qui n'étaient pas prévues par le programmeur. On dit aussi qu'à un instant donné, l'état futur des variables est difficilement prévisible à cause des effets de bord.</span>
<span style="display: block; margin: 8px 0 0 0;">Un paradigme de programmation se propose d'éviter au maximum les effets de bords : <a href="https://fr.wikipedia.org/wiki/Programmation_fonctionnelle" target="_blank">__la programmation fonctionnelle__</a>.</span>
<center markdown = "1">
<div class="encadré3_AM_d">
Synthèse
</div>
</center>

Voilà en résumé ce qu'il faut retenir sur les variables locales et globales: 

!!! notes1 "__Définition__"
	Par définition, une variable est __locale__ si elle est déclarée à l'intérieur d'un sous-programme. Elle est __globale__ dans le cas contraire. 

!!! notes2 "__Portée__"
	Une __variable globale__ est utilisable par tous les sous-programmes contenus dans le fichier où elle est déclarée.  

	Une __variable locale__, au contraire, n'est utilisable qu'à l'intérieur du sous-programme dans lequel elle est déclarée. 

!!! notes1 "__Durée de vie__"
	La durée de vie d'une __variable globale__ est égale à celle du programme. La zone mémoire allouée pour cette variable lui reste allouée tant que le programme s'exécute.  
	<span style="display: block; margin: 8px 0 0 0;">La durée de vie d'une __variable locale__ est celle d'une exécution du sous-programme dans lequel elle est déclarée. Elle peut donc avoir plusieurs vies : elle renait chaque fois que le sous-programme s'exécute et meurt chaque fois qu'il se termine.</span>

!!! notes2 "__Déclarations locales multiples__"
	Si une "même" variable est déclarée dans plusieurs sous-programmes, tout se passe comme si on avait donné des noms de variables distincts pour ces différentes déclarations. Autrement dit, chaque déclaration engendre une variable totalement indépendante des autres. 

!!! notes1 "__Déclaration simultanée en local et en global__"
	Si une "même" variable est déclarée en local et en global :
	<div class="couleur_puce43">

    * Dans les sous-programmes où cette variable n'est pas déclarée, c'est la déclaration globale qui est prise en compte.
    * A l'intérieur des sous-programmes ou cette variable est déclarée, c'est la déclaration locale qui est prise en compte.
    
    </div>
