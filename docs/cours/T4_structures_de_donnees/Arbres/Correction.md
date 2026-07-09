# <center><div class = "titre2">Correction des exercices</div></center>

### <div class = "encadré_exo"> __Correction de l'exercice 1__ </div>
<div class="list1_1" markdown="1">

1.  
``` python
def est_complet(self):

    assert not self.est_vide(), "L'arbre est vide"

    return self.taille() == 2 ** (self.hauteur() + 1) - 1

```

</div>
<div class="list1_2" markdown="1">

2.  

</div>
<div class="decal1" markdown="1">

=== "Version itérative"
    ``` python
    def est_strict_iter(self):
        
        if self.est_vide():
            return False
        
        f = File()
        f.enfiler(self)
        
        while not f.est_vide():
            tree = f.defiler()
            tree.affichage()
            gauche, droit = tree.sous_arbre_gauche(), tree.sous_arbre_droit()
            
            if gauche.est_vide() ^ droit.est_vide():
                return False
            
            if not gauche.est_vide() and not droit.est_vide():
                f.enfiler(gauche)
                f.enfiler(droit)
        
        return True

    ```

=== "Version récursive"
    ``` python
    def est_strict_rec(self):
        
        if self.est_vide():
            return False
        
        gauche, droit = self.sous_arbre_gauche(), self.sous_arbre_droit()
        
        if gauche.est_vide() ^ droit.est_vide():
            return False
        
        if self.est_feuille():
            return True
        
        return gauche.est_strict_rec() and droit.est_strict_rec()

    ```

</div>

### <div class = "encadré_exo"> __Correction de l'exercice 2__ </div>

=== "Version itérative"
    ``` python
    def compte_iter(self, x):
        
        assert self.est_ABR(), "Ce n'est pas un ABR"
        
        compteur = 0
        f = File()
        f.enfiler(self)
            
        while not f.est_vide():
            tree = f.defiler()
            val = tree.cle()
            gauche, droit = tree.sous_arbre_gauche(), tree.sous_arbre_droit()
            
            if x <= val:
                
                if x == val:
                    compteur += 1
                    
                    if not gauche.est_vide():
                        f.enfiler(gauche)
                    
                    if not droit.est_vide():
                        f.enfiler(droit)
                
                else:
                    
                    if not gauche.est_vide():
                        f.enfiler(gauche)
           
            else:
                
                if not droit.est_vide():
                    f.enfiler(droit)
        
        return compteur

    ```

=== "Version récursive"
    ``` python
    def compte_rec(self, x):
        
        if self.est_vide():
            return 0
            
        assert self.est_ABR(), "Ce n'est pas un ABR"
            
        gauche, droit = self.sous_arbre_gauche(), self.sous_arbre_droit()
            
        if x <= self.cle():
            
            if x == self.cle():
                return 1 + gauche.compte_rec(x) + droit.compte_rec(x)
            
            return gauche.compte_rec(x)
        
        return droit.compte_rec(x)

    ```

### <div class = "encadré_exo"> __Correction de l'exercice 3__ </div>

=== "Version itérative"
    ``` python
    def est_egal_iter(self, tree):
        
        if self.est_vide() and tree.est_vide():
            return True        
        
        if self.est_vide() ^ tree.est_vide():
            return False
        
        f_self , f_tree = File(), File()
        f_self.enfiler(self)
        f_tree.enfiler(tree)
        
        while not f_self.est_vide() and not f_tree.est_vide():
            arbre_self = f_self.defiler()
            arbre_tree = f_tree.defiler()
            
            if arbre_self.cle() != arbre_tree.cle():
                return False
            
            g_self, d_self = arbre_self.sous_arbre_gauche(), arbre_self.sous_arbre_droit()
            g_tree, d_tree = arbre_tree.sous_arbre_gauche(), arbre_tree.sous_arbre_droit()
            
            if g_self.est_vide() ^ g_tree.est_vide():
                return False
            
            if not g_self.est_vide() and not g_tree.est_vide():
                f_self.enfiler(g_self)
                f_tree.enfiler(g_tree)
            
            if d_self.est_vide() ^ d_tree.est_vide():
                return False
            
            if not d_self.est_vide() and not d_tree.est_vide():
                f_self.enfiler(d_self)
                f_tree.enfiler(d_tree)
        
        return True

    ```

=== "Version récursive"
    ``` python
    def __eq__(self, tree):
        
        if self.est_vide() and tree.est_vide():
            return True
        
        if self.est_vide() ^ tree.est_vide():
            return False
        
        if self.cle() != tree.cle():
            return False
        
        g_self, d_self = self.sous_arbre_gauche(), self.sous_arbre_droit()
        g_tree, d_tree = tree.sous_arbre_gauche(), tree.sous_arbre_droit()
        
        return g_self.__eq__(g_tree) and d_self.__eq__(d_tree)

    ```

### <div class = "encadré_exo"> __Correction de l'exercice 4__ </div>

``` python
def max_branche(self):
    
    if self.est_vide():
        return 0
    
    gauche, droit = self.sous_arbre_gauche(), self.sous_arbre_droit()
    return self.cle() + max(gauche.max_branche(), droit.max_branche())

```

### <div class = "encadré_exo"> __Correction de l'exercice 5__ </div>
<div class="list1_1" markdown="1">

1.  

</div>
<div class="decal1" markdown="1">

``` python
def est_valide(self):
    
    if self.est_vide():
        return False
        
    if self.est_feuille():
        return isinstance(self.cle(), int)
        
    gauche, droit = self.sous_arbre_gauche(), self.sous_arbre_droit()
        
    if self.cle() in ['+', '-', '*', '/', '**']:
        return gauche.est_valide() and droit.est_valide()
            
    return False

```

</div>
<div class="list1_2" markdown="1">

2.  

</div>
<div class="decal1" markdown="1">

``` python
def evaluation(self):
    
    if self.est_feuille():
        return self.cle()
        
    gauche, droit = self.sous_arbre_gauche(), self.sous_arbre_droit()
    return eval(str(gauche.evaluation()) + self.cle() + str(droit.evaluation()))
    
```

</div>
