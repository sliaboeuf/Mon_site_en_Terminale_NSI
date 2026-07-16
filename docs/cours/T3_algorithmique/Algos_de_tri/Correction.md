---
password: "corr_Tri"
---

# <center><div class = "titre2">Correction des exercices</div></center>

### <div class = "encadré_exo"> __Correction de l'exercice 6__ </div>

```python

def tri_selection_decr(tableau):
    for i in range(len(tableau) - 1):
        i_maxi = i
        for j in range(i + 1, len(tableau)):
            if tableau[j] > tableau[i_maxi]:
                i_maxi = j
        tableau[i], tableau[i_maxi] = tableau[i_maxi], tableau[i]
```

### <div class = "encadré_exo"> __Correction de l'exercice 7__ </div>

```python

def tri_insertion_decr(tableau):
    for i in range(1, len(tableau)):
        valeur_a_inserer = tableau[i]
        j = i
        while j > 0 and tableau[j - 1] < valeur_a_inserer:
            tableau[j] = tableau[j - 1]
            j = j - 1
        tableau[j] = valeur_a_inserer
```

### <div class = "encadré_exo"> __Correction de l'exercice 8__ </div>

```python

def indice_minimum_depuis(tableau, i):
    i_mini = i
    for j in range(i + 1, len(tableau)):
        if tableau[j][0] > tableau[i_mini][0]:
            i_mini = j
        elif tableau[j][0] == tableau[i_mini][0]:
            if tableau[j][1] < tableau[i_mini][1]:
                i_mini = j
    return i_mini


def tri_eleves(tableau):
    for i in range(len(tableau) - 1):
        i_mini = indice_minimum_depuis(tableau, i)
        tableau[i], tableau[i_mini] = tableau[i_mini], tableau[i]
```