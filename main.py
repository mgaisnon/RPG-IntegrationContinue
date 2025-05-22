"""Point d'entrée du jeu RPG."""
from RPG.joueur import Joueur

def main():
    """Fonction principale"""
    joueur1 =  Joueur("Yassin le Mastermind")
    joueur2 = Joueur("Mathieu le Lobotomisateur")

    tour = 0
    while joueur1.vie > 0 and joueur2.vie > 0:
        if tour % 2 ==0:
            joueur1.tour(joueur2)
        else:
            joueur2.tour(joueur1)
        tour+=1

    print("\n🏁 Fin du jeu !")
    if joueur1.vie > 0:
        print(f"🎉 {joueur1.nom} a gagné !")
    else:
        print(f"🎉 {joueur2.nom} a gagné !")

if __name__ == "__main__":
    main()