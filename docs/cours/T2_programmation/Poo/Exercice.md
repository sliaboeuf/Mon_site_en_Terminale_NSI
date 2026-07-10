# <center><div class = "titre2">Exercice</div> </center>

Le domino est un jeu très ancien constitué de 28 pièces toutes différentes. Sur chacune de ces pièces, il y a deux côtés qui sont constitués de 0 (blanc) à 6 points noirs.  
Lorsque les 2 côtés possèdent le même nombre de points, on l'appelle domino double.

<center markdown="1">
![Domino](images/Dominos.png)
</center>
<div class="list1_1" markdown="1">

1. Proposer une classe __Domino__ permettant de représenter une pièce. Les objets seront initialisés avec les valeurs des deux côtés (gauche et droite).  
<span style="display: block; margin: 5px 0 0 0;">On définira les méthodes suivantes :</span>

</div>
<div class="couleur_puce14" markdown="1">

* `#!python afficher_domino(self)` qui affiche les valeurs des deux faces de manière horizontale pour un domino classique et de manière verticale pour un domino double comme le montre la figure suivante :

![Domino](images/Affichage_dominos_2.png){: .center width=40% .image}

* `#!python nb_points(self)` qui compte le nombre de points sur un domino.
* `#!python est_blanc(self)` qui teste si le domino est blanc (c'est-à-dire si au moins un des côtés est blanc).
* `#!python est_double(self)` qui teste si le domino est double. 

</div>
<div class="list1_2" markdown="1">

2. Proposer une classe __JeuDeDomino__ permettant de manipuler le jeu de domino complet.  
<span style="display: block; margin: 5px 0 0 0;">On définira les méthodes suivantes :</span>

</div>
<div class="couleur_puce14" markdown="1">

* `#!python creer_jeu(self)` qui crée un jeu de 28 pièces toutes différentes.
* `#!python melanger(self)` qui mélange aléatoirement le jeu de dominos.
* `#!python distribuer(self, nb_joueur)` qui extrait des dominos du jeu pour un joueur et retourne une liste de 6 ou 7 dominos selon le nombre de joueurs.
* `#!python afficher_jeu(self)` qui affiche toutes les pièces du jeu ou la pioche s'il y a eu distribution.
* `#!python afficher_jeu_joueur(self)` qui affiche les dominos qui viennent d'être distribués au joueur ainsi que le nombre de points dans son jeu.

</div>


