---
password: "corr_Diviser_rotation"
---

# <center><div class = "titre2"> Rotation d'un quart de tour d'une image : correction </div></center>

## <div class = "partie"><span style="color : #f36379;">Partie A</span></div>
<div class="list1_2" markdown="1">

2. On prend garde à la syntaxe, un tuple devant être passé à la fonction et non deux variables :
```python
img_rot = Image.new("RGB", (n, n))

```
3. Deux boucles imbriquées vont permettre la réalisation technique de cette opération. On prend garde aux indices : comme `#!python x` va de `#!python 0` à `#!python n - 1`, on accède à l'élément des ordonnées à l'aide de `#!python n - 1 - x` et non `#!python n - x`.
```python
for i in range(n):
    for j in range(n):
        img_rot.putpixel((i, j), im.getpixel((j, n - 1 - i)))
    
img_rot.show()

```
4. Les opérations `#!python img_rot.putpixel` et `#!python im.getpixel` ont des coûts unitaires. Elles sont répétées $~n^2~$ fois où $~n~$ est la hauteur (ou la largeur) de l'image : l'algorithme à donc une complexité __quadratique__.
<span style="display:block; margin: 5px 0px 10px 0px;">Par ailleurs, il nécessite la création d'une nouvelle image, occupant $~n^2~$ pixels. Comme la taille d'une pixel est fixe (à priori 3 octets dans le cadre du code <span style="font-family: 'Trebuchet MS';font-weight: bold">RGB</span>), la complexité spatiale de l'algorithme est donc également __quadratique__.
</span>

</div>

## <div class = "partie"><span style="color : #f36379;">Partie B</span></div>
<div class="list1_1" markdown="1">

1. Il suffit de récupérer les valeurs des pixels et de les mettre à leur nouvel emplacement :
```python
def echange_pix(image, x0, y0, x1, y1):
    a = im.getpixel((x0, y0))
    b = im.getpixel((x1, y1))
    im.putpixel((x0, y0), b)
    im.putpixel((x1, y1), a)
    
```

</div>
<div class="decal1" markdown="1">

!!! rocket "__Rappel__"
    Ce qui précède est une procédure et non une fonction, on l'utilise ainsi :

    ```python
    echange_pix(img, 0, 0, 120, 120) # a pour effet de modifier img
    
    ```
    et non ainsi :

    ```python
    img = echange_pix(img, 0, 0, 120, 120) # incorrect
    
    ```

</div>
<div class="list1_2" markdown="1">

2. On se sert de la procédure précédente dans deux boucles imbriquées. Là non plus, on ne renvoie pas de valeur.
```python
def echange_quadrant(image, x0, y0, x1, y1, n):
    for i in range(n):
        for j in range(n):
            echange_pix(image, x0 + i, y0 + j, x1 + i, y1 + j)
```
3. On applique l'algorithme, en faisant attention à ne le faire que si le quadrant que l'on cherche à tourner est au moins de taille $2 × 2$. A défaut, le quadrant est composé d'un unique pixel et il est inutile de faire quoi que ce soit. On fait également bien attention à utiliser une division entière, pour préserver le type des coordonnées.
```python
def tourne_quadrants(image, x0, y0, n):
    if n >= 2:
        m = n//2
        tourne_quadrants(image, x0, y0, m)
        tourne_quadrants(image, x0, y0 + m, m)
        tourne_quadrants(image, x0 + m, y0, m)
        tourne_quadrants(image, x0 + m, y0 + m, m)
        echange_quadrant(image, x0, y0, x0 + m, y0, m)
        echange_quadrant(image, x0, y0, x0 + m, y0 + m, m)
        echange_quadrant(image, x0, y0, x0, y0 + m, m)
```
4. Il suffit d'initialiser un appel à `#!python tourne_quadrants` et de lancer les instructions finales.
```python
def tourne_image(image):
    largeur, hauteur = image.size
    assert largeur == hauteur
    tourne_quadrants(image, 0, 0, largeur)

# Programme principal
im = Image.open("horloge.png")
tourne_image(im)
im.show()
im.save("quart_tour.png")
```

</div>
