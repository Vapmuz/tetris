import unittest 
from pezzo import Pezzo

class TestPezzo(unittest.TestCase):
    def test_creazione(self):
        p= Pezzo('punto','x',[(0,0)])
        #self.assertEqual(2,1)
        self.assertEqual('punto:l=1',str(p))