# <center><div class = "titre2"> Correction des exercices </div></center>

### <div class = "encadré_exo"> __Correction de l'exercice 1__ </div>
<div class="list1_1" markdown="1">

1. 
<span style="display: block; margin: 0 0 0 0;">
	```SQL
	SELECT NomStation
	FROM Stations
	WHERE Stations.Capacite > 200
	```
   La requête __SQL__ retourne le résultat suivant :  
</span>

<center markdown="1">

 | NomStation    |
 | :--------:	 |
 | Tanger    	 |
 | La Bourboule  |
 | Courchevel	 |

</center>
</div>
<div class="list1_2" markdown="1">

2. 
<span style="display: block; margin: 0 0 0 0;">
	```SQL
	SELECT Nom
	FROM Clients
	WHERE Nom LIKE 'J%' OR Solde >= 10000
	```
   La requête __SQL__ retourne le résultat suivant :  
</sapn>

<center markdown="1">

 | Nom           |
 | :--------:	 |
 | Smith    	 |
 | Jonhson		 |

</center>
</div>
<div class="list1_3" markdown="1">

3. 
<span style="display: block; margin: 0 0 0 0;">
	```SQL
	SELECT NomStation
	FROM Activites
	WHERE Libelle = 'Plongée'
	```
   La requête __SQL__ retourne le résultat suivant :  
</span>

<center markdown="1">

 | NomStation    |
 | :--------:	 |
 | Tanger    	 |
 | Victoria		 |

</center>
</div>
<div class="decal4" markdown="1">

!!! tip "A noter"
	Lorsque les valeurs sont de type chaîne de caractères, on les place entre les symboles « ' » pour pouvoir effectuer les comparaisons. 

</div>
<div class="list1_4" markdown="1">

4. 
<span style="display: block; margin: 0 0 0 0;">
	```SQL
	SELECT Nom
	FROM Clients
	INNER JOIN Sejours ON ((Clients.Id = Sejours.IdClient) AND (Sejours.Station = 'La Bourboule'))
	```
   La requête __SQL__ retourne le résultat suivant :  
</span>

<center markdown="1">

 | Nom 			 |
 | :--------:	 |
 | Jonhson    	 |
 | Smith		 |

</center>
</div>
<div class="decal4" markdown="1">

!!! tip "A noter"
	Il s'agit bien ici d'une jointure de 2 relations qui doit respecter 2 conditions. Pour simplifier l'écriture, on peut également utiliser des alias pour les noms des relations. Ce que donnerait par exemple la requête suivante :  
	```SQL
	SELECT Nom
	FROM Clients AS c
	INNER JOIN Sejours AS s ON ((c.Id = s.IdClient) AND (s.Station = 'La Bourboule'))
	```

</div>
<div class="list1_5" markdown="1">

5. Intuitivement, on a envie de faire la jointure suivante :
<span style="display: block; margin: 0 0 0 0;">
	```SQL
	SELECT Station
	FROM Sejours AS s
	INNER JOIN Clients AS c ON ((c.Id = s.IdClient) AND (c.Region = 'Europe'))
	```
   Le résultat de cette requête donne :
</span>

 <center markdown="1">

 | Station       |
 | :--------:	 |
 | Courchevel  	 |
 | Courchevel  	 |
 | La Bourboule	 |
 | Victoria		 |

</center> 
<span style="display: block; margin: 0 0 0 38px;">
On s'aperçoit qu'il y a des doublons, ce qui est logique puisque Courchevel a été visitée par M.Bauer mais aussi par M. Smith.</span>
<span style="display: block; margin: 0 0 0 38px;">Il nous faut donc éliminer ce doublon en utilisant le mot-clé __DISTINCT__, ce qui donne la requête suivante :

```SQL
SELECT DISTINCT Station
FROM Sejours AS s
INNER JOIN Clients AS c ON ((c.Id = s.IdClient) AND (c.Region = 'Europe'))
```
</span>
</div>

### <div class = "encadré_exo"> __Correction de l'exercice 2__ </div>
<div class="list1_1" markdown="1">

1. Cela revient à compter toutes les lignes où `Station = 'Victoria'`.
<span style="display: block; margin: 0 0 0 0px;">
	```SQL
	SELECT COUNT(*) AS Total
	FROM Sejours 
	WHERE Station = 'Victoria'
	```
   Le résultat obtenu est :
</span>

<center markdown="1">

 | Total         |
 | :--------:	 |
 | 2		  	 |

</center>
</div>
<div class="list1_2" markdown="1">

