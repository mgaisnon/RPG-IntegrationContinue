class Joueur:
    def __init__(self, nom, vie=10):
        self.nom = nom
        self.vie = vie
        
    def attaque(self, dommage=1):
        self.vie -= dommage
        print(f"{self.nom} perd {dommage} point(s) de vie (PV restant: {self.vie}).")
        if self.vie <=0:
            print(f"{self.nom} est mort")

    def tour(self, cible):
        print(f"J1 : {self.nom} | PV : {self.vie}")
        print(f"J2 : {cible.nom} | PV : {cible.vie}")
        print(f"{self.nom} attaque {cible.nom}")
        cible.attaque()

if __name__ == "__main__":
    j1 = Joueur("Maa")
    j2 = Joueur("Matheuz")
    j2.tour(j1)