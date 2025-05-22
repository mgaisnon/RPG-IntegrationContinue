import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import unittest
from RPG.joueur import Joueur

class TestEnvironnement(unittest.TestCase):
    def test_attaque_joueur(self):
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
