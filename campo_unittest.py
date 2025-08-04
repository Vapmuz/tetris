"""Test dell'oggetto Campo"""

import unittest
from campo import Campo
from pezzo import Pezzi
from pezzo import Pezzo

pp = Pezzi()


class TestCampo(unittest.TestCase):
    """test campo"""

    def test_creazione(self):
        """Istanzia l'oggetto e controlla sia tutto vuoto"""
        c = Campo(2, 3)
        self.assertEqual(
            ",,,|" ",,,|",
            str(c),
        )

    def test_builder(self):
        """Costruisce l'oggetto partendo da rappresentazione stringa"""
        v = ",,x,|" "xy,z|"

        c = Campo.build(v)
        self.assertEqual((2, 4), (c.rows, c.cols), "Numero righe e colonne")
        self.assertEqual(v, str(c), "Come la rappresentazione iniziale")

    def test_as_bw(self):
        """Stampa l'oggetto monocolore"""
        v = ",,q,|" "ab,c|"

        c = Campo.build(v)
        self.assertEqual(",,x,|" "xx,x|", c.as_bw())
        self.assertEqual(",,y,|" "yy,y|", c.as_bw(present="y"))

    def test_get_set(self):
        """Lettura e scrittura valori"""
        c = Campo(2, 3)
        c.set_at((0, 1), "blue")
        c.set_at((1, 2), "red")

        self.assertEqual(",b,|" ",,r|", str(c))
        self.assertEqual("blue", c.val_at((0, 1)))
        self.assertEqual("red", c.val_at((1, 2)))
        self.assertEqual("", c.val_at((0, 0)))

    def test_is_all_empty(self):
        """controlla che sia tutto vuoto oppure no"""
        c = Campo(4, 4)
        self.assertEqual(True, c.is_all_empty())
        c.plot_at((1, 1), pp.s())
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
        self.assertEqual(True, c.plot_at((1, 1), pp.s()))
        self.assertEqual(
            ",bb,|" "bb,,|" ",,,,|" ",,,,|",
            str(c),
        )
        # lo ridisegno allo stesso posto - non lo fa
        self.assertEqual(False, c.plot_at((1, 1), pp.s()))
        # anche se lo sposto in su di 1, non lo deve fare
        self.assertEqual(False, c.plot_at((0, 1), pp.s()))

        # Il campo rimane immutato
        self.assertEqual(
            ",bb,|" "bb,,|" ",,,,|" ",,,,|",
            str(c),
        )

    def test_unplot_at(self):
        """
        test per la funzione del_plot. In questa funzione si darà
        in pasto alla fuzione una matrice colorata
        """
        c = Campo(4, 4)
        c.plot_at((1, 1), pp.s())
        self.assertEqual(True, c.unplot_at((1, 1), pp.s()))
        self.assertEqual(True, c.is_all_empty())

    def test_unplot_at_cancellazione(self):
        """
        test per la funzione del_plot. In questa funzione si darà
        in pasto alla fuzione una matrice colorata
        """
        c = Campo(4, 4)
        c.plot_at((0, 1), pp.s())
        c.plot_at((2, 2), pp.s())

        self.assertEqual(False, c.unplot_at((1, 1), pp.s()), "non è pieno")
        self.assertEqual(True, c.unplot_at((0, 1), pp.s()), "cancella il primo blocco")
        self.assertEqual(
            ",,,,|"  #
            ",,bb|"
            ",bb,|"
            ",,,,|",
            str(c),
        )

        self.assertEqual(False, c.unplot_at((1, 1), pp.s()), "non è pieno")
        self.assertEqual(True, c.unplot_at((2, 2), pp.s()), "cancella il secondo")
        self.assertEqual(True, c.is_all_empty(), "campo vuoto")

    def test_fulline_at(self):
        """
        controlla se delle righe sono piene oppure no
        """
        c = Campo(3, 4)
        self.assertEqual([], c.fullline_at(), "controlla che non ci siano linee piene")

        c.plot_at((2, 1), pp.riga_test())
        self.assertEqual([2], c.fullline_at(), "controlla che la riga 2 sia piena ")

        c.unplot_at((2, 1), pp.riga_test())
        c.plot_at((1, 1), pp.riga_test())
        self.assertEqual([1], c.fullline_at(), "controlla che la riga 1 sia piena ")

        c.unplot_at((1, 1), pp.riga_test())
        c.plot_at((0, 1), pp.riga_test())
        c.plot_at((2, 1), pp.riga_test())
        self.assertEqual([0, 2], c.fullline_at(), "controlla che siano piene riga 0,2")

    def test_compact_rows(self):
        "test per la compattazione delle righe"
        c = Campo(4, 4)
        c.plot_at((2, 1), pp.riga_test())
        n_compacted = c.compact_rows()
        self.assertEqual(1, n_compacted)
        self.assertEqual(",,,,|" ",,,,|" ",,,,|" ",,,,|", str(c))

    def test_compact_rows_single(self):
        "Campo complesso, 1 riga"
        c = Campo(5, 4)
        c.plot_at((2, 1), pp.riga_test())
        c.plot_at((1, 1), pp.s())
        c.set_at((4, 1), "x")
        c.set_at((3, 0), "x")
        # c.compact_rows()
        self.assertEqual(",bb,|" "bb,,|" "rrrr|" "x,,,|" ",x,,|", str(c))
        n_compacted = c.compact_rows()
        self.assertEqual(1, n_compacted)
        self.assertEqual(",,,,|" ",bb,|" "bb,,|" "x,,,|" ",x,,|", str(c))

    def test_compact_rows_more_rows(self):
        "Campo complesso, 2 righe"
        c = Campo(5, 4)
        c.plot_at((2, 1), pp.riga_test())
        c.plot_at((1, 1), pp.s())
        c.plot_at((4, 1), pp.riga_test())
        c.set_at((3, 0), "x")
        # c.compact_rows()
        self.assertEqual(",bb,|" "bb,,|" "rrrr|" "x,,,|" "rrrr|", str(c))
        n_compacted = c.compact_rows()
        self.assertEqual(2, n_compacted)
        self.assertEqual(",,,,|" ",,,,|" ",bb,|" "bb,,|" "x,,,|", str(c))

    def test_pezzi_predefiniti(self):
        """
        funzione che disegna tutti i pezzi
        """
        c = Campo(4, 4)
        c.plot_at((1, 1), pp.s())
        self.assertEqual(
            ",bb,|" "bb,,|" ",,,,|" ",,,,|",
            str(c),
        )

        c = Campo(4, 4)
        c.plot_at((1, 1), pp.z())
        self.assertEqual(
            ",,,,|" "gg,,|" ",gg,|" ",,,,|",
            str(c),
        )

        c = Campo(4, 4)
        c.plot_at((0, 2), pp.i())
        self.assertEqual(
            "rrrr|" ",,,,|" ",,,,|" ",,,,|",
            str(c),
        )

        c = Campo(4, 4)
        c.plot_at((1, 1), pp.j())
        self.assertEqual(
            ",,,,|" ",b,,|" ",b,,|" "bb,,|",
            str(c),
        )

        c = Campo(4, 4)
        c.plot_at((1, 1), pp.l())
        self.assertEqual(
            ",,,,|" ",o,,|" ",o,,|" ",oo,|",
            str(c),
        )

        c = Campo(4, 4)
        c.plot_at((1, 1), pp.t())
        self.assertEqual(
            ",,,,|" "ppp,|" ",p,,|" ",,,,|",
            str(c),
        )

        c = Campo(4, 4)
        c.plot_at((1, 1), pp.o())
        self.assertEqual(
            ",gg,|" ",gg,|" ",,,,|" ",,,,|",
            str(c),
        )

    def test_all_L_rotations(self):
        """testa tutte le rotazioni del tetramino L"""
        L = pp.l()
        lst = [
            ",,,,,|" ",,,,,|" ",,x,,|" ",,x,,|" ",,xx,|",
            ",,,,,|" ",,,,,|" "xxx,,|" "x,,,,|" ",,,,,|",
            ",xx,,|" ",,x,,|" ",,x,,|" ",,,,,|" ",,,,,|",
            ",,,,,|" ",,,,x|" ",,xxx|" ",,,,,|" ",,,,,|",
        ]
        for x in range(4):
            self.assertEqual(lst[x], Campo.return_piece_rotation(L))


# end of the file
