# <center><div class = "titre5">Classification sur les Pokemon</div></center>

Les pokemons sont des animaux imaginaires inventés par Nintendo :simple-nintendo:{ .nintendo }.
<span style="display: block; margin: 10px 0 0 0;">Ils possèdent tous des caractéristiques différentes :</span>
<div class="couleur_puce22" markdown="1">

- Un nom (`#!python name`)
- Un nombre de points d'attaque (`#!python attack`)
- Un nombre de pas pour le faire éclore (`#!python base_egg_steps`)
- Un type principal (`#!python type1`)
- Un éventuel type secondaire (`#!python type2`)
- Un nombre de points de vie (`#!python hp`)
- Un nombre de points de défense (`#!python defense`)
- Un nombre de points d'attaque spéciale (`#!python sp_attack`)
- Un nombre de points de défense spéciale (`#!python sp_defense`)
- Un nombre caractérisant sa vitesse (`#!python speed`)
- Un entier indiquant la génération du pokemon (`#!python generation`)
- Un booléen indiquant si le pokemon est légendaire ou non (`#!python is_legendary`)

</div>
Ces données proviennent du jeu Pokemon Go. Les pokemons sont consignés dans des fichiers `csv`.
Ces fichiers contiennent les données sous forme de tables :

??? table "Extrait d'une table"

	| name       | attack | base_egg_steps | base_happiness | capture_rate | classification      | defense | experience_growth | height_m | hp | pokedex_number | sp_attack | sp_defense | speed | type1    | type2  | weight_kg | generation | is_legendary |
	|:--------------:|:----------:|:------------------:|:------------------:|:----------------:|:----------------------:|:-----------:|:---------------------:|:------------:|:------:|:------------------:|:-------------:|:--------------:|:---------:|:------------:|:----------:|:-------------:|:--------------:|:----------------:|
	| Magmar     | `#!python 95`       | `#!python 6400`             | `#!python 70`               | `#!python 45`             | Spitfire Pokémon   | `#!python 57`        | `#!python 1000000`             | `#!python 1.3`      | `#!python 65`   | `#!python 126`              | `#!python 100`         | `#!python 85`           | `#!python 93`      | fire     |          | `#!python 44.5`      | `#!python 1`           | `#!python 0`              |
	| Pinsir     | `#!python 155`      | `#!python 6400`             | `#!python 70`               | `#!python 45`             | Stagbeetle Pokémon | `#!python 120`       | `#!python 1250000`             | `#!python 1.5`      | `#!python 65`   | `#!python 127`              | `#!python 65`          | `#!python 90`           | `#!python 105`     | bug      |          | `#!python 55.0`      | `#!python 1`            | `#!python 0`              |
	| Tauros     | `#!python 100`      | `#!python 5120`             | `#!python 70`               | `#!python 45`             | Wild Bull Pokémon  | `#!python 95`        | `#!python 1250000`             | `#!python 1.4`      | `#!python 75`   | `#!python 128`              | `#!python 40`          | `#!python 70`           | `#!python 110`     | normal   |          | `#!python 88.4`      | `#!python 1`            | `#!python 0`              |
	| Magikarp   | `#!python 10`       | `#!python 1280`             | `#!python 70`              | `#!python 255`            | Fish Pokémon       | `#!python 55`        | `#!python 1250000`             | `#!python 0.9`      | `#!python 20`   | `#!python 129`              | `#!python 15`          | `#!python 20`           | `#!python 80`      | water    |          | `#!python 10.0`      | `#!python 1`            | `#!python 0`              |
	| Gyarados   | `#!python 155`      | `#!python 1280`             | `#!python 70`               | `#!python 45`             | Atrocious Pokémon  |`#!python  109`       | `#!python 1250000`             | `#!python 6.5`      | `#!python 95`   | `#!python 130`              | `#!python 70`          | `#!python 130`          | `#!python 81`      | water    | flying | `#!python 235.0`     | `#!python 1`            | `#!python 0`              |
	| Lapras     | `#!python 85`       | `#!python 10240`            | `#!python 70`               | `#!python 45`             | Transport Pokémon  | `#!python 80`        | `#!python 1250000`             | `#!python 2.5`      | `#!python 130`  | `#!python 131`              | `#!python 85`          | `#!python 95`           | `#!python 60`      | water    | ice    | `#!python 220.0`     | `#!python 1`            | `#!python 0`             |
	| Ditto      | `#!python 48`       | `#!python 5120`             | `#!python 70`               | `#!python 35`             | Transform Pokémon  | `#!python 48`        | `#!python 1000000`             | `#!python 0.3`      | `#!python 48`   | `#!python 132`              | `#!python 48`          | `#!python 48`           | `#!python 48`      | normal   |          | `#!python 4.0`       | `#!python 1`            | `#!python 0`              |
	| Eevee      | `#!python 55`       | `#!python 8960`             | `#!python 70`               | `#!python 45`             | Evolution Pokémon  | `#!python 50`        | `#!python 1000000`             | `#!python 0.3`      | `#!python 55`   | `#!python 133`              | `#!python 45`          | `#!python 65`           | `#!python 55`      | normal   |          | `#!python 6.5`       | `#!python 1`            | `#!python 0`              |
	| Vaporeon   | `#!python 65`       | `#!python 8960`             | `#!python 70`               | `#!python 45`             | Bubble Jet Pokémon | `#!python 60`        | `#!python 1000000`             | `#!python 1.0`      | `#!python 130`  | `#!python 134`              | `#!python 110`         | `#!python 95`           | `#!python 65`      | water    |          | `#!python 29.0`      | `#!python 1`            | `#!python 0`              |
	| Jolteon    | `#!python 65`       | `#!python 8960`             | `#!python 70`               | `#!python 45`             | Lightning Pokémon  | `#!python 60`        | `#!python 1000000`             | `#!python 0.8`     | `#!python 65`   | `#!python 135`              | `#!python 110`         | `#!python 95`           | `#!python 130`     | electric |          | `#!python 24.5`      | `#!python 1`            | `#!python 0`              |
	| Flareon    | `#!python 130`      | `#!python 8960`             | `#!python 70`               | `#!python 45`             | Flame Pokémon      | `#!python 60`        | `#!python 1000000`             | `#!python 0.9`      | `#!python 65`   | `#!python 136`              | `#!python 95`          | `#!python 110`          | `#!python 65`      | fire     |          | `#!python 25.0`      | `#!python 1`            | `#!python 0`              |
	| Porygon    | `#!python 60`       | `#!python 5120`             | `#!python 70`               | `#!python 45`             | Virtual Pokémon    | `#!python 70`        | `#!python 1000000`             | `#!python 0.8`      | `#!python 65`   | `#!python 137`              | `#!python 85`          | `#!python 75`           | `#!python 40`      | normal   |          | `#!python 36.5`      | `#!python 1`            | `#!python 0`              |
	| Omanyte    | `#!python 40`       | `#!python 7680`             | `#!python 70`               | `#!python 45`             | Spiral Pokémon     | `#!python 100`       | `#!python 1000000`             | `#!python 0.4`      | `#!python 35`   | `#!python 138`              | `#!python 90`          | `#!python 55`           | `#!python 35`      | rock     | water  | `#!python 7.5`       | `#!python 1`            | `#!python 0`              |
	| Omastar    | `#!python 60`       | `#!python 7680`             | `#!python 70`               | `#!python 45`             | Spiral Pokémon     | `#!python 125`       | `#!python 1000000`             | `#!python 1.0`      | `#!python 70`   | `#!python 139`              | `#!python 115`         | `#!python 70`           | `#!python 55`      | rock     | water  | `#!python 35.0`      | `#!python 1`            | `#!python 0`              |
	| Kabuto     | `#!python 80`       | `#!python 7680`             | `#!python 70`               | `#!python 45`             | Shellfish Pokémon  | `#!python 90`        | `#!python 1000000`             | `#!python 0.5`      | `#!python 30`   | `#!python 140`              | `#!python 55`          | `#!python 45`           | `#!python 55`      | rock     | water  | `#!python 11.5`      | `#!python 1`            | `#!python 0`              |
	| Kabutops   | `#!python 115`      | `#!python 7680`             | `#!python 70`               | `#!python 45`             | Shellfish Pokémon  | `#!python 105`       | `#!python 1000000`             | `#!python 1.3`      | `#!python 60`   | `#!python 141`              | `#!python 65`          | `#!python 70`           | `#!python 80`      | rock     | water  | `#!python 40.5`      | `#!python 1`            | `#!python 0`              |
	| Aerodactyl | `#!python 135`      | `#!python 8960`             | `#!python 70`               | `#!python 45`             | Fossil Pokémon     | `#!python 85`        | `#!python 1250000`             | `#!python 1.8`      | `#!python 80`   | `#!python 142`              | `#!python 70`          | `#!python 95`           | `#!python 150`     | rock     | flying | `#!python 59.0`      | `#!python 1`            | `#!python 0`              |
	| Snorlax    | `#!python 110`      | `#!python 10240`            | `#!python 70`               | `#!python 25`             | Sleeping Pokémon   | `#!python 65`        | `#!python 1250000`             | `#!python 2.1`      | `#!python 160`  | `#!python 143`              | `#!python 65`          | `#!python 110`          | `#!python 30`      | normal   |          | `#!python 460.0`     | `#!python 1`            | `#!python 0`              |
	| Articuno   | `#!python 85`       | `#!python 20480`            | `#!python 35`               | `#!python 3`             | Freeze Pokémon     | `#!python 100`       | `#!python 1250000`             | `#!python 1.7`      | `#!python 90`   | `#!python 144`              | `#!python 95`          | `#!python 125`          | `#!python 85`      | ice      | flying | `#!python 55.4`      | `#!python 1`            | `#!python 1`              |
	| Zapdos     | `#!python 90`       | `#!python 20480`            | `#!python 35`               | `#!python 3`              | Electric Pokémon   | `#!python 85`        | `#!python 1250000`             | `#!python 1.6`      | `#!python 90`   | `#!python 145`              | `#!python 125`         | `#!python 90`           | `#!python 100`     | electric | flying | `#!python 52.6`      | `#!python 1`            | `#!python 1`              |


