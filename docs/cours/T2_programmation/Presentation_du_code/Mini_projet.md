# <center><div class = "titre3"> Exercice </div></center>

Cet exercice consiste à réaliser une application qui valide ou non la création d'un mot de passe. 
Ce mot de passe doit être constitué de 8 caractères au minimum et doit comprendre au minimum :
<div class= "couleur_puce9" markdown="1">

* 3 chiffres ;
* 1 majuscule ;
* 2 caractères spéciaux parmi les 5 suivants : `#!python #`, `#!python @`, `#!python |`, `#!python ~` et `#!python §`.

</div>

Un des objectifs de ce mini-projet est de développer des processus de mise au point et de validation de ce programme.
<div class = "list2_1" markdown="1">

1. Créer les fonctions unitaires suivantes :

</div>
<div class = "list3_a" markdown="1">

1. `#!python type_parametre(text)` qui renvoie le type de la variable `#!python text`.
2. `#!python presence_3_chiffres_min(text)` qui teste la présence d'au minimum 3 chiffres dans le mot de passe.
3. `#!python presence_maj(text)` qui teste la présence d'au moins une majuscule dans le mot de passe.
4. `#!python nb_caract_speciaux(text)` qui renvoie le nombre de caractères spéciaux contenus dans le mot de passe parmi les 5 de la liste.
5. `#!python presence_8_caract_min(text)` qui teste la présence d'au moins 8 caractères dans le mot de passe.

</div>
<div class = "list2_2" markdown="1">

2. Proposer à l'aide du module __unittest__ un jeu de test permettant de tester et valider ces fonctions.

</div>
<div class="decal1" markdown="1">

??? tools "__Conseil__"
	On pourra par exemple tester :
	<div class= "couleur_puce6">

	* La fonction `#!python type_parametre()` sur les 4 types principaux de Python : `#!python int`, `#!python float`, `#!python str` et `#!python bool`.
	* La fonction `#!python presence_3_chiffres_min()` avec les chaînes suivantes : `#!python "1234"`, `#!python "123"`, `#!python "12a"`, `#!python ""` et `#!python "a234"`.
	* La fonction `#!python presence_maj()` avec les chaînes suivantes : `#!python "a"`, `#!python "A"`, `#!python "1"` et `#!python "@"`.
	* La fonction `#!python nb_caract_speciaux()` avec les chaînes suivantes : `#!python "12-"`, `#!python "#a"` et `#!python "#@|~§"`.
	* La fonction `#!python presence_8_caract_min()` avec les chaînes suivantes : `#!python "12345678"` et `#!python "#a"`.

	</div>

</div>
<div class = "list2_3" markdown="1">

3. Modifier les fonctions pour lesquelles le jeu de tests a fait apparaître une erreur.
4. Créer enfin la fonction `#!python test_MDP(text)` qui valide ou non un mot de passe.

</div>

