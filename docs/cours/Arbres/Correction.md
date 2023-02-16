# <center><div class = "titre3">Correction des exercices</div></center>

### <div class = "encadré21"> __Correction de l'exercice 1__ </div>
<div class="list8" markdown="1">

1.  

</div>
<div style="display: block; margin: 0px 0px 0px 2.5em;" markdown="1">

``` python
def estComplet(self):
    return self.taille() == 2**(self.hauteur() + 1) - 1

```

</div>
<div class="list8_2" markdown="1">

2.  

</div>
<div style="display:block; margin: 0px 0px 0px 2.5em;" markdown="1">

=== "Version itérative"
    ``` python
    def estStrict(self):
        if self.estVide():
            return False

        f = File()
        f.enfiler(self)

        while not f.estVide():
            n = f.defiler()
            fg, fd = n.sousArbreGauche(), n.sousArbreDroit()
            if not fg.estVide():
                f.enfiler(fg)
            if not fd.estVide():
                f.enfiler(fd)
            if (fg.estVide() and not fd.estVide()) or (fd.estVide() and not fg.estVide()) :
                return False
        return True

    ```

=== "Version récursive"
    ``` python
    def estStrict(self):
        if self.estVide():
            return False
            
        gauche, droit = self.sousArbreGauche(), self.sousArbreDroit()
            
        if gauche.estVide() and not droit.estVide():
            return False
        elif not gauche.estVide() and droit.estVide():
            return False
        elif self.estFeuille():
            return True
        else:
            return gauche.estStrict() and droit.estStrict()

    ```

</div>

### <div class = "encadré21"> __Correction de l'exercice 2__ </div>

``` python
def compte(self, x):
    if self.estVide():
        return 0
            
    gauche, droit = self.sousArbreGauche(), self.sousArbreDroit()
        
    if self.cle() == x:
        return 1 + gauche.compte(x) + droit.compte(x)
        
    return gauche.compte(x) + droit.compte(x)

```

### <div class = "encadré21"> __Correction de l'exercice 3__ </div>

=== "Version itérative"
    ``` python
    def estEgal(self, arbre):
        f = File()
        g = File()
        f.enfiler(self) # On enfile l'arbre tout entier dans une file
        g.enfiler(arbre) # et l'autre arbre dans l'autre file

        while not f.estVide(): # tant que la file f (et donc g) n'est pas vide
            n = f.defiler() # on défile l'arbre en tête de file
            m = g.defiler() # idem

            if n.cle() != m.cle(): # si les racines sont différentes
                return False
            # sinon, ils sont pour l'instant égaux, on s'intéresse donc à leurs éventuels fils
            gauche_n, droit_n = n.sousArbreGauche(), n.sousArbreDroit()
            gauche_m, droit_m = m.sousArbreGauche(), m.sousArbreDroit()

            if not n.estFeuille(): # si l'arbre n a au moins un fils
                if not gauche_n.estVide(): # s'il a un fils gauche
                    if not gauche_m.estVide(): # et si l'arbre m aussi
                        f.enfiler(gauche_n) # on les place chacun dans la file correspondante
                        g.enfiler(gauche_m)
                    else: # l'arbre m n'a pas de fils gauche, ils ne sont donc pas égaux
                        return False

                if not droit_n.estVide(): # si l'arbre n a un fils droit
                    if not droit_m.estVide(): # et l'arbre m aussi
                        f.enfiler(droit_n) # on les place chacun dans la file correspondante
                        g.enfiler(droit_m)
                    else: # l'arbre m n'a pas de fils droit, ils ne sont donc pas égaux
                        return False
            else: # si l'arbre n'a pas de fils
                if not gauche_m.estVide() or not droit_m.estVide(): # alors que l'arbre m en a au moins un
                    return False
        return True

    ```

=== "Version récursive"
    ``` python
    def estEgal(self, arbre):
        if self.estVide() and arbre.estVide():
            return True
        if self.estVide() ^ arbre.estVide():
            return False
            
        gauche_self, droit_self = self.sousArbreGauche(), self.sousArbreDroit()
        gauche_arbre, droit_arbre = arbre.sousArbreGauche(), arbre.sousArbreDroit()
            
        return gauche_self.estEgal(gauche_arbre) and droit_self.estEgal(droit_arbre)

    ```

### <div class = "encadré21"> __Correction de l'exercice 4__ </div>

``` python
def maxBranche(self):
    if self.estVide():
        return 0
        
    if self.estFeuille():
        return self.cle()
        
    gauche, droit = self.sousArbreGauche(), self.sousArbreDroit()
    return self.cle() + max(gauche.maxBranche(), droit.maxBranche())

```

### <div class = "encadré21"> __Correction de l'exercice 5__ </div>
<div class="list8" markdown="1">

1.  

</div>
<div style="display: block; margin: 0px 0px 0px 2.5em;" markdown="1">

``` python
def estValide(self):
    if self.estVide():
        return False
        
    if self.estFeuille():
        return isinstance(self.cle(), int)
        
    gauche, droit = self.sousArbreGauche(), self.sousArbreDroit()
        
    if self.cle() in ['+', '-', '*', '/', '**']:
        return gauche.estValide() and droit.estValide()
            
    return False

```

</div>
<div class="list8_2" markdown="1">

2.  

</div>
<div style="display: block; margin: 0px 0px 0px 2.5em;" markdown="1">

``` python
def evaluation(self):
    if self.estFeuille():
        return self.cle()
        
    gauche, droit = self.sousArbreGauche(), self.sousArbreDroit()
    return eval(str(gauche.evaluation()) + self.cle() + str(droit.evaluation()))
    
```

</div>
