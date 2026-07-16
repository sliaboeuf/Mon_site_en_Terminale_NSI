# <center><div class = "titre2"> Correction des exercices du cours </div></center>

### <div class = "encadré_exo"> __Correction de l'exercice 1__ </div>
<div class = "list1_1" markdown="1">

1. Illustrons le résultat de chaque étape de cette séquence :

</div>
<div class = "couleur_puce14_decal" markdown="1">

* `#!python L = liste_vide()` <span style="color:red">⇒</span> `#!python L = ()`  
* `#!python inserer_elt('A', 1, L)` <span style="color:red">⇒</span> `#!python L = ('A')`   
* `#!python inserer_elt('O', 2, L)` <span style="color:red">⇒</span> `#!python L = ('A', 'O')`  
* `#!python inserer_elt('B', 1, L)` <span style="color:red">⇒</span> `#!python L = ('B', 'A', 'O')`  
* `#!python contenu(L, 2)` <span style="color:red">⇒</span> `#!python 'A'`  
* `#!python inserer_elt('V', 3, L)` <span style="color:red">⇒</span> `#!python L = ('B', 'A', 'V', 'O')`  
* `#!python inserer_elt('R', 2, L)` <span style="color:red">⇒</span> `#!python L = ('B', 'R', 'A', 'V', 'O')`  

</div>
<div class = "list1_2" markdown="1">

2. Même chose ici :

</div>
<div class = "couleur_puce14_decal" markdown="1">

* `#!python L1 = liste_vide()` <span style="color:red">⇒</span> `#!python L1 = ()`  
* `#!python L2 = liste_vide()` <span style="color:red">⇒</span> `#!python L2 = ()`  
* `#!python inserer_elt(6, 1, L1)` <span style="color:red">⇒</span> `#!python L1 = (6)`  
* `#!python inserer_elt(7, 2, L1)` <span style="color:red">⇒</span> `#!python L1 = (6, 7)`  
* `#!python inserer_elt(8, 3, L1)` <span style="color:red">⇒</span> `#!python L1 = (6, 7, 8)`  
* `#!python inserer_elt(9, 4, L1)` <span style="color:red">⇒</span> `#!python L1 = (6, 7, 8, 9)`  
* `#!python inserer_elt(contenu(L1, 1), 1, L2)` <span style="color:red">⇒</span> `#!python L2 = (6)`  
* `#!python inserer_elt(contenu(L1, 2), 1, L2)` <span style="color:red">⇒</span> `#!python L2 = (7, 6)`  
* `#!python inserer_elt(contenu(L1, 3), 1, L2)` <span style="color:red">⇒</span> `#!python L2 = (8, 7, 6)`  
* `#!python inserer_elt(contenu(L1, 4), 1, L2)` <span style="color:red">⇒</span> `#!python L2 = (9, 8, 7, 6)`  
* `#!python supprimer_elt(L1, 2)` <span style="color:red">⇒</span> `#!python L1 = (6, 8, 9)`  
* `#!python contenu(L1, 2)` <span style="color:red">⇒</span> `#!python 8`  
* `#!python supprimer_elt(L1, 2)` <span style="color:red">⇒</span> `#!python L1 = (6, 9)` 
* `#!python longueur(L1)` <span style="color:red">⇒</span> `#!python 2`  
* `#!python acces(L1, contenu(L2, 1))` <span style="color:red">⇒</span> `#!python acces(L1, 9)` <span style="color:red">⇒</span> `2`

</div>


### <div class = "encadré_exo"> __Correction de l'exercice 2__ </div>
<div class="list1_1" markdown="1">

1. La différence fondamentale entre pile et file est que le __dernier objet__ inséré dans une pile est le __premier à sortir__, tandis que le __premier objet__ inséré dans une file est le __premier à sortir__.
2. __FIFO = First In, First Out__ et __LIFO = Last In, First Out__.
3. Pour une pile : mémorisation des pages web visitées, la touche __Ctrl Z__ ("Annuler frappe") dans un éditeur de texte, la récursivité...  
Pour une file : requêtes d'un serveur d'impression, ordonnancement d'un processeur...
4. Les piles et les files sont des listes possédant des restrictions au niveau de l’ajout ou de la suppression de leurs éléments.  
Pour une liste, on peut lui supprimer un élément quelconque.

</div>

### <div class = "encadré_exo"> __Correction de l'exercice 3__ </div>
<div class="list1_1" markdown="1">

1. Les tableaux et les listes chaînées servent à représenter sur une machine les types abstraits de données que sont les listes, les piles et les files.
2. Contrairement aux tableaux statiques dont la taille est fixe, celle d'un tableau dynamique peut varier.
3. Le principal avantage d'une liste chaînée est l'ajout/suppression de valeurs qui se fait en temps constant, contrairement au tableau dont le coût est linéaire.

