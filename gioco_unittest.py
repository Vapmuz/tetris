"""unit test"""

import unittest
from gioco import Gioco



class TestGioco(unittest.TestCase):
    """Prova il gioco"""

    def test_creazione(self):
        """Creo la classe"""
        g = Gioco()
        self.assertTrue( len(str(g))>0)
