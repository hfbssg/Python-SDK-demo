import unittest
from math_sdk.math_sdk import MathOperations, DivisionByZeroError

class TestMathOperations(unittest.TestCase):
    
    def setUp(self):
        self.math = MathOperations()
    
    def test_add(self):
        self.assertEqual(self.math.add(2, 3), 5)
        self.assertEqual(self.math.add(-1, 1), 0)
    
    def test_subtract(self):
        self.assertEqual(self.math.subtract(5, 3), 2)
        self.assertEqual(self.math.subtract(3, 5), -2)
    
    def test_multiply(self):
        self.assertEqual(self.math.multiply(2, 3), 6)
        self.assertEqual(self.math.multiply(2, 0), 0)
    
    def test_divide(self):
        self.assertEqual(self.math.divide(6, 3), 2)
        self.assertEqual(self.math.divide(5, 2), 2.5)
        
        with self.assertRaises(DivisionByZeroError):
            self.math.divide(5, 0)
    
    def test_power(self):
        self.assertEqual(self.math.power(2, 3), 8)
        self.assertEqual(self.math.power(5, 0), 1)

if __name__ == '__main__':
    unittest.main()