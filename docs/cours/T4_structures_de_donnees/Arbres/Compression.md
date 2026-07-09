# <center><div class = "titre1">La compression des données</div></center>

## <div class = "encadré2">__Pourquoi compresser les données ?__</div>

![Illustration](images/Compression.png){: .image}

De nos jours, le volume gigantesque de données échangées sur internet, et stockées sur des serveurs ne serait possible sans la compression des données.  
<span style="display: block; margin: 10px 0 0 0;">En effet, une simple chanson pourrait prendre jusqu’à 150 Mo, ou 5 min de film 1Go, sans parler de l’ensemble des métadonnées, ...</span>
<span style="display: block; margin: 10px 0 0 0;">Outre le gain d'espace, la compression améliore la vitesse de transmission des données sur les réseaux. Elle permet donc de réduire les coûts matériels de stockage, mais aussi les coûts liés à la bande passante réseau.</span>
<span style="display: block; margin: 10px 0 0 0;">Elle donne lieu encore de nos jours à de nombreuses recherches en raison des enjeux économiques.</span>

## <div class = "encadré2">__Les types de compression__</div>

De nombreux algorithmes de compressions existent, chacun ayant sa particularité et surtout un type de données cible : images, vidéos, textes, exécutables, textes, ...
<span style="display: block; margin: 10px 0 0 0;">En effet un algorithme de compression très efficace pour un fichier texte sera une catastrophe pour de la vidéo et inversement.</span>
<span style="display: block; margin: 10px 0 0 0;">Lors de la décompression, la reconstruction des données s’effectue par un algorithme inverse ou différent de celui de la compression.</span> 

<center>
### <div class = "encadré3">__Compression symétrique / asymétrique__</div>
</center>

??? book "__La compression symétrique__" 
    Dans ce cas, la compression et la décompression utilisent la même méthode, et nécessitent la même quantité de calculs.
    ![Illustration](images/sym.png){: .image}

??? book2 "__La compression asymétrique__" 
    Dans ce cas, la compression et la décompression ne demandent pas la même quantité de travail. Par exemple la compression en MP3 est plus lente que la décompression pour la lecture, idem pour les vidéos.

<center>
### <div class = "encadré3">__Compression avec / sans pertes__</div>
</center>

??? book "__La compression sans perte (Lossless)__" 
    Les algorithmes de compression sans pertes permettent une reconstitution exacte de l’information après le cycle de compression / décompression. Ils s’utilisent pour les fichiers contenant du texte, les programmes informatiques (.exe), …  
    <span style="display: block; margin: 10px 0 0 0;">S'il est facile de citer des formats de compression connus sans pertes (__7z__, __Zip__, __Rar__, __Ace__, __Cab__, __gzip__, ...), on connaît moins le nom des algorithmes derrière ces extensions.</span>
    <span style="display: block; margin: 10px 0 0 0;">Pour __7z__ par exemple, il s'agit du <a href="https://fr.wikipedia.org/wiki/LZMA" target="_blank">LZMA</a> (pour *Lempel-Ziv-Markov chain-Algorithm*), pour __Zip__ du <a href="https://fr.wikipedia.org/wiki/LZ77_et_LZ78#LZ77" target="_blank">LZ77</a> et du <a href="https://fr.wikipedia.org/wiki/Codage_de_Huffman" target="_blank">codage Huffman</a>, pour __RAR__ du <a href="https://fr.wikipedia.org/wiki/LZ77_et_LZ78" target="_blank">Lempel-Ziv</a> et de la prédiction par reconnaissance partielle (<a href="https://fr.wikipedia.org/wiki/Pr%C3%A9diction_par_reconnaissance_partielle" target="_blank">PPM</a>).</span>

??? book2 "__La compression avec perte (Lossy)__" 
    Lors de la compression, l’algorithme supprime irrémédiablement des données en essayant de conserver une qualité de lecture/visionnage optimale. On parle de compression irréversible.  
    <span style="display: block; margin: 10px 0 0 0;">Les données dont la qualité se limite aux perceptions humaines (images, vidéos, sons, …) peuvent utiliser la compression avec pertes (JPEG, JPEG2000, ondelettes, fractales, MP3, MPEG...).</span>

## <div class = "encadré2">__Les critères de compression__</div>

La compression peut se définir par différents critères tels que :  
<div class="couleur_puce11" markdown="1">

* Le taux de compression (taille fichier compressé / taille fichier initial) qui s’exprime en pourcentage. Ou son inverse, le quotient (ratio) de compression = taille fichier initial / taille fichier compressé.
* La vitesse de compression/décompression.
* L’usage des ressources matérielles (mémoire, processeur).
* Rapport qualité/taux de compression (avec pertes).
* Robustesse : sensibilité de l’algorithme à des petites altérations du code compressé (erreurs de transmission).

</div>

