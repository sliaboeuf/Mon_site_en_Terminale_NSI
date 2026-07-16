# <center><div class = "titre2">Exercices</div> </center>

### <div class = "encadré_exo"> __Exercice 1__ </div>
   
> Le Titanic appareille de Southampton (Angleterre) le mercredi 10 avril à 12 h 15.
> <span style="display: block; margin: 8px 0 0 0;">Six heures plus tard, à 18 h 15, il fait escale dans la rade de Cherbourg. Il y débarque 24 passagers et en embarque 274, amenés par les transbordeurs Nomadic et Traffic. Il appareille à 20 h 10.</span>
> <span style="display: block; margin: 8px 0 0 0;">Le Titanic fait route vers l'Irlande. Il arrive à Queenstown (aujourdhui Cobh) le 11 avril à 11 h 30. Il débarque 7 passagers et en embarque 120. À 13 h 30, le paquebot appareille et entame sa traversée de l'Atlantique vers New York.</span>
> <span style="display: block; margin: 8px 0 0 0;">Le 14 avril, à 23 h 40 (heure locale, GMT-3), il percute un iceberg au large de Terre-Neuve. Il sombre le 15 avril à 2 h 20, causant la mort de 1 524 personnes.</span>
> <span style="display: block; margin: 12px 0 0 0;">(source [wikimanche](https://www.wikimanche.fr/Titanic){. target="_blank"} )</span>

On souhaite analyser les données de bord du Titanic lors de cette aventure. On dispose d'une liste Python avec des informations sur les passagers. Chaque élément de la liste est un passager représenté par un dictionnaire. En voici un extrait :

```python
passagers = [
    {'PassengerId': 1,
     'Survived': False,
     'Pclass': 3,
     'Name': 'Braund, Mr. Owen Harris',
     'Sex': 'male',
     'Age': 22.0,
     'SibSp': 1,
     'Parch': 0,
     'Ticket': 'A/5 21171',
     'Fare': 7.25,
     'Embarked': 'S'
    },
    {'PassengerId': 2,
     'Survived': True,
     'Pclass': 1,
     'Name': 'Cumings, Mrs. John Bradley (Florence Briggs Thayer)',
     'Sex': 'female',
     'Age': 38.0,
     'SibSp': 1,
     'Parch': 0,
     'Ticket': 'PC 17599',
     'Fare': 71.2833,
     'Cabin': 'C85',
     'Embarked': 'C'
    },
    ...
]
```

Télécharger ce fichier ([donnees_titanic.py](Fichiers/donnees_titanic.py)) dans le même dossier que votre code Python.
<span style="display: block; margin: 8px 0 0 0;">Le fichier ci-dessus contient la liste non-exhaustive de 891 passagers. En raison de sa taille importante, son ouverture peut faire planter votre logiciel de programmation. Pensez donc à enregistrer votre travail régulièrement !</span>
<span style="display: block; margin: 8px 0 0 0;">En cas d'absence d'information, la clé n'est pas présente ! Vous devez donc vous assurer que la clé existe avant de récupérer sa valeur.</span>
<span style="display: block; margin: 8px 0 0 0;">Afin d'importer ces données, ajouter le code suivant dans votre fichier `#!python titanic.py` :</span>

```python
from donnees_titanic import passagers
```
<div class="list1_1" markdown="1">

1. Rédiger un programme qui :

</div>
<div class="list1_a" markdown="1">

1. affiche le nombre de passagers dans la liste (891) ;
2. vérifie que le passager 54 est :
*Faunthorpe, Mrs. Lizzie (Elizabeth Anne Wilkinson) agée de 29 ans, embarquée à Southampton en classe 2 et a survécu au naufrage* ;
3. affiche le nombre de survivants (342).

</div>
<div class="list1_2" markdown="1">

1. Sachant qu'il y a [trois classes](https://fr.wikipedia.org/wiki/Passagers_du_Titanic#Des_passagers_aux_origines_diverses){. target="_blank"} (1, 2 et 3), écrire un programme qui affiche le pourcentage de survivants par classe.
2. Sachant qu'un passager embarqué à Cherbourg est représenté par la valeur `#!python 'C'` associée à la clé `#!python 'Embarked'`, écrire un programme qui donne le nombre de survivants embarqués à Cherbourg (18%).

</div>
<center>
[Correction de l'exercice 1 :material-cursor-default-click:](Correction_des_exercices.md#correction-de-lexercice-1){:target="_blank" .md-button}
</center>

### <div class = "encadré_exo"> __Exercice 2__ </div>

On souhaite écrire un programme qui compte les occurences de mots dans un texte afin de connaître les mots les plus fréquents.
<div class="list1_1" markdown="1">

1. Compléter la définition de la fonction `#!python occurences(sequence)` en respectant les spécifications.
	```python
	def occurrences(sequence):
	    """
	    Compte les occurences dans une liste
	    :param sequence: Une séquence ordonnée (tuple, list ou str)
	    :return: dictionnaire tel que :
	            - les clefs sont les valeurs de la séquence
	            - les valeurs sont les occurrences de ces clefs dans la séquence
	    >>> occurrences([4, 2, 3, 4, 1, 4, 3, 4])
	    {4: 4, 2: 1, 3: 2, 1: 1}
	    >>> occurrences("abracadrabra")
	    {'a': 5, 'b': 2, 'r': 3, 'c': 1, 'd': 1}
	    """
	    pass
    
    ```
2. Compléter la définition de la fonction `#!python compte_mots(phrase)` en respectant les spécifications.
	```python	
	def compte_mots(phrase):
	    """
	    Compte les occurences de mots dans une chaîne de caractères
	    :param phrase: une chaîne de caractère comportant des espaces
	    :return: dict – dictionnaire tel que :
	            - les clés sont les mots de la chaine
	            - les valeurs sont les occurrences des mots
	    >>> compte_mots("a b a c ab")
	    {'a': 2, 'b': 1, 'c': 1, 'ab': 1}
	    """
	    pass

	```
3. Télécharger le texte du ([« Petit Chaperon Rouge »](Fichiers/Petit_Chaperon_Rouge_Sans_Ponctuation.txt)) dans le même dossier que le code Python.
<span style="display: block; margin: 5px 0 0 0;">Dans le programme principal, importer ce texte puis écrire les instructions nécessaires pour afficher, dans la console, chaque mot de ce texte suivi de son nombre d'occurrences dans le texte.</span>
<div class="decal1" markdown="1">

??? tools "Rappel : ouverture d'un fichier en mode lecture"
	```python
	f = open('nom.txt', 'r')
	chaine_de_caracteres = f.read()
	f.close()
	```
</div>

</div>
<div class="list1_4" markdown="1">

4. Compléter la définition de la fonction `#!python compte_tous_mots(phrase)` en respectant ses spécifications.
	```python
	def compte_tous_mots(phrase):
	    """
	    Compte le nombre de mots selon la taille dans une chaîne de caractères
	    :param phrase: une chaîne de caractère comportant des espaces
	    :return: dict – dictionnaire tel que :
	            - les clés sont des entiers (longueurs possibles pour un mot)
	            - les valeurs sont les occurrences des mots ayant cette longueur
	    >>> compte_tous_mots("a b a c ab")
	    {1: 4, 2: 1}
	    """
	    pass

	```
Appliquer ensuite, dans le programme principal, cette fonction au texte du « Petit Chaperon Rouge ».
5. Compléter la définition de la fonction `#!python plus_frequent(dico, longueur)` qui prend en paramètre un dictionnaire dont les clés sont des chaînes de caractères et un entier strictement positif `#!python longueur`.
	```python
	def plus_frequent(dico, longueur):
	    """
	    Renvoie les mots les plus fréquents de la longueur donnée. En cas d'égalité en fréquence, on renverra tous les mots
	    de cette égalité.
	    :param dico: dictionnaire de chaines avec leur occurence
	    :param longueur: longueur à regarder pour trouver les mots
	    :return: string – chaine de taille longueur ayant
	             l'occurence la plus grande.
	    >>> plus_frequent({'a': 3, 'b': 2, 'c': 3, 'ab': 5}, 1)
	    ['a', 'c']
	    """
	    pass

	```
Cette fonction renvoie un tableau constitués des chaînes de caractères de taille la longueur spécifiée et associées à la plus grande valeur dans le dictionnaire.

</div>
<center>
[Correction de l'exercice 2 :material-cursor-default-click:](Correction_des_exercices.md#correction-de-lexercice-2){:target="_blank" .md-button}
</center>