# <center><div class = "titre2">Rotation d'un quart de tour d'une image</div></center>

L'objectif de ce problème est d'implémenter des algorithmes permettant de faire tourner une image d'un quart de tour dans le sens des aiguilles d'une montre.
<span style="display:block; margin: 8px 0px 0px 0px;">Une image est un tableau (bidimensionnel) composé de pixels. Un pixel est, dans le cadre du codage <span style="font-family: 'Trebuchet MS';font-weight: bold">RGB</span>, un triplet d'entiers compris entre `#!python 0` et `#!python 255` correspondant aux intensités lumineuses respectives du rouge (*red*), du vert (*green*) et du bleu (*blue*).</span>
<span style="display:block; margin: 8px 0px 0px 0px;">Par exemple, un pixel de valeur `#!python (0, 0, 0)` est noir ; un pixel de valeur `#!python (255, 255, 255)` est blanc ; un pixel de valeur `#!python (0, 255, 0)` est vert et un pixel de valeur `#!python (255, 255, 0)` est jaune.</span>
<span style="display:block; margin: 8px 0px 0px 0px;">Danc cet exercice, on exploitera une image carrée comportant 2<sup>*n*</sup> lignes et colonnes.</span>
<span style="display:block; margin: 8px 0px 0px 0px;">Nous utilisons le module <span style="font-family: 'Trebuchet MS';font-weight: bold">PIL</span> qui permet de gérer aisément les images.</span>
<span style="display:block; margin: 5px 0px 0px 0px;">
La partie qui nous intéresse de ce module peut être importée à l'aide de :</span>
<span style="display:block; margin: 5px 0px 0px 0px;">
`#!python from PIL import Image`</span>
<span style="display:block; margin: 5px 0px 0px 0px;">
On ouvre alors l'image à l'aide de :</span>
<span style="display:block; margin: 5px 0px 0px 0px;">
`#!python img = Image.open("nom_du_fichier")`</span>
<span style="display:block; margin: 5px 0px 0px 0px;">
Les dimensions de l'image peuvent être récupérées à l'aide de :</span>
<span style="display:block; margin: 5px 0px 0px 0px;">
`#!python largeur, hauteur = img.size`</span>
<span style="display:block; margin: 5px 0px 0px 0px;">
La valeur du pixel d'abscisse `#!python x` et d'ordonnée `#!python y` peut être récupérée à l'aide de :</span>
<span style="display:block; margin: 5px 0px 0px 0px;">
`#!python img.getpixel((x, y))`</span>
<span style="display:block; margin: 5px 0px 0px 0px;">
On rappelle que la première coordonnée correspond à l'abscisse dans l'image et la seconde à l'ordonnée, l'origine du repère étant en haut à gauche de l'image, les axes allant vers la droite et vers le bas.</span>
<span style="display:block; margin: 5px 0px 0px 0px;">
On peut affecter le triplet `#!python (r, g, b)` au pixel de coordonnées `#!python (x, y)` à l'aide de :</span>
<span style="display:block; margin: 5px 0px 0px 0px;">
`#!python img.putpixel((x, y), (r, g, b))`</span>
<span style="display:block; margin: 5px 0px 0px 0px;">
L'image peut être sauvegardée à l'aide de :</span>
<span style="display:block; margin: 5px 0px 0px 0px;">
`#!python img.save("nom_du_fichier")`</span>
<span style="display:block; margin: 5px 0px 0px 0px;">
Elle peut être affichée à l'aide de :</span>
<span style="display:block; margin: 5px 0px 0px 0px;">
`#!python img.show()`</span>
<span style="display:block; margin: 5px 0px 0px 0px;">
Enfin, une nouvelle image (noire par défaut, elle sera modifiée par la suite) peut être créée à l'aide de :</span>
<span style="display:block; margin: 5px 0px 0px 0px;">
`#!python im = Image.new("RGB", (largeur, hauteur))`</span>

## <div class = "partie"><span style="color : #f36379;">Partie A</span> : Algorithme simple de rotation d'un quart de tour</div>
<div class="list1_1" markdown="1">

1. Enregistrer l'image [<span style="font-family: 'Trebuchet MS' ; font-weight: bold">horloge.png</span>](images/horloge.png) dans votre environnement de travail.
2. Créer une nouvelle image, `#!python img_rot`, de même format, destinée à stocker l'image obtenue par rotation.
3. Pour une image `#!python img` carrée de taille *n* × *n*, l'image `#!python img_rot` obtenue par rotation d'un quart de tour dans le sens des aiguilles d'une montre a pour pixel `#!python (x, y)` celui initialement en `#!python (y, n - 1 - x)` dans `#!python img`.
<span style="display:block; margin: 8px 0px 0px 0px;">
Ecrire une suite d'instructions qui stocke dans la nouvelle image celle obtenue par rotation de la précédente et qui affiche le résultat.</span> 
4. Quelle est la complexité temporelle de cet algorithme ? Et sa complexité spatiale ? (C'est-à-dire l'ordre de grandeur de la taille mémoire utilisée, en fonction de *n*.)

</div>

## <div class = "partie"><span style="color : #f36379;">Partie B</span> : Rotation d'une image en espace mémoire constant</div>
La suite de ce problème a pour objectif de réaliser un algorithme permettant d'effectuer une rotation d'un quart de tour d'une image sans utiliser d'espace mémoire supplémentaire. Cet algorithme, lent, n'est pas utilisé en pratique.
<div class="list1_1" markdown="1">

1. Ecrire une procédure `#!python echange_pix(image, x0, y0, x1, y1)` qui échange les pixels de coordonnées `#!python (x0, y0)` et `#!python (x1, y1)` de l'image passée en paramètre.
<span style="display:block; margin: 5px 0px 0px 0px;">
On adopte dans cet exercice une stratégie diviser pour régner. L'image est divisée en quatre quadrants. Chaque quadrants est tourné récursivement puis une permutation circulaire des quadrants est effectuée.
<span style="display:block; margin: 15px 0px 0px 0px;">
<center markdown="1">
    <img src="images/Quadrant.png" style="width: 80%; height: 80%;">
</center>
</span>
<span style="display:block; margin: 15px 0px 0px 0px;">La permutation circulaire est réalisée en enchaînant plusieurs échanges de quadrants.
<span style="display:block; margin: 5px 0px 15px 0px;">Le schéma suivant présente un exemple de stratégie permettant de le faire :</span>
<center markdown="1">
<img src="images/Permut.png" style="width: 80%; height: 80%;">
</center>
</span>
2. Ecrire une procédure `#!python echange_quadrant(image, x0, y0, x1, y1, n)` qui échange deux quadrants carrés de taille *n* dont le premier a pour coordonnées de départ `#!python (x0, y0)` et le second pour coordonnées de départ `#!python (x1, y1)`.
3. Ecrire une procédure récursive `#!python tourne_quadrants(image, x0, y0, n)` qui prend en argument l'image considérée, un couple de coordonnées de départ `#!python (x0, y0)`, une taille *n* ; qui applique récursivement des rotations à chaque quadrant, puis qui applique les permutations circulaires échangeant les quatre quadrants pour finaliser la rotation.
4. Ecrire une procédure effectuant la rotation de quart de tour de l'image. Enregistrer l'image et l'afficher.

</div>
<center markdown="1">
[Correction de l'exercice :material-cursor-default-click:](Correction_exo_rotation.md#Rotation-dun-quart-de-tour-dune-image-:-correction){:target="_blank" .md-button}
</center>