## <div class = "encadré2">__David Albert Huffman__</div>

![Illustration](images/Huffman3.png){: .image}

Le professeur Huffman (1925 - 1999) a été un des pionniers dans le domaine de l’informatique.
<span style="display: block; margin: 10px 0 0 0;">Né dans l’Ohio, Huffman a obtenu une licence en ingénierie électrique à 18 ans. Puis il a travaillé pour la Marine militaire des États-Unis chargé de la maintenance des radars. Il a obtenu ensuite un master à l'université de l'Ohio et son doctorat au MIT en 1953.</span>
<span style="display: block; margin: 10px 0 0 0;">Huffman contribua beaucoup au développement de la théorie de l'information et du codage, dont les découvertes sont à la base des systèmes de compression de fichiers informatiques dans toutes les machines de nos jours.</span>
<span style="display: block; margin: 10px 0 0 0;">Il a également apporté sa contribution dans d’autres domaines tels que les signaux pour les radars par exemple.</span>
<span style="display: block; margin: 10px 0 0 0;">Huffman a longtemps enseigné la théorie de l'information et l'analyse des signaux à l’université de Californie à Santa Cruz.</span>

## <div class = "encadré2">__L’algorithme de compression de Huffman__</div>

Le codage de Huffman est un codage statistique à longueur variable. David Albert Huffman l’a conçu alors qu'il était étudiant au MIT. Il publia l'algorithme en 1952 dans un article intitulé "A Method for the Construction of Minimum-Redundancy Codes".
<span style="display: block; margin: 10px 0 0 0;">La compression se fait en remplaçant les caractères les plus fréquents par des codes courts et les caractères les moins fréquents par des codes longs. On observe ainsi des réductions de taille de l'ordre de 20 à 90 %.</span>
<span style="display: block; margin: 10px 0 0 0;">C'est une méthode de compression largement utilisée, souvent en complément d'autres algorithmes.</span>

<center>
### <div class = "encadré3">__L’algorithme__</div>
</center>

!!! clavier "__Les différentes phases de l'algorithme__"
    === "__Création d'un arbre binaire__"
        <div class = "list13_1">  

        1. A chaque caractère du fichier source, on associe sa fréquence. Chaque caractère de fréquence non nulle représente un arbre binaire à un élément.
        2. Classer chaque arbre binaire par valeur croissante ou décroissante de fréquence.
        3. Enlever de la liste les 2 arbres binaires de plus faible fréquence. Rattacher ces 2 arbres à une nouvelle racine qui vaut la somme des fréquences des 2 arbres précédents.
        4. Recommencer à <b><span style="color: rgb(252, 137, 22)">2.</span></b>, jusqu'à ce qu'il ne reste plus qu'un arbre binaire unique.

        </div>
    
    === "__Codage des caractères__"
        Pour connaître le code de Huffman associé à chaque caractère du fichier source, il suffit de parcourir l'arbre, en partant de la racine pour rejoindre le caractère voulu (feuille de l’arbre).  
        <span style="display: block; margin: 10px 0 0 0;">A chaque nœud, on ajoute "<b><span style="color: red">0</span></b>" au code en cours si on part dans le fils gauche et "<b><span style="color: green">1</span></b>" si on part dans le fils droit.</span>
    
    === "__Ecriture du fichier compressé__"
        On réécrit le fichier source en utilisant le nouveau code binaire des caractères, puis l’on joint la table de codage des caractères. 
        <span style="display: block; margin: 10px 0 0 0;">En pratique c’est l’encodage de l’arbre de Huffman qui est joint avant le codage du texte compressé.</span>

<center>
### <div class = "encadré3">__Utilisation__</div>
</center>

L’algorithme de compression de Huffman est utilisé par exemple, en complément d’autres algorithmes (souvent utilisé en deuxième passage), dans les formats de compression aussi variés que ZIP, PNG, JPEG, MP3.

<center>
### <div class = "encadré3">__Caractéristiques__</div>
</center>
<div class="couleur_puce17" markdown="1">

* Algorithme simple
* Sans pertes
* Asymétrique
* Plus lent que d’autres algorithmes puisque compression en 2 temps (1<sup>ère</sup> lecture du fichier pour l’étude statistique, puis encodage et écriture du fichier compressé).

</div>

## <div class = "encadré2">__Exemple de compression__</div>

