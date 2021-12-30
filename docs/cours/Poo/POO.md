# <center><div class = "titre1_POO">La programmation orientée objet</div> </center>

## <div class = "encadré1_POO">__Paradigme de programmation__</div>

!!! note1 "D'après Wikipédia :"
    __Un paradigme de programmation est une façon d'approcher la programmation informatique et de traiter les solutions aux
    problèmes et leur formulation dans un langage de programmation approprié.__

Jusqu'à présent nous avons vu un seul paradigme de programmation : la __programmation procédurale__ (ou __impérative__).

## <div class = "encadré2_POO">__Programmation procédurale__</div>

La programmation __procédurale__, dite aussi programmation __impérative__, est celle que vous avez utilisée jusqu'à maintenant, elle repose donc sur des notions qui vous sont familières :
<div class="couleur_puce1etoi">

*  La séquence d'instructions (les instructions d'un programme s'exécutent l'une après l'autre).
*  L'affectation (on attribue une valeur à une variable, par exemple : `#!python a = 5`).  
*  L'instruction conditionnelle (`#!python if` / `#!python else`).  
*  La boucle (`#!python while` et `#!python for`).  

</div>
Elle consiste aussi à diviser un programme en blocs réutilisables appelés fonctions.

Vous essayez autant que possible de garder votre code en blocs modulaires, en décidant de manière logique quel bloc est appelé. Cela demande moins d’efforts pour visualiser ce que votre programme fait et rend plus facile la maintenance du code puisque vous pouvez voir ce que fait une portion de code. Le fait d’améliorer une fonction (qui est réutilisée) peut améliorer la performance à plusieurs endroits dans votre programme.

Il y a donc des variables, qui contiennent vos données, et des fonctions. Vous passez vos variables à vos fonctions – qui agissent sur elles et peut-être les modifient. L'interaction entre les variables et les fonctions n'est pas toujours simple à gérer : les variables locales, globales, les effets de bords que provoquent certaines fonctions qui modifient des variables globales sont souvent source de bugs difficiles à déceler.

On touche ici aux limites de la programmation procédurale, lorsque le nombre de fonctions et de variables devient important.

La programmation impérative est loin d'être le seul paradigme de programmation (même si c'est sans doute le plus courant). Cette année nous allons étudier deux autres paradigmes : le **paradigme objet** et le **paradigme fonctionnel**. 

## <div class = "encadré3_POO">__Les objets : un moyen de séparer la conception de l’utilisation__</div>

La programmation orientée objet repose, comme son nom l'indique, sur le concept d'objet.

Un objet dans la vie de tous les jours, vous connaissez, mais en informatique, qu'est-ce que  
c'est ? 
Une variable ? Une fonction ? Ni l'un ni l'autre, c'est un nouveau concept.

