# <center><div class = "titre2">Exercices</div></center>

### <div class = "encadré_exo"> __Exercice 1__ </div>
<span style="color: #f36379; font-weight: bold; font-size: 1.2rem; text-align: center; display: block;">Quel tri ? (1)</span>

On considère le tableau `#!python [6, 1, 4, 5, 2, 3]`.
<span style="display: block; margin: 10px 0 0 0;">Après la première itération d'un tri, on obtient le tableau `#!python [1, 6, 4, 5, 2, 3]`.</span>

!!! check "Cocher la ou les affirmations correctes"
	=== "Proposition"
	    - [ ] On a utilisé un tri par insertion.
	    - [ ] On a utilisé un tri par sélection.
	    - [ ] On a utilisé un tri à bulles.
	    - [ ] On a utilisé un tri par insertion ou par sélection.

	=== "Solution"

		- [x] Lors de la première itération on échange les valeurs d'indices `#!python 0`et `#!python 1`. 
		- [x] Lors de la première itération on insère le minimum, qui a pour valeur `#!python 1`, à sa place correcte à gauche.
		- [ ] On aurait déplacé le `#!python 6` à la fin du tableau.
		- [x] C'est juste, voir les deux premières questions.

### <div class = "encadré_exo"> __Exercice 2__ </div>
<span style="color: #f36379; font-weight: bold; font-size: 1.2rem; text-align: center; display: block;">Quel tri ? (2)</span>

On considère le tableau `#!python [6, 1, 4, 5, 2, 3]`.
<span style="display: block; margin: 10px 0 0 0;">Après la première itération d'un tri, on obtient le tableau `#!python [1, 6, 4, 5, 2, 3]`.</span>
<span style="display: block; margin: 10px 0 0 0;">Après la deuxième itération du tri :</span>

!!! check "Cocher la ou les affirmations correctes"

	=== "Proposition"

	    - [ ] par sélection, on obtient le tableau : `#!python [1, 2, 6, 4, 5, 3]`.
	    - [ ] par sélection, on obtient le tableau : `#!python [1, 2, 4, 5, 6, 3]`.
	    - [ ] par insertion, on obtient le tableau : `#!python [1, 4, 6, 5, 2, 3]`.
	    - [ ] par insertion, on obtient le tableau : `#!python [1, 2, 4, 5, 3, 6]`.

	=== "Solution"

		- [ ] On sélectionne la valeur minimale, le `#!python 2` à l'indice `#!python 4` et on l'échange avec le `#!python 6` à l'indice `#!python 1`. 
		- [x] Voir réponse ci-dessus.
		- [x] On insère la valeur d'indice `#!python 2` au bon endroit.
		- [ ] Voir réponse ci-dessus.

### <div class = "encadré_exo"> __Exercice 3__ </div>
<span style="color: #f36379; font-weight: bold; font-size: 1.2rem; text-align: center; display: block;">Quel tri ? (3)</span>

On considère le tableau `#!python [5, 4, 3, 2, 1]`.  
<span style="display: block; margin: 10px 0 0 0;">Après deux itérations :</span>

!!! check "Cocher la ou les affirmations correctes"

	=== "Proposition"

	    - [ ] du tri par sélection on obtient le tableau : `#!python [1, 2, 3, 4, 5]`.
	    - [ ] du tri par sélection on obtient le tableau : `#!python [1, 2, 5, 4, 3]`.
	    - [ ] du tri par insertion on obtient le tableau : `#!python [3, 4, 5, 2, 1]`.
	    - [ ] du tri par insertion on obtient le tableau : `#!python [1, 2, 3, 5, 4]`.

	=== "Solution"

		- [x] étape 1 : `#!python [1, 4, 3, 2, 5]`, étape 2 : `#!python [1, 2, 3, 4, 5]`.
		- [ ] $~$
		- [x] étape 1 : `#!python [4, 5, 3, 2, 1]`, étape 2 : `#!python [3, 4, 5, 2, 1]`.
		- [ ] $~$

### <div class = "encadré_exo"> __Exercice 4__ </div>
<span style="color: #f36379; font-weight: bold; font-size: 1.2rem; text-align: center; display: block;">Quel tri ? (4)</span>

On considère les fonctions suivantes dont certaines sont incorrectes.
```python

def tri_A(tableau):
    for i in range(len(tableau) - 1):
        i_mini = i
        for j in range(i + 1, len(tableau)):
            if tableau[j] < tableau[i_mini]:
                i_mini = j
        tableau[i], tableau[i_mini] = tableau[i_mini], tableau[i]

def tri_B(tableau):
    for i in range(len(tableau) - 1):
        i_mini = i
        for j in range(i + 1, len(tableau) - 1):
            if tableau[j] < tableau[i_mini]:
                i_mini = j
        tableau[i], tableau[i_mini] = tableau[i_mini], tableau[i]

def tri_C(tableau):
    for i in range(1, len(tableau)):
        valeur_a_inserer = tableau[i]
        j = i
        while j > 0 and tableau[j - 1] > valeur_a_inserer:
            tableau[j] = tableau[j - 1]
            j = j + 1 
        tableau[j] = valeur_a_inserer

def tri_D(tableau):
    for i in range(1, len(tableau)):
        valeur_a_inserer = tableau[i]
        j = i
        while j > 0 and tableau[j - 1] > valeur_a_inserer:
            tableau[j] = tableau[j - 1]
            j = j - 1
        tableau[j] = valeur_a_inserer
```

