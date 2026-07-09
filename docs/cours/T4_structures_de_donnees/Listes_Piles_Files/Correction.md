# <center><div class = "titre2"> Correction des exercices </div></center>

### <div class = "encadré_exo"> __Correction de l'exercice 1__ </div>
<div class="list1_1" markdown="1">

1. 
```python
def renvoie_N_ieme_element(N, pile):
    if N > pile.taille():
        return ("Taille de pile insuffisante")
    pile_temp = Pile()
    for i in range(N-1):
        pile_temp.empiler(pile.depiler())
    valeur = pile.lire_sommet()
    for i in range(N-1):
        pile.empiler(pile_temp.depiler())
    return valeur 
```
2. 
```python
def recherche_element_dans_pile(elt, pile):
    pile_temp = Pile()
    while not pile.est_vide():
        if elt != pile.lire_sommet():
            pile_temp.empiler(pile.depiler())
        else:
            while not pile_temp.est_vide():
                pile.empiler(pile_temp.depiler())
            return True
    while not pile_temp.est_vide():
        pile.empiler(pile_temp.depiler())
    return False
```
3. 
```python
def concatene(pile1, pile2):
    pile3 = Pile()
    t1 = pile1.taille()
    t2 = pile2.taille()
    while not pile1.est_vide():
        pile2.empiler(pile1.depiler())
    for i in range(t1):
        pile3.empiler(pile2.lire_sommet())
        pile1.empiler(pile2.depiler())
    while not pile2.est_vide():
        pile1.empiler(pile2.depiler())
    for i in range(t2):
        pile3.empiler(pile1.lire_sommet())
        pile2.empiler(pile1.depiler())
    return pile3
```
4. 
```python
def place_sommet_au_fond(pile):
    pile_temp = Pile()
    valeur = pile.depiler()
    while not pile.est_vide():
        pile_temp.empiler(pile.depiler())
    pile.empiler(valeur)
    while not pile_temp.est_vide():
        pile.empiler(pile_temp.depiler())
    return pile
```

</div>

### <div class = "encadré_exo"> __Correction de l'exercice 2__ </div>
<div class="list1_1" markdown="1">

1. 
```python
def tri_pairs_et_impairs(pile1):
    pile2, pile_pairs, pile_impairs = Pile(), Pile(), Pile()
    while not pile1.est_vide():
        valeur = pile1.depiler()
        if valeur % 2 == 0:
            pile_pairs.empiler(valeur)
        else:
            pile_impairs.empiler(valeur)
    while not pile_pairs.est_vide():
        pile2.empiler(pile_pairs.depiler())
    while not pile_impairs.est_vide():
        pile2.empiler(pile_impairs.depiler())
    return pile2
```
2. 
```python
def tri_pairs(pile1):
    pile2, pile_temp = Pile(), Pile()
    while not pile1.est_vide():
        pile_temp.empiler(pile1.depiler())
    while not pile_temp.est_vide():
        valeur = pile_temp.depiler()
        if valeur % 2 == 0:
            pile2.empiler(valeur)
        pile1.empiler(valeur)
    return pile2
```

### <div class = "encadré_exo"> __Correction de l'exercice 3__ </div>

```python
def inverser_file_via_pile(file):
    pile = Pile()
    while not file.est_vide():
        pile.empiler(file.defiler())
    while not pile.est_vide():
        file.enfiler(pile.depiler())
    return file
```

### <div class = "encadré_exo"> __Correction de l'exercice 4__ </div>

```python
def valide(chaine):
    pile = Pile()
    for element in chaine:
        if element in ['(', '[']:
            pile.empiler(element)
        if element == ')':
            if pile.est_vide() or not (pile.lire_sommet() == '('):
                return False
            else:
                pile.depiler()
        if element == ']':
            if pile.est_vide() or not (pile.lire_sommet() == '['):
                return False
            else:
                pile.depiler()
    return pile.est_vide()
```