Imaginez un objet (de la vie de tous les jours) très complexe (par exemple un moteur de voiture) : il est évident qu'en regardant cet objet, on est frappé par sa complexité (pour un non spécialiste). Imaginez que l'on enferme cet objet dans une caisse et que l'utilisateur de l'objet n'ait pas besoin d'en connaître son principe de fonctionnement interne pour pouvoir l'utiliser. L'utilisateur a, à sa disposition, des boutons, des manettes et des écrans de contrôle pour faire fonctionner l'objet, ce qui rend son utilisation relativement simple. La mise au point de l'objet (par des ingénieurs) a été très complexe, en revanche son utilisation est relativement simple. Programmer de manière orientée objet, c'est un peu reprendre cette idée : utiliser des objets sans se soucier de leur complexité interne. Pour utiliser ces objets, nous n'avons pas à notre disposition des boutons, des manettes ou encore des écrans de contrôle, mais des __attributs__ et des __méthodes__ (nous aurons l'occasion de revenir longuement sur ces 2 concepts). Un des nombreux avantages de la programmation orientée objet (__POO__), est qu'il existe des milliers d'objets (on parle plutôt de classes, mais là aussi nous reviendrons sur ce terme de classe un peu plus loin) prêts à être utilisés (vous en avez déjà utilisés de nombreuses fois sans le savoir). On peut réaliser des programmes extrêmement complexes uniquement en utilisant des classes préexistantes.

**Objets et POO sont au centre de la manière dont Python fonctionne**. Il n'est pas obligatoire d'utiliser la __POO__ dans un programme - mais comprendre le concept est essentiel pour devenir plus qu'un débutant. Et notamment parce que vous aurez besoin d'utiliser les classes et objets fournis par la librairie standard.

Ainsi, en manipulant les tableaux en python, vous avez certainement remarqué qu'il y a deux syntaxes pour appeler des fonctions :

```python
tableau = [1, 3, 5, 8]
taille = len(tableau)
tableau.append(11)
```
<div class="couleur_puce11">

* Le calcul de la longueur du tableau se fait par l'appel à la fonction `#!python len()` avec une syntaxe identique aux fonctions que vous avez l'habitude d'écrire.
* L'ajout d'un élément dans le tableau est un peu différent car la fonction `#!python append` semble provenir du tableau lui même : dans ce cas, on ne parle pas de fonction mais de méthode associée à l'objet tableau.

</div>
Un __objet__ est une structure de données qui intègre des variables (que l'on nomme __propriétés__) et des fonctions (que l'on nomme __méthodes__). Nous allons voir l'intérêt de cette approche, omniprésente dans Python, en particulier lorsqu'on développe des interfaces graphiques, mais avant quelques petits repères historiques et éléments de contexte.

## <div class = "encadré4_POO">__Petit historique__</div>

La notion de programmation orientée objet remonte aux années 1960. _Simula_ est considéré comme le premier langage de programmation orienté objet.

Les années 1970 voient les principes de la programmation par objet se développer et prendre forme au travers notamment du langage _Smalltalk_.

À partir des années 1980, commence l'effervescence des langages à objets : _Objective C_ (début des années 1980, utilisé sur les plateformes Mac et iOS), _C++_ (C with classes) en 1983 sont les plus célèbres.

Les années 1990 voient l'âge d'or de l'extension de la programmation par objet dans les différents secteurs du développement logiciel, notemment grâce à l'émergence des systèmes d'exploitation basés sur une interface graphique (MacOS, Linux, Windows) qui font appel abondamment aux principes de la __POO__.

## <div class = "encadré5_POO">__Les classes__</div>

Dans la vie réelle, un objet ne sort pas de nulle part. En effet, chaque objet est défini selon des caractéristiques et un plan bien précis. En __POO__, ces informations sont contenues dans ce qu'on appelle des __classes__.

Prenons un exemple très simple : les gâteaux et leur moule. Le moule est unique. Il peut produire une quantité infinie de gâteaux. Dans ce cas-là, les gâteaux sont les _objets_ et le moule est la _classe_ : le moule va définir la forme du gâteau. La classe contient donc le plan de fabrication d'un objet et on peut s'en servir autant qu'on veut afin d'obtenir une infinité d'objets.

Une classe est une entité regroupant des variables et des fonctions que tout objet issu de cette classe possédera.
<div class = "couleur_puce12">

!!! book "Un peu de vocabulaire autour de cette notion de classe :"

    * Le type de données avec ses **caractéristiques** et ses **actions** possibles s’appelle **classe**.
    * Les **caractéristiques** (ou **variables**) de la classe s’appellent les **attributs**.  
    * Les **actions** possibles à effectuer avec la classe s’appellent les **méthodes**.  
    * La classe définit donc les **attributs** et les actions possibles sur ces attributs, les **méthodes**.
    * Un objet du type de la classe s’appelle une **instance de la classe** et la création d’un objet d’une classe s’appelle une **instanciation de cette classe**.
    * Lorsqu’on définit les attributs d’un objet de la classe, on parle aussi d’instanciation.
    * On dit que les attributs et les méthodes sont **encapsulés** dans la classe.

</div>
Python permet d’utiliser la programmation procédurale mais il permet aussi d’utiliser la __POO__. Il est même possible, comme nous le verrons plus loin, d’utiliser les 2 manières de programmer dans un même programme.

La création d’une classe en python commence toujours par le mot `#!python class`. Ensuite toutes les instructions de la classe seront indentées :


```python
class leNomDeMaClasse :
    # instructions de la classe
# La définition de la classe est terminée.
```

## <div class = "encadré6_POO">__Premier programme__</div>

Pour développer toutes ces notions (et d’autres), nous allons écrire un premier programme :

Nous allons commencer par écrire une classe `#!python personnage` (qui sera dans un premier temps une coquille vide) et, à partir de cette classe créer 2 instances : `#!python darkVador` et `#!python lukeSkywalker`.

Ensuite ils vont se combattre...


---
<div class ="viewPort">
<div class="monTitre">
Exercice 1
</div>
<div class="cylon_eye"></div>
</div>

Analysez et testez ce code :

{{ IDEv('ex1') }}

---

## <div class = "encadré7_POO">__Les attributs__</div>

Pour l’instant, notre classe ne sert à rien et nos instances d’objet ne peuvent rien faire. Comme il n’est pas possible de créer une classe totalement vide, nous avons utilisé l’instruction `#!python pass` qui ne fait rien. Ensuite nous avons créé 2 instances de la classe `#!python personnage` : `#!python darkVador` et `#!python lukeSkywalker`.

Comme nous l'avons vu précédemment, une instance de classe possède des attributs et des méthodes. Commençons par les attributs :

__Un attribut est une variable spécifique à la classe.__

Nous allons associer un attribut `#!python vie` à notre classe `#!python personnage` (chaque instance aura un attribut `#!python vie`, quand la valeur de `#!python vie` deviendra nulle, le personnage sera mort !)

Ces attributs s’utilisent comme des variables, l’attribut `#!python vie` pour `#!python lukeSkywalker` sera noté :


```python
lukeSkywalker.vie
```

De la même façon l’attribut `#!python vie` de l’instance `#!python darkVador` sera noté :


```python
darkVador.vie
```

---
<div class ="viewPort">
<div class="monTitre">
Exercice 2
</div>
<div class="cylon_eye"></div>
</div>

Analysez et testez ce code :

{{ IDEv('ex2') }}

Comme pour une variable, il est possible d'utiliser la console Python pour afficher la valeur référencée par un attribut. Il suffit de taper dans la console `#!python darkVador.vie` ou `#!python lukeSkywalker.vie` (sans avoir oublié d'exécuter le programme au préalable !).

