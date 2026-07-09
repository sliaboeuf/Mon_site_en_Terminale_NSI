# <center><div class = "titre2"> Correction des exercices</div></center>

### <div class = "encadré_exo"> __Correction de l'exercice 1__ </div>

```python
from Class_Pile_Avec_Liste_Chainee import Pile

def parcours_DFS(self, sommet):
    p = Pile()
    sommets_visites = {}
    p.empiler(sommet)
    while not p.est_vide():
        tmp = p.depiler()
        if tmp not in sommets_visites:
            sommets_visites[tmp] = True
        liste_voisins = [y for y in self.voisins(tmp) if y not in sommets_visites]
        for voisins in liste_voisins:
            p.empiler(voisins)
    return sommets_visites

```

### <div class = "encadré_exo"> __Correction de l'exercice 2__ </div>

```python
from Class_File_Avec_Liste_Chainee import File

def parcours_BFS(self, sommet):
    f = File()
    sommets_visites = {}
    f.enfiler(sommet)
    while not f.est_vide():
        tmp = f.defiler()
        if tmp not in sommets_visites:
            sommets_visites[tmp] = True
        liste_voisins = [y for y in self.voisins(tmp) if y not in sommets_visites]
        for voisins in liste_voisins:
            f.enfiler(voisins)
    return sommets_visites

```

### <div class = "encadré_exo"> __Correction de l'exercice 3__ </div>

```python
def is_cycle(self):
    sommets = self.liste_sommets()

    for sommet in sommets:
        p = Pile()
        sommets_visites = {}
        p.empiler(sommet)
        while not p.est_vide():
            tmp = p.depiler()
            if tmp in sommets_visites:
                return True
            sommets_visites[tmp] = True
            liste_voisins = [y for y in self.voisins(tmp) if y not in sommets_visites]
            for voisin in liste_voisins:
                p.empiler(voisin)

        return False

```

### <div class = "encadré_exo"> __Correction de l'exercice 4__ </div>

```python
def is_circuit(self):
    sommets = self.liste_sommets()

    for sommet in sommets:
        p = Pile()
        sommets_visites = {}
        p.empiler(sommet)
        while not p.est_vide():
            tmp = p.depiler()
            if tmp not in sommets_visites:
                sommets_visites[tmp] = True
            liste_successeurs = [y for y in self.successeurs(tmp)]
            for succ in liste_successeurs:
                if succ == sommet:
                    return True
                p.empiler(succ)
    return False

```
