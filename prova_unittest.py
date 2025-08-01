import unittest 
from prova import pippo

class TestProva(unittest.TestCase):
    def test_pippo(self):
        self.assertEqual(1,pippo())