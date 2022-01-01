# <center><div class = "titre2" markdown="1"> Exercices </div></center>
  
### <div class = "encadré17" markdown="1"> __Exercice 1__ </div>

Donner l'expression __SQL__ des requêtes suivantes ainsi que le résultat obtenu :
<div class="list1_1" markdown="1">

1. Noms des stations ayant strictement plus de 200 places.
2. Noms des clients dont le nom commence par « J » ou dont le solde est supérieur à 10000.
3. Noms des stations qui proposent de la plongée.
4. Noms des clients qui sont allés à La Bourboule.
5. Noms des stations visitées par des européens.
</div>

[Correction de l'exercice](Correction_des_exercices.md#correction-de-lexercice-1){:target="_blank"}

### <div class = "encadré17" markdown="1"> __Exercice 2__ </div>

Donner l'expression __SQL__ des requêtes suivantes ainsi que le résultat obtenu :
<div class="list1_1" markdown="1">

1. Combien de séjours ont eu lieu à Victoria ? On stockera le résultat dans une colonne nommée *Total*.
2. Donner le prix moyen d'une activité à Tanger. On stockera le résultat dans une colonne nommée *Prix Moyen Activites Tanger*.
</div>

[Correction de l'exercice](Correction_des_exercices.md#correction-de-lexercice-2){:target="_blank"}

### <div class = "encadré17" markdown="1"> __Exercice 3__ </div>
<div class="list1_1" markdown="1">

1. Donner l'expression __SQL__ de la requête permettant d'afficher la liste des stations suivie du lieu (en majuscule) entre parenthèses <div class="decal2" markdown="1">et du tarif HT et TTC comme le montre l'exemple suivant :</div>

<center>

| Stations	        	| Tarif HT	    |Tarif TTC 	    |
| :---------------: 	| :-----------: |:-----------:	|	
|Tanger (MAROC)			|	1200		|	1440		|
|La Bourboule (AUVERGNE)|	700			|	840			|
|Courchevel (ALPES)		|	2200		|	2640		|
|Victoria (SEYCHELLES)	|	1500		|	1800		|

</center>
<div class="decal4" markdown="1"> On supposera que le prix saisi dans la base est le tarif HT et que le taux de TVA est de 20 %.</div>
</div>
<div class="list1_2" markdown="1">

2. Les données qui correspondent au tarif TTC des stations sont-elles stockées dans la base de données ?
</div>

[Correction de l'exercice](Correction_des_exercices.md#correction-de-lexercice-3){:target="_blank"}

### <div class = "encadré17" markdown="1"> __Exercice 4__ </div>
<div class="list1_1" markdown="1">

1. Donner l'expression __SQL__ des requêtes permettant d'ajouter la cliente venant de Toronto (Canada) suivante : Mme Karibou <div class="decal2" markdown="1">Juliette avec un solde de 7213 €. Cette cliente a séjourné (3 places) à La Bourboule le 10/07/2020.</div>
2. Peut-on, dans l'état, ajouter à cette base que Mme Karibou a fait de la randonnée ?
</div>

[Correction de l'exercice](Correction_des_exercices.md#correction-de-lexercice-4){:target="_blank"}

### <div class = "encadré17" markdown="1"> __Exercice 5__ </div>
<div class="list1_1" markdown="1">

1. Donner l'expression __SQL__ de la requête permettant de mettre à jour la capacité de la station Courchevel à 450 places ainsi que <div class="decal2" markdown="1">le nouveau tarif de 2300 €.</div>
2. Peut-on changer ici le nom de l'attribut *Prix* en *Prix HT* de la relation « Activites » par une requête de type __UPDATE__ ?
</div>

[Correction de l'exercice](Correction_des_exercices.md#correction-de-lexercice-5){:target="_blank"}

### <div class = "encadré17" markdown="1"> __Exercice 6__ </div>
<div class="list1_1" markdown="1">

1. Donner l'expression __SQL__ de la requête permettant de supprimer tout ce qui concerne Mme Karibou (données insérées dans le <div class="decal2" markdown="1">cadre de l'exercice 4).  
On supposera que la structure est bien correcte, à savoir que l'attribut *IdClient* de la relation « Sejours » est bien une clé étrangère liée en référence à l'attribut *Id* de la relation « Clients ».</div>
2. Que faire si la clé étrangère n'a pas été définie dans la relation « Sejours » ?
</div>

[Correction de l'exercice](Correction_des_exercices.md#correction-de-lexercice-6){:target="_blank"}