Dans ce TP, on cherche à répondre à cette question :
<span style="display: block; margin: 10px 0 0 0;">Étant données les caractéristiques d'un pokemon dont on ne sait s'il est légendaire ou non, peut-on prédire si ce pokemon est légendaire ou non ?</span>

## <div class = "encadré2_TP">__Matériel fourni__</div>

Tous les fichiers dont vous aurez besoin se trouvent ici : [pokemon.zip](documents/pokemon.zip)

### <div class = "encadré3_TP">__Fichiers csv__</div>

Cinq jeux de données sont fournis :
<div class="couleur_puce35" markdown="1">

- le fichier <span style="font-family: 'Trebuchet MS' ; font-weight: bold">pokemon_train.csv</span> contient les pokemons sur lesquels va se baser l'apprentissage ;
- le fichier <span style="font-family: 'Trebuchet MS' ; font-weight: bold">pokemon_test.csv</span> contient les pokemons grâce auxquels nous allons tester la qualité de l'apprentissage ;
- le fichier <span style="font-family: 'Trebuchet MS' ; font-weight: bold">pokemon_small.csv</span> contient les caractéristiques de 20 pokemons, utilisés pour les doctests ;
- le fichier <span style="font-family: 'Trebuchet MS' ; font-weight: bold">pokemon_suspect1.csv</span> contient les caractéristiques de certains pokemons ;
- le fichier <span style="font-family: 'Trebuchet MS' ; font-weight: bold">pokemon_suspect2.csv</span> contient les caractéristiques de certains pokemons.

