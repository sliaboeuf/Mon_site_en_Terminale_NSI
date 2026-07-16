# <center><div class = "titre5">TP : Implémentation d'un dictionnaire</div></center>

__Objectif :__ Dans ce TP, nous allons dans un premier temps écrire plusieurs implémentations d'un dictionnaire.
<span style="display: block; margin: 3px 0 0 0;">Ensuite, nous comparerons expérimentalement les complexités de différentes implémentations dont celles qui ont été écrites en mesurant leur temps d'exécution.</span>
<span style="display: block; margin: 10px 0 0 0;">Pour ces implémentations, la taille maximale du dictionnaire est choisie à l’avance, lors de sa création.</span>
<span style="display: block; margin: 3px 0 0 0;">Par exemple : `#!python Dico1(4)` générera un objet dictionnaire pouvant contenir $~2^4=16~$ entrées au maximum.</span>
<span style="display: block; margin: 10px 0 20px 0;">Voici la liste des méthodes nécessaires au bon fonctionnement des dictionnaires quelle que soit leur implémentation :</span>
<center>

<table>
<thead>
<tr>
<th align="center">Méthode</th>
<th align="center">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td align="center" style="vertical-align:middle"> <code>est_vide()</code> </td>
<td>Renvoie <code>True</code> si et seulement si l'objet de type <code>Dico</code> est vide.<br> 
    Renvoie <code>False</code> sinon.</td>
</tr>
<tr>
<td align="center" style="vertical-align:middle"><code>affichage()</code></td>
<td>Affiche dans la console le contenu du dictionnaire sous la<br> forme suivante :<br>
<code>
DEBUT<br>
cle1 : valeur1<br>
cle2 : valeur2<br>
(...)<br>
FIN
</code><br>
Les cellules vides ne s'affichent pas.<br>
Cette méthode ne renvoie rien.</td>
</tr>
<tr>
<td align="center" style="vertical-align:middle"><code>taille()</code></td>
<td style="vertical-align:middle">Renvoie le nombre d’entrées stockées dans le dictionnaire.</td>
</tr>
<tr>
<td align="center" style="vertical-align:middle"><code>trouver_index(cle)</code></td>
<td>Renvoie la valeur de l'index de la clé dans la table de données.<br>
Renvoie <code>False</code> si la clé n'existe pas dans la table.</td>
</tr>
<tr>
<td align="center" style="vertical-align:middle"><code>lire(cle)</code></td>
<td>Renvoie la valeur correspondante à la clé passée en paramètre.<br>
Renvoie <code>None</code> si cette clé n'existe pas.</td>
</tr>
<tr>
<td align="center" ><code>est_plein()</code></td>
<td style="vertical-align:middle">Renvoie <code>True</code> si le dictionnaire est plein, <code>False</code> sinon.</td>
</tr>
<tr>
<td align="center" style="vertical-align:middle"><code>ecrire(cle, valeur)</code></td>
<td>Ajoute l’entrée <code>(cle,valeur)</code> au dictionnaire.<br>
Si la clé existe déjà, seule la (nouvelle) valeur est enregistrée <br>à la place de l'ancienne.<br>
Ne renvoie rien.</td>
</tr>
<tr>
<td align="center" style="vertical-align:middle"><code>supprimer(cle)</code></td>
<td>Supprime l’entrée <code>cle</code> dans la table.<br>
Ne renvoie rien.</td>
</tr>
</tbody></table>

</center>

### <div class = "encadré3_TP">Implémentation d'un dictionnaire à partir de deux listes</div>

<span class="border1"> __Description__ </span><div></div>
Les entrée du dictionnaire sont stockées dans deux listes distinctes :
<div class="couleur_puce35" markdown = "1">

- La première contient les clés.
- La seconde contient les valeurs correspondantes.

</div>
Par exemple, pour un dictionnaire de taille 5 contenant 3 éléments :
```python
table1 = ['un', 'deux', 'trois', None, None ]
table2 = [ 1, 2, 3, None, None ]
```

