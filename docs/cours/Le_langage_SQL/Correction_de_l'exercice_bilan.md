# <center><div class = "titre5"> Correction de l'exercice bilan </div>
</center>
<div class= "list2_1">

1. __Requêtes de base__</div>  

<div></div>  
<div class= "list3_a">

1. La liste des continents et de leurs superficies, triés par superficie croissante.
	```SQL
	SELECT * 
	FROM Continent 
	ORDER BY Area ASC
	```
2. La liste des capitales mondiales, triées par ordre alphabétique.
	```SQL
	SELECT Capital 
	FROM Country 
	ORDER BY Capital ASC
	```
3. Le nom, la ville et la date de fondation des quatre plus anciennes organisations mondiales.
	```SQL
	SELECT Name , City , Established 
	FROM Organization
	WHERE Established IS NOT NULL
	ORDER BY Established ASC
	LIMIT 4
	```
4. Le nom des volcans de plus de 6 000 mètres.
	```SQL
	SELECT Name, Height
	FROM Mountain 
	WHERE Type = 'volcano' AND Height > 6000
	ORDER BY Height DESC
	```
5. Les dix villes les plus peuplées au monde.
	```SQL
	SELECT Name, Population 
	FROM City
	WHERE Population IS NOT NULL
	ORDER BY Population DESC
	LIMIT 10
	```

</div>
<div class= "list2_2">

2. __Jointures__</div>

<div></div>  
<div class= "list3_a">

1. Le nom des pays membres des Nations Unies, triés par ordre alphabétique.
	```SQL
	SELECT c.Name 
	FROM (Country AS c 
	INNER JOIN isMember AS i ON c.Code = i.Country)
	WHERE i.organization = 'UN'
	ORDER BY c.name ASC
	```
2. Les monarchies constitutionnelles.
	```SQL
	SELECT c.Name 
	FROM (Country AS c 
	INNER JOIN Politics AS p ON c.Code = p.Country)
	WHERE p.Government = 'constitutional monarchy'
	```
3. Les fleuves de France (c’est-à-dire les rivières de France qui se jettent dans la mer).
	```SQL
	SELECT DISTINCT r.Name
	FROM ((River AS r 
	INNER JOIN Geo_River AS gr ON gr.River = r.Name)
	INNER JOIN Country AS c ON c.Code = gr.Country)
	WHERE r.Sea IS NOT NULL AND c.Name = 'France'
	```
4. Le nom des montagnes d’Alaska de plus de 5 000 mètres.
	```SQL
	SELECT m.Name , m.Height
	FROM Mountain AS m 
	INNER JOIN geo_Mountain AS gm ON gm.Mountain = m.Name
	WHERE m.Height > 5000 AND gm.Province = 'Alaska'
	```
5. Les trois plus hautes montagnes africaines.
	```SQL
	SELECT m.Name , m.Height 
	FROM (((Mountain AS m
	INNER JOIN geo_Mountain AS gm ON m.Name = gm.Mountain)
	INNER JOIN Country AS c ON gm.Country = c.Code)
	INNER JOIN encompasses AS e ON c.Code = e.Country)
	WHERE e.Continent = 'Africa'
	ORDER BY m.Height DESC
	LIMIT 3
	```

</div>
<div class= "list2_3">

3. __Fonctions d’agrégation__</div>

<div></div>  
<div class= "list3_a">

1. La longueur moyenne des fleuves qui se jettent dans la Mer Noire.
	```SQL
	SELECT AVG(Length) 
	FROM River 
	WHERE Sea = 'Black Sea'
	```
2. Le nombre de rivières françaises présentes dans la base de données.
	```SQL
	SELECT COUNT(DISTINCT gm.River) AS 'Nombre de rivières'
	FROM geo_River AS gm 
	INNER JOIN Country AS c ON gm.Country = c.Code
	WHERE c.Name = 'France'
	```
3. Le nombre total de pays traversés par chacun des fleuves se jetant dans la mer <div class="decal5">Méditerranée.</div>
	```SQL
	SELECT r.Name, COUNT(DISTINCT gr.Country) AS 'Nombre de pays'
	FROM River AS r 
	INNER JOIN geo_River AS gr ON r.Name = gr.River
	WHERE r.Sea = 'Mediterranean Sea'
	GROUP BY r.Name
	```
4. Les organisations regroupant plus de 100 pays, avec la population totale de ceux-ci.
	```SQL
	SELECT o.Name, SUM(c.Population)
	FROM ((Organization AS o  
	INNER JOIN isMember AS i ON i.Organization = o.Abbreviation)
	INNER JOIN Country AS c ON c.Code = i.Country)
	GROUP BY o.Name HAVING COUNT(o.Name) > 100
	```
5. La liste des pays des Amériques avec leur plus haute montagne.
	```SQL
	SELECT c.Name AS Pays, m.Name AS Nom, MAX(m.Height) AS 'Hauteur de la plus haute montagne'
	FROM (((geo_Mountain AS gm 
	INNER JOIN Mountain AS m ON gm.Mountain = m.Name)
	INNER JOIN Country AS c ON gm.Country = c.Code)
	INNER JOIN encompasses AS e ON c.Code = e.Country)
	WHERE e.Continent = 'America'
	GROUP BY c.Name
	```

</div>