</div>

### <div class = "encadré3_TP">__Le module <span style="font-family: 'Trebuchet MS' ; font-weight: bold">pokemon.py</span>__</div>

Le fichier <span style="font-family: 'Trebuchet MS' ; font-weight: bold">pokemon_squel.py</span> contient :
<div class="couleur_puce35" markdown="1">

- la définition du type  `#!python Pokemon` ;
- la fonction `#!python read_pokemon_csv` permettant de lire le fichier de données ;
- la fonction `#!python split_pokemons` permettant de séparer l'ensemble des données en deux sous-ensembles ;
- la fonction `#!python min_max_values` permettant de calculer les valeurs minimales et maximale d'un attribut numérique d'une liste de pokemons ;
- les fonctions `#!python pokemon_euclidian_distance` (à compléter) et `#!python pokemon_manhattan_distance` permettant de calculer la distance entre deux pokemons.
<span style="display: block; margin: 3px 0 0 0;">Pour des questions de normalisation, ces méthodes prennent également en paramètre un dictionnaire associant à chaque attribut numérique le couple `#!python (mini, maxi)` des valeurs minimales et maximale de l'attribut.</span>

</div>

### <div class = "encadré3_TP">__Le module <span style="font-family: 'Trebuchet MS' ; font-weight: bold">knn_pokemon</span>__</div>