Compression du mot "__BIENVENUE__" soit $~9~$ caractères ASCII et donc $~9×8=72~$ bits.
<center>
        <table>
        <tr>
        <th align="center" style="vertical-align:middle"><b>Symbole du fichier source</b></th>
        <td align="center" style="vertical-align:middle"><b>B</b></td>
        <td align="center" style="vertical-align:middle"><b>I</b></td>
        <td align="center" style="vertical-align:middle"><b>V</b></td>
        <td align="center" style="vertical-align:middle"><b>U</b></td>
        <td align="center" style="vertical-align:middle"><b>N</b></td>
        <td align="center" style="vertical-align:middle"><b>E</b></td>
        </tr>
        <tr>
        <th align="center" style="vertical-align:middle"><b>Fréquence d’apparition</b></th>
        <td align="center" style="vertical-align:middle"><b><span style="color:red">1</span></b></td>
        <td align="center" style="vertical-align:middle"><b><span style="color:red">1</span></b></b></td>
        <td align="center" style="vertical-align:middle"><b><span style="color:red">1</span></b></b></td>
        <td align="center" style="vertical-align:middle"><b><span style="color:red">1</span></b></b></td>
        <td align="center" style="vertical-align:middle"><b><span style="color:red">2</span></b></b></td>
        <td align="center" style="vertical-align:middle"><b><span style="color:red">3</span></b></b></td>
        </tr>
        </table>
        </center>

!!! star1 "__Etape 1__"
    Création d’un arbre (à un seul élément) par symbole du texte, triés dans l’ordre croissant (ou décroissant) de leurs fréquences d’apparition.
    ![Illustration](images/Huffman4.png){: .image}

!!! star2 "__Etape 2__"
    Suppression des 2 arbres de gauche, remplacés par un arbre qui les somme. Le nouvel arbre est inséré dans la liste en respectant l'ordre croissant (ou décroissant).
    ![Illustration](images/Huffman5.png){: .image}

!!! star3 "__Etape 3__"
    On recommence jusqu'à ce qu'il ne reste plus qu'un seul arbre binaire.
    ![Illustration](images/Huffman6.png){: .image}

!!! star4 "__Etape 4__"
    ![Illustration](images/Huffman7.png){: .image}

!!! star5 "__Etape 5__"
    ![Illustration](images/Huffman8.png){: .image}

!!! star6 "__Etape 6__"
    ![Illustration](images/Huffman9.png){: .image}

!!! star7 "__Etape 7__"
    On note :
    <div class="couleur_puce27">

    * <span style="color:red">0</span> les branches de gauche ;
    * <span style="color:green">1</span> les branches de droite.

    </div>
    Et on obtient alors l'__arbre de Huffman__ :
    ![Illustration](images/Huffman10.png){: .image}
    <span style="display: block; margin: 25px 0 0 0;"></span>

!!! star8 "__Etape 8__"
    Ecriture de la table de codage optimale des caractères. Le code associé à chaque caractère du code source est le chemin d'accès de la racine à la feuille.
    <center>
    <table>
    <tr>
    <th align="center" style="vertical-align:middle"><b>Symbole du fichier source</b></th>
    <td align="center" style="vertical-align:middle"><b>E</b></td>
    <td align="center" style="vertical-align:middle"><b>N</b></td>
    <td align="center" style="vertical-align:middle"><b>I</b></td>
    <td align="center" style="vertical-align:middle"><b>B</b></td>
    <td align="center" style="vertical-align:middle"><b>U</b></td>
    <td align="center" style="vertical-align:middle"><b>V</b></td>
    </tr>
    <tr>
    <th align="center" style="vertical-align:middle"><b>Nouveau codage</b></th>
    <td align="center" style="vertical-align:middle"><b>$~~$<span style="color:green">11</span>$~~$</b></td>
    <td align="center" style="vertical-align:middle"><b>$~~$<span style="color:green">1</span><span style="color:red">0</span>$~~$</b></td>
    <td align="center" style="vertical-align:middle"><b>$~$<span style="color:red">0</span><span style="color:green">11</span>$~$</b></td>
    <td align="center" style="vertical-align:middle"><b>$~$<span style="color:red">0</span><span style="color:green">1</span><span style="color:red">0</span>$~$</b></td>
    <td align="center" style="vertical-align:middle"><b>$~$<span style="color:red">00</span><span style="color:green">1</span>$~$</b></td>
    <td align="center" style="vertical-align:middle"><b>$~$<span style="color:red">000</span>$~$</b></td>
    </tr>
    </table>
    </center>

!!! star9 "__Etape 9__"
    Compression (réécriture) du code source avec la table de codage optimale.  
    Le mot "__BIENVENUE__" codé devient : 
    <b><span style="color:red">0</span><span style="color:green">1</span><span style="color:red">00</span><span style="color:green">11111</span><span style="color:red">0000</span><span style="color:green">111</span><span style="color:red">000</span><span style="color:green">111</span></b>

Ce qui fait, après compression, __22 bits__ au lieu de __72__ en ASCII, soit un taux de compression d'environ __30 %__.
<span style="display: block; margin: 10px 0 0 0;">En pratique on incorpore en entête du fichier compressé, le codage de l’arbre de Huffman afin de retrouver l’encodage optimal des symboles. Ce surplus est négligeable même pour des fichiers de petites tailles.</span>

