---
password: "corr_Graphe"
---

# <center><div class = "titre2"> Correction des exercices du cours </div></center>

### <div class = "encadré_exo"> __Correction de l'exercice 1__ </div>
<div class = "list1_1" markdown = "1">

1. Le graphe non orienté est le graphe $\small{G_2}$.
2. 

</div>
<div class = "list1_a" markdown = "1">

1. Les sommets $\small{A}$ et $\small{B}$ sont deux sommets adjacents.
<span style="margin :5px 0 0 0; display: block;">Les sommets $\small{A}$ et $\small{E}$ ne sont pas adjacents.</span>
2. Les voisins de $\small{A}$ sont les sommets $\small{B}$ et $\small{C}$.
3. $\small{d(B)=2}$, $\small{d(C)=3}$ et $\small{d(E)=1}$.
4. $\small{A, B, F, D, C, A}$ est un cycle.
5. Il y a 2 chaînes simples entre les sommets $\small{A}$ et $\small{D}$ : $\small{A, C, D}$ et $\small{A, B, F, D}$

</div>
<div class = "list1_3" markdown = "1">

3. 

</div>
<div class = "list1_a" markdown = "1">

1. Le sommet $\small{A}$ a deux successeurs : $\small{B}$ et $\small{D}$ mais aucun prédécesseur. 
<span style="margin :5px 0 0 0; display: block;">Le sommet $\small{C}$ a deux successeurs : $\small{E}$ et $\small{F}$ et deux prédécesseurs : $\small{B}$ et $\small{G}$.</span>
2. $\small{G, C, E, B}$ est un chemin entre $\small{G}$ et $\small{B}$.
<span style="margin :5px 0 0 0; display: block;">Il n'existe aucun chemin entre $\small{B}$ et $\small{D}$.</span>
3. $\small{B, C, E, B}$ est un circuit.
4. $\small{C}$ est le sommet de plus grand degré : $\small{d(C)=d_+(C)+d_−(C)=2+2=4}$.

</div>

### <div class = "encadré_exo"> __Correction de l'exercice 2__ </div>
<div class = "list1_1" markdown = "1">

1. 
	<center>
    $\small{G_1=\begin{pmatrix} 0 & 1 & 0 & 1 & 0 & 0 & 0\\0 & 0 & 1 & 0 & 0 & 0 & 0\\0 & 0 & 0 & 0 & 1 & 1 & 0\\0 & 0 & 0 & 0 & 1 & 0 & 0\\ 0 & 1 & 0 & 0 & 0 & 0 & 0\\0 & 0 & 0 & 0 & 0 & 0 & 0\\0 & 0 & 1 & 0 & 0 & 0 & 0\end{pmatrix}}$
    $~~~~~~~~~$
    $\small{G_2=\begin{pmatrix} 0 & 1 & 1 & 0 & 0 & 0\\1 & 0 & 0 & 0 & 0 & 1\\1 & 0 & 0 & 1 & 1 & 0\\0 & 0 & 1 & 0 & 0 & 1\\ 0 & 0 & 1 & 0 & 0 & 0\\0 & 1 & 0 & 1 & 0 & 0\end{pmatrix}}$
	</center>
2. Pour $\small{G_1}$ :
```python
dico_G1 = {

"A": ["B", "D"],
"B": ["C"],
"C": ["E", "F"],
"D": ["E"],
"E": ["B"],
"F": [],
"G": ["C"]

}

```
Et pour $\small{G_2}$ :
```python
dico_G2 = {

"A": ["B", "C"],
"B": ["A", "F"],
"C": ["A", "D", "E"],
"D": ["C", "F"],
"E": ["C"],
"F": ["B", "D"]

}

```
3. Pour le graphe $\small{G_3}$, on remarque que la matrice d'adjacence n'est pas symétrique, donc le graphe est forcément orienté.  
<span style="margin :5px 0 0 0; display: block;">On obtient le graphe suivant :
![Illustration](images/Exercice2(1).png){: .image}
Pour le graphe $\small{G_4}$, on remarque que la matrice d'adjacence est symétrique, donc le multigraphe est forcément non-orienté.
<span style="margin :5px 0 0 0; display: block;">On obtient le multigraphe suivant :</span>
![Illustration](images/Exercice2(2).png){: .image}
4. Pour le graphe $\small{G_5}$, on remarque que l'on est en présence d'une liste des prédécesseurs, donc le graphe est forcément orienté.
<span style="margin :5px 0 0 0; display: block;">On obtient le graphe suivant :</span>
![Illustration](images/Exercice2(3).png){: .image}
Pour le graphe $\small{G_6}$, on remarque que l'on est en présence d'une liste de voisins, donc le graphe est forcément non-orienté.
<span style="margin :5px 0 0 0; display: block;">On obtient le graphe suivant :</span>
![Illustration](images/Exercice2(4).png){: .image}
</span>

</div>

### <div class = "encadré_exo"> __Correction de l'exercice 3__ </div>

