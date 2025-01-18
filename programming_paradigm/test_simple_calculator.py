import unittest
from simple_calculator import SimpleCalculator

class TestSimpleCalculator(unittest.TestCase):


    def setUp(self):
        """Set up the SimpleCalculator instance before each test."""
        self.calc = SimpleCalculator()

    def test_addition(self):
        """Test the addition method."""
        self.assertEqual(self.calc.add(3, 2), 5)
        self.assertEqual(self.calc.add(-1, 1), 0)

        # Add more assertions to thoroughly test the add method.
    def test_subtraction(self):
        """Test the subtraction method."""
        self.assertEqual(self.calc.subtract(7, 4), 3)
        self.assertEqual(self.calc.subtract(5, 6), -1)

    def test_multiplication(self):
        """Test the multiplication method."""
        self.assertEqual(self.calc.multiply(3, 4), 12)
        self.assertEqual(self.calc.multiply(0, 1), 0)

    def test_division(self):
        """Test the division method."""
        self.assertEqual(self.calc.divide(6, 2), 3)
        self.assertEqual(self.calc.divide(9, 3), 3)
    
        self.assertIsNone(self.calc.divide(9, 0), 3) #Edge case: division by zero
         
if __name__ == "__main__":
  unittest.main()
