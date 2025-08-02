"""unit test"""

import unittest
from nextup import Nextup
from pezzo import Pezzo


class TestNextup(unittest.TestCase):
    """Prova la bag per nextup"""

    def test_creazione(self):
        """Creo la classe"""
        n = Nextup()
        self.assertEqual("Nextup:(0)", str(n))

    def test_peek_pop(self):
        """Prova peek e pop"""
        n = Nextup()
        peeked = []
        for p in range(100):
            peeked.append(n.peek(p))
        self.assertTrue(len(n.queue) >= 100,
                        "ho fatto 100 peek quindi ho almeno 100 elementi")

        for p in range(100):
            v = n.pop()
            self.assertEqual(v, peeked[p], f"Elemento in pos #{p}")

        self.assertTrue(len(n.queue) < 10,
                        "ho fatto 100 pop, tolto molti elementi")

    def test_pop_autorefill(self):
        """Controlla il refill automatico"""
        n = Nextup()

        for _ in range(100):
            v = n.pop()
            self.assertTrue(isinstance(v, Pezzo),
                            f"pezzo {str(v)} è un Pezzo")

    def test_conta_elementi(self):
        """Conta il numero di elementi poppati"""
        n = Nextup()
        for _ in range(100):
            n.pop()
        self.assertEqual(100, n.pops)

    def test_elementi_unici(self):
        """Sui primi 7 elementi, ho 7 elementi unici"""
        n = Nextup()
        n_uniques = 7
        items = []
        for _ in range(n_uniques):
            items.append(n.pop())
        unique_items = set(map(lambda p: p.name, items))
        self.assertEqual(n_uniques, len(unique_items))

        # controllo siano sempre 7
        for _ in range(107):
            items.append(n.pop())
        unique_items = set(map(lambda p: p.name, items))
        self.assertEqual(n_uniques, len(unique_items))
