class Joueur:
    def __init__(self, nom, vie):
        self.nom = nom
        self.vie = vie

    def attaque(self, cible):
        degats = 1
        cible.vie -= degats
        print(f"{self.nom} attaque {cible.nom} et lui inflige {degats} points de dégâts !")
        print(f"{cible.nom} a maintenant {cible.vie} points de vie.")

