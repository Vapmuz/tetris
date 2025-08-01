"""Test dell'oggetto Campo"""
import unittest
from campo import Campo
from pezzo import ESSE


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

    def test_is_valid(self):
        """
        Controlla se una posizione è vaida.
        """
        c = Campo(2, 3)
        self.assertEqual(c.valid_pos((9, 9)), False)
        self.assertEqual(c.valid_pos((1, 1)), True)
        self.assertEqual(c.valid_pos((10, 1)), False)
        self.assertEqual(c.valid_pos((1, 10)), False)

    def test_plot(self):
        """
        Disegna l'oggetto se il campo è libero
        """
        c = Campo(4, 4)
        self.assertEqual(True, c.plot_at((1, 1), ESSE))
        self.assertEqual((",,,,|"
                          ",gg,|"
                          "gg,,|"
                          ",,,,|"),
                         str(c))
        # lo ridisegno allo steso posto - non lo fa
        self.assertEqual(False, c.plot_at((1, 1), ESSE))
        # anche se lo sposto in su di 1, non lo deve fare
        self.assertEqual(False, c.plot_at((0, 1), ESSE))

        # Il campo rimane immutato
        self.assertEqual((",,,,|"
                          ",gg,|"
                          "gg,,|"
                          ",,,,|"),
                         str(c))
