import unittest
from pezzo import Pezzo, ESSE


class TestPezzo(unittest.TestCase):
    def test_creazione(self):
        p = Pezzo('punto', 'x', [(0, 0)])
        # self.assertEqual(2,1)
        self.assertEqual('punto:l=1', str(p))

    def test_rotpos(self):
        p = Pezzo('vuoto', 'x', [(0, 0)])
        self.assertEqual((0, 1), p.rotpos((-1, 0)), 'rotazione tupla vuota')
        self.assertEqual((-1, 0), p.rotpos((0, -1)), 'rotazione tupla vuota')
        self.assertEqual((0, -1), p.rotpos((1, 0)), 'rotazione tupla vuota')
        self.assertEqual((1, 0), p.rotpos((0, 1)), 'rotazione tupla vuota')

    def test_rotate(self):
        p = Pezzo('vuoto', 'x', [(0, 1), (0, 2)])
        self.assertEqual([(1, 0), (2, 0)], p.rotate().pos)

    def test_positionate(self):
        p = Pezzo('vuoto', 'x', [(0, 1), (0, 2)])
        b = (10, 20)
        self.assertEqual(p.positionate((0, 1), b),  (10, 21))
        self.assertEqual(p.positionate((-11, 1), b),  (-1, 21))
        self.assertEqual(p.positionate((1, -21), b),  (11, -1))

    def test_positionate_piece(self):
        """
        Posiziona un pezzo e controlla che vengano ritornate
        solo le righe positive
        """
        p = Pezzo('rigo', 'x', [(0, 0), (0, 1), (1, 1)])
        self.assertEqual(p.positionate_piece((0, 0)),
                         [(0, 0), (0, 1), (1, 1)],
                         "inalterato")
        self.assertEqual(p.positionate_piece((3, 3)),
                         [(3, 3), (3, 4), (4, 4)],
                         "a (3,3)")
        self.assertEqual(p.positionate_piece((-1, 2)),
                         [(0, 3)],
                         "a (-1,2) rimane solo un pixel")

    def test_positionate_piece_esse(self):
        """
        Posizioni assolute per l'oggetto ESSE
        """
        self.assertEqual(ESSE.positionate_piece((1, 1)),
                         [(1, 1), (1, 2), (2, 0), (2, 1)],
                         "Posizione normale")
