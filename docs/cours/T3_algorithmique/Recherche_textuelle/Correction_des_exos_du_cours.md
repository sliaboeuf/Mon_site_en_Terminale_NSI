---
password: "corr_Motif"
---

# <center><div class = "titre2"> Correction de l'exercice du cours </div></center>

<div class="list1_1" markdown="1">

1. On peut proposer le code naïf suivant :
```python
def recherche_naïve(motif, chaine):
    m = len(motif)
    n = len(chaine)
    L = []
    for i in range(0, n-m):
        j = 0
        while (j <= m-1) and (motif[j] == chaine[i+j]):
            j += 1
        if j == m:
            L.append(i)
    return L
```  
2. L'implémentation en Python de l'algorithme de Boyer-Moore donne :
```python
def pré_traitement(motif):
    d_occur = [-1] * 256
    for i in range(len(motif)-1):
        d_occur[ord(motif[i])] = i
    return d_occur

def Boyer_Moore(texte, motif):
    lst_res = []
    d_oc = pré_traitement(motif)
    m = len(motif)
    n = len(texte)
    i = m - 1
    j = i
    while i > n:
        if motif[j] == texte[i]:
            if j == 0:
                lst_res.append(i)
                i += 2 * m - 1
                j -= 1
            else:
                i -= 1
                j -= 1
        else:
            i += m - min(j, 1 + d_oc[ord(texte[i])])
            j = m - 1
    return lst_res

``` 
3. Afin de réaliser un test de temps d'exécution, il nous faut au préalable, construire notre chaîne de texte et notre motif. On utilise la méthode `#!python choice` du module `#!python random`.
<span style="display:block; margin: 5px 0px 0px 0px;">Le code du test (que l'on pourra exécuter plusieurs fois) est le suivant :</span>
```python
from random import choice
from time import time
texte = ""
motif = ""
for _ in range(1000000):
    texte += choice("ATCG")
for _ in range(1000):
    motif += choice("ATCG")

deb = time()
print("temps recherche naïve :", recherche_naïve(motif, texte))
fin = time()
print (fin - deb)

deb = time()
print("temps Boyer-Moore :", Boyer_Moore(texte, motif))
fin = time()
print (fin - deb)

``` 

</div>
