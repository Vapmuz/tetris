"""file creato per unittest"""

import unittest
from pezzo import Pezzo, Pezzi

pp = Pezzi()


class TestPezzo(unittest.TestCase):
    """test per il file pezzo.py"""

    def test_creazione(self):
        """test di funzionamento istanzazione classe"""
        p = Pezzo("punto", "x", [(0, 0)])
        # self.assertEqual(2,1)
        self.assertEqual("punto:l=1", str(p))

    def test_rotpos(self):
        """
        test di funzionamento rotazione punti nello spazio
        """
        p = Pezzo("vuoto", "x", [(0, 0)])
        self.assertEqual((0, 0), p.rotpos((0, 0)), "(0,0)")
        self.assertEqual((0, -1), p.rotpos((1, 0)), "rotazione tupla con un nr =0")
        self.assertEqual((-1, -1), p.rotpos((1, -1)), "rotazione tupla con un nr = 0")
        self.assertEqual((1, 0), p.rotpos((0, 1)), "rotazione tupla con un nr = 0")
        self.assertEqual((-1, -2), p.rotpos((2, -1)), "rotazione tupla con un nr = 0")
        self.assertEqual(
            (-2, 1), p.rotpos((-1, -2)), "rotazione tupla quarto quadrante"
        )
        self.assertEqual((1, 2), p.rotpos((-2, 1)), "rotazione tupla primo quadrante")
        self.assertEqual(
            (-1, -1), p.rotpos((1, -1)), "rotazione tupla secondo quadrante"
        )
        self.assertEqual((-1, 1), p.rotpos((-1, -1)), "rotazione tupla terzo quadrante")
        self.assertEqual((0, 0), p.rotpos((0, 0)), "(0,0)")

    def test_prova_rotazione(self):
        """test finto per vederela rotazione"""

    def test_rotate(self):
        """test per la rotazione dei pezzi"""
        p = Pezzo("vuoto", "x", [(0, 1), (0, 2)])
        self.assertEqual([(1, 0), (2, 0)], p.rotate().pos)

    def test_rotate_o(self):
        """test per la rotazione della o"""
        p = Pezzo("o", "g", [(0, -1), (0, 0), (1, 0), (-1, -1)])
        self.assertEqual([(-1, 0), (0, 0), (0, -1), (-1, 1)], p.rotate().pos)

    def test_unrotate(self):
        """test per la contro-rotazione dei pezzi"""
        p = Pezzo("vuoto", "x", [(0, 1), (0, 2)])
        p.rotate()
        p.unrotate()
        self.assertEqual([(0, 1), (0, 2)], p.pos)

    def test_positionate(self):
        """
        test per il posizionamento dei pezzi. Si controlla che data la psoizione relativa
        i pezzi ricevano una posizione assoluta
        """
        p = Pezzo("vuoto", "x", [(0, 1), (0, 2)])
        b = (10, 20)
        self.assertEqual(p.positionate((0, 1), b), (10, 21))
        self.assertEqual(p.positionate((-11, 1), b), (-1, 21))
        self.assertEqual(p.positionate((1, -21), b), (11, -1))

    def test_positionate_piece(self):
        """
        Posiziona un pezzo e controlla che vengano ritornate
        solo le righe positive
        """
        p = Pezzo("rigo", "x", [(0, 0), (0, 1), (1, 1)])
        self.assertEqual(
            p.positionate_piece((0, 0)), [(0, 0), (0, 1), (1, 1)], "inalterato"
        )
        self.assertEqual(
            p.positionate_piece((3, 3)), [(3, 3), (3, 4), (4, 4)], "a (3,3)"
        )
        self.assertEqual(
            p.positionate_piece((-1, 2)), [(0, 3)], "a (-1,2) rimane solo un pixel"
        )

    def test_positionate_piece_esse(self):
        """
        Posizioni assolute per l'oggetto ESSE
        """
        self.assertEqual(
            pp.s().positionate_piece((1, 1)),
            [(1, 0), (1, 1), (0, 1), (0, 2)],
            "Posizione normale",
        )  # End-of-file (EOF)
