# <center><div class = "titre4"> Exercice bilan </div></center>
Considérons la base de données __Mondial__. Il s’agit d’une __BDR__ qui compile un certain nombre de données géographiques et qui est gérée par l’université de Göttingen.
On retrouvera en annexe de ce document une description d’une partie du schéma relationnel de cette base de données disponible <a href="mondial_schema.db" >ici</a>.
<div class= "list2_1">

1. __Requêtes de base__</div>

<div class="decal4">Rédiger une requête <span class="gras">SQL</span> pour obtenir :</div>  
<div class= "list3_a">

1. La liste des continents et de leurs superficies, triés par superficie croissante.
2. La liste des capitales mondiales, triées par ordre alphabétique.
3. Le nom, la ville et la date de fondation des quatre plus anciennes organisations mondiales.
4. Le nom des volcans de plus de 6 000 mètres.
5. Les dix villes les plus peuplées au monde.

</div>
<div class= "list2_2">

2. __Jointures__</div>

<div class="decal4">Rédiger une requête <span class="gras">SQL</span> pour obtenir :</div>  
<div class= "list3_a">

1. Le nom des pays membres des Nations Unies, triés par ordre alphabétique.
2. Les monarchies constitutionnelles.
3. Les fleuves de France (c’est-à-dire les rivières de France qui se jettent dans la mer).
4. Le nom des montagnes d’Alaska de plus de 5 000 mètres.
5. Les trois plus hautes montagnes africaines.

</div>
<div class= "list2_3">

3. __Fonctions d’agrégation__</div>

<div class="decal4">Rédiger une requête <span class="gras">SQL</span> pour obtenir :</div>  
<div class= "list3_a">

1. La longueur moyenne des fleuves qui se jettent dans la Mer Noire.
2. Le nombre de rivières françaises présentes dans la base de données.
3. Le nombre total de pays traversés par chacun des fleuves se jetant dans la mer Méditerranée.
</div>
<div class="decal4">

!!! tip "__Remarques__"
	Lorsqu'on souhaite appliquer une fonction d'agrégation (une somme dans notre cas) sur plusieurs attributs (plusieurs fleuves ici) qu'on appelle alors __clé de groupe__, on utilise l'opérateur __GROUP BY__ suivi de la clé de groupe. Cette requète s'écrira alors :
	```SQL
	SELECT ... 
	FROM ... 
	GROUP BY ...
	```
	On peut même rajouter une condition supplémentaire sur la clé de groupe grâce à l'opérateur __HAVING__ (combiné à __GROUP BY__).  
	Dans notre exemple, on ne pourrait s'intéresser par exemple qu'aux fleuves d'une longueur supérieure à 500 km :
	```SQL
	SELECT ... 
	FROM ... 
	GROUP BY ...
	HAVING River.length > 500
	```

</div>
<div class= "list2_4">

4. Les organisations regroupant plus de 100 pays, avec la population totale de ceux-ci.
5. La liste des pays des Amériques avec leur plus haute montagne.

</div>

## <div class = 'taille1'>__Annexe : la base de données Mondial__</div>

Voici une partie du schéma relationnel de la base de données __Mondial__.  
Sont soulignés le ou les attributs constituant la clé primaire de chacune des tables.
<br>  
__Continent__ : <u>Name</u>, Area ;
<br>
<div class = "taille3">__Country__ : Name, <u>Code</u>, Capital, Province, Area, Population ;</div><div class = "taille2">(Province est la région de la capitale)</div>  
<br>
<div class = "taille4">__City__ : <u>Name</u>, <u>Country</u>, <u>Province</u>, Population, Longitude, Latitude ;</div><div class = "taille5">(Country est le code du pays)</div>
<br>  
__Encompasses__ : <u>Country</u>, <u>Continent</u>, Percentage ;
<br>  
<div class = "taille6">__Borders__ : <u>Country1</u>, <u>Country2</u>, Length ;</div><div class = "taille7">(Country1 < Country2 pour l’ordre lexicographique)</div>
<br>  
<div class = "taille8">__Organization__ : <u>Abbreviation</u>, Name, City, Country, Province, Established ;</div><div class = "taille9">(Established est la date de fondation)</div>
<br>  
__IsMember__ : <u>Country</u>, <u>Organization</u>, Type ;
<br>  
__Population__ : <u>Country</u>, Population_growth, infant_mortality ;
<br>  
<div class = "taille10">__Economy__ : <u>Country</u>, GDP, Agriculture, Service, Industry, Inflation ;</div><div class = "taille11">(GDP est le PIB)</div>
<br>  
<div class = "taille12">__Politics__ : <u>Country</u>, Independence, Dependent, Government ;</div><div class = "taille13">(Indépendance est une date, Dependent l’ex-pays colonisateur)</div>
<br>  
__Language__ : <u>Name</u>, <u>Country</u>, Percentage ;
<br>  
__EthnicGroup__ : <u>Name</u>, <u>Country</u>, Percentage ;
<br>  
__Religion__ : <u>Name</u>, <u>Country</u>, Percentage ;
<br>  
__Mountain__ : <u>Name</u>, Mountains, Elevation, Type, Longitude, Latitude ;
<br>  
__Geo_Mountain__ : <u>Mountain</u>, <u>Country</u>, <u>Province</u> ;
<br>  
__Sea__ : <u>Name</u>, Depth ;
<br>  
__Geo_Sea__ : <u>Sea</u>, Country</u>, <u>Province</u> ;
<br>  
__Lake__ : <u>Name</u>, Area, Depth, Elevation, Type, River, Longitude, Latitude ;
<br>  
__Geo_Lake__ : <u>Lake</u>, <u>Country</u>, <u>Province</u> ;
<br>  
<div class = "taille14">__River__ : <u>Name</u>, River, Lake, Sea, Length ;</div><div class = "taille15">(la rivière se jette dans une rivière, un lac ou la mer)</div>
<br>  
__Geo_River__ : <u>River</u>, <u>Country</u>, <u>Province</u>.