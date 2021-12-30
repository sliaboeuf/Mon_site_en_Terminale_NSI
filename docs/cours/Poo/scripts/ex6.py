class personnage:

    def __\__init__\__(self, pointDeVie):
        self.vie = pointDeVie

    def donneEtat(self):
        return self.vie

    def perdVie(self):
        self.vie = self.vie - 1

lukeSkywalker = personnage(15)
lukeSkywalker.perdVie()
point = lukeSkywalker.donneEtat()