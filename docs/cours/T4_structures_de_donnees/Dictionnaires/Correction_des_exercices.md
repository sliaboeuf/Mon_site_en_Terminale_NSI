# <center><div class = "titre2">Correction des exercices</div> </center>

### <div class = "encadré_exo"> __Correction de l'exercice 1__ </div>

```python
from donnees_titanic import passagers


# Question 1

print(f"Il y a {len(passagers)} passagers dans cette liste.")

id_recherche = 54
for passager in passagers:
    if passager['PassengerId'] == id_recherche:
        print(passager)

nb_survivants = 0
for passager in passagers:
    if passager['Survived']:
        nb_survivants += 1
print(f"Il y a {nb_survivants} survivants dans cette liste.")


# Question 2

nb_survivants_par_classe = [0, 0, 0, 0]
nb_passagers_par_classe = [0, 0, 0, 0]
# Par simplicité, la classe 1 sera à l'indice 1, idem pour la classe 2 et la classe 3.
for passager in passagers:
    if 'Pclass' in passager and 'Survived' in passager:
        nb_passagers_par_classe[passager['Pclass']] += 1
        if passager['Survived']:
            nb_survivants_par_classe[passager['Pclass']] += 1
print("Les pourcentages de survie sont :")
for classe in [1, 2, 3]:
    print(f"- Classe {classe} : {nb_survivants_par_classe[classe] * 100 // nb_passagers_par_classe[classe]}%")


# Question 3

nb_passager_cherbourg = 0
nb_survivants_cherbourg = 0
for passager in passagers:
    if 'Embarked' in passager:
        if passager['Embarked'] == 'C':
            nb_survivants_cherbourg += 1
        nb_passager_cherbourg += 1
print(f"{nb_survivants_cherbourg * 100 // nb_passager_cherbourg}% des passagers embarqués à Cherbourg ont survécu.")

```

### <div class = "encadré_exo"> __Correction de l'exercice 2__ </div>

```python
def occurrences(sequence):
    """
    Compte les occurences dans une liste
    :param sequence: Une séquence ordonnée (tuple, list ou str)
    :return: dictionnaire tel que :
            - les clefs sont les valeurs de la séquence
            - les valeurs sont les occurrences de ces clefs dans la séquence
    >>> occurrences([4, 2, 3, 4, 1, 4, 3, 4])
    {4: 4, 2: 1, 3: 2, 1: 1}
    >>> occurrences("abracadrabra")
    {'a': 5, 'b': 2, 'r': 3, 'c': 1, 'd': 1}
    """
    dico = {}
    for valeur in sequence:
        if valeur in dico:
            # Si la valeur est déjà dans le dico, on incrémente
            dico[valeur] += 1
        else:
            # Sinon on l'ajoute
            dico[valeur] = 1
    return dico


def compte_mots(phrase):
    """
    Compte les occurences de mots dans une chaîne de caractères
    :param phrase: une chaîne de caractère comportant des espaces
    :return: dict – dictionnaire tel que :
            - les clés sont les mots de la chaine
            - les valeurs sont les occurrences des mots
    >>> compte_mots("a b a c ab")
    {'a': 2, 'b': 1, 'c': 1, 'ab': 1}
    """
    # On découpe la phrase à chaque espace (méthode split)
    liste = phrase.split()
    # On se sert de la fonction précédente
    return occurrences(liste)


def compte_tous_mots(phrase):
    """
    Compte le nombre de mots selon la taille dans une chaîne de caractères
    :param phrase: une chaîne de caractère comportant des espaces
    :return: dict – dictionnaire tel que :
            - les clés sont des entiers (longueurs possibles pour un mot)
            - les valeurs sont les occurrences des mots ayant cette longueur
    >>> compte_tous_mots("a b a c ab")
    {1: 4, 2: 1}
    """
    dico_mots = compte_mots(phrase)
    dico_taille = {}

    for mot, nombre in dico_mots.items():
        taille = len(mot)
        if taille in dico_taille:
            # Si la taille du mot est déjà dans le dico, on ajoute son nombre d'occurences
            dico_taille[taille] += nombre
        else:
            # Sinon on le rajoute
            dico_taille[taille] = nombre

    return dico_taille

def plus_frequent(dico, longueur):
    """
    Renvoie les mots les plus fréquents de la longueur donnée. En cas d'égalité en fréquence, on renverra tous les mots
    de cette égalité.
    :param dico: dictionnaire de chaines avec leur occurence
    :param longueur: longueur à regarder pour trouver les mots
    :return: string – chaine de taille longueur ayant
             l'occurence la plus grande.
    >>> plus_frequent({'a': 3, 'b': 2, 'c': 3, 'ab': 5}, 1)
    ['a', 'c']
    """
    # Intitialisation à une liste vide et une fréquence nulle
    maximum = []
    frequence_maximum = 0

    for mot in dico:
        # Vérification de la contrainte de longueur
        if len(mot) == longueur:
            # Vérification de la fréquence du mot
            if dico[mot] > frequence_maximum:
                # Si plus grand, on remet à zéro
                maximum = [mot]
                frequence_maximum = dico[mot]
            elif dico[mot] == frequence_maximum:
                # Si égalité, on ajoute dans notre liste de maximums
                maximum.append(mot)
            # Sinon, on ne fait rien

    return maximum


##----- Programme principal et tests -----##
if __name__ == '__main__':
    import doctest
    doctest.testmod()
    
    # Importation du fichier du "Petit Chaperon Rouge"
    f = open("Petit_Chaperon_Rouge_Sans_Ponctuation.txt")
    texte = f.read()

    # Question 3
    dico = compte_mots(texte)
    for mot, nombre in dico.items():
        print(f"{mot} -> {nombre}")

    # Question 4
    print(compte_tous_mots(texte))

    # Question 5
    for longueur in range(13, 0, -1):
        print(f"Mot(s) de longueur {longueur} les plus fréquents : {plus_frequent(dico, longueur)}.")

```