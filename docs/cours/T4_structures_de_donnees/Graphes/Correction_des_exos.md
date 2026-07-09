# <center><div class = "titre2">Correction des exercices</div></center>

### <div class = "encadré_exo"> __Correction de l'exercice 1__ </div>
<div class="list1_1" markdown="1">

1. C'est la même méthode pour les deux classes :
```python
def degre_sommet(self, s):
    return len(self.voisins(s))

```
2. Ici aussi :
```python
def degre_sommet(self, s):
    return len(self.predecesseurs(s)) + len(self.successeurs(s))

```

</div>

### <div class = "encadré_exo"> __Correction de l'exercice 2__ </div>

```python
''' Classes graphes non-orientés implémentés à l'aide d'un ensemble (set())'''

class grapheNoLsSet:

    def __init__(self):
        self.graphe = {}

    def est_vide(self):
        return not self.graphe

    def add_sommet(self, s):
        """Ajoute un sommet au graphe sans aucun voisin.
        """
        assert s not in self.graphe.keys(), 'Vous ne pouvez pas ajouter un sommet déjà existant'
        self.graphe[s] = set()

    def existe_sommet(self, s):
        return s in self.graphe.keys()

    def add_arete(self, s1, s2):
        """Crée une arête en reliant sommet1 avec sommet2.
        """
        assert not self.existe_arete(s1, s2), 'Vous ne pouvez pas ajouter une arête déjà existante'
        assert not s1 == s2, 'Vous ne pouvez pas faire de boucle'
        self.graphe[s1].add(s2)
        self.graphe[s2].add(s1)

    def existe_arete(self, s1, s2):
        return s2 in self.graphe[s1]

    def rem_sommet(self, s):
        """Supprime un sommet du graphe.
        """
        assert self.existe_sommet(s),"Vous ne pouvez pas supprimer un sommet qui n'existe pas"
        for sommet_voisin in self.graphe[s]:
            self.graphe[sommet_voisin].remove(s)
        del self.graphe[s]

    def rem_arete(self, s1, s2):
        """Supprime une arête.
        """
        assert self.existe_arete(s1, s2),"Vous ne pouvez pas supprimer une arête qui n'existe pas"
        self.graphe[s2].remove(s1)
        self.graphe[s1].remove(s2)

    def voisins(self, s):
        assert self.existe_sommet(s),"Ce sommet n'existe pas"

        return self.graphe[s]

    def degre_sommet(self, s):
        return len(self.voisins(s))

    def liste_sommets(self):
        return self.graphe.keys()

    def affichage(self):
        """Affiche le graphe sous forme de listes d'adjacences.
        """
        for sommet in sorted(self.graphe.keys()):
            if len(self.graphe[sommet]) != 0:
                print (sommet, " --> ",self.graphe[sommet])
            else :
                print (sommet, " -->  {}")

```

### <div class = "encadré_exo"> __Correction de l'exercice 3__ </div>
<div class="list1_1" markdown="1">

