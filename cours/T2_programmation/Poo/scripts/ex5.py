class personnage:

    def __\__init__\__(self, pointDeVie):
        self.vie = pointDeVie

    def donneEtat(self):
        return self.vie

    def perdVie(self):
        self.vie = self.vie - 1

darkVador = personnage(20)
lukeSkywalker = personnage(15)