??? exercice2 {{exercice(False, prem=0, niveau=2)}}
    Implémenter ce premier dictionnaire en se basant sur le squelette suivant :
    ```python
    """ Implémentation n°1 d'un dictionnaire en programmation orientée objet Python

        Ce fichier est le squelette de départ d'un code d'une classe Dico1, destinée à produire des dictionnaires.

        Pour cette première implémentation, l'idée est de stocker nos données dans deux listes :
            - la première contenant nos clés ;
            - la seconde contenant les valeurs correspondantes.
    """

    ## Code à compléter
    class Dico1:
        """ Dictionnaire contenant deux listes non ordonnées """

        def __init__(self, nb_de_bits):
            """ Constructeur : va créer deux listes vides composées chacune de (2**nb_de_bits) None"""
            self.longueur = 2 ** nb_de_bits
            self.cles = [None] * self.longueur
            self.valeurs = [None] * self.longueur
            self.nbre_elements = 0

        def est_vide(self):
            """ Renvoie True si et seulement si l'objet de type Dico1 est vide,  
                sinon renvoie False. """
            # CODER CI-DESSOUS, à la place de pass la méthode est_vide()
            pass

        def affichage(self):
            """ Affiche dans la console le contenu du dictionnaire sous la forme suivante :
                    DEBUT
                    cle1 : valeur1
                    cle2 : valeur2
                    (...)
                    FIN
                Les cellules vides ne s'affichent pas.
                Cette méthode ne renvoie rien. """
            # CODER CI-DESSOUS, à la place de pass la méthode affichage()
            pass    
    
        def trouver_index(self, cle):
            """ Trouve et renvoie l'index qui correspond à cle, renvoie None si la 
                clé est absente du dictionnaire. """
            # CODER CI-DESSOUS, à la place de pass la méthode trouver_index(cle)
            pass
        
        def ecrire(self, cle, valeur):
            """ Ajoute respectivement la clé et la valeur à la première position disponible de       
                chaque liste.
                On commence par tester si la clé existe déjà, si elle existe on remplace la valeur 
                associée dans la seconde liste des valeurs.
                Sinon on ajoute cle à la première position disponible, donc à la première
                valeur à None de la liste des clés et on fait de même pour valeur.
                Ne renvoie rien. """
            # CODER CI-DESSOUS, à la place de pass la méthode ecrire(cle,valeur)
            pass
        
        def taille(self):
            """ Renvoie le nombre de clés non vides stockées dans le dictionnaire"""
            # CODER CI-DESSOUS, à la place de pass la méthode taille()
            pass
        
        def est_plein(self):
            """ Renvoie True si le dictionnaire est plein , sinon renvoie False."""
            # CODER CI-DESSOUS, à la place de pass la méthode est_plein()
            pass
        
        def supprimer(self, cle):
            """ Supprime la valeur correspondante à clé dans la liste self.valeurs,
                Supprime cette clé de la liste self.cles. 
                Ne renvoie rien. """
            # CODER CI-DESSOUS, à la place de pass la méthode supprimer(cle)
            pass
    
        def contient(self, cle):
            """ Renvoie True si la clé existe, sinon renvoie False. """
            # CODER CI-DESSOUS, à la place de pass la méthode contient(cle)
            pass
        
        def lire(self, cle):
            """ Renvoie la valeur correspondante à la clé passée en paramètre.
                Renvoie None si cette clé n'existe pas. """
            # CODER CI-DESSOUS, à la place de pass la méthode lire(cle)
            pass
        
        
    ## Dictionnaire "dico" pré-rempli pour tester vos méthodes        
    from random import shuffle

    if __name__=='__main__':
        jeu_donnees = [i for i in range(10)]
        shuffle(jeu_donnees)
        dico = Dico1(4)
        for j in jeu_donnees:
            dico.ecrire(str(j), j)
    ```
    <center>
    [Correction de l'exercice 1 :material-cursor-default-click:](Correction_des_exos_du_TP.md#correction-de-lexercice-1){:target="_blank" .md-button}
    </center>

### <div class = "encadré3_TP">Implémentation d'un dictionnaire à partir d'une liste de tuples</div>

<span class="border1"> __Description__ </span><div></div>
Les entrées du dictionnaire sont stockées dans une liste de tuples `#!python (clef, valeur)` triée par ordre croissant de clé.  
<span style="display: block; margin: 10px 0 0 0;">Par exemple, pour un dictionnaire de taille 5 contenant 3 éléments :</span>
<span style="display: block; margin: 3px 0 0 0;">`#!python table = [(), (), ("deux", 2) , ("trois", 3), ("un", 1)]`</span>

La position des éléments se justifie par l’ordre alphabétique.

??? exercice2 {{exercice(False, niveau=2)}}
    Implémenter ce second dictionnaire en se basant sur le squelette suivant :
    ```python
    """ Implémentation n°2 d'un dictionnaire en programmation orientée objet Python

        Ce fichier est le squelette de départ d'un code d'une classe Dico2, destinée 
        à produire des dictionnaires.

        Pour cette seconde implémentation, l'idée est de stocker nos données dans une 
        liste de tuples (cle, valeur) : [(cle1, valeur1), (cle2, valeur2), ... ] 
    
        La liste est toujours triée par ordre croissant des clés, ce qui permettra 
        une recherche plus rapide.
    
    """

    ## Code à compléter

    class Dico2:
        """ Dictionnaire contenant une liste ordonnée de tuples (cle, valeur)."""

        def __init__(self, nb_de_bits):
            """ Constructeur : va créer une liste vide composée chacune de (2**nb_de_bits) 
                doublets vides ()."""
            self.doublets = []
            # CODER CI-DESSOUS, à la place de pass, le remplissage de la liste self.doublets
            pass

        def est_vide(self):
            """ Renvoie True si et seulement si l'objet de type Dico2 est vide, c'est à 
                dire qu'il ne contient qu'une liste de doublets vides ().
                Sinon renvoie False."""
            # CODER CI-DESSOUS, à la place de pass, la méthode est_vide()
            pass

        def affichage(self):
            """ Affiche dans la console le contenu du dictionnaire sous la forme suivante :
                        DEBUT
                        cle1 : valeur1
                        cle2 : valeur2
                        (...)
                        FIN
                Les cellules vides ne s'affichent pas.
                Cette méthode ne renvoie rien."""
            # CODER CI-DESSOUS, à la place de pass, la méthode affichage()
            pass    
    
        def taille(self):
            """ Renvoie le nombre de doublets stockés dans le dictionnaire."""
            # CODER CI-DESSOUS, à la place de pass, la méthode taille()
            pass
 
        def trouver_index(self, cle):
            """ Renvoie la valeur de l'index du doublet de la liste self.doublets 
                contenant cle, renvoie False si la clé est absente du dictionnaire."""
            # Pour une meilleure efficacité, la recherche s'effectuera par dichotomie.
            if self.est_vide() :
                return False
            b = len(self.doublets) - 1
            a = b - self.taille() + 1
            m = (a + b) // 2
            while a < b :
                if self.doublets[m][0] == cle:
                    return m
                elif self.doublets[m][0] > cle:
                    b = m - 1
                else :
                    a = m + 1
                m = (a + b) // 2
            if self.doublets[a][0] == cle:
                return a
            return False

        def lire(self, cle):
            """ Renvoie la valeur correspondante à la clé passée en paramètre.
                La recherche s'effectura par dichotomie.
                Renvoie None si cette clé n'existe pas."""
            # CODER CI-DESSOUS, à la place de pass, la méthode lire(cle)
            pass
        
        def est_plein(self):
            """ Renvoie True si le dictionnaire est plein , sinon renvoie False."""
            # CODER CI-DESSOUS, à la place de pass, la méthode est_plein()
            pass
      
        def ecrire(self, cle, valeur):
            """ Ajoute le doublet (cle, valeur) à la liste self.doublets
                Si la clé existe déjà, seule la (nouvelle) valeur est enregistrée 
                à la place de l'ancienne. 
                Ne renvoie rien."""
            # CODER CI-DESSOUS, à la place de pass, la méthode ecrire()
            pass
               
        def supprimer(self, cle):
            """ Supprime le doublet contenant cle dans la liste self.doublets.
                Ne renvoie rien."""
            # CODER CI-DESSOUS, à la place de pass, la méthode supprimer()
            pass
        

    ## Dictionnaire "dico" pré-rempli pour tester vos méthodes        
    if __name__=='__main__':
        dico = Dico2(4)
        for i in range(7):
            dico.ecrire(str(i), i)


    # Après avoir tout implémenté, esssayer d'entrer dico.ecrire( 3,'trois')... 
    # Que se passe-t-il ? Pourquoi ?
    # Rencontre-t-on le même problème avec votre première implémentation ? Pourquoi ?
    ```
    <center>
    [Correction de l'exercice 2 :material-cursor-default-click:](Correction_des_exos_du_TP.md#correction-de-lexercice-2){:target="_blank" .md-button}
    </center>

### <div class = "encadré3_TP">Implémentation d'un dictionnaire à partir d'une table de hachage</div>

<span class="border1"> __Description__ </span><div></div>
Les entrée du dictionnaire sont stockées dans une table de hachage qui est une liste de listes :
<div class="couleur_puce35" markdown = "1">

- La position de l’élément dans la table de niveau 0 est déterminée à partir de la fonction de hachage de Python.
- Les collisions sont gérées au moyen d'une liste de niveau 1 qui contient tous les éléments donnant le même résultat par la fonction de hachage.

</div>
Par exemple, pour un dictionnaire de taille 4 contenant 3 éléments :

```python
table = [[('trois', 3)], [('un', 1)], [('deux', 2], [ ]]
```

La position des éléments se justifie par :
<div class="couleur_puce35etoi" markdown = "1">

* `#!python hash('un')` renvoie `#!python -5160269262281110283` et `#!python -5160269262281110283 % 4` renvoie `#!python 1` donc la clé `#!python 'un'` sera stockée en position `#!python 1`.
* `#!python hash('deux') % 4` renvoie `#!python 2`.
* `#!python hash('trois') % 4` renvoie `#!python 0`

</div>

??? exercice2 {{exercice(False, niveau=2)}}
    Implémenter ce troisième et dernier dictionnaire en se basant sur le squelette suivant :
    ```python
    """ Implémentation n°3 d'un dictionnaire en programmation orientée objet Python

        Ce fichier est le squelette de départ d'un code d'une classe Dico3, destinée à produire     
        des dictionnaires.

        Pour cette troisième implémentation, l'idée est de stocker nos données dans une table 
        de hachage:
            - la position de l'élement dans la table est déterminée à partir de la fonction 
              de hash de Python;
            - les collisions sont gérées par chaînage linéaire au moyen d'une liste.
    """

    ## Code à compléter
    from math import floor, sqrt

    class Dico3:
        """ Dictionnaire contenant une table de hachage """

        def __init__(self, nb_de_bits):
            """ Constructeur : va créer une table dont les (2**nb_de_bits) éléments sont 
                initialisés à None."""
            self.longueur = 2 ** nb_de_bits
            self.table = [None] * self.longueur

        def _hachage(self, x):
            return hash(x) % self.longueur

        def est_vide(self):
            """ Renvoie True si et seulement si l'objet de type Dico3 est vide.
                Renvoie False sinon."""
            # CODER CI-DESSOUS, à la place de pass la méthode est_vide()
            pass
    
        def affichage(self):
            """ Affiche dans la console le contenu du dictionnaire sous la forme suivante :
                        DEBUT
                        indice1 - cle1 : valeur1
                        indice2 - cle2 : valeur2
                        (...)
                        FIN
                Les cellules vides ne s'affichent pas.
                Cette méthode ne renvoie rien."""
            # CODER CI-DESSOUS, à la place de pass la méthode affichage()
            pass
        
        def ecrire(self, cle, valeur):
            """ Ajoute le tuple (cle, valeur) à la position index = hash(cle) dans la table de 
                hachage."""
            # CODER CI-DESSOUS, à la place de pass la méthode ecrire()
            pass
        
        def taille(self):
            """ Renvoie le nombre de clés non vides stockées dans le dictionnaire """
            # CODER CI-DESSOUS, à la place de pass la méthode taille()
            pass
        
        def est_plein(self):
            """ Renvoie True ssi le dictionnaire est plein, sinon renvoie False."""
            # CODER CI-DESSOUS, à la place de pass la méthode est_plein()
            pass
        
        def supprimer(self, cle):
            """ Supprime le tuple (cle,valeur).
                Ne renvoie rien."""
            # CODER CI-DESSOUS, à la place de pass la méthode supprimer(cle)
            pass
        
        def contient(self, cle):
            """ Renvoie True si la clé existe, sinon renvoie False."""
            # CODER CI-DESSOUS, à la place de pass la méthode contient(cle)
            pass
        
        def lire(self, cle):
            """ Renvoie la valeur correspondante à la clé passée en paramètre.
                Renvoie None si cette clé n'existe pas."""
            # CODER CI-DESSOUS, à la place de pass la méthode lire(cle)
            pass
            

    ## Dictionnaire "dico" pré-rempli pour tester vos méthodes        
    if __name__=='__main__':
        dico = Dico3(4)
        for i in range(7):
            dico.ecrire(str(i), i)
    ```
    <center>
    [Correction de l'exercice 3 :material-cursor-default-click:](Correction_des_exos_du_TP.md#correction-de-lexercice-3){:target="_blank" .md-button}
    </center>

### <div class = "encadré3_TP">__Etude des complexités temporelles__</div>

#### <div class = "encadré4_TP">__Complexités théoriques__</div>

Dans ce paragraphe, nous allons étudier sommairement les complexités théoriques de 5 implémentations différentes d'un dictionnaire, à savoir :
<div class="couleur_puce35" markdown = "1">

* Les 3 dictionnaires que nous venons d'implémenter (`#!python Dico1` avec indexation à l'aide de deux listes, `#!python Dico2` avec indexation à l'aide d'une liste de tuples et `#!python Dico3` avec indexation par fonction de hachage et gestion des collisions par chaînage linéaire).
* `#!python Dico4` dont l'indexation se fait par fonction de hachage et la gestion des collisions par sondage linéaire :

</div>
<div class="decal1" markdown = "1">

??? plus-circle "__Code__"
    ```python
    """ Implémentation n°4 d'un dictionnaire en programmation orientée objet Python
        Ce fichier est le squelette de départ d'un code d'une classe Dico4, destinée 
        à produire des dictionnaires.
        Pour cette quatrième implémentation, l'idée est de stocker nos données en 
        déterminant leur position à partir d'une fonction de hachage :
            - Utilisation de la fonction hash de python.  
            - Gestion des collisions par sondage linéaire.
    """

    class Dico4:
        """ Dictionnaire contenant une table de hachage """

        def __init__(self, nb_de_bits):
            """ Constructeur : va créer une table dont les (2**nb_de_bits) éléments 
                sont initialisés à None."""
            
            self.longueur = 2 ** nb_de_bits      # nombre total d'éléments
            self.table = [None] * self.longueur
            self.collision = 0                 # compteur de collision

        def _hachage(self, x):
            return hash(x) % self.longueur

        def est_vide(self):
            """ Renvoie True si et seulement si l'objet de type Dico3 est vide, 
                sinon renvoie False"""
            
            for e in self.table:
                if e:
                    return False
            return True

        def affichage(self):
            """ Affiche dans la console le contenu du dictionnaire sous la forme 
                suivante :
                        DEBUT
                        indice1 - cle1 : valeur1
                        indice2 - cle2 : valeur2
                        (...)
                        FIN
                Les cellules vides ne s'affichent pas.
                Cette méthode ne renvoie rien."""
            
            ch = 'DEBUT\n'
            for index, valeurs in self.table.items():
                if valeurs:
                    if valeurs == 'del':
                        ch += f'{index} - del\n'
                    else:
                        cle, valeur = valeurs
                        ch += f'{index} - {cle} : {valeur}\n'
            ch += 'FIN'
            print(ch)
        
        def ecrire(self, cle, valeur):
            """ Ajoute le tuple (cle, valeur) à la position index = hash(cle) dans 
                la table de hachage."""
            
            index = self._hachage(cle)
            if self.table[index] and self.table[index][0] == cle:
                self.table[index] = (cle, valeur)
            else:
                cpt = 0
                while cpt < self.longueur and self.table[index] not in (None,'del'):
                    cpt += 1
                    index = (index + 1) % self.longueur # pour recommencer en début de liste une fois arrivé à la fin
                if cpt == self.longueur:
                    print('Débordement de la table de hachage')
                else:
                    self.table[index] = (cle,valeur)
                    self.collision += cpt 
            
        def taille(self):
            """ Renvoie le nombre de clés non vides stockées dans le dictionnaire."""
            
            cpt = 0
            for e in self.table:
                if e:
                    cpt += 1
            return cpt
            
        def est_plein(self):
            """ Renvoie True si le dictionnaire est plein , sinon renvoie False."""
            
            for e in self.table:
                if not e:
                    return False
            return True
            
        def supprimer(self, cle):
            """ Supprime le tuple (cle, valeur) : la case vidée de son contenu est
                alors marquée à 'del' afin de la distinguer d'une case jamais remplie et
                ainsi ne pas corrompre la méthode de gestion des collisions.
                Ne renvoie rien."""
            
            index = self._hachage(cle)
            cpt = 0
            while cpt < self.longueur and self.table[index]:
                if cle == self.table[index][0]:
                    self.table[index] = 'del'
                cpt += 1
                index = (index + 1) % self.longueur
            
        def contient(self, cle):
            """ Renvoie True si la clé existe, sinon renvoie False."""

            index = self._hachage(cle)
            cpt = 0
            while cpt < self.longueur and self.table[index]:
                if cle == self.table[index][0]:
                    return True
                cpt += 1
                index = (index + 1) % self.longueur
            return False
            
        def lire(self, cle):
            """ Renvoie la valeur correspondante à la clé passée en paramètre.
                Renvoie None si cette clé n'existe pas."""
            
            index = self._hachage(cle)
            cpt = 0
            while cpt < self.longueur and self.table[index]:
                if cle == self.table[index][0]:
                    return self.table[index][1]
                cpt += 1
                index = (index + 1) % self.longueur
            return None
    

    from random import shuffle        

    if __name__=='__main__':
        jeu_donnees = [i for i in range(12)]
        shuffle(jeu_donnees)
        dico = Dico4(4)
        for i in jeu_donnees:
            dico.ecrire(str(i), i)

    ```
</div>
<div class="couleur_puce35" markdown = "1">

* `#!python DicoPython` dont l'indexation se fait par fonction de hachage et la gestion des collisions par redimensionnement dynamique :

</div>
<div class="decal1" markdown = "1">

??? plus-circle "__Code__"
    ```python
    """ Implémentation "Python" d'un dictionnaire en programmation orientée objet Python.
        Ce fichier utilise des dictionnaires Python.
    """

    class DicoPython:
        """ Dictionnaire contenant deux listes non ordonnées """

        def __init__(self, nb_de_bits):
            """ Constructeur : """
            self.dico = {}

        def est_vide(self):
            """ Renvoie True si et seulement si l'objet de type DicoPython est vide,
                c'est à dire qu'il ne contient que des listes de None.
                Sinon renvoie False."""

            return len(self.dico) == 0

        def affichage(self):
            """ Affiche dans la console le contenu du dictionnaire sous la forme suivante :
                        DEBUT
                        cle1 : valeur1
                        cle2 : valeur2
                        (...)
                        FIN
                Les cellules vides ne s'affichent pas.
                Cette méthode ne renvoie rien."""

            print("DEBUT")
            for cle, valeur in self.dico.items():
                print(cle, ":", valeur)
            print('FIN')

        def ecrire(self, cle, valeur):
            """ Ajoute cle en queue de la liste self.cles,
                ajoute valeur en queue de la liste self.valeurs.
                Si la clé existe déjà, seule la (nouvelle) valeur est enregistrée
                à la place de l'ancienne.
                Ne renvoie rien."""

            self.dico[cle] = valeur

        def taille(self):
            """"Renvoie le nombre de cles non vides stockées dans le dictionnaire"""

            return len(self.dico)

        def supprimer(self, cle):
            """ Supprime la valeur correspondante à cle dans la liste self.valeurs,
                Supprime cette clé de la liste self.cles.
                Ne renvoie rien."""

            del self.dico[cle]

        def contient(self, cle):
            """ Renvoie True si la clé existe, sinon renvoie False."""

            if cle in self.dico.keys():
                return True
            return False

        def lire(self, cle):
            """ Renvoie la valeur correspondante à la clé passée en paramètre.
                Renvoie None si cette clé n'existe pas."""

            return self.dico[cle]


    from random import shuffle

    if __name__=='__main__':
        jeu_donnees = [i for i in range(12)]
        shuffle(jeu_donnees)
        dico = DicoPython(4)
        for i in jeu_donnees:
            dico.ecrire(str(i), i)
    ```

</div>
Pour chacune des cinq implémentations, nous allons estimer la complexité temporelle des trois méthodes de classe `#!python ecrire`, `#!python lire` et `#!python supprimer` à partir de l’analyse algorithmique de leur code source :
<div class="couleur_puce35etoi" markdown = "1">

* `#!python Dico1` __:__  
<span style="display: block; margin: 5px 0 0 0;">Les deux méthodes `#!python lire` et `#!python supprimer` font appel à la fonction `#!python trouver_index` qui implémente une boucle bornée.</span> 
<span style="color:red">⇒</span> complexité en $~\mathcal{O}(n)$.  
<span style="display: block; margin: 5px 0 10px 0;">Concernant la méthode `#!python ecrire`, en plus de l’appel à la fonction `#!python trouver_index` il faut également procéder à la recherche du premier emplacement vide (recherche de type séquentielle de complexité linéaire).</span>
<span style="color:red">⇒</span> __Complexité temporelle globale en $~\mathcal{O}(n)$.__
* `#!python Dico2` __:__  
<span style="display: block; margin: 5px 0 0 0;">La méthode `#!python lire` fait appel à la fonction `#!python trouver_index` dont le principe algorithmique est celui de la recherche par dichotomie dans une liste triée <span style="color:red">⇒</span> complexité temporelle en $~\mathcal{O}(\operatorname{log_2}$$(n$$))$.</span>
<span style="display: block; margin: 5px 0 10px 0;">Les méthodes `#!python ecrire` et `#!python supprimer` font également appel à la fonction `#!python trouver_index`, mais elles implémentent en plus une fonction de tri (`#!python sort`).</span>
<span style="color:red">⇒</span> __Complexité temporelle globale en $~\mathcal{O}(n\operatorname{log_2}(n))$.__
* `#!python Dico3` __:__  
<span style="display: block; margin: 5px 0 0 0;">Les trois méthodes `#!python lire`, `#!python ecrire` et `#!python supprimer` font appel à la fonction `#!python _hachage` (coût constant) pour déterminer l’indice correspondant à la position réelle d’une donnée.</span>
<span style="display: block; margin: 5px 0 0 0;">Compte tenu de la méthode de gestion des collisions (par chaînage linéaire), la recherche d’un élément à une position donnée s’opère de façon séquentielle c’est-à-dire avec une complexité temporelle linéaire.</span>
<span style="display: block; margin: 5px 0 10px 0;">Toutefois, dans l’hypothèse d’un nombre faible de collisions voire d’une absence de collision (cas le plus favorable), l’accès aux données se fait directement à partir de la position calculée par la fonction de hachage (coût constant) puisqu’à chaque élément de la liste correspond alors un unique tuple de données.</span>
<span style="color:red">⇒</span> __Complexité temporelle en $~\mathcal{O}(1)~$ dans le cas le plus favorable pour les trois méthodes.__
* `#!python Dico4` __:__  
<span style="display: block; margin: 5px 0 0 0;">Les trois méthodes `#!python lire`, `#!python ecrire` et `#!python supprimer` font appel à la fonction `#!python _hachage` (coût constant) pour calculer l’indice correspondant à la position d’une donnée.</span>
<span style="display: block; margin: 5px 0 0 0;">Compte tenu de la méthode de gestion des collisions (par sondage linéaire), la recherche d’un élément à partir de sa position calculée s’opère de façon séquentielle c’est à dire avec une complexité temporelle linéaire.</span>
<span style="display: block; margin: 5px 0 10px 0;">Toutefois, dans l’hypothèse d’un nombre faible de collisions voire d’une absence de collision (cas le plus favorable), l’accès aux données se fait directement à partir de la position calculée par la fonction de hachage (coût constant) qui correspond alors à la position réelle dans la liste.</span>
<span style="color:red">⇒</span> __Complexité temporelle en $~\mathcal{O}(1)~$ dans le cas le plus favorable pour les trois méthodes.__
* `#!python DicoPython` __:__  
<span style="display: block; margin: 5px 0 0 0;">Cette implémentation utilise directement le type natif `#!python dict` de Python (cf documentation ci-dessous) :</span>

</div> 
<div class="couleur_puce35carré_decal" markdown = "1">

- Types natifs -- Les types de correspondances — dict  
<a href="https://docs.python.org/fr/3/library/stdtypes.html#mapping-types-dict" target="_blank">https://docs.python.org/fr/3/library/stdtypes.html#mapping-types-dict</a>
- PEP 456 -- Secure and interchangeable hash algorithm : SipHash  
<a href="https://www.python.org/dev/peps/pep-0456/#siphash" target="_blank">https://www.python.org/dev/peps/pep-0456/#siphash</a>

</div>
<center markdown = "1">
<span class="border2"> __Synthèse des résultats__ </span><div></div>
</center>
<center markdown = "1">

|               | `#!python Dico1`                       | `#!python Dico2`                                                      | `#!python Dico3`                           | `#!python Dico4`                   | `#!python DicoPython`              |
|:------------: |:----------------------------: |:-----------------------------------------------------------: |:-------------------------: |:------------------------: |:------------------------: | 
|`#!python lire`         | $~\mathcal{O}(n)$   |$~\mathcal{O}(\operatorname{log_2}(n))$   |$~\mathcal{O}(1)$|$~\mathcal{O}(1)$|$~\mathcal{O}(1)$|
|`#!python ecrire`       | $~\mathcal{O}(n)$   |$~\mathcal{O}(n\operatorname{log_2}(n))$  |$~\mathcal{O}(1)$|$~\mathcal{O}(1)$|$~\mathcal{O}(1)$|
|`#!python supprimer`    | $~\mathcal{O}(n)$   |$~\mathcal{O}(n\operatorname{log_2}(n))$  |$~\mathcal{O}(1)$|$~\mathcal{O}(1)$|$~\mathcal{O}(1)$|

</center>

#### <div class = "encadré4_TP">__Complexités mesurées__</div>

Protocole de tests :
<div class="couleur_puce18" markdown = "1">

* Liste de dimension fixe avec $~N=2^{12}=4096~$ éléments.
* Jeux de données constitués d’une série de `#!python n` tuples de la forme `#!python (str(x), int(x))` sans doublons et ordonnés aléatoirement, avec `#!python n` variant de 100 à 2000 éléments.

</div>

??? exercice2 {{exercice(False, niveau=2)}}
    <div class = "list7_1">

    1. A l'aide du script suivant, ordonner par ordre croissant du temps d’exécution les cinq implémentations `#!python Dico1`, `#!python Dico2`, `#!python Dico3`, `#!python Dico4` et `#!python DicoPython` pour chacune des trois méthodes de classe `#!python ecrire`, `#!python lire` et `#!python supprimer`:
    ```python
    # -*- coding: utf-8 -*-
    """
        Mesure des complexités temporelles des méthodes ECRIRE, LIRE et SUPPRIMER pour
        les différentes implémentations du type dictionnaire.
        Représentation des résultats par méthodes implémentées.
        !!! Penser à changer éventuellement le nom des scripts contenant chaque dico !!!
    """

    from Implementation_avec_2_listes import Dico1
    from Implementation_avec_liste_de_tuples import Dico2
    from Implementation_avec_table_de_hachage_chainage import Dico3
    from Implementation_avec_table_de_hachage_sondage import Dico4
    from Implementation_de_Python import DicoPython
    import timeit
    from random import shuffle
    from functools import partial
    import matplotlib.pyplot as plt


    # =============================================================================
    # METHODES A MESURER
    # =============================================================================

    taille_dico_en_bits = 12

    def creation(DicoX):
        #print("Génération de ", DicoX, end="")
        return DicoX(taille_dico_en_bits)

    def ecrire(D, d):
        for clef, valeur in d:
            D.ecrire(clef,valeur)
        #print(len(d), " entrées écrites", end="")

    def lire(D, d):
        for clef,val in d:
            valeur_poubelle = D.lire(clef)
        #print(len(d), " entrées lues", end="")

    def supprimer(D, d):
        for clef,val in d:
            D.supprimer(clef)
        #print(len(d), " entrées supprimées", end="")

    # =============================================================================
    # TESTS
    # =============================================================================

    liste_des_dicos = [Dico1, Dico2, Dico3, Dico4, DicoPython]

    # Création des jeux de données
    jeux_donnees = []
    for nb_elements in [100*i for i in range(21)]:
        donnees = [(str(x),x) for x in range(nb_elements)] # Listes de couples (cle, valeur) de taille 0, 100, 200, ... ,2000.
        shuffle(donnees) # On mélange les éléments de chaque liste
        jeux_donnees.append(donnees) # ajout de chaque liste générée dans une liste


    # Mesures : une liste de 3 listes pour chacun des dictionnaires
    mesures = [[[] for _ in range(3)] for _ in range(len(liste_des_dicos))]

    for i, dico in liste_des_dicos.items(): # Pour chaque dico
        for d in jeux_donnees: # Pour chaque liste du jeu de données
            D = creation(dico) # instantanciation d'un dictionnaire
            curryE = partial(partial(ecrire, D), d) # A l'aide de la méthode partial, curryE est une fonction qui renvoie (ecrire(D, d))
            mesureE = timeit.Timer(curryE) # On mesure le temps d'exécution de (ecrire(D, d))
            tE = mesureE.repeat(repeat = 1, number = 1)
            mesures[i][0].append((len(d), tE)) # On ajoute le couple (longueur du dico, temps d'exécution de la méthode ecrire) dans le tableau mesures
            curryL = partial(partial(lire, D), d)
            mesureL = timeit.Timer(curryL)
            tL = mesureL.repeat(repeat = 1, number = 1)
            mesures[i][1].append((len(d), tL)) # Même chose avec la méthode lire
            curryS = partial(partial(supprimer, D), d)
            mesureS = timeit.Timer(curryS)
            tS = mesureS.repeat(repeat = 1, number = 1)
            mesures[i][2].append((len(d), tS)) # Et la méthode supprimer


    # Graphiques
    couleurs = ['r', 'g', 'b', 'y', 'c', 'm', 'k']
    fonctions_de_test = [ecrire, lire, supprimer]

    for j in range(len(fonctions_de_test)):
        plt.figure("Temps d'execution de la méthode " + fonctions_de_test[j].__name__ +" en fonction du nombre d'opérations effectées" )
        for i in range(len(liste_des_dicos)):
            x, y = [], []
            for d, t in mesures[i][j]:
                x.append(d)
                y.append(t)
            titre = fonctions_de_test[j].__name__ + " dans " + liste_des_dicos[i].__name__
            plt.plot(x, y, color = couleurs[i], label = titre)
        plt.legend(loc = 'upper left')
        plt.grid(True)
    plt.show()
    ```
    2. Les résultats obtenus sont-ils cohérents avec ceux établis lors de l’étude théorique des complexités temporelles ? Conclure.
    
    </div>
    <center>
    [Correction de l'exercice 4 :material-cursor-default-click:](Correction_des_exos_du_TP.md#correction-de-lexercice-4){:target="_blank" .md-button}
    </center>

