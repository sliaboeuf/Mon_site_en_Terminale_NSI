""" Module dicoFrequencesLangues

Ce module présente six fonctions qui retournent toutes un dictionnaire :

- freqFr: renvoie la fréquence théorique d'apparition des 26 lettres de l'alphabet latin moderne dans un texte écrit en français.
- freqAll: renvoie la fréquence théorique d'apparition des 26 lettres de l'alphabet latin moderne dans un texte écrit en allemand.
- freqEsp: renvoie la fréquence théorique d'apparition des 26 lettres de l'alphabet latin moderne dans un texte écrit en espagnol.
- freqPor: renvoie la fréquence théorique d'apparition des 26 lettres de l'alphabet latin moderne dans un texte écrit en portugais.
- freqIt: renvoie la fréquence théorique d'apparition des 26 lettres de l'alphabet latin moderne dans un texte écrit en italien.
- freqAng: renvoie la fréquence théorique d'apparition des 26 lettres de l'alphabet latin moderne dans un texte écrit en anglais.
"""

def freqFr():
    dico = {
    'a' : 0.08643 ,
    'b' : 0.01020 ,
    'c' : 0.03690 ,
    'd' : 0.04153 ,
    'e' : 0.16656 ,
    'f' : 0.01207 ,
    'g' : 0.00980 ,
    'h' : 0.00834 ,
    'i' : 0.08522 ,
    'j' : 0.00617 ,
    'k' : 0.00055 ,
    'l' : 0.06176 ,
    'm' : 0.03360 ,
    'n' : 0.08031 ,
    'o' : 0.06087 ,
    'p' : 0.03420 ,
    'q' : 0.01542 ,
    'r' : 0.07418 ,
    's' : 0.08997 ,
    't' : 0.08200 ,
    'u' : 0.07144 ,
    'v' : 0.01843 ,
    'w' : 0.00129 ,
    'x' : 0.00438 ,
    'y' : 0.00349 ,
    'z' : 0.00154 ,
    }
    return (dico)

def freqAll():
    dico = {
    'a' : 0.07107 ,
    'b' : 0.02063 ,
    'c' : 0.03341 ,
    'd' : 0.05546 ,
    'e' : 0.18996 ,
    'f' : 0.01812 ,
    'g' : 0.03286 ,
    'h' : 0.05197 ,
    'i' : 0.08242 ,
    'j' : 0.00295 ,
    'k' : 0.01321 ,
    'l' : 0.03755 ,
    'm' : 0.02762 ,
    'n' : 0.10677 ,
    'o' : 0.02740 ,
    'p' : 0.00862 ,
    'q' : 0.00022 ,
    'r' : 0.07642 ,
    's' : 0.07937 ,
    't' : 0.06714 ,
    'u' : 0.04749 ,
    'v' : 0.00731 ,
    'w' : 0.02063 ,
    'x' : 0.00033 ,
    'y' : 0.00044 ,
    'z' : 0.01234
    }
    return (dico)

def freqEsp():
    dico = {
    'a' : 0.14538 ,
    'b' : 0.01648 ,
    'c' : 0.05430 ,
    'd' : 0.06799 ,
    'e' : 0.15872 ,
    'f' : 0.00801 ,
    'g' : 0.01172 ,
    'h' : 0.00812 ,
    'i' : 0.07251 ,
    'j' : 0.00511 ,
    'k' : 0.00012 ,
    'l' : 0.05766 ,
    'm' : 0.03655 ,
    'n' : 0.07785 ,
    'o' : 0.10071 ,
    'p' : 0.02912 ,
    'q' : 0.01021 ,
    'r' : 0.07971 ,
    's' : 0.09259 ,
    't' : 0.05372 ,
    'u' : 0.04560 ,
    'v' : 0.01044 ,
    'w' : 0.00023 ,
    'x' : 0.00255 ,
    'y' : 0.01044 ,
    'z' : 0.00603
    }
    return (dico)

def freqPor():
    dico = {
    'a' : 0.17265 ,
    'b' : 0.01227 ,
    'c' : 0.04579 ,
    'd' : 0.05889 ,
    'e' : 0.14834 ,
    'f' : 0.01204 ,
    'g' : 0.01534 ,
    'h' : 0.01511 ,
    'i' : 0.07293 ,
    'j' : 0.00472 ,
    'k' : 0.00024 ,
    'l' : 0.03281 ,
    'm' : 0.05594 ,
    'n' : 0.05959 ,
    'o' : 0.12662 ,
    'p' : 0.02974 ,
    'q' : 0.01416 ,
    'r' : 0.07706 ,
    's' : 0.09216 ,
    't' : 0.05594 ,
    'u' : 0.05464 ,
    'v' : 0.01971 ,
    'w' : 0.00012 ,
    'x' : 0.00248 ,
    'y' : 0.00012 ,
    'z' : 0.00555
    }
    return (dico)

def freqIt():
    dico = {
    'a' : 0.13449 ,
    'b' : 0.01054 ,
    'c' : 0.05155 ,
    'd' : 0.04273 ,
    'e' : 0.13507 ,
    'f' : 0.01088 ,
    'g' : 0.01879 ,
    'h' : 0.01764 ,
    'i' : 0.12922 ,
    'j' : 0.00000 ,
    'k' : 0.00000 ,
    'l' : 0.07458 ,
    'm' : 0.02875 ,
    'n' : 0.07882 ,
    'o' : 0.11261 ,
    'p' : 0.03494 ,
    'q' : 0.00584 ,
    'r' : 0.07298 ,
    's' : 0.05705 ,
    't' : 0.06438 ,
    'u' : 0.03448 ,
    'v' : 0.02406 ,
    'w' : 0.00000 ,
    'x' : 0.00000 ,
    'y' : 0.00000 ,
    'z' : 0.00561
    }
    return (dico)

def freqAng():
    dico = {
    'a' : 0.08954 ,
    'b' : 0.01851 ,
    'c' : 0.03524 ,
    'd' : 0.04422 ,
    'e' : 0.13918 ,
    'f' : 0.02405 ,
    'g' : 0.01995 ,
    'h' : 0.05840 ,
    'i' : 0.08023 ,
    'j' : 0.00155 ,
    'k' : 0.00698 ,
    'l' : 0.04477 ,
    'm' : 0.02881 ,
    'n' : 0.08178 ,
    'o' : 0.08278 ,
    'p' : 0.02117 ,
    'q' : 0.00100 ,
    'r' : 0.07114 ,
    's' : 0.07303 ,
    't' : 0.10140 ,
    'u' : 0.03092 ,
    'v' : 0.01108 ,
    'w' : 0.02094 ,
    'x' : 0.00233 ,
    'y' : 0.01828 ,
    'z' : 0.00078
    }
    return (dico)
