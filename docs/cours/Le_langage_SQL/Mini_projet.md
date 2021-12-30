# <center><div class = "titre6"> Mini-projet </div></center>

Dans cette partie sont présentés les « cahiers des charges » de mini-projets proposés pour créer un Système d’Informations basé sur le modèle relationnel.

L’objectif est de choisir un projet différent par groupe de 2 ou 3 élèves dans la liste proposée ci-dessous et de modéliser, à partir de ce cahier des charges, un Système d’Informations.

__Le travail demandé consiste à établir trois versions du Système d’Informations :__
<div class= "list4_1">

1. Identification des informations et créations d’exemples (éléments) dans une seule table (ensemble).
2. Structuration de la base de données en s’appuyant sur la modélisation Entité-Association (E/A).
3. Interrogation (requêtes SQL) sur la base afin de vérifier la cohérence du modèle proposé.

</div>
__La première version__ permettra de relever l’ensemble des informations nécessaires et les associations entre ces informations. A partir de cette étude, une première base de données sera créée. Cette base sera constituée d'une seule table contenant toutes les informations relevées dans le cahier des charges. On alimentera cette base avec un nombre limité d’enregistrements (environ 20 éléments).

__La deuxième version__ consistera à structurer la base en proposant un modèle de données constitué de plusieurs entités et associations. Une fois ce modèle de données établi, on répartira l’ensemble des informations de la première version dans les tables identifiées. Le nombre de tables sera limité (5 tables). On vérifiera à partir de ces instances de relations que la jointure sur l’ensemble des tables permet de retrouver l’ensemble des informations de la base de données qui étaient renseignées dans la première version.

__La version finale__ consistera à mettre en place des requêtes SQL pour récupérer les informations :
<div class= "list4_1">

1. Sur une seule table avec projections (sélections simples) et critères de restriction (utilisation du `WHERE`).
2. Sur plusieurs tables par jointure et critères de restriction.
3. En appliquant des fonctions d’agrégats (`COUNT()`,`SUM()`,`MAX()`,`MIN()`,`AVG()`...).
4. En faisant des groupements (`GROUP BY`).
5. Puis des groupements avec critères de restrictions (`GROUP BY ... HAVING`).

</div>

On proposera __3 requêtes__ pour chacun de ces types de requêtes.

??? hand-right1 "__Banques__ </span>"
	Un organisme d’agences bancaires veut mettre en place un système d’informations pour gérer les agences et les comptes de leurs clients ainsi que les opérations qu’ils effectuent sur ces comptes.
	<br><br>
	Chaque agence bancaire a un nom, un numéro d’agence, le nom de la ville où elle se trouve, un numéro de téléphone et une adresse URL. Une personne peut ouvrir un ou plusieurs comptes dans une agence bancaire. Elle doit donner son nom, son adresse, et éventuellement son numéro de téléphone.
	<br><br>
	Chaque compte a une seule date d’ouverture, un numéro d’identification de compte et un type (compte de chèques, compte épargne, etc.). Un compte a un seul titulaire. A l’ouverture du compte le solde est nul.
	<br><br>
	Une opération est effectuée par une seule personne (le titulaire du compte) et concerne au plus deux comptes : le compte émetteur et, éventuellement, le compte recevant l’opération. Une opération a un numéro d’identification, une date, une heure, un lieu, un type qui indique la nature de l’opération : retrait par carte bancaire, versement de salaire, encaissement ou paiement de chèque, virement de compte en compte, etc.

??? hand-right2 "__Bibliothèque__"
	Un département cherche à fédérer les bibliothèques municipales installées sur son territoire. Un habitant d’une commune ne peut être inscrit que dans la bibliothèque de sa commune.
	<br><br>
	Pour emprunter des livres il doit être à jour de sa cotisation annuelle. Il peut emprunter directement au plus 5 livres dans sa bibliothèque et faire au plus un prêt inter-bibliothèque.
	<br><br>
	Chaque bibliothèque possède un ensemble de livres. Un livre est défini par son titre, sa cote, son (ses) auteur(s), ainsi qu’un des mots-clés pris parmi un ensemble fixé a priori. Parmi ces mots-clés on trouve les genres littéraires (roman, essai, policier, science-fiction, vie pratique, …). Un livre peut-être en rayon, en réserve, en entretien ou emprunté. Dans ce dernier cas il ne peut-être emprunté que par une seule personne.