---

__Mais cette façon de faire n'est pas très "propre" et n'est pas une bonne pratique.__

En effet, nous ne respectons pas un principe de base de la __POO__ : l'encapsulation.

Il ne faut pas oublier que notre classe doit être "enfermée dans une caisse" pour que l'utilisateur puisse l'utiliser facilement sans se préoccuper de ce qui se passe à l'intérieur, or, ici, ce n'est pas vraiment le cas.

En effet, les attributs (`#!python darkVador.vie` et `#!python lukeSkywalker.vie`) font parties de la classe et devraient donc être enfermés dans la "caisse" !

## <div class = "encadré8_POO">__Les méthodes__</div>

Pour résoudre ce problème, nous allons définir les attributs, dans la classe, à l'aide d'une méthode d'initialisation des attributs.

Cette méthode est définie dans le code source par la ligne : 

```python
def __init__ (self) :
```

La méthode `#!python __init__` est automatiquement exécutée au moment de la création d’une instance. La variable `#!python self` est obligatoirement le premier argument d’une méthode (nous reviendrons ci-dessous sur ce mot `#!python self`)

Nous retrouvons ce mot `#!python self` lors de la définition des attributs. La définition des attributs sera de la forme :

```python
self.vie = 20
```

Le mot `#!python self` représente l’instance. Quand vous définissez une instance de classe (`#!python darkVador` ou `#!python lukeSkywalker`) le nom de votre instance va remplacer le mot `#!python self`.

Dans le code source, nous allons avoir :

```python
class personnage :
    def __init__ (self) :
        self.vie = 20
```

