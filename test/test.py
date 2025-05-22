"""Module de test."""

import sys
import os
import unittest
from RPG.joueur import Joueur
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

class TestEnvironnement(unittest.TestCase):
    def test_attaque_joueur(self):
        """Teste si l'attaque retourne la bonne valeur (exemple)."""
        j1 = Joueur("Maa")
        j2 = Joueur("Matheuz")

        j1.tour(j2)
        assert j2.vie == 9
        
    # def test_fail_attaque_joueur2(self):
    #     j1 = Joueur("Maa")
    #     j2 = Joueur("Matheuz")

    #     j1.tour(j2)
    #     assert j2.vie == 10


if __name__ == "__main__":
    unittest.main()
