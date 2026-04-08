import unittest
from calculator import *

class TestCalculator(unittest.TestCase):
    ######### Partner 2
    # def test_add(self): # 3 assertions
    #     fill in code

    # def test_subtract(self): # 3 assertions
    #     fill in code
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
    # def test_divide_by_zero(self): # 1 assertion
    #     # call division function inside, example:
    #     # with self.assertRaises(<INSERT_ERROR_TYPE>):
    #     #     div(0, 5)
    #     fill in code

    # def test_logarithm(self): # 3 assertions
    #     fill in code

    # def test_log_invalid_base(self): # 1 assertion
    #     # use same technique from test_divide_by_zero
    #     fill in code
    # ##########################
    
    ######## Partner 1
    def test_log_invalid_argument(self): # 1 assertion
        with self.assertRaises(ValueError):
            log(0, 5)

    def test_hypotenuse(self): # 3 assertions
        self.assertTrue(hypotenuse(2, 3) == 4)
        self.assertTrue(hypotenuse(5, 12) == 13)
        self.assertTrue(hypotenuse(8, 15) == 17)

    def test_sqrt(self): # 3 assertions
        with self.assertRaises(ValueError):
            square_root(-4)
        self.assertTrue(square_root(4) == 2)
        self.assertTrue(square_root(121) == 11)
    ##########################

# Do not touch this
if __name__ == "__main__":
    unittest.main()