1. 
```python
''' Classe graphe valué non-orienté implémenté par une matrice d'adjacence'''

from random import choice, randint

class grapheValueNoMa:

    def __init__(self):
        self.sommets = []
        self.matrice = []

    def est_vide(self):
        return not self.sommets

    def existe_sommet(self, s):
        return s in self.sommets

    def affichage(self):
        print('   ', end = '')
        for elt in self.sommets:
            print(elt, end = '  ')
        print()
        for i, ligne in enumerate(self.matrice):
            print(f'{self.sommets[i]} {ligne}')
        print()

    def add_sommet(self, s):
        assert not self.existe_sommet(s),'Vous ne pouvez pas ajouter un sommet déjà existant'
        n = len(self.sommets)
        self.sommets.append(s)
        self.matrice.append([0 for i in range(n)])
        for ligne in self.matrice:
            ligne.append(0)

    def add_arete(self, s1, s2, poids):
        assert not self.existe_arete(s1, s2),'Vous ne pouvez pas ajouter un arête déjà existante'
        i = self.sommets.index(s1)
        j = self.sommets.index(s2)
        self.matrice[i][j] = self.matrice[j][i] = poids

    def existe_arete(self, s1, s2):
        i = self.sommets.index(s1)
        j = self.sommets.index(s2)
        return self.matrice[i][j] != 0

    def rem_sommet(self, s):
        assert self.existe_sommet(s),"Vous ne pouvez pas supprimer un sommet qui n'existe pas"
        n = self.sommets.index(s)
        self.sommets.remove(s)
        for ligne in self.matrice:
            del ligne[n]
        del self.matrice[n]

    def rem_arete(self, s1, s2):
        assert self.existe_arete(s1, s2),"Vous ne pouvez pas supprimer une arête qui n'existe pas"
        i = self.sommets.index(s1)
        j = self.sommets.index(s2)
        self.matrice[i][j] = self.matrice[j][i] = 0

    def voisins(self, s):
        assert self.existe_sommet(s),"Ce sommet n'existe pas"
        v = []
        i = self.sommets.index(s)
        for j in range(len(self.sommets)):
            if self.matrice[i][j] != 0:
                v.append(self.sommets[j])
        return v

    def degre_sommet(self, s):
        return len(self.voisins(s))

    def liste_sommets(self):
        return self.sommets

def gen_graph_value_no_ma(nb_sommets, nb_aretes):
    alphabet = [chr(i+65) for i in range(nb_sommets)]
    G = grapheValueNoMa()

    for lettre in alphabet:
        G.add_sommet(lettre)

    s1 = choice(alphabet)
    s2 = choice(alphabet)

    for i in range(nb_aretes):
        while s1 == s2 or G.existe_arete(s1, s2):
            s1 = choice(alphabet)
            s2 = choice(alphabet)
        poids = randint(0, 9)
        G.add_arete(s1, s2, poids)
    return G

G = gen_graph_value_no_ma(10, 10)
G.affichage()

```
2. 
``` python
''' Classe graphe valué non-orienté implémenté par une liste de successeurs'''

from random import choice, randint

class grapheValueNoLs:

    def __init__(self):
        self.graphe = {}

    def est_vide(self):
        return not self.graphe

    def add_sommet(self, s):
        """Ajoute un sommet au graphe sans aucun voisin.
        """
        assert s not in self.graphe.keys(), 'Vous ne pouvez pas ajouter un sommet déjà existant'
        self.graphe[s] = {}

    def existe_sommet(self, s):
        return s in self.graphe.keys()

    def add_arete(self, s1, s2, p):
        """Crée une arête de poids p en reliant sommet1 avec sommet2.
        """
        assert not self.existe_arete(s1, s2), 'Vous ne pouvez pas ajouter une arête déjà existante'
        assert not s1 == s2, 'Vous ne pouvez pas faire de boucle'
        self.graphe[s1][s2] = self.graphe[s2][s1] = p

    def existe_arete(self, s1, s2):
        return s2 in self.graphe[s1]

    def affichage(self):
        """Affiche le graphe sous forme de dictionnaires d'adjacences.
        """
        for i in sorted(self.graphe.keys()):
            print (i, " --> ",self.graphe[i])

    def rem_sommet(self, s):
        """Supprime un sommet du graphe.
        """
        assert self.existe_sommet(s),"Vous ne pouvez pas supprimer un sommet qui n'existe pas"
        for sommet_voisin in self.graphe[s]:
            del(self.graphe[sommet_voisin][s])
        del self.graphe[s]

    def rem_arete(self, s1, s2):
        """Supprime une arête.
        """
        assert self.existe_arete(s1, s2),"Vous ne pouvez pas supprimer une arête qui n'existe pas"
        del(self.graphe[s2][s1])
        del(self.graphe[s1][s2])

    def voisins(self, s):
        assert self.existe_sommet(s),"Ce sommet n'existe pas"

        return self.graphe[s]

    def degre_sommet(self, s):
        return len(self.voisins(s))

    def liste_sommets(self):
        return self.graphe.keys()

def gen_graph_value_no_ls(nb_sommets, nb_aretes):
    alphabet = [chr(i+65) for i in range(nb_sommets)]
    G = grapheValueNoLs()

    for lettre in alphabet:
        G.add_sommet(lettre)

    s1 = choice(alphabet)
    s2 = choice(alphabet)

    for i in range(nb_aretes):
        while s1 == s2 or G.existe_arete(s1, s2):
            s1 = choice(alphabet)
            s2 = choice(alphabet)
        poids = randint(0, 9)
        G.add_arete(s1, s2, poids)
    return G

G = gen_graph_value_no_ls(10, 10)
G.affichage() 
    
```

</div>

### <div class = "encadré_exo"> __Correction de l'exercice 4__ </div>

```python
def parcours_DFS_rec(self, sommet, vus=None):
    """ Parcours en profondeur à partir du sommet s
    --> vus contient l'ensemble des sommets visités
    """
    if vus is None:
        vus = []
    if not sommet in vus:
        vus.append(sommet)
        for v in self.voisins(sommet)[::-1]: # Pour que l'appel récursif sur le sommet voisin se fasse dans le même ordre que l'empilement de la version itérative
            self.parcours_DFS_rec(v, vus)
    return vus
```