</div>

### <div class = "encadré_exo"> __Correction de l'exercice 4__ </div>
On commence par instancier un objet de la classe `Pile` de la manière suivante :
```python
ma_pile = Pile()
```
<div class = "list1_1" markdown="1">

1. Voici les différentes instructions à effectuer dans l'ordre chronologique :
```python
ma_pile.empiler(12)
ma_pile.empiler(14)
ma_pile.empiler(8)
ma_pile.empiler(7)
ma_pile.empiler(19)
ma_pile.empiler(22)
```
2.  
```python
ma_pile.lire_sommet()
```
3.  
```python
ma_pile.taille()
```
4. Il va falloir dépiler les éléments jusqu'à ce que le sommet de la pile soit `#!python 8`, insérer l'élément `#!python 20` et enfin redéposer dans la pile les éléments précédemment dépilés.
```python
ma_pile.depiler()
ma_pile.depiler()
ma_pile.depiler()
ma_pile.empiler(20)
ma_pile.empiler(7)
ma_pile.empiler(19)
ma_pile.empiler(22)
```
5.  
```python
ma_pile.depiler()
```
6. De la façon suivante : 
```python
while not ma_pile.est_vide():
    ma_pile.depiler()
```

</div>

### <div class = "encadré_exo"> __Correction de l'exercice 5__ </div>
<div class = "list1_1" markdown="1">

1. Le constructeur de la classe `Pile`, qui consiste en l'initialisation d'une liste vide, est :
```python
def __init__(self):
    self.liste = []
```
2. Les différentes méthodes de la classe `#!python Pile` sont les méthodes `#!python empiler(valeur)`, `#!python depiler()`, `#!python est_vide()`, `#!python taille()` et `#!python lire_sommet()`.
<span style="display: block; margin: 3px 0 0 0;">Et il y a deux méthodes spéciales : le constructeur `#!python __init__` et la méthode `#!python __str__` permettant la représentation d'une pile.</span>

</div>

### <div class = "encadré_exo"> __Correction de l'exercice 6__ </div>
```python
p = Pile()
p.empiler(9)
p.empiler(2)
p.empiler(5)
p.empiler(4)
print(p)
print(p.lire_sommet())
print(p.taille())

p.depiler()
p.depiler()
print(p)
print(p.lire_sommet())
print(p.taille())

p.empiler(78)
print(p)
print(p.lire_sommet())
print(p.taille())
```

### <div class = "encadré_exo"> __Correction de l'exercice 7__ </div>
<div class = "list1_1" markdown="1">

1. En notation polonaise inversée, l’opération arithmétique : $~3 × (2 + 4)~$ sera codée $~× + 2~4~3$.
2. On peut représenter ainsi l’exécution du calcul précédent :

</div>
<center markdown="1">

<table>
<thead>
<tr>
<th align="center"> </th>
<th align="center">Entrée </th>
<th align="center">Opération </th>
<th align="center">Pile </th>
</tr>
</thead>
<tbody>
<tr>
<td align="center" >Etape 1</td>
<td align="center">3</td>
<td align="center">Empiler l'opérande</td>
<td align="center">3</td>
</tr>
<tr>
<td align="center" style="vertical-align:middle">Etape 2</td>
<td align="center" style="vertical-align:middle">4</td>
<td align="center" style="vertical-align:middle">Empiler l'opérande</td>
<td align="center" style="vertical-align:middle">4<br>3</td>
</tr>
<tr>
<td align="center" style="vertical-align:middle">Etape 3</td>
<td align="center" style="vertical-align:middle">2</td>
<td align="center" style="vertical-align:middle">Empiler l'opérande</td>
<td align="center" style="vertical-align:middle">2<br>4<br>3</td>
</tr>
<tr>
<td align="center" style="vertical-align:middle">Etape 4</td>
<td align="center" style="vertical-align:middle">+</td>
<td align="center" style="vertical-align:middle">Addition</td>
<td align="center" style="vertical-align:middle">6<br>3</td>
</tr>
<tr>
<td align="center" >Etape 5</td>
<td align="center">×</td>
<td align="center">Multiplication</td>
<td align="center">18</td>
</tr>
</tbody></table>

</center>
<div class = "list1_3" markdown="1">

3. Représentation de l’évolution de la pile permettant de réaliser le calcul sous forme d'un tableau :

</div>
<center markdown="1">

