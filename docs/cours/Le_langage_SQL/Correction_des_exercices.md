# <center><div class = "titre3"> Correction des exercices </div></center>

### <div class = "encadré18"> __Correction de l'exercice 1__ </div>
<div class="list1_1">

1. 
<div class="decal2">

	```SQL
	SELECT NomStation
	FROM Stations
	WHERE Capacite > 200
	```
   La requête __SQL__ retourne le résultat suivant :  
</div>

<center>

 | NomStation    |
 | :--------:	 |
 | Tanger    	 |
 | La Bourboule  |
 | Courchevel	 |

</center>
</div>
<div class="list1_2">

2. 
<div class="decal2">

	```SQL
	SELECT Nom
	FROM Clients
	WHERE Nom LIKE 'J%' OR Solde >= 10000
	```
   La requête __SQL__ retourne le résultat suivant :  
</div>

<center>

 | Nom           |
 | :--------:	 |
 | Smith    	 |
 | Jonhson		 |

</center>
</div>
<div class="list1_3">

3. 
<div class="decal2">

	```SQL
	SELECT NomStation
	FROM Activites
	WHERE Libelle = 'Plongée'
	```
   La requête __SQL__ retourne le résultat suivant :  
</div>

<center>

 | NomStation    |
 | :--------:	 |
 | Tanger    	 |
 | Victoria		 |

</center>
</div>
<div class="decal3">

!!! tip "A noter"
	Lorsque les valeurs sont de type chaîne de caractères, on les place entre les symboles « ' » pour pouvoir effectuer les comparaisons. 

</div>
<div class="list1_4">

4. 
<div class="decal2">

	```SQL
	SELECT Nom
	FROM Clients
	INNER JOIN Sejours ON ((Clients.Id = Sejours.IdClient) AND (Sejours.Station = 'La Bourboule'))
	```
   La requête __SQL__ retourne le résultat suivant :  
</div>

<center>

 | Nom 			 |
 | :--------:	 |
 | Jonhson    	 |
 | Smith		 |

</center>
</div>
<div class="decal4">

!!! tip "A noter"
	Il s'agit bien ici d'une jointure de 2 relations qui doit respecter 2 conditions. Pour simplifier l'écriture, on peut également utiliser des alias pour les noms des relations. Ce que donnerait par exemple la requête suivante :  
	```SQL
	SELECT Nom
	FROM Clients AS c
	INNER JOIN Sejours AS s ON ((c.Id = s.IdClient) AND (s.Station = 'La Bourboule'))
	```

</div>
<div class="list1_5">

5. Intuitivement, on a envie de faire la jointure suivante :

<div class="decal4">

	```SQL
	SELECT Station
	FROM Sejours AS s
	INNER JOIN Clients AS c ON ((c.Id = s.IdClient) AND (c.Region = 'Europe'))
	```
   Le résultat de cette requête donne :
</div>

 <center>

 | Station       |
 | :--------:	 |
 | Courchevel  	 |
 | Courchevel  	 |
 | La Bourboule	 |
 | Victoria		 |

</center> 
<div class="decal4">

On s'aperçoit qu'il y a des doublons, ce qui est logique puisque Courchevel a été visitée par M.Bauer mais aussi par M. Smith.  
Il nous faut donc éliminer ce doublon en utilisant le mot-clé __DISTINCT__, ce qui donne la requête suivante :

```SQL
SELECT DISTINCT Station
FROM Sejours AS s
INNER JOIN Clients AS c ON ((c.Id = s.IdClient) AND (c.Region = 'Europe'))
```
</div>
</div>

### <div class = "encadré18"> __Correction de l'exercice 2__ </div>
<div class="list1_1">

1. Cela revient à compter toutes les lignes où `Station = 'Victoria'`.

<div class="decal4">

	```SQL
	SELECT COUNT(*) AS Total
	FROM Sejours 
	WHERE Station = 'Victoria'
	```
   Le résultat obtenu est :
</div>

<center>

 | Total         |
 | :--------:	 |
 | 2		  	 |

</center>
</div>
<div class="list1_2">

2. 
<div class="decal2">

	```SQL
	SELECT AVG(Prix) AS 'Prix Moyen Activites Tanger'
	FROM Activites
	WHERE Activites.NomStation = 'Tanger'
	```
   Le résultat obtenu est :  