### <div class = "encadré_exo"> __Correction de l'exercice 5__ </div>
<span style="color : #f36379; font-size: 18px; font-weight: bold;">Partie A</span>    
<div class="list1_1" markdown="1">

1. Si le graphe est connexe, un parcours - en largeur ou en profondeur - permet de visiter tous les sommets de ce graphe et réciproquement. Il suffit donc de tester si le parcours du graphe renvoie bien une liste de la même longueur que l'ordre du graphe.
2. 
```python
def est_connexe(self):
    return len(self.parcours_DFS('A')) == len(self.liste_sommets())

```

</div>
<span style="color : #f36379; font-size: 18px; font-weight: bold;">Partie B</span>  
<div class="list1_1" markdown="1">

1. Le problème des ponts de Königsberg peut être résolu en utilisant les graphes : les quartiers de la ville sont vus comme des sommets, et les ponts comme des arêtes.
<span style="margin: 5px 0 0 0; display:block;">Parcourir tous les ponts une fois et une seule consiste à trouver une chaîne eulérienne sur ce graphe. On applique alors le théorème d'Euler : le graphe est bien connexe mais, si on appelle Sud, Est, Nord et Centre ses quartiers, ils ont comme degré respectifs : 3, 3, 3 et 5.</span>
<span style="margin: 5px 0 0 0; display:block;">Il y a donc 4 sommets de degré impair et pas de chaîne eulérienne : le problème des ponts de Königsberg n'a pas de solution.</span>
2. On applique simplement le théorème d'Euler en prenant garde de renvoyer un booléen :
```python
def est_eulerien(self):
    c = 0
    sommets = self.liste_sommets()

    for sommet in sommets:
        if self.degre_sommet(sommet) % 2 == 1:
            c += 1
    return self.est_connexe() and (c == 0 or c ==2)
```

</div>

### <div class = "encadré_exo"> __Correction de l'exercice 6__ </div>
<div class="list1_1" markdown="1">

1. De haut en bas et de gauche à droite, si on nomme les différents graphes $\small{G_1}$, $\small{G_2}$, $\small{G_3}$, $\small{G_4}$ et $\small{G_5}$, on obtient :

</div>
<div class="couleur_puce14_decal" markdown="1">

* $\small{G_1}$ a pour nombre chromatique $\small{3}$.
* $\small{G_2}$ a pour nombre chromatique $\small{4}$.
* $\small{G_3}$ a pour nombre chromatique $\small{4}$.
* $\small{G_4}$ a pour nombre chromatique $\small{3}$.
* $\small{G_5}$ a pour nombre chromatique $\small{4}$.

</div>
<div class="list1_2" markdown="1">

2. 

</div>
<div class="list1_a" markdown="1">

1. Implémentation de l'algorithme glouton :
```python
from Graphes_non_orientes import genGraphNoLs, grapheNoLs as Grph

def coloration_greedy(graphe):
    liste_som = list(graphe.liste_sommets())
    print(liste_som)
    dico_couleurs = {som: 0 for som in liste_som}

    while len(liste_som) > 0:
        i = 0
        sommet = liste_som.pop(0)
        liste_voisins = graphe.voisins(sommet)
        if liste_voisins :
            liste_couleur_voisins = [dico_couleurs[som] for som in liste_voisins]
            while i in liste_couleur_voisins:
                i += 1
            dico_couleurs[sommet] = i
    return dico_couleurs

```
2. Implémentation de l'algorithme de Welsh-Powell :
```python
from Graphes_non_orientes import genGraphNoLs, grapheNoLs as Grph

def colorationWP(graphe):
    liste_som = list(graphe.liste_sommets())
    liste_degres = []
    dico_couleurs = {}

    for sommet in liste_som:
        liste_degres.append((sommet, len(graphe.voisins(sommet))))

    liste_triee_degre = sorted(liste_degres, key=lambda tuple: tuple[1], reverse=True)

    i = 0
    while len(liste_triee_degre) > 0:
        liste_tuples_a_enlever = []

        for tup in liste_triee_degre:
            sommet, degre = tup
            liste_voisins = graphe.voisins(sommet)
            trouve_voisin_indice_i = False
            for voisin in liste_voisins:
                if voisin in dico_couleurs and dico_couleurs[voisin] == i :
                    trouve_voisin_indice_i = True
            if trouve_voisin_indice_i == False :
                dico_couleurs[sommet] = i
                liste_tuples_a_enlever.append(tuple)

        for tuple in liste_tuples_a_enlever:
            liste_triee_degre.remove(tuple)

        i += 1

    return dico_couleurs

```

</div>
