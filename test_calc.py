import unittest
import calc

class TestCalc(unittest.TestCase):
    def test_add(self):
        self.assertEqual(calc.add(2,4), 6)
    def test_subtract(self):
        self.assertEqual(calc.subtract(2,4), -2)
    def test_multiply(self):
        self.assertEqual(calc.multiply(2,4), 8)
    def test_divide(self):
        self.assertEqual(calc.divide(4,2), 2)

if __name__ == '__main__':
    unittest.main(verbosity=2)