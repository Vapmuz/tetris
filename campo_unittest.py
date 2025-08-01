"""Test dell'oggetto Campo"""
import unittest
from campo import Campo


class TestCampo(unittest.TestCase):
    """test campo"""

    def test_creazione(self):
        "Istanzia l'oggetto e controlla sia tutto vuoto"
        c = Campo(2, 3)
        self.assertEqual((",,,|"
                          ",,,|"), str(c))

    def test_get_set(self):
        """Lettura e scrittura valori"""
        c = Campo(2, 3)
        c.set_at((0, 1), "blue")
        c.set_at((1, 2), "red")

        self.assertEqual((",b,|"
                          ",,r|"), str(c))
        self.assertEqual("blue", c.val_at((0, 1)))
        self.assertEqual("red", c.val_at((1, 2)))
        self.assertEqual("", c.val_at((0, 0)))

    def test_get_set_out_of_bounds(self):
        """
        Controlla che si abbia errore leggendo e 
        scrivendo fuori del range dichiarato
        """
        c = Campo(2, 3)
        with self.assertRaises(IndexError):
            c.set_at((9, 9), "x")
        with self.assertRaises(IndexError):
            c.val_at((9, 9))
