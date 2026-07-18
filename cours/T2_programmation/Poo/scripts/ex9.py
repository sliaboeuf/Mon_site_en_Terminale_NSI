import random

class personnage:
    def __\__init__\__(self, pointDeVie):
        self.vie = pointDeVie

    def donneEtat(self):
        return self.vie

    def perdVie(self):
        if random.random() > 0.5:
            nbPoint = 1
        else:
            nbPoint = 2
        self.vie = self.vie - nbPoint

lukeSkywalker = personnage(15)
lukeSkywalker.perdVie()
lukeSkywalker.perdVie()
lukeSkywalker.perdVie()
point = lukeSkywalker.donneEtat()