Le fichier <span style="font-family: 'Trebuchet MS' ; font-weight: bold">knn_pokemon_squel.py</span> contient les en-têtes des fonctions nécessaires à l'implémentation de l'algorithme des $k$ plus proches voisins.

## <div class = "encadré2_TP">__Travail à réaliser__</div>

- [ ] Renommer le fichier <span style="font-family: 'Trebuchet MS' ; font-weight: bold">pokemon_squel.py</span> fourni en <span style="font-family: 'Trebuchet MS' ; font-weight: bold">pokemon.py</span>, puis compléter la fonction de distance `#!python pokemon_euclidian_distance`.
<span style="display: block; margin: 3px 0 0 0;">Les attributs utilisés pour calculer la distance sont fournis dans la variable `#!python POKE_PROP_USED_FOR_DISTANCE`.</span>

- [ ] Renommer le fichier <span style="font-family: 'Trebuchet MS' ; font-weight: bold">knn_pokemon_squel.py</span> fourni en <span style="font-family: 'Trebuchet MS' ; font-weight: bold">knn_pokemon.py</span>, puis compléter les fonctions :
<div class="decal1" markdown="1">
<div class="couleur_puce22" markdown="1">

- `#!python nearest_neighbors` : renvoie la liste des `#!python k` plus proches pokemons.
<span style="display: block; margin: 3px 0 0 0;">Vous pourrez par exemple construire la liste des couples `#!python (distance, voisin)`, puis la trier selon la première clé.</span>
- `#!python knn` : effectue la prédiction de l'attribut en déterminant l'attribut majoritaire dans le voisinage.

</div>
</div>

- [ ] Utiliser les fonctions précédentes pour compléter le tableau suivant :

<div class="decal12" markdown="1">

| Fichier                | Meilleur $k$ pour la <br> distance euclidienne   | Meilleur $k$ pour la <br> distance de Manhattan   |
|:------------------------:|:---------------------------------------------:|:----------------------------------------------:|
| `#!python pokemon_test.csv`     |                                             |                                              |
| `#!python pokemon_suspect1.csv` |                                             |                                              |
| `#!python pokemon_suspect2.csv` |                                             |                                              |

</div>

### <div class = "encadré3_TP">__Méthodologie__</div>

On charge les quatre jeux de données :

```python
train = read_pokemon_csv('pokemon_train.csv')
test = read_pokemon_csv('pokemon_test.csv')
suspect1 = read_pokemon_csv('pokemon_suspect1.csv')
suspect2 = read_pokemon_csv('pokemon_suspect2.csv')
```
<div class="couleur_puce35" markdown="1">

- Première ligne du tableau : utiliser la fonction `#!python knn_data` avec `#!python train` et `#!python test` pour estimer les meilleurs `#!python k` :
    ```python
    [knn_data(test, train, k , ...) for k in range(5, 20)]
    ```
- Deuxième ligne du tableau :

</div>
<div class="couleur_puce35etoi_decal" markdown="1">

- Utiliser la fonction `#!python knn_data` avec `#!python suspect1` et `#!python test`.
- Que constate-t-on ? Pourquoi ?

</div>
<div class="couleur_puce35" markdown="1">

- Troisième ligne du tableau :

</div>
<div class="couleur_puce35etoi_decal" markdown="1">

- Utiliser la fonction `#!python knn_data` avec `#!python suspect2` et `#!python test`.
- Que constate-t-on ? Pourquoi ?

</div>
<div class="decal1" markdown="1">

!!! remarque "__Remarque__"
    c'est moins flagrant ici, la méthode continue de bien classer les pokemons. Il faudrait modifier les attributs utilisés dans la fonction distance pour constater une dégradation)

</div>

## <div class = "encadré2_TP">__Pour aller plus loin__</div>

- [ ] Ajouter d'autres attributs dans le calcul de la distance. Constatez que cela peut dégrader le résultat.

- [ ] Déterminer les pokemons mal classés, découvrir pourquoi.

- [ ] Modifier la méthode de vote dans la fonction `#!python knn` pour que les voisins les plus proches aient davantage de poids.

- [ ] Modifier la fonction de distance en attribuant un poids à chaque attribut.

