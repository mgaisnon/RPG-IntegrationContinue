"""Module de test."""

import sys
import os
import unittest

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from RPG.joueur import Joueur
from unittest.mock import patch


"""Class d'environnement de test"""
class TestEnvironnement(unittest.TestCase):
    @patch('builtins.input', return_value='')  # Mock l'entrée utilisateur
    def test_attaque_joueur(self, _):
        """Teste si l'attaque retourne la bonne valeur (exemple)."""
        j1 = Joueur("Maa")
        j2 = Joueur("Matheuz")

        j1.tour(j2)

        self.assertEqual(j2.vie,9)
        
    # def test_fail_attaque_joueur2(self):
    #     j1 = Joueur("Maa")
    #     j2 = Joueur("Matheuz")

    #     j1.tour(j2)
    #     assert j2.vie == 10


if __name__ == "__main__":
    unittest.main()