??? hand-right3 "__Cinéma__"
	Une compagnie de salles de cinémas souhaitent mettre en place un système d’informations sur les salles qu’elle doit gérer.
	<br><br>
	Dans cette base de données pour chaque salle de cinéma on connaît son nom, sa capacité et la ville où elle se trouve.
	<br><br>
	Pour chaque salle on doit pouvoir connaître la date et l’heure des films qui sont à l’affiche. Un film peut être projeté dans plusieurs salles et chaque salle peut programmer plusieurs films.
	<br><br>
	Pour chaque film on connaît le titre, un résumé, la date de création, la durée et on doit pouvoir trouver la liste des acteurs qui y ont un rôle ainsi que les informations sur le réalisateur.
	<br><br>
	Des acteurs, on connaît leur nom, prénom, âge et leur nationalité. Des réalisateurs, on a les mêmes informations et le nombre de films qu’ils ont réalisés.

??? hand-right4 "__Colloques__"
	Pour organiser un ensemble de cycle de conférences on souhaite disposer d’un système d’informations.
	<br><br>
	Dans cette base de données, les conférences se déroulent dans des universités et sont constituées d’un ensemble d’exposés. Chaque exposé est présenté par un conférencier.
	<br><br>
	Une conférence est caractérisée par son nom, les dates de début et de fin.
	<br><br>
	Une université est identifiée par son nom, le nombre d’étudiants inscrits et la ville où elle se trouve.
	<br><br>
	Un exposé est constitué d’un titre, d’un résumé et sera présenté par un seul conférencier qui peut faire plusieurs exposés dans différentes conférences. Le conférencier est caractérisé par ses nom, prénom, âge, son domaine de spécialité, son adresse mail et l’université d’où il provient.

??? hand-right5 "__Festivals__"
	Une société responsable d’un certain nombre de festivals organisés sur le territoire national souhaite mettre en place un système d’informations pour mieux gérer l’organisation.
	<br><br>
	Pour chaque festival on connait le nom, la ville et la période (date de début et de fin) où il a lieu. On sait aussi qu’il a lieu sur plusieurs journées.
	<br><br>
	Pour chaque journée, on connait la date et la liste des concerts qui auront lieu ce jour-là.
	<br><br>
	Pour chaque concert, on connait le nom du groupe, l’heure prévue et la durée du concert.
	<br><br>
	Un concert est donné par un groupe dont on connait le nom et le style de musique.
	<br><br>
	Tous les groupes jouent lors du festival un certain nombre d’oeuvres musicales dont on connait le titre, le nom du compositeur, la date de création et la durée du morceau.

??? hand-right6 "__Hopital__"
	On souhaite mettre en place un système d’informations pour gérer les services hospitaliers sur le territoire national. Un hopital est composé de plusieurs services et laboratoires dans lesquels travaillent des médecins qui consultent des patients.
	<br><br>
	On connait le nom de l’hopital et la ville où il se trouve. On distingue chaque service et chaque laboratoire quel que soit son hopital d’appartenance. Ainsi deux maternités, deux laboratoires de cancérologie etc …, seront bien distincts mais seront rattachés à un seul hopital. Pour chaque service et laboratoire, on connait leur nom.
	<br><br>
	Un médecin ne peut exercer que dans un seul service et fait sa recherche dans un seul laboratoire. On connait le nom du médecin, la ville où il exerce et sa spécialité. Un service et un laboratoire sont, bien évidemment, constitués de plusieurs médecins. Un patient peut consulter plusieurs médecins d’un hôpital et un médecin peut recevoir plusieurs patients. Du patient on connait ses nom, prénom, date de naissance et ville où il habite.

??? hand-right7 "__Journalisme__"
	Un organisme de presse veut créer une base de données sur les journaux nationaux, leurs journalistes, les articles qu’ils écrivent sur différents sujets ainsi que les personnalités qu’ils interviewent. Le journaliste est connu par son nom, son prénom, son âge, la ville où il réside et sa signature (son pseudo). Un journaliste peut travailler pour plusieurs journaux comme un journal emploie évidemment plusieurs journalistes. On doit alors pouvoir connaître la date d’entrée du journaliste au quotidien pour lequel il rédige des articles. On connaît le nom du quotidien et son adresse URL.
	<br><br>
	Chaque journaliste peut interviewer différentes personnalités dont on connait le nom, prénom, pseudo, âge, nationalité et domaine d’activité. Une personnalité peut bien entendu être interviewée par plusieurs journalistes.
	<br><br>
	Les journalistes écrivent des articles dont on connait le titre et le contenu. Chaque article est relatif à un domaine qui peut être lié à une ou plusieurs personnalités.

