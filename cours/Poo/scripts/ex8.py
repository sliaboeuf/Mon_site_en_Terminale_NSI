class personnage:

    def __\__init__\__(self, pointDeVie):
        self.vie = pointDeVie

    def donneEtat(self):
        return self.vie

    def perdVie(self, nbPoint):
        self.vie = self.vie - nbPoint

lukeSkywalker = personnage(15)
lukeSkywalker.perdVie(2)
point = lukeSkywalker.donneEtat()