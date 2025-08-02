"""Test dell'oggetto Campo"""

import unittest
from campo import Campo
from pezzo import S, RIGA_TEST, I, Z, L, J, T, O


class TestCampo(unittest.TestCase):
    """test campo"""

    def test_creazione(self):
        """Istanzia l'oggetto e controlla sia tutto vuoto"""
        c = Campo(2, 3)
        self.assertEqual(
            (
                ",,,|"  #
                ",,,|"
            ),
            str(c),
        )

    def test_get_set(self):
        """Lettura e scrittura valori"""
        c = Campo(2, 3)
        c.set_at((0, 1), "blue")
        c.set_at((1, 2), "red")

        self.assertEqual((",b,|" ",,r|"), str(c))
        self.assertEqual("blue", c.val_at((0, 1)))
        self.assertEqual("red", c.val_at((1, 2)))
        self.assertEqual("", c.val_at((0, 0)))

    def test_is_all_empty(self):
        """controlla che sia tutto vuoto oppure no"""
        c = Campo(4, 4)
        self.assertEqual(True, c.is_all_empty())
        c.plot_at((1, 1), S)
        self.assertEqual(False, c.is_all_empty())

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
        self.assertEqual(True, c.plot_at((1, 1), S))
        self.assertEqual(
            (",bb,|" "bb,,|" ",,,,|" ",,,,|"),
            str(c),
        )
        # lo ridisegno allo steso posto - non lo fa
        self.assertEqual(False, c.plot_at((1, 1), S))
        # anche se lo sposto in su di 1, non lo deve fare
        self.assertEqual(False, c.plot_at((0, 1), S))

        # Il campo rimane immutato
        self.assertEqual(
            (
                ",bb,|"  #
                "bb,,|"
                ",,,,|"
                ",,,,|"
            ),
            str(c),
        )

    def test_unplot_at(self):
        """
        test per la funzione del_plot. In questa funzione si darà
        in pasto alla fuzione una matrice colorata
        """
        c = Campo(4, 4)
        c.plot_at((1, 1), S)
        self.assertEqual(True, c.unplot_at((1, 1), S))
        self.assertEqual(True, c.is_all_empty())

    def test_unplot_at_cancellazione(self):
        """
        test per la funzione del_plot. In questa funzione si darà
        in pasto alla fuzione una matrice colorata
        """
        c = Campo(4, 4)
        c.plot_at((0, 1), S)
        c.plot_at((2, 2), S)

        self.assertEqual(False, c.unplot_at((1, 1), S), "non è pieno")
        self.assertEqual(True, c.unplot_at((0, 1), S), "cancella il primo blocco")
        self.assertEqual(
            (
                ",,,,|"  #
                ",,bb|"
                ",bb,|"
                ",,,,|"
            ),
            str(c),
        )

        self.assertEqual(False, c.unplot_at((1, 1), S), "non è pieno")
        self.assertEqual(True, c.unplot_at((2, 2), S), "cancella il secondo")
        self.assertEqual(True, c.is_all_empty(), "campo vuoto")

    def test_fulline_at(self):
        """
        controlla se delle righe sono piene oppure no
        """
        c = Campo(3, 4)
        self.assertEqual([], c.fullline_at(), "controlla che non ci siano linee piene")

        c.plot_at((2, 1), RIGA_TEST)
        self.assertEqual([2], c.fullline_at(), "controlla che la riga 2 sia piena ")

        c.unplot_at((2, 1), RIGA_TEST)
        c.plot_at((1, 1), RIGA_TEST)
        self.assertEqual([1], c.fullline_at(), "controlla che la riga 1 sia piena ")

        c.unplot_at((1, 1), RIGA_TEST)
        c.plot_at((0, 1), RIGA_TEST)
        c.plot_at((2, 1), RIGA_TEST)
        self.assertEqual([0, 2], c.fullline_at(), "controlla che siano piene riga 0,2")


def print_piece():
    """
    funzione che disegna tutti i pezzi
    """
    c = Campo(6, 6)
    c.plot_at((2, 2), I)
    c.__str__()
    c.unplot_at((2, 2), I)
    c.plot_at((2, 2), Z)
    c.__str__()
    c.unplot_at((2, 2), Z)
    c.plot_at((2, 2), S)
    c.__str__()
    c.unplot_at((2, 2), S)
    c.plot_at((2, 2), L)
    c.__str__()
    c.unplot_at((2, 2), L)
    c.plot_at((2, 2), J)
    c.__str__()
    c.unplot_at((2, 2), J)
    c.plot_at((2, 2), T)
    c.__str__()
    c.unplot_at((2, 2), T)
    c.plot_at((2, 2), O)
    c.__str__()
    c.unplot_at((2, 2), O)
# end of the file