??? hand-right8 "__Père Noël__"
	Le père Noel a décidé de mettre en oeuvre un système d’informations permettant de faciliter la collecte des souhaits des enfants ainsi que la distribution des jouets. Pour cela il faut recencer les magasins dans les différentes villes du territoire.
	<br><br>
	Les villes comme les magasins sont caractérisés par un nom. Les jouets peuvent être distribués par plusieurs magasins.
	<br><br>
	Les jouets portent un nom (par exemple « Sherlock Holmes »), appartiennent à une marque (« Parkeur ») et sont recommandés pour les enfants à partir d’un certain âge (8 ans). Un compte du nombre d’articles (par exemple le nombre de boites de « Sherlock Holmes ») est représenté pour chaque magasin. D’autre part chaque jouet peut être caractérisé par plusieurs étiquettes (tags). Par exemple « jeux de société », « jeux d’adresse », « jeux d’éveil ». Les tags sont organisés de façon hiérarchique : un jeux de société est un jouet d’intérieur, un vélo est un jeux d’extérieur.
	<br><br>
	L’idée est de permettre à l’utilisateur de pouvoir faire des requêtes de plus en plus précises (commencer par « jouet d’intérieur » puis de choisir parmi les tags correspondant à des jouets d’intérieur). D’autres hiérarchies peuvent être envisagées … En particulier des hiérarchies avec plus de niveaux. D’autre part plusieurs hiérarchies peuvent être utilisées.
	<br><br>
	Chaque enfant est représenté par son nom, son prénom ainsi que son âge. Un enfant habite une ville et ne peut fréquenter que les magasins de sa ville. D’autre part il doit faire une liste de souhaits en fonction de ses préférences (en terme de tags) et de son âge.

??? hand-right9 "__Restaurants__"
	Une association de restaurateurs veut mettre en place un système d’informations pour avoir accès aux informations sur les restaurants de l’association.
	<br><br>
	Les restaurants proposent un ensemble de menus constitués de différents plats.
	<br><br>
	Chaque plat est connu par une recette dont on connait les ingrédients.
	<br><br>
	Le restaurant sera décrit par son nom, la ville où il se trouve, son nombre d’étoiles, le nombre de tables et le nombre de couverts (nombre de personnes pouvant y manger simultanément) Les restaurateurs estiment que chaque plat de leur restaurant est unique et proposé par un seul restaurant même s’il porte le même nom, dans un autre restaurant. La redondance dans les noms de plats n’est donc pas un problème.
	<br><br>
	Les restaurateurs se sont accordés sur une liste de catégories (hors d’oeuvre, entrée, plat principal, dessert, …). Pour chacun de leur plat, ils indiqueront la catégorie dans laquelle ils souhaitent le ranger. Chaque plat sera classé dans une seule catégorie.
	<br><br>
	Un menu est constitué de plusieurs plats dans différentes catégories (entrée, plat principal, dessert …). On connaît le nom et le prix de chaque menu.
	<br><br>
	Chaque plat a un nom, un prix et on peut trouver la recette qui est constituée d’un liste d’ingrédients dont on connaît le poids dans la recette. Pour chaque ingrédient on connaît le nom, le pays et la région de production.

??? hand-right10 "__Tourisme__"
	Un organisme de tourisme veut proposer à ses clients un système de réservations de circuits touristiques constitué d’itinéraires entre deux villes.
	<br><br>
	Les clients sont connus par leur nom, prénom, ville où ils résident et leur mot de passe pour accéder aux réservations.
	<br><br>
	Une réservation est faite par un client et concerne un circuit. Une réservation se fait pour un certain nombre de personnes et en deux phases (une demande et une validation).
	<br><br>
	Chaque circuit aura un nom, commencera et se terminera à une date précise pour un nombre de places limités. On doit connaitre le prix du circuit ainsi que le nombre de réservations faites.
	<br><br>
	Les circuits sont constitués de plusieurs étapes. Pour chaque étape on connaît le nom des villes et les heures de départ et d’arrivée. Une étape se fait entre deux villes dont on connaît le nom, le pays où elle se trouve ainsi que le nom de l’hôtel où seront logés les participants.