</div>

<center>

 | Prix Moyen Activites Tanger  |
 | :--------:					|
 | 90						  	|

</center>
</div>

### <div class = "encadré18"> __Correction de l'exercice 3__ </div>
<div class="list1_1">

1. 
<div class="decal2">

	```SQL
	SELECT NomStation || ' (' || UPPER(Lieu) || ')' AS Stations, Tarif AS 'Tarif HT', Tarif * 1.2 AS 'Tarif TTC'
	FROM Stations
	```
</div>

</div>
<div class="list1_2">

2. Les données calculées à partir de données présentes dans une requête __SELECT__ ne sont pas stockées dans la base de <div class="decal2">données.</div>
</div>
<div class="decal4">

!!! tip "A noter"
	Pour pouvoir stocker ces valeurs, il faudrait au préalable modifier la structure de la base de données comme par exemple ajouter un attribut dans la relation « Stations ».  
</div>

### <div class = "encadré18"> __Correction de l'exercice 4__ </div>
<div class="list1_1">

1.  La mise à jour de la base de données se décompose en l'ajout d'une occurrence <div class="decal2">dans la relation « Clients » et d'une occurrence dans la relation « Sejours ».</div>

<div class="decal4">

```SQL
INSERT INTO Clients VALUES (4, 'Karibou', 'Juliette', 'Toronto', 'Amérique', 7213),
INSERT INTO Sejours VALUES (4, 'La Bourboule', '10/07/2020', 3)
```
</div>

</div>
<div class="list1_2">

2. En l'état, il n'y a aucune relation (association) entre la relation « Sejours » et la relation « Activites ». On ne peut donc pas dire <div class="decal2">que Mme Karibou a fait de la randonnée.</div>
</div>
<div class="decal4">

!!! tip "A noter"
	Il faudrait au préalable modifier la structure de la base de données comme par exemple ajouter une clé primaire *IdActivite* dans la relation « Activites » et la clé étrangère associée dans la relation « Sejours ».  
</div>

### <div class = "encadré18"> __Correction de l'exercice 5__ </div>
<div class="list1_1">

1. 
<div class="decal2">

	```SQL
	UPDATE Stations SET Capacite = 450, Tarif = 2300
	WHERE NomStation = 'Courchevel'
	```
</div>

</div>
<div class="list1_2">

2. Avec une requête de type __UPDATE__, on ne peut mettre à jour que des valeurs. On se trouve ici dans la partie __LMD__ du langage <div class="decal2">__SQL__.</div>
</div>
<div class="decal4">

!!! tip "A noter"
	Si l'on souhaite changer le nom d'un attribut, il faut modifier la structure de la base de données au niveau __LDD__ du langage __SQL__ avec le mot clé __ALTER TABLE__ comme le montre la requête suivante :

	```SQL
	ALTER TABLE Activites RENAME COLUMN Prix TO 'Prix HT'
	```  

</div>

### <div class = "encadré18"> __Correction de l'exercice 6__ </div>
<div class="list1_1">

1. 
<div class="decal2">

	```SQL
	DELETE FROM Clients
	WHERE Id = 4
	```
</div>

</div>
<div class="decal4">

!!! tip "A noter"
	Le critère du __WHERE__ est bien l'attribut *Id* car c'est lui qui est l'identifiant (clé primaire). En effectuant cette requête, toutes les relations référencées seront modifiées.

</div>
<div class="list1_2">

2. S'il n'y a aucune référence à d'autres relations, il faut en pratique supprimer toutes les occurrences concernées dans la relation <div class="decal2">« Sejours » avec la requête suivante :</div>
</div>
<div class="decal4">

```SQL
DELETE FROM Sejours
WHERE IdClient = 4
```
</div>
<div class="decal4">

!!! tip "A noter"
	Afin d'éviter le plus possible les anomalies (lignes orphelines dans une relation), il est primordial d'avoir bien réfléchi à la structure de la base de données.  
	Il est aussi impératif de bien savoir le risque que l'on prend lorsqu'on supprime des données. Il est souvent recommandé de faire une sauvegarde avant toute suppression.  
</div>