!!! check "Cocher la ou les affirmations correctes"

	=== "Proposition"

	    - [ ] La fonction `#!python tri_A` met en œuvre un tri par sélection.
		- [ ] La fonction `#!python tri_A` met en œuvre un tri par insertion.
		- [ ] La fonction `#!python tri_B` met en œuvre un tri par sélection.
		- [ ] La fonction `#!python tri_B` met en œuvre un tri par insertion.
		- [ ] La fonction `#!python tri_C` met en œuvre un tri par sélection.
		- [ ] La fonction `#!python tri_C` met en œuvre un tri par insertion.
		- [ ] La fonction `#!python tri_D` met en œuvre un tri par sélection.
		- [ ] La fonction `#!python tri_D` met en œuvre un tri par insertion.

	=== "Solution"

		- [x] $~$
		- [ ] $~$
		- [ ] Il faudrait `#!python for j in range(i + 1, len(tableau)):` pour lire la dernière valeur du tableau.
		- [ ] $~$
		- [ ] $~$
		- [ ] Il faudrait `#!python j = j - 1` car on prend la valeur se trouvant à gauche pour la décaler vers la droite.
		- [ ] $~$
		- [x] $~$

### <div class = "encadré_exo"> __Exercice 5__ </div>
<span style="color: #f36379; font-weight: bold; font-size: 1.2rem; text-align: center; display: block;">Quel tri ? (5)</span>

On considère les fonctions suivantes mettant toutes en œuvre le tri par insertion ou par sélection mais dans d'autres langages que le Python.

!!! code "Language"
	=== "Java"
		
		```Java
		public static void tri_A(int[] A){
		    for(int i = 1; i < A.length; i++){
		        int value = A[i];
		        int j = i - 1;
		        while(j >= 0 && A[j] > value){
		            A[j + 1] = A[j];
		            j = j - 1;
		        }
		        A[j + 1] = value;
		    }
		}
		```

	=== "Kotlin"

		```Kotlin
		fun <T : Comparable<T>> Array<T>.tri_B() {
		    for (i in 0..size - 2) {
		        var k = i
		        for (j in i + 1..size - 1)
		            if (this[j] < this[k])
		                k = j

		        if (k != i) {
		            val tmp = this[i]
		            this[i] = this[k]
		            this[k] = tmp
		        }
		    }
		}
		```

	=== "C"

		```C

		#include <stdio.h>

		void tri_C(int *a, const size_t n) {
		    for(size_t i = 1; i < n; ++i) {
		        int key = a[i];
		        size_t j = i;
		        while( (j > 0) && (key < a[j - 1]) ) {
		            a[j] = a[j - 1];
		            --j;
		        }
		        a[j] = key;
		    }
		}
		```

	=== "Haskell"

		```Haskell
		import Data.List (delete)

		tri_D :: (Ord a) => [a] -> [a]
		tri_D [] = []
		tri_D xs = tri_D (delete x xs) ++ [x]
		where x = maximum xs
		```

!!! check "Cocher la ou les affirmations correctes"

	=== "Proposition"

	    - [ ] La fonction `#!python tri_A` met en œuvre un tri par sélection.
		- [ ] La fonction `#!python tri_A` met en œuvre un tri par insertion.
		- [ ] La fonction `#!python tri_B` met en œuvre un tri par sélection.
		- [ ] La fonction `#!python tri_B` met en œuvre un tri par insertion.
		- [ ] La fonction `#!python tri_C` met en œuvre un tri par sélection.
		- [ ] La fonction `#!python tri_C` met en œuvre un tri par insertion.
		- [ ] La fonction `#!python tri_D` met en œuvre un tri par sélection.
		- [ ] La fonction `#!python tri_D` met en œuvre un tri par insertion.

	=== "Solution"

	    - [ ] La fonction `#!python tri_A` met en œuvre un tri par sélection.
		- [x] La fonction `#!python tri_A` met en œuvre un tri par insertion.
		- [x] La fonction `#!python tri_B` met en œuvre un tri par sélection.
		- [ ] La fonction `#!python tri_B` met en œuvre un tri par insertion.
		- [ ] La fonction `#!python tri_C` met en œuvre un tri par sélection.
		- [x] La fonction `#!python tri_C` met en œuvre un tri par insertion.
		- [x] La fonction `#!python tri_D` met en œuvre un tri par sélection.
		- [ ] La fonction `#!python tri_D` met en œuvre un tri par insertion.

### <div class = "encadré_exo"> __Exercice 6__ </div>
<span style="color: #f36379; font-weight: bold; font-size: 1.2rem; text-align: center; display: block;">Tri par sélection dans l'ordre décroissant</span>

