# <center><div class = "titre5" markdown="1"> Correction de l'exercice bilan </div>
</center markdown="1">
<div class="list2_1" markdown="1">

1. 

</div>
<div class="list3_a" markdown="1">

1. On peut identifier 4 entités :

</div>
<div class="couleur_puce10" markdown="1">

- « Vendeur » et l'identifiant est « *Code_ven* »
- « Client » et l'identifiant est « *Code_cli* » 
- « Facture » et l'identifiant est « *Num_fact* »
- « Produit » et l'identifiant est « *Num_prod* »

</div>
<div class="list3_b" markdown="1">

2. Pour l'association « Etablir » :

</div>
<div class="decal6" markdown="1">
<center markdown="1">![Etablir](Images/Ex_bilan_5.1/Etablir.png)</center>

!!! tools "__Précisions__"
	<div class="couleur_puce6" markdown="1">

	* Un vendeur peut ne pas être associé à une facture ou bien il peut être associé à plusieurs factures, d'où la cardinalité coté « Vendeur » de $(0,N)$.
	 * Une facture ne peut être associée qu'à un seul vendeur.

	</div>
<br>
Pour l'association « Recevoir » :
<br>
<center markdown="1">![Recevoir](Images/Ex_bilan_5.1/Recevoir.png)</center>

!!! tip "__Remarques__"
	<div class = "couleur_puce4" markdown="1">

	* Un client peut ne pas être associé à une facture ou bien il peut être associé à plusieurs factures, d'où la cardinalité coté « Client » de $(0,N)$.
	* Une facture ne peut être associée qu'à un seul client.

	</div>
<br>
Et enfin, pour l'association « Ajouter » :
<br>
<center markdown="1">![Recevoir](Images/Ex_bilan_5.1/Ajouter.png)</center>

!!! tip "__Remarques__"
	<div class = "couleur_puce4" markdown="1">

	* Un produit peut ne pas être associé à une facture ou bien il peut être associé à plusieurs factures, d'où la cardinalité coté « Produit » de $(0,N)$.
	* Une facture peut être associée au minimum à un produit mais aussi à plusieurs.

	</div>
</div>
<div class="list2_2" markdown="1">

1. <center markdown="1">![MCD](Images/Ex_bilan_5.1/MCD.png)</center>  
2. <center markdown="1">![MLD](Images/Ex_bilan_5.1/MLD.png)</center>
</div>