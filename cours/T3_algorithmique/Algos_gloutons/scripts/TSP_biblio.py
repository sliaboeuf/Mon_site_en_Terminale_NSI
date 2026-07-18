# coding: UTF-8
import random, numpy, math, pylab, copy

def get_tour_fichier(f):
    """
    : lecture fichier de ville format ville, latitude, longitude
    : renvoie un tour contenant les villes dans l ordre du fichier
    : param f: file
    : return: (list)
    """
    fichier = open(f, "r")
    tour_initial = fichier.read().replace (",", ".").split ("\n")
    fichier.close()
    tour_initial=[t.split ("\t") for t in tour_initial]
    tour_initial = [t[:1] + [float(x) for x in t[1:]] for t in tour_initial]
    return tour_initial


def distance(tour, i, j):
    """
    Calcul la distance euclidienne entre i et j
    : param tour: sequence de ville
    : param i: numero de la ville de départ
    : param j: numero de la ville d arrivee
    : return: float
    CU: i et j dans le tour
    """
    dx = tour[i][1] - tour[j][1]
    dy = tour[i][2] - tour[j][2]
    return (dx ** 2 + dy ** 2) ** 0.5


def longueur_tour(tour):
    """
    calcul la longueur total d une tournée de la ville de départ et retourne à la ville de départ
    : param tour: tournee de ville n villes = n segments
    : return: float distance totale
    """
    d = 0
    for i in range (0, len(tour)-1):
        d += distance (tour, i, i+1)
    # il ne faut pas oublier de boucler pour le dernier segment  pour retourner à la ville de départ
    d += distance (tour, 0, -1)
    return d

def distances_entre_villes(tour):
    distances = []
    for i in range(len(tour)):
        dist = []
        for j in range(len(tour)):
            dist.append(distance(tour, i, j))
        distances.append(dist)
    return distances

def indice_distance_min(ville, liste_ville, distances):
    '''
    Renvoie l'indice de la ville la plus proche étant
    donnée une ville, une liste de villes sous forme d'indices, une matrice de
    distances.

    :param ville: (int) indice d'une ville
    :param liste_ville: (list) liste d'indices des villes
    :param (distance):  (list of list of float) matrice des distances
    :return: (int) l'indice de la ville la plus proche parmi ceux de la liste
    '''
    dist_min = None
    for i in range(len(liste_ville)):
        d = distances[ville][liste_ville[i]]
        if (dist_min == None or (0 < d < dist_min)) and d != 0:
            dist_min = d
            ind_min = liste_ville[i]

    return ind_min

tour = get_tour_fichier("exemple.txt")
print(distances_entre_villes(tour))
liste_ville = [i for i in range(len(tour))]
print(indice_distance_min(0, liste_ville, distances_entre_villes(tour)))

def trace(tour):
    """
    Trace la tournée realisée
    : param tour: list de ville
    """
    x =[t[1] for t in tour]
    y =[t[2] for t in tour]
    x += [x[0]] # on ajoute la dernière ville pour boucler
    y += [y[0]] #
    pylab.plot(x, y, linewidth=5)
    for ville, x, y in tour:
        pylab.text(x, y, ville)
    pylab.show()

def tour_glouton(ville_dep:str) -> float:
    the_tour = get_tour_fichier("exemple.txt")

    distances = distances_entre_villes(the_tour)
    liste_villes = [i for i in range(len(the_tour))]

    for i in range(len(the_tour)):
        if the_tour[i][0] == ville_dep:
            ind_ville_dep = i

    new_tour = [the_tour[ind_ville_dep]]
    ind_ville = ind_ville_dep
    liste_villes.remove(ind_ville)

    while len(liste_villes) != 0:
        ind_next_ville = indice_distance_min(ind_ville, liste_villes, distances)
        new_tour.append(the_tour[ind_next_ville])
        liste_villes.remove(ind_next_ville)
        ind_ville = ind_next_ville

    new_tour.append(the_tour[ind_ville_dep])

    trace(new_tour)

    return longueur_tour(new_tour)

print(tour_glouton('Paris'))