Ensuite lors de la création de l’instance `#!python darkVador`, python va automatiquement remplacer `#!python self` par `#!python darkVador` et ainsi créer un attribut `#!python darkVador.vie` qui aura pour valeur de départ la valeur donnée à `#!python self.vie` dans la méthode `#!python __init__`

Il se passera exactement la même chose au moment de la création de l’instance `#!python lukeSkywalker`, on aura automatiquement la création de l’attribut `#!python lukeSkywalker.vie`.


---
<div class ="viewPort">
<div class="monTitre">
Exercice 3
</div>
<div class="cylon_eye"></div>
</div>

Analysez et testez ce code :

{{ IDEv('ex3') }}

Utilisez la console Python comme dans l'exercice 2.

---

Le résultat de l'exercice 3 est identique au résultat de l’exemple de l'exercice 2. Mais cette fois nous n’avons pas défini l’attribut `#!python darkVador.vie = 20` ou `#!python lukeSkywalker.vie = 20` en dehors de la classe, nous avons utilisé une méthode `#!python __init__`.

C’est une meilleure pratique.

## <div class = "encadré9_POO">__Passer des paramètres à une instance de classe__</div>

Imaginons que nos 2 personnages n’aient pas au départ les mêmes points de vie ! Pour l’instant, impossible d’introduire cette contrainte (`#!python self.vie = 20`)

Une méthode, comme une fonction, peut prendre des paramètres.

Le passage de paramètres se fait au moment de la création de l’instance.

---
<div class ="viewPort">
<div class="monTitre">
Exercice 4
</div>
<div class="cylon_eye"></div>
</div>

Analysez et testez ce code :

{{ IDEv('ex4') }}

Utilisez la console Python pour vérifier que `#!python darkVador.vie` est égal à `#!python 20` et `#!python lukeSkywalker.vie` est égal à `#!python 15`.

---

Au moment de la création de l’instance `#!python darkVador`, on passe comme argument le nombre de vies (`#!python darkVador = personnage(20)`).

Ce nombre de vies est attribué au premier argument de la méthode `#!python __init__`, la variable `#!python pointDeVie` (`#!python pointDeVie` n’est pas tout à fait le premier argument de la méthode `#!python __init__` puisque devant il y a `#!python self`, mais bon, `#!python self` étant obligatoire, nous pouvons dire que `#!python pointDeVie` est le premier argument non obligatoire).

N.B : `#!python pointDeVie` est bien une variable (car ce n’est pas un attribut de la classe `#!python personnage` puisqu’elle ne commence pas par `#!python self`).

Nous pouvons passer plusieurs arguments à la méthode `#!python __init__` (comme pour n’importe quelle fonction).

Nous allons créer 2 nouvelles méthodes :
<div class="couleur_puce11">

* Une méthode qui enlèvera un point de vie au personnage blessé
* Une méthode qui renverra le nombre de vies restantes
</div>
---
<div class ="viewPort">
<div class="monTitre">
Exercice 5
</div>
<div class="cylon_eye"></div>
</div>

Analysez et testez ce code :

{{ IDEv('ex5') }}

Pour tester ce programme, dans la console, tapez successivement les instructions suivantes :
<div class="couleur_puce11">

* `#!python darkVador.donneEtat()`
* `#!python lukeSkywalker.donneEtat()`
* `#!python darkVador.perdVie()`
* `#!python darkVador.donneEtat()`
* `#!python lukeSkywalker.perdVie()`
* `#!python lukeSkywalker.donneEtat()`
</div>
---


Vous avez sans doute remarqué que lors de "l'utilisation" des instances `#!python lukeSkywalker` et `#!python darkVador`, nous avons uniquement utilisé des méthodes et nous n’avons plus directement utilisé des attributs (plus de `#!python darkVador.vie`).

## <div class = "encadré10_POO">__Encapsulation et interface__</div>

Il est important de savoir que l’utilisation des attributs en dehors de la classe est une mauvaise pratique en programmation orientée objet : les attributs doivent rester "à l'intérieur" de la classe, l’utilisateur de la classe ne doit pas les utiliser directement.