```python
def voisins(self, s):
    assert self.existe_sommet(s),"Ce sommet n'existe pas"
    v = []
    i = self.sommets.index(s)
    for j in range(len(self.sommets)):
        if self.matrice[i][j] != 0:
            v.append(self.sommets[j])
    return v

```

### <div class = "encadré_exo"> __Correction de l'exercice 4__ </div>

```python
class grapheOMa:

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

    def add_arc(self, s1, s2):
        i = self.sommets.index(s1)
        j = self.sommets.index(s2)

        assert self.matrice[i][j] == 0,'Vous ne pouvez pas ajouter un arc déjà existant'

        self.matrice[i][j] = 1

    def rem_sommet(self, s):
        n = self.sommets.index(s)
        self.sommets.remove(s)
        for ligne in self.matrice:
            del ligne[n]
        del self.matrice[n]

    def rem_arete(self, s1, s2):
        i = self.sommets.index(s1)
        j = self.sommets.index(s2)
        self.matrice[i][j] = 0

    def liste_sommets(self):
        return self.sommets

    def predecesseurs(self, s):
        assert self.existe_sommet(s),"Ce sommet n'existe pas"

        v = []
        i = self.sommets.index(s)
        for j in range(len(self.sommets)):
            if self.matrice[j][i] == 1:
                v.append(self.sommets[j])
        return v

    def successeurs(self, s):
        assert self.existe_sommet(s),"Ce sommet n'existe pas"

        v = []
        i = self.sommets.index(s)
        for j in range(len(self.sommets)):
            if self.matrice[i][j] == 1:
                v.append(self.sommets[j])
        return v

```

### <div class = "encadré_exo"> __Correction de l'exercice 5__ </div>

```python
class grapheNoLs:

    def __init__(self):
        self.graphe = {}

    def est_vide(self):
        return not self.graphe

    def affichage(self):
        """Affiche le graphe sous forme de listes d'adjacences.
        """
        for sommet in sorted(self.graphe.keys()):
            print (sommet, " --> ",self.graphe[sommet])

    def add_sommet(self, s):
        """Ajoute un sommet au graphe sans aucun voisin.
        """
        assert s not in self.graphe.keys(), 'Vous ne pouvez pas ajouter un sommet déjà existant'
        self.graphe[s] = []

    def existe_sommet(self, s):
        return s in self.graphe.keys()

    def add_arete(self, s1, s2):
        """Crée une arête en reliant sommet1 avec sommet2.
        """
        assert not self.existe_arete(s1, s2), 'Vous ne pouvez pas ajouter une arête déjà existante'
        self.graphe[s1].append(s2)
        self.graphe[s2].append(s1)

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

```

### <div class = "encadré_exo"> __Correction de l'exercice 6__ </div>

```python
class grapheOLs:

    def __init__(self):
        self.graphe = {}

    def est_vide(self):
        return not self.graphe

    def affichage(self):
        """Affiche le graphe sous forme de listes d'adjacences.
        """
        for sommet in sorted(self.graphe.keys()):
            print (sommet, " --> ",self.graphe[sommet])
    
    def add_sommet(self, s):
        """Ajoute un sommet au graphe sans aucun voisin.
        """
        assert s not in self.graphe.keys(), 'Vous ne pouvez pas ajouter un sommet déjà existant'
        self.graphe[s] = []

    def existe_sommet(self, s):
        return s in self.graphe.keys()

    def add_arc(self, s1, s2):
        """Crée un arc en reliant sommet1 avec sommet2.
        """
        assert not self.existe_arc(s1, s2), 'Vous ne pouvez pas ajouter un arc déjà existant'
        self.graphe[s1].append(s2)

    def existe_arc(self, s1, s2):
        return s2 in self.graphe[s1]

    def rem_sommet(self, s):
        """Supprime un sommet du graphe.
        """
        assert self.existe_sommet(s),"Vous ne pouvez pas supprimer un sommet qui n'existe pas"
        for sommet_voisin in self.graphe[s]:
            self.graphe[sommet_voisin].remove(s)
        del self.graphe[s]

    def rem_arc(self, s1, s2):
        """Supprime un arc.
        """
        assert self.existe_arete(s1, s2),"Vous ne pouvez pas supprimer une arête qui n'existe pas"
        self.graphe[s1].remove(s2)

    def successeurs(self, s):
        return self.graphe[s]

    def predecesseurs(self, s):
        pred = []
        for sommet in self.graphe.keys():
            if s in self.graphe[sommet]:
                pred.append(sommet)
        return pred

```

### <div class = "encadré_exo"> __Correction de l'exercice 7__ </div>

```python
def ma_to_ls(gma):
    gls = grapheNoLs()
    for elt in gma.liste_sommets():
        gls.add_sommet(elt)
    for elt in gma.liste_sommets():
        for voisin in gma.voisins(elt):
            gls.add_arete(elt, voisin)
    return gls

def ls_to_ma(gls):
    gma = grapheNoMa()
    for elt in gls.liste_sommets():
        gma.add_sommet(elt)
    for elt in gls.liste_sommets():
        for voisin in gls.voisins(elt):
            gma.add_arete(elt, voisin)
    return gma

```
