import Calculator
import unittest
class TestCalculator(unittest.TestCase):
    def test_add(self):
        x = 10
        y = 22
        result = Calculator.add(x,y)
        self.assertEqual(result,x+y)

    def test_sub(self):
        x = 10
        y = 22
        result = Calculator.sub(x,y)
        self.assertEqual(result,x-y)

    def test_mult(self):
        x = 12
        y = 20
        result = Calculator.mult(x,y)
        self.assertEqual(result,x*y)

    def test_div(self):
        x = 22
        y = 22
        result = Calculator.div(x,y)
        self.assertEqual(result,x/y)

if __name__=="__main__":
    unittest.main()