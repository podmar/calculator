import unittest
from calculator import convert, add, subtract, multiply, divide, calculate, calculator_main

# struggling to write assertions for funtions taking no arguments or returning multiple arguments. 

class TestCalculator(unittest.TestCase): 
    def test_add(self): 
        """Testing addition funtion
        """
        self.assertEqual(add(3, 9), 12)
        self.assertEqual(add(-3, 9), 6)
        self.assertEqual(add(0, 9.5), 9.5)

    def test_subtract(self): 
        """Testing subtraction funtion
        """
        self.assertEqual(subtract(6, 19), -13)

    def test_multiply(self):
        """Testing multiplication funtion
        """
        self.assertEqual(multiply(3.12, 2), 6.24)

    def test_divide(self):
        """Testing division funtion
        """
        self.assertEqual(divide(6.80, 2), 3.4)
        self.assertEqual(divide(1, 5), 0.2)

    def test_calculate(self): 
        """Testing the funtion that decides which operation to conduct
        """
        self.assertEqual(calculate(5, -120, "+"), -115)
        self.assertEqual(calculate(-10, 203, "-"), -213)
        self.assertEqual(calculate(0.1, 5, "*"), 0.5)
        self.assertEqual(calculate(10, 20, "/"), 0.5)
        self.assertEqual(calculate(10, 0, "/"), None)
    
    def test_convert(self): 
        """Testing the function converting the user input
        """
        self.assertIsInstance(convert("52+2"), tuple)
        self.assertEqual(convert("52+2"), (52, 2, "+"))
        self.assertEqual(convert("5736*(-12)"), (5736, -12, "*"))
        self.assertEqual(convert("0/2"), (0, 2, "/"))
        self.assertEqual(convert("-5736/3"), (-5736, 3, "/"))
        self.assertEqual(convert("2/0"), (2, 0, "/"))

    # def test_main(self): 
    #     """Testing if program quits
    #     """
    #     self.assertEqual(calculator_main(), second)

    # def test_main(self): 
    #     """Testing main calculator funtion
    #     """
    #     self.assertEqual(calculator_main(), second)

if __name__ == "__main__": 
    unittest.main()