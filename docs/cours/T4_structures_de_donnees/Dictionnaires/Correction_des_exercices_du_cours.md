# <center><div class = "titre2"> Correction des exercices du cours </div></center>

### <div class = "encadré_exo"> __Correction de l'exercice 1__ </div>
<div class = "list1_1" markdown = "1">

1.  
	```pycon
	>>> dico = {}
	```
2.  
	```pycon
	>>> dico['house'] = 'maison'
	>>> dico['bunk beds'] = 'lits superposés'
	>>> dico['kitchen'] = 'cuisine'
	>>> dico['bed room'] = 'pièce lit'
	```
3. 
	```pycon
	>>> dico
	{'house': 'maison', 'bunk beds': 'lits superposés', 'kitchen': 'cuisine', 'bed room': 'pièce lit'}
	```
4. 
	```pycon
	>>> len(dico)
	4
	```

</div>

### <div class = "encadré_exo"> __Correction de l'exercice 2__ </div>

```pycon
>>> dico.get('kitchen')
'cuisine'

>>> dico['bed room']
'pièce lit'

>>> dico.get('corridor')

>>> dico.get('corridor', "cette clé n'est pas dans le dictionnaire")
"cette clé n'est pas dans le dictionnaire"
```

### <div class = "encadré_exo"> __Correction de l'exercice 3__ </div>

```pycon
>>> dico['bed room'] = 'chambre'

>>> dico
{'house': 'maison', 'bunk beds': 'lits superposés', 'kitchen': 'cuisine', 'bed room': 'chambre'}
```

### <div class = "encadré_exo"> __Correction de l'exercice 4__ </div>

```pycon
>>> dico.pop('house')
'maison'

>>> dico
{'bunk beds': 'lits superposés', 'kitchen': 'cuisine', 'bed room': 'chambre'}
```

### <div class = "encadré_exo"> __Correction de l'exercice 5__ </div>
<div class = "list1_1" markdown = "1">

1. 
	```pycon
	>>> list(dico.keys())
	['bunk beds', 'kitchen', 'bed room']

	>>> tuple(dico.keys())
	('bunk beds', 'kitchen', 'bed room')

	>>> list(dico.values())
	['lits superposés', 'cuisine', 'chambre']

	>>> tuple(dico.values())
	('lits superposés', 'cuisine', 'chambre')

	>>> dico.items()
	dict_items([('bunk beds', 'lits superposés'), ('kitchen', 'cuisine'), ('bed room', 'chambre')])
	```
2. 
	```pycon
	>>> for cle in dico.keys() :
	...     print(f"Les clés du dictionnaire sont {cle}")
	...     
	... 
	Les clés du dictionnaire sont bunk beds
	Les clés du dictionnaire sont kitchen
	Les clés du dictionnaire sont bed room
	```
3. 
	```pycon
	>>> for valeur in dico.values() :
	...     print(f"Les valeurs du dictionnaire sont {valeur}")
	...     
	... 
	Les valeurs du dictionnaire sont lits superposés
	Les valeurs du dictionnaire sont cuisine
	Les valeurs du dictionnaire sont chambre
	```

</div>
### <div class = "encadré_exo"> __Correction de l'exercice 6__ </div>
<div class = "list6_1" markdown = "1">

1. 
	```pycon
	>>> list(dico.keys())
	['bunk beds', 'kitchen', 'bed room']

	>>> tuple(dico.keys())
	('bunk beds', 'kitchen', 'bed room')

	>>> list(dico.values())
	['lits superposés', 'cuisine', 'chambre']

	>>> tuple(dico.values())
	('lits superposés', 'cuisine', 'chambre')

	>>> dico.items()
	dict_items([('bunk beds', 'lits superposés'), ('kitchen', 'cuisine'), ('bed room', 'chambre')])
	```
2. 
	```pycon
	>>> dico2 = dico.copy()

	>>> dico2
	{'bunk beds': 'lits superposés', 'kitchen': 'cuisine', 'bed room': 'chambre'}

	>>> dico2['house'] = 'maison'

	>>> dico2
	{'bunk beds': 'lits superposés', 'kitchen': 'cuisine', 'bed room': 'chambre', 'house': 'maison'}

	>>> dico
	{'bunk beds': 'lits superposés', 'kitchen': 'cuisine', 'bed room': 'chambre'}
	```

</div>

### <div class = "encadré_exo"> __Correction de l'exercice 7__ </div>
<div class = "list6_1" markdown = "1">

1. L'opérateur modulo donne le reste de la division euclidienne..
2. 
</div>
<div class="decal1" markdown = "1">

| Clé : $x$ | 10          |              22|      31  |              4 |              28|
| :-------: | :---------: | :-------------:|:--------:| :-------------:| :-------------:| 
| $h(x)$    |    10       |   0            |  9       |     4          |       6        |

</div>
<div class = "list6_3" markdown = "1">

3. Compléter la table de hachage en plaçant les clés.
</div>
<div class="decal1" markdown = "1">

| 0     | 1     |       2|       3  |         4 |       5|       6|       7|       8|       9|      10|
|:----: |:----: |:------:|:--------:| :--------:| :-----:| :-----:| :-----:| :-----:| :-----:| :-----:| 
|22     |       |        |          |   4       |        |   28   |        |        |  31    |     10 |
    
</div>
<span style="display: block; margin: 30px 0 0 0;">On cherche maintenant à placer la clé $~15$.</span>
<div class = "list6_4" markdown = "1">

4. On obtient $~4~$ qui est déjà occupée.
5. Il y a une méthode qui semble évidente : décaler et trouver une place vide mais comment décaler ?

</div>

### <div class = "encadré_exo"> __Correction de l'exercice 8__ </div>
<div class = "list6_1" markdown = "1">

1. Une liste chaînée est une liste dans laquelle les cellules contiennent une info de valeur et une info de lien avec la suivante.  
On doit donc la parcourir de façon séquentielle.
2. 
</div>
<div class="decal1" markdown = "1">

| 0     | 1     |       2|       3  |         4 |       5|       6|       7|       8|       9|      10|
|:----: |:----: |:------:|:--------:| :--------:| :-----:| :-----:| :-----:| :-----:| :-----:| :-----:| 
|22     |       |        |          |    4      |        |  28    |        |        |   31   | 10     |
|88     |       |        |          |    15     |        |  83    |        |        |        |        |
|<br>   |       |        |          |    59     |        |        |        |        |        |        |
|<br>   |       |        |          |    37     |        |        |        |        |        |        |

</div>
<div class = "list6_3" markdown = "1">

3. Elle requiert de la mémoire externe à la table.

</div>

### <div class = "encadré_exo"> __Correction de l'exercice 9__ </div>

On retrouve $~h(x)~~mod~m~$ ce qui donne $~x~~mod~11$.

### <div class = "encadré_exo"> __Correction de l'exercice 10__ </div>

| 0     | 1     |       2|       3  |         4 |       5|       6|       7|       8|       9|      10|
|:----: |:----: |:------:|:--------:| :--------:| :-----:| :-----:| :-----:| :-----:| :-----:| :-----:| 
|22     |    37 |        | 59       |   4       | 15     |   28   | 83     |   88   | 31     |     10 |