<table>
<thead>
<tr>
<th align="center"> </th>
<th align="center">Entrée </th>
<th align="center">Opération </th>
<th align="center">Pile </th>
</tr>
</thead>
<tbody>
<tr>
<td align="center" >Etape 1</td>
<td align="center">6</td>
<td align="center">Empiler l'opérande</td>
<td align="center">6</td>
</tr>
<tr>
<td align="center" style="vertical-align:middle">Etape 2</td>
<td align="center" style="vertical-align:middle">3</td>
<td align="center" style="vertical-align:middle">Empiler l'opérande</td>
<td align="center" style="vertical-align:middle">3<br>6</td>
</tr>
<tr>
<td align="center" style="vertical-align:middle">Etape 3</td>
<td align="center" style="vertical-align:middle">4</td>
<td align="center" style="vertical-align:middle">Empiler l'opérande</td>
<td align="center" style="vertical-align:middle">4<br>3<br>6</td>
</tr>
<tr>
<td align="center" style="vertical-align:middle">Etape 4</td>
<td align="center" style="vertical-align:middle">2</td>
<td align="center" style="vertical-align:middle">Empiler l'opérande</td>
<td align="center" style="vertical-align:middle">2<br>4<br>3<br>6</td>
</tr>
<tr>
<td align="center" style="vertical-align:middle">Etape 5</td>
<td align="center" style="vertical-align:middle">10</td>
<td align="center" style="vertical-align:middle">Empiler l'opérande</td>
<td align="center" style="vertical-align:middle">10<br>2<br>4<br>3<br>6</td>
</tr>
<tr>
<td align="center" style="vertical-align:middle">Etape 6</td>
<td align="center" style="vertical-align:middle">/</td>
<td align="center" style="vertical-align:middle">Division</td>
<td align="center" style="vertical-align:middle">5<br>4<br>3<br>6</td>
</tr>
<tr>
<td align="center" style="vertical-align:middle">Etape 7</td>
<td align="center" style="vertical-align:middle">-</td>
<td align="center" style="vertical-align:middle">Soustraction</td>
<td align="center" style="vertical-align:middle">1<br>3<br>6</td>
</tr>
<tr>
<td align="center" style="vertical-align:middle">Etape 8</td>
<td align="center" style="vertical-align:middle">×</td>
<td align="center" style="vertical-align:middle">Multiplication</td>
<td align="center" style="vertical-align:middle">3<br>6</td>
</tr>
<tr>
<td align="center" >Etape 9</td>
<td align="center">+</td>
<td align="center">Addition</td>
<td align="center">9</td>
</tr>
</tbody></table>

</center>

### <div class = "encadré_exo"> __Correction de l'exercice 8__ </div>
On commence par instancier un objet de la classe `#!python File` de la manière suivante :
```python
ma_file = File()
```
<div class = "list1_1" markdown="1">

1. Voici les différentes instructions à effectuer dans l'ordre chronologique :
```python
ma_file.enfiler(22)
ma_file.enfiler(19)
ma_file.enfiler(7)
ma_file.enfiler(8)
ma_file.enfiler(14)
ma_file.enfiler(12)
```
2. On enlève à deux reprises l'élément en tête de file, soit `#!python 22` puis `#!python 19`. Le nouvel élément en tête de file est alors `#!python 7`.  
On enfile ensuite l'élément `#!python 78`, ce qui donne la file `#!python 78`, `#!python 12`, `#!python 14`, `#!python 8`, `#!python 7`.

</div>

### <div class = "encadré_exo"> __Correction de l'exercice 9__ </div>
Voici l'affichage obtenu :
```python
Etat de la file :

75|78|92|93|95|

La file est-elle vide ? False
5

Etat de la file :

92|93|95|

3

Etat de la file :

92|93|95|75|78|
```
Au moment du premier affichage de la file, la tête de file est `#!python 75` et la queue est `#!python 95`.
Les différentes méthodes opérées sur l'objet semble correspondre au comportement d'une file.

### <div class = "encadré_exo"> __Correction de l'exercice 10__ </div>
En ajoutant les mêmes instructions que pour l'implémentation à l'aide d'un tableau dynamique, à savoir :
```python
f = File()
f.enfiler(75)
f.enfiler(78)
f.enfiler(92)
f.enfiler(93)
f.enfiler(95)

print(f)
print("La file est-elle vide ?",f.est_vide())
print(f.taille())

f.defiler()
f.defiler()

print(f)
print(f.taille())

f.enfiler(75)
f.enfiler(78)
print(f)
```
on obtient exactement les mêmes résultats :
```python
Etat de la file :
75|78|92|93|95|

La file est-elle vide ? False
5

Etat de la file :
92|93|95|

3

Etat de la file :
92|93|95|75|78|
```