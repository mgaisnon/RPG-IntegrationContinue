"""Module joueur du RPG."""
class Joueur:
    """Classe représentant un joueur."""
    def __init__(self, nom, vie=10):
        """Initialise un joueur avec son nom et ses points de vie."""
        self.nom = nom
        self.vie = vie

    def attaque(self, dommage=1):
        """Logique d'attaque du joueur."""
        if dommage <= 0:
            print(f"Attaque invalide ({dommage}). Aucun dégât infligé.")
            return
        if self.est_mort():
            print(f"{self.nom} est déjà mort. Attaque ignorée.")
            return
        self.vie = max(0, self.vie - dommage)
        print(f"{self.nom} perd {dommage} point(s) de vie (PV restant: {self.vie}).")
        if self.vie <= 0:
            print(f"{self.nom} est mort")

    def est_mort(self):
        """Retourne True si le joueur est mort."""
        return self.vie <= 0

    def tour(self, cible, dommage=1):
        """Logique de bataille entre les joueurs."""
        print(f"\n🎮 {self.nom} joue son tour !")
        print(f"J1 : {self.nom} | PV : {self.vie}")
        print(f"J2 : {cible.nom} | PV : {cible.vie}")
        input(f"Appuie sur Entrée pour attaquer {cible.nom}...")
        cible.attaque(dommage=dommage)

