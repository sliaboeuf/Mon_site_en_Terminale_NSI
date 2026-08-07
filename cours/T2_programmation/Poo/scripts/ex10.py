import random

class personnage:

    def __\__init__\__(self, pointDeVie):
        self.vie = pointDeVie

    def donneEtat(self):
        return self.vie

    def perdVie(self):
        if random.random() > 0.5:
            nbPoint = 1
        else :
            nbPoint = 2
        self.vie = self.vie - nbPoint

def game():
    lukeSkywalker = personnage(20)
    darkVador = personnage(20)

    while lukeSkywalker.donneEtat() > 0 and darkVador.donneEtat() > 0:
        lukeSkywalker.perdVie()
        darkVador.perdVie()

    if lukeSkywalker.donneEtat() <= 0 and darkVador.donneEtat() > 0:
        msg = f'''Dark Vador est vainqueur, il lui reste encore {darkVador.donneEtat()} points de vie alors que Luke Skywalker est mort'''

    elif darkVador.donneEtat() <= 0 and lukeSkywalker.donneEtat() > 0:
        msg = f'''Luke Skywalker est vainqueur, il lui reste encore {lukeSkywalker.donneEtat()} points de vie alors que Dark Vador est mort'''

    else:
        msg = "Les deux combattants sont morts en même temps"

    return msg