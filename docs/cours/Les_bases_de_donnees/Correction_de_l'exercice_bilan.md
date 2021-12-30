# <center><div class = "titre5"> Correction de l'exercice bilan </div>
</center>
<div class="list2_1">

1. 

</div>
<div class="list3_a">

1. On peut identifier 4 entités :

</div>
<div class="couleur_puce10">

- « Vendeur » et l'identifiant est « *Code_ven* »
- « Client » et l'identifiant est « *Code_cli* » 
- « Facture » et l'identifiant est « *Num_fact* »
- « Produit » et l'identifiant est « *Num_prod* »

</div>
<div class="list3_b">

2. Pour l'association « Etablir » :

</div>
<div class="decal6">
<center>![Etablir](Images/Ex_bilan_5.1/Etablir.png)</center>
<div class="couleur_puce6">

!!! tools "__Précisions__"
	* Un vendeur peut ne pas être associé à une facture ou bien il peut être associé à plusieurs factures, d'où la cardinalité coté « Vendeur » de $(0,N)$.
	 * Une facture ne peut être associée qu'à un seul vendeur.
</div>
<br>
Pour l'association « Recevoir » :
<br>
<center>![Recevoir](Images/Ex_bilan_5.1/Recevoir.png)</center>
<div class = "couleur_puce4">

!!! tip "__Remarques__"
	* Un client peut ne pas être associé à une facture ou bien il peut être associé à plusieurs factures, d'où la cardinalité coté « Client » de $(0,N)$.
	* Une facture ne peut être associée qu'à un seul client.
</div>
<br>
Et enfin, pour l'association « Ajouter » :
<br>
<center>![Recevoir](Images/Ex_bilan_5.1/Ajouter.png)</center>
<div class = "couleur_puce4">

!!! tip "__Remarques__"
		* Un produit peut ne pas être associé à une facture ou bien il peut être associé à plusieurs factures, d'où la cardinalité coté « Produit » de $(0,N)$.
		* Une facture peut être associée au minimum à un produit mais aussi à plusieurs.

</div>
</div>
<div class="list2_2">

1. <center>![MCD](Images/Ex_bilan_5.1/MCD.png)</center>  
2. <center>![MLD](Images/Ex_bilan_5.1/MLD.png)</center>
</div>