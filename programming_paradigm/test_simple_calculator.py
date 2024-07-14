import unittest
from simple_calculator import SimpleCalculator

class testSimpleCalculator(unittest.TestCase):
    def setUp(self):
        self.cal = SimpleCalculator()

    def test_add(self):
        self.assertEqual(self.cal.add(1,3),5)
        self.assertEqual(self.cal.add(-1,1),0)
        self.assertEqual(self.cal.add(-1,-1),-2)
        self.assertEqual(self.cal.add(0,0),0)

    def test_subtract(self):
        self.assertEqual(self.cal.subtract(3,2),1)
        self.assertEqual(self.cal.subtract(-1,1),-1)
        self.assertEqual(self.cal.subtract(-1,-1),1)
        self.assertEqual(self.cal.subtract(0,1),0)

    def test_multiply(self):
        self.assertEqual(self.cal.multiply(3,2),6)
        self.assertEqual(self.cal.multiply(-1,1),-1)
        self.assertEqual(self.cal.multiply(-1,-1),1)
        self.assertEqual(self.cal.multiply(0,1),0)

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