### <div class = "encadré_exo"> __Correction de l'exercice 5__ </div>
<div class="list1_1" markdown="1">

1. 
```python
def melange(P1, P2):
    P3 = Pile()
    while not P1.est_vide() and not P2.est_vide():
        sommetP1 = P1.lire_sommet()
        sommetP2 = P2.lire_sommet()
        sommet_choisi = random.choice([sommetP1, sommetP2])
        if sommet_choisi == sommetP1:
            P3.empiler(P1.depiler())
        else:
            P3.empiler(P2.depiler())
    while not P1.est_vide():
        P3.empiler(P1.depiler())
    while not P2.est_vide():
        P3.empiler(P2.depiler())
    return P3
```
2. 
```python
from random import randint

def couper(P):
    autre_P = Pile()
    taille = P.taille()
    k = randint(1, 2*taille)
    print("k = ", k)
    if k >= taille:
        while not P.est_vide():
            autre_P.empiler(P.depiler())
    else: 
        for i in range(k):
            autre_P.empiler(P.depiler())
    return autre_P
```
3. 
```python
def Gilbreath(K):
    liste_cartes = [9, 10, "reine", "roi", "as"]
    pile1 = Pile()
    for i in range(K):
        for elt in liste_cartes:
            pile1.empiler(elt)
    pile2 = couper(pile1)
    return melange(pile1, pile2)
```

### <div class = "encadré_exo"> __Correction de l'exercice 6__ </div>

```python
def palindrome(chaine):
    ma_pile = Pile()
    ma_file = File()
    for element in chaine:
        ma_pile.empiler(element)
        ma_file.enfiler(element)
    while not ma_pile.est_vide():
        if ma_pile.lire_sommet() == ma_file.lire_tete():
            ma_pile.depiler()
            ma_file.defiler()
        else:
            return False
    return True
```

### <div class = "encadré_exo"> __Correction de l'exercice 7__ </div>
<div class="list1_" markdown="1">

1. 
```python
class File_via_2_piles:
    """Implémentation des files à l'aide de deux piles"""

    def __init__(self):
        self.p_gauche = Pile()
        self.p_droite = Pile()

    def enfiler(self, valeur):
        self.p_gauche.empiler(valeur)

    def defiler(self):
        while not self.p_gauche.est_vide():
            self.p_droite.empiler(self.p_gauche.depiler())
        valeur = self.p_droite.depiler()
        while not self.p_droite.est_vide():
            self.p_gauche.empiler(self.p_droite.depiler())
        return valeur

    def __str__(self):
        ch = ''
        while not self.p_gauche.est_vide():
            valeur = self.p_gauche.depiler()
            self.p_droite.empiler(valeur)
            ch = str(valeur) + '|' + ch
        ch = "\nEtat de la file :\n" + ch
        ch += "\n"
        while not self.p_droite.est_vide():
            self.p_gauche.empiler(self.p_droite.depiler())
        return ch
```
2. 
```python
class Pile_via_2_files:
    """Implémentation des piles à l'aide de deux files"""

    def __init__(self):
        self.f_gauche = File()
        self.f_droite = File()

    def empiler(self, valeur):
        self.f_gauche.enfiler(valeur)

    def depiler(self):
        while not self.f_gauche.est_vide():
            valeur = self.f_gauche.defiler()
            if not self.f_gauche.est_vide():
                self.f_droite.enfiler(valeur)
            else:
                while not self.f_droite.est_vide():
                    self.f_gauche.enfiler(self.f_droite.defiler())
                return valeur

    def __str__(self):
        ch = ""
        while not self.f_gauche.est_vide():
            valeur = self.f_gauche.defiler()
            self.f_droite.enfiler(valeur)
            ch = '|' + str(valeur) + '|\n' + ch
        ch = "\nEtat de la pile :\n" + ch
        ch += "\n"
        while not self.f_droite.est_vide():
            self.f_gauche.enfiler(self.f_droite.defiler())
        return ch
```

</div>
