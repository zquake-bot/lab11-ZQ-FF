import unittest
from calculator import *
import math

class TestCalculator(unittest.TestCase):
    ######### Partner 2
    def test_add(self): # 3 assertions
        self.assertEqual(add(4, 5), 4+5)

    def test_subtract(self): # 3 assertions
        self.assertEqual(subtract(7,3), 4)
    # ##########################

    ######## Partner 1
    def test_multiply(self): # 3 assertions
        self.assertTrue(mul(1, 2) == 2)
        self.assertTrue(mul(-3, 6) == -18)
        self.assertTrue(mul(0, -512) == 0)

    def test_divide(self): # 3 assertions
        self.assertTrue(div(2, 1) == 0.5)
        self.assertTrue(div(6, -18) == -3)
        self.assertTrue(div(100, 100) == 1)
    # ##########################

    ######## Partner 2
    def test_divide_by_zero(self): # 1 assertion
        with self.assertRaises(ZeroDivisionError):
            div(0, 5)


    #     # call division function inside, example:
    #     # with self.assertRaises(<INSERT_ERROR_TYPE>):
    #     #     div(0, 5)
    #     fill in code

    def test_logarithm(self): # 3 assertions
        self.assertEqual(logarithm(1, 10), 0)
        self.assertTrue(logarithm(4, 5), math.log(4, 5))
        self.assertTrue(logarithm(6, 7), math.log(6, 7))

    def test_log_invalid_base(self): # 1 assertion
        with self.assertRaises(ValueError):
            logarithm(0, 10)

    ######## Partner 1
    def test_log_invalid_argument(self): # 1 assertion
        with self.assertRaises(ValueError):
            logarithm(0, 5)

    def test_hypotenuse(self): # 3 assertions
        self.assertTrue(hypotenuse(3, 4) == 5)
        self.assertTrue(hypotenuse(5, 12) == 13)
        self.assertTrue(hypotenuse(7, 24) == 25)

    def test_sqrt(self): # 3 assertions
        with self.assertRaises(ValueError):
            square_root(-4)
        self.assertTrue(square_root(4) == 2)
        self.assertTrue(square_root(121) == 11)
    ##########################

# Do not touch this
if __name__ == "__main__":
    unittest.main()