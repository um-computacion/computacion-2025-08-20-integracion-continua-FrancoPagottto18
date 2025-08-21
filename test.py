import unittest
from main import suma

class TestPrueba(unittest.TestCase):
    def test_suma(self):
       self.assertEquals(suma(1,2),3)

if __name__ == '__main__':
    unittest.main()
    