Il peut les manipuler, mais uniquement par l’intermédiaire d’une méthode (la méthode `#!python self.perdVie` permet de manipuler l’attribut `#!python self.vie`).

Les méthodes constituent "l'interface" de l’objet.

Pour l’instant nous avons utilisé les méthodes uniquement en tapant des instructions dans la console, il est évidemment possible d’utiliser ces méthodes directement dans votre programme :

---
<div class ="viewPort">
<div class="monTitre">
Exercice 6
</div>
<div class="cylon_eye"></div>
</div>

Analysez et testez ce code :

{{ IDEv('ex6') }}

Évaluez la variable `#!python point` à l’aide de la console.

---
<div class ="viewPort">
<div class="monTitre">
Exercice 7
</div>
<div class="cylon_eye"></div>
</div>

Nos personnages peuvent boire une potion qui leur ajoute un point de vie. Modifiez le programme de l'exercice 5 en ajoutant une méthode `#!python boirePotion`. Testez ensuite cette modification à l’aide de la console.

{{ IDEv('ex5') }}

---
<div class ="viewPort">
<div class="monTitre">
Exercice 8
</div>
<div class="cylon_eye"></div>
</div>

Analysez et testez ce code :

{{ IDEv('ex8') }}

Évaluez la variable `#!python point` à l’aide de la console.

---
<div class ="viewPort">
<div class="monTitre">
Exercice 9
</div>
<div class="cylon_eye"></div>
</div>

Analysez et testez ce code :

{{ IDEv('ex9') }}

Évaluez la variable `#!python point` à l’aide de la console.

N.B : `#!python random.random()` renvoie une valeur aléatoire comprise entre `#!python 0` et `#!python 1`.

Expliquez le fonctionnement de la méthode `#!python perdVie`.

---

Comme vous l’avez remarqué, il est possible d’utiliser une instruction conditionnelle (`#!python if` / `#!python else`) dans une méthode. Il est donc possible d’utiliser dans le même programme le paradigme objet et le paradigme impératif.

Nous allons maintenant organiser un combat virtuel entre nos personnages :

---
<div class ="viewPort">
<div class="monTitre">
Exercice 10
</div>
<div class="cylon_eye"></div>
</div>

Analysez et testez ce code :

{{ IDEv('ex10') }}

Pour tester le programme, exécutez la fonction `#!python game` dans une console. Vérifiez que l’on peut obtenir des résultats différents en exécutant plusieurs fois la fonction `#!python game`.

Nous avons ici la démonstration qu’il est possible d’utiliser le paradigme objet et le paradigme impératif dans un même programme.


---
<div class ="viewPort">
<div class="monTitre">
Exercice 11
</div>
<div class="cylon_eye"></div>
</div>

Améliorez le programme développé dans l'exercice 10 en modifiant les méthodes et en implémentant les méthodes suivantes :
<div class="list5_1">

1. Dans l’initialisation, on ne peut donner de nom au personnage !

</div>
<div class="list5_a">

1. Créez un attribut `#!python nom` qu’on doit donner en premier paramètre : on crée une instance de `#!python personnage` comme ceci :
    <div class="decal2">
       ```python
       darkVador = personnage("Dark Vador", 20)
       ``` 
</div>
2. Créez une méthode `#!python donneNom` qui renvoie le nom du personnage.

</div>
<div class="list5_2">

2. Modifiez la fonction `#!python game` pour qu’elle tienne compte du nom du personnage.  
<div class="decal2">On doit pouvoir créer d’autres personnages et les messages doivent tenir compte des noms de ceux-ci.
     ```python
     >>> lukeSkywalker = personnage("Luke Skywalker", 20)
     >>> darkMaul = personnage("Dark Maul", 25)
     >>> game(lukeSkywalker, darkMaul)
     Dark Maul est vainqueur, il lui reste encore 3 points de vie alors que Luke Skywalker est mort
     ```
</div>
<div class="decal2">Remarquez bien que la *signature* de la fonction `#!python game` est différente !  
<br>
On doit créer les personnages __avant__ de l’appeler. Il faut changer plusieurs éléments.</div>

