import unittest
import sys
sys.path.insert(0, 'src')
from calculator import add, subtract, multiply, divide, power, modulo, compound_operation

class TestCalculator(unittest.TestCase):
    
    def test_add(self):
        self.assertEqual(add(5, 3), 8)
        self.assertEqual(add(-1, 1), 0)
    
    def test_subtract(self):
        self.assertEqual(subtract(10, 3), 7)
    
    def test_multiply(self):
        self.assertEqual(multiply(4, 5), 20)
    
    def test_divide(self):
        """🆕 Test custom divide function"""
        self.assertEqual(divide(10, 2), 5)
        with self.assertRaises(ValueError):
            divide(10, 0)
    
    def test_power(self):
        """🆕 Test custom power function"""
        self.assertEqual(power(3, 2), 9)
    
    def test_modulo(self):
        """🆕 Test custom modulo function"""
        self.assertEqual(modulo(10, 3), 1)
    
    def test_compound_operation(self):
        """🆕 Test custom compound operation"""
        self.assertEqual(compound_operation(1, 2, 3), 9)

if __name__ == '__main__':
    unittest.main()