2. 
<span style="display: block; margin: 0 0 0 0px;">
	```SQL
	SELECT AVG(Prix) AS 'Prix Moyen Activites Tanger'
	FROM Activites
	WHERE Activites.NomStation = 'Tanger'
	```
   Le résultat obtenu est :  
</span>

<center markdown="1">

 | Prix Moyen Activites Tanger  |
 | :--------:					|
 | 90						  	|

</center>
</div>

### <div class = "encadré_exo"> __Correction de l'exercice 3__ </div>
<div class="list1_1" markdown="1">

1. 
<span style="display: block; margin: 0 0 0 0px;">
	```SQL
	SELECT NomStation || ' (' || UPPER(Lieu) || ')' AS Stations, Tarif AS 'Tarif HT', Tarif * 1.2 AS 'Tarif TTC'
	FROM Stations
	```
</span>

</div>
<div class="list1_2" markdown="1">

2. Les données calculées à partir de données présentes dans une requête __SELECT__ ne sont pas stockées dans la base de données.
</div>
<div class="decal4" markdown="1">

!!! tip "A noter"
	Pour pouvoir stocker ces valeurs, il faudrait au préalable modifier la structure de la base de données comme par exemple ajouter un attribut dans la relation « Stations ».  
</div>

### <div class = "encadré_exo"> __Correction de l'exercice 4__ </div>
<div class="list1_1" markdown="1">

1.  La mise à jour de la base de données se décompose en l'ajout d'une occurrence dans la relation « Clients » et d'une occurrence dans la relation « Sejours ».
<span style="display: block; margin: 0 0 0 0px;">
```SQL
INSERT INTO Clients VALUES (4, 'Karibou', 'Juliette', 'Toronto', 'Amérique', 7213),
INSERT INTO Sejours VALUES (4, 'La Bourboule', '10/07/2020', 3)
```
</span>

</div>
<div class="list1_2" markdown="1">

2. En l'état, il n'y a aucune relation (association) entre la relation « Sejours » et la relation « Activites ». On ne peut donc pas dire que Mme Karibou a fait de la randonnée.

</div>
<div class="decal4" markdown="1">

!!! tip "A noter"
	Il faudrait au préalable modifier la structure de la base de données comme par exemple ajouter une clé primaire *IdActivite* dans la relation « Activites » et la clé étrangère associée dans la relation « Sejours ».  
</div>

### <div class = "encadré_exo"> __Correction de l'exercice 5__ </div>
<div class="list1_1" markdown="1">

1. 
<span style="display: block; margin: 0 0 0 0px;">
	```SQL
	UPDATE Stations SET Capacite = 450, Tarif = 2300
	WHERE NomStation = 'Courchevel'
	```
</span>

</div>
<div class="list1_2" markdown="1">

2. Avec une requête de type __UPDATE__, on ne peut mettre à jour que des valeurs. On se trouve ici dans la partie __LMD__ du langage __SQL__.

</div>
<div class="decal4" markdown="1">

!!! tip "A noter"
	Si l'on souhaite changer le nom d'un attribut, il faut modifier la structure de la base de données au niveau __LDD__ du langage __SQL__ avec le mot clé __ALTER TABLE__ comme le montre la requête suivante :

	```SQL
	ALTER TABLE Activites RENAME COLUMN Prix TO 'Prix HT'
	```  

</div>

### <div class = "encadré_exo"> __Correction de l'exercice 6__ </div>
<div class="list1_1" markdown="1">

1. 
<span style="display: block; margin: 0 0 0 0;">
	```SQL
	DELETE FROM Clients
	WHERE Id = 4
	```
</span>

</div>
<div class="decal4" markdown="1">

!!! tip "A noter"
	Le critère du __WHERE__ est bien l'attribut *Id* car c'est lui qui est l'identifiant (clé primaire). En effectuant cette requête, toutes les relations référencées seront modifiées.

</div>
<div class="list1_2" markdown="1">

2. S'il n'y a aucune référence à d'autres relations, il faut en pratique supprimer toutes les occurrences concernées dans la relation « Sejours » avec la requête suivante :
</div>
<div class="decal4" markdown="1">

```SQL
DELETE FROM Sejours
WHERE IdClient = 4
```
</div>
<div class="decal4" markdown="1">

!!! tip "A noter"
	Afin d'éviter le plus possible les anomalies (lignes orphelines dans une relation), il est primordial d'avoir bien réfléchi à la structure de la base de données.  
	Il est aussi impératif de bien savoir le risque que l'on prend lorsqu'on supprime des données. Il est souvent recommandé de faire une sauvegarde avant toute suppression.  
</div>