Compléter la fonction `#!python tri_selection_decr` prenant en argument un tableau et le triant en place à l'aide du tri par sélection dans l'ordre décroissant.

```python
def tri_selection_decr(tableau):
    ...


tableau = [3, 1, 2]
tri_selection_decr(tableau)
assert tableau == [3, 2, 1], "Erreur avec [3, 1, 2]"

tableau = [1, 2, 3, 4]
tri_selection_decr(tableau)
assert tableau == [4, 3, 2, 1], "Erreur avec [1, 2, 3, 4]"

tableau = [-2, -5]
tri_selection_decr(tableau)
assert tableau == [-2, -5], "Erreur avec des valeurs négatives"

tableau = []
tri_selection_decr(tableau)
assert tableau == [], "Erreur avec un tableau vide"

print("Bravo !")
```

<center markdown="1">
[Correction de l'exercice 6 :material-cursor-default-click:](Correction.md#correction-de-lexercice-6){:target="_blank" .md-button}
</center>

### <div class = "encadré_exo"> __Exercice 7__ </div>
<span style="color: #f36379; font-weight: bold; font-size: 1.2rem; text-align: center; display: block;">Tri par insertion dans l'ordre décroissant</span>

Compléter la fonction `#!python tri_insertion_decr` prenant en argument un tableau et le triant en place à l'aide du tri par insertion dans l'ordre décroissant.

```python
def tri_insertion_decr(tableau):
    ...


tableau_0 = [3, 1, 2]
tri_insertion_decr(tableau_0)
assert tableau_0 == [3, 2, 1], "Erreur avec [3, 1, 2]"

tableau_1 = [1, 2, 3, 4]
tri_insertion_decr(tableau_1)
assert tableau_1 == [4, 3, 2, 1], "Erreur avec [1, 2, 3, 4]"

tableau_2 = [-2, -5]
tri_insertion_decr(tableau_2)
assert tableau_2 == [-2, -5], "Erreur avec des valeurs négatives"

tableau_3 = []
tri_insertion_decr(tableau_3)
assert tableau_3 == [], "Erreur avec un tableau vide"

print("Bravo !")
```

<center markdown="1">
[Correction de l'exercice 7 :material-cursor-default-click:](Correction.md#correction-de-lexercice-7){:target="_blank" .md-button}
</center>

### <div class = "encadré_exo"> __Exercice 8__ </div>
<span style="color: #f36379; font-weight: bold; font-size: 1.2rem; text-align: center; display: block;">Tri de couples de valeurs</span>

Le secrétariat d'un collège souhaite établir la liste de ses élèves triée par niveau puis par ordre alphabétique.
<span style="display: block; margin: 10px 0 0 0;">Il veut ainsi obtenir une liste dans laquelle :</span>
<div class="couleur_puce11" markdown="1">

* on rencontre tout d'abord les élèves de 6ème puis ceux de 5ème, de 4ème et enfin ceux de 3ème ;
* au sein de chaque niveau, les élèves sont triés dans l'ordre alphabétique de leur nom.

</div>
Chaque élève est décrit par un `#!python tuple` Python dans lequel la première valeur est le niveau dans lequel il est scolarisé (entier allant de `#!python 3` à `#!python 6`) et la seconde son nom (une chaîne de caractères).
<span style="display: block; margin: 10px 0 0 0;">On se propose d'utiliser le __tri par sélection__.</span>
<span style="display: block; margin: 10px 0 0 0;">Par exemple :</span>

```pycon

>>> eleves = [(4, "Targeur Samia"), (5, "Blennie Aymeric"), (5, "Alose Tom"), (6, "Targeur Samir")]

>>> tri_eleves(eleves)

>>> eleves
[(6, 'Targeur Samir'), (5, 'Alose Tom'), (5, 'Blennie Aymeric'), (4, 'Targeur Samia')]

```

On rappelle que Python trie nativement les chaînes de caractères dans l'ordre lexicographique :

```pycon

>>> "Alose Tom" < "Blennie Aymeric"
True
>>> "Targeur Samia" > "Targeur Samir"
False
```

Compléter les fonctions `#!python indice_minimum_depuis` et `#!python tri_eleves` ci-dessous afin d'effectuer le tri souhaité à l'aide du tri par sélection.

```python
def indice_minimum_depuis(tableau, i):
    ...


def tri_eleves(tableau):
    ...


eleves = [(4, "Targeur Samia"), (5, "Blennie Aymeric"), (5, "Alose Tom"), (6, "Targeur Samir")]
tri_eleves(eleves)

# Tests
assert eleves == [(6, "Targeur Samir"), (5, "Alose Tom"), (5, "Blennie Aymeric"), (4, "Targeur Samia")]
print("Bravo !")
```

<center markdown="1">
[Correction de l'exercice 8 :material-cursor-default-click:](Correction.md#correction-de-lexercice-8){:target="_blank" .md-button}
</center>