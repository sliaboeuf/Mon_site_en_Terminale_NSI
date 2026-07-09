from etageres import *


def tester_tout():
    tester_generer_livres()
    print("test generer_livres : ok")
    tester_ranger_livres()
    print("test ranger_livres : ok")


def tester_generer_livres():
    nombre = 10
    livres = generer_livres(nombre)
    assert len(livres) == nombre, "le nombre de livres est incorrect"
    for livre in livres:
        assert LARGEUR_MIN <= livre <= LARGEUR_MAX, "les livres doivent avoir une taille entre LARGEUR_MIN et LARGEUR_MAX"


def tester_ranger_livres():
    '''
    Vérifie les critères donnés pour les étagères.
    @SE: lève une exception si un des critères n'est pas vérifié
    '''
    nombre = 10
    livres = generer_livres(nombre)
    etageres = ranger_livres(livres)
    print(etageres)
    plat = [livre for etagere in etageres for livre in etagere]
    assert len(plat) == nombre, "le nombre total de livres n'est pas correct"
    print(plat, list(range(nombre)))
    assert plat == livres, "les livres doivent être rangés dans l'ordre"
    for etagere in etageres:
        assert sum(etagere) <= LARGEUR_ETAGERE, f"l'étagère {index} est trop remplie"


if __name__ == '__main__':
    tester_tout()
