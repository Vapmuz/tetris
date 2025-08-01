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
    
    def test_positionate(self):
        p= Pezzo('vuoto','x', [(0,1),(0,2)])
        self.assertEqual( p.positionate((0,1)) ,  (10 , 21))
        self.assertEqual( p.positionate((-11,1)) ,  False)
        self.assertEqual( p.positionate((1,-21)) ,  False)
        
    def test_positionate_piece(self):
         p= Pezzo('vuoto','x', [(0,1),(0,2)])
         self.assertEqual(p.positionate_piece(), [ (10, 21) , (10,22) ])