</div>
<div class="list5_3">

3. Améliorez encore la fonction `#!python game` pour qu’elle affiche un journal détaillé du combat :  
   <div class="decal2">
    ```python
    >>> hanSolo = Personnage(10)
    >>> jabbaLeHutt = Personnage(10)
    >>> game(hanSolo, jabbaLeHutt)
    Han Solo perd un point de vie
    Jabba le Hutt perd deux points de vie

    ...
    Han Solo perd deux points de vie
    Jabba le Hutt perd deux points de vie
    Han Solo est vainqueur, il lui reste encore 2 points de vie alors que Jabba le Hutt est mort
    ```
</div>

</div>
<div class="list5_4">

4. Revenons à `#!python personnage`.  
   <div class="decal2">On dispose maintenant des méthodes suivantes :
    ```python
    class personnage:
        |
        |  donneEtat
        |     --> int
        |     renvoie le nombre de pts de vie
        |
        |  perdVie
        |     enleve un ou deux points de vie
        |
        |  donneNom
        |     --> str
        |     renvoie le nom du personnage
    ```
</div>
<div class="decal2">On veut créer un attribut `#!python chance` lors de l’instanciation du personnage.  
C’est un entier entre `#!python 0` et `#!python 4`.  
L’effet de la chance est le suivant :
dans la méthode `#!python perdVie`, on tire toujours un nombre aléatoire entre `#!python 0` et `#!python 1`.</div>

</div>
<div class = "couleur_puce13">

* Si ce nombre multiplié par `#!python 10` dépasse la chance du personnage, il perd un point de vie.
* Sinon il ne perd pas de vie et on affiche `#!python "Han Solo a de la chance !"`
</div>
<div class="decal4">

Par exemple, Han Solo a `#!python 2` de chance.
</div>
<div class = "couleur_puce13">

* Dans `#!python perdVie`, on tire `#!python 0.3`,
  `#!python 10 * 0.3 = 3` et `#!python 3 > 2` : il perd un point de vie.
* Dans `#!python perdVie`, on tire `#!python 0.12345`
  `#!python 10 * 0.12345 = 1.2345` et `#!python 1.2345 < 2` : il ne perd pas de vie.
</div>
<div class="decal8">

Il faut aussi changer la méthode `#!python __init__` pour pouvoir créer nos personnages ainsi :

```python
hanSolo = Personnage("Han Solo", 10, 2)
``` 

Implémentez la chance et faites quelques essais.

Attention, si vous donnez une chance trop élevée, le personnage ne perdra jamais de vie et la boucle de la fonction `#!python game` sera infinie !

</div>
<div class="list5_5">

5. Maintenant qu’on peut donner un attribut `#!python chance`, il faut *protéger* le programme.  

</div>
<div class="decal8">

Une valeur de chance trop élevée peut conduire à un programme qui ne termine jamais, il suffit de donner une chance de `#!python 10` pour qu’un personnage soit invicible !

Nous allons créer une méthode interne `#!python __limiterChance` qui empêche la chance d’être supérieure à `#!python 4`.

Si le paramètre `#!python chance` est inférieur ou égal à `#!python 4`, il est inchangé, s’il dépasse `#!python 4`, il est ramené à `#!python 4`.

Cette méthode interne ne sera pas appelée par les éléments extérieurs au programme, seulement par le programme lui-même !

On utilise cette méthode interne dans `#!python __init__`, il faut penser à l’appeler.
</div>

---
<div class ="viewPort">
<div class="monTitre">
Exercice 12
</div>
<div class="cylon_eye"></div>
</div>

Continuer ce jeu en mode texte avec vos propres méthodes.

On pourrait créer des méthodes comme `#!python taper` dans la classe `#!python personnage`, qui dépendrait de la `#!python chance` et d’un attribut `#!python force` à définir…

`#!python taper` pourrait renvoyer un nombre aléatoire entre 1 et `#!python force`, par exemple. Et c’est ce nombre qui définirait le nombre de points perdus par le personnage… Ce ne sont que des idées, je vous laisse libre de choisir une amélioration.

---
