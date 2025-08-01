import unittest 
from campo import Campo

class TestCampo(unittest.TestCase):
    
    def test_creazione(self):
        c = Campo(2,3)
        self.assertEquals( (",,,\n"
                            ",,,\n"), str(c))

    def test_get_set(self):
        c = Campo(2,3)
        c.set_at((0,1), "blue")
        c.set_at((1,2), "red")
        
        self.assertEqual( (",b,\n"
                            ",,r\n"), str(c))
        self.assertEqual( "blue", c.val_at((0,1)))
        self.assertEqual( "red", c.val_at((1,2)))
        self.assertEqual( "", c.val_at((0,0)))
        


