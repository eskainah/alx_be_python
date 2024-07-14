import unittest
from simple_calculator import SimpleCalculator

class testSimpleCalculator(unittest.TestCase):
    def setUp(self):
        self.calc = SimpleCalculator()

    def test_addition(self):
        self.assertEqual(self.calc.add(1,3),5)
        self.assertEqual(self.calc.add(-1,1),0)
        self.assertEqual(self.calc.add(-1,-1),-2)
        self.assertEqual(self.calc.add(0,0),0)

    def test_subtraction(self):
        self.assertEqual(self.calc.subtract(3,2),1)
        self.assertEqual(self.calc.subtract(-1,1),-1)
        self.assertEqual(self.calc.subtract(-1,-1),1)
        self.assertEqual(self.calc.subtract(0,1),0)

    def test_multiply(self):
        self.assertEqual(self.calc.multiply(3,2),6)
        self.assertEqual(self.calc.multiply(-1,1),-1)
        self.assertEqual(self.calc.multiply(-1,-1),1)
        self.assertEqual(self.calc.multiply(0,1),0)

    def test_division(self):
        """Test the division method."""
        self.assertEqual(self.cal.divide(6, 3), 2)
        self.assertEqual(self.cal.divide(-6, 3), -2)
        self.assertEqual(self.cal.divide(-6, -3), 2)
        self.assertEqual(self.cal.divide(5, 2), 2.5)
        self.assertEqual(self.cal.divide(0, 1), 0)
        self.assertEqual(self.cal.divide(1, 0), None)
        self.assertEqual(self.cal.divide(0, 0), None)

    if __name__ == "__main__":
        unittest.main()