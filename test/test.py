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

    @patch('builtins.input', return_value='')  # Mock l'entrée utilisateur
    def test_est_mort_apres_10_attaques(self, _):
        j1 = Joueur("Maa")
        j2 = Joueur("Matheuz")

        for _ in range(10):
            j1.tour(j2)

        self.assertTrue(j2.est_mort())

    @patch('builtins.input', return_value='')  # Mock l'entrée utilisateur
    def test_vie_ne_descend_pas_sous_zero(self, _):
        j1 = Joueur("Maa")
        j2 = Joueur("Matheuz")

        for _ in range(15):
            j1.tour(j2)

        self.assertEqual(j2.vie, 0)

    @patch('builtins.input', return_value='')
    def test_attaque_personnalisee(self, _):
        j1 = Joueur("Maa")
        j2 = Joueur("Matheuz")

        j1.tour(j2, dommage=3)

        self.assertEqual(j2.vie, 7)

    @patch('builtins.input', return_value='')
    def test_pas_attaque_si_mort(self, _):
        j1 = Joueur("Maa")
        j2 = Joueur("Matheuz")

        for _ in range(10):
            j1.tour(j2)  # j2 est mort ici

        vie_avant = j2.vie
        j1.tour(j2)  # attaque après mort

        self.assertEqual(j2.vie, vie_avant)

    @patch('builtins.input', return_value='')
    def test_attaque_invalide_dommage_negatif(self, _):
        j1 = Joueur("Maa")
        j2 = Joueur("Matheuz")

        j1.tour(j2, dommage=-3)

        self.assertEqual(j2.vie, 10)  # aucun dégât infligé


if __name__ == "__main__":
    unittest.main()
