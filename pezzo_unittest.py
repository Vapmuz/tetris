import unittest 
from pezzo import Pezzo

class TestPezzo(unittest.TestCase):
    def test_creazione(self):
        p= Pezzo('punto','x',[(0,0)])
        #self.assertEqual(2,1)
        self.assertEqual('punto:l=1',str(p))

    def test_rotpos(self):
        p=Pezzo('vuoto','x', [(0,0)])
        self.assertEqual( (0,1) , p.rotpos( (-1,0) ), 'rotazione tupla vuota' )
        self.assertEqual( (-1,0) , p.rotpos( (0,-1) ), 'rotazione tupla vuota' )        
        self.assertEqual( (0,-1) , p.rotpos( (1,0) ), 'rotazione tupla vuota' )       
        self.assertEqual( (1,0) , p.rotpos( (0,1) ), 'rotazione tupla vuota' )

    def test_rotate(self):
        p= Pezzo('vuoto','x', [(0,1),(0,2)])
        self.assertEqual([ (1,0) , (2,0) ],p.rotate().pos)