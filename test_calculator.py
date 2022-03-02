import unittest
from calculator import convert, add, subtract, multiply, divide, calculate, calculator_main

class TestCalculator(unittest.TestCase): 
    def test_operations(self): 
        """Testing the operations funtions: add, subtract, multiply & divide.
        """
        self.assertEqual(add(3, 9), 12)
        self.assertEqual(add(-3, 9), 6)
        self.assertEqual(add(0, 9.5), 9.5)
        self.assertEqual(subtract(6, 19), -13)
        self.assertEqual(multiply(3.12, 2), 6.24)
        self.assertEqual(divide(6.80, 2), 3.4)
        self.assertEqual(divide(1, 5), 0.2)


    def test_calculate_negative_numbers(self): 
        """Testing calculate funtion with negative numbers
        """

        self.assertEqual(calculate(5, -120, "+"), -115)
        self.assertEqual(calculate(5, -120, "-"), 125)
        self.assertEqual(calculate(5, -120, "*"), -600)
        self.assertEqual(calculate(120, -5, "/"), -24)

        self.assertEqual(calculate(-5, 120, "+"), 115)
        self.assertEqual(calculate(-5, 120, "-"), -125)
        self.assertEqual(calculate(-5, 120, "*"), -600)
        self.assertEqual(calculate(-120, 5, "/"), -24)

        self.assertEqual(calculate(-5, -120, "+"), -125)
        self.assertEqual(calculate(-10, -203, "-"), 193)
        self.assertEqual(calculate(-0.1, -5, "*"), 0.5)
        self.assertEqual(calculate(-10, -20, "/"), 0.5)

    def test_calculate_zero(self): 
        """Testing the calculate function with operations with 0
        """

        self.assertEqual(calculate(0, 120, "+"), 120)
        self.assertEqual(calculate(0, 120, "-"), -120)
        self.assertEqual(calculate(0, 120, "*"), 0)
        self.assertEqual(calculate(0, 5, "/"), 0)

        self.assertEqual(calculate(5, 0, "+"), 5)
        self.assertEqual(calculate(5, 0, "-"), 5)
        self.assertEqual(calculate(5, 0, "*"), 0)
        self.assertEqual(calculate(120, 0, "/"), None)

        self.assertEqual(calculate(0, 0, "+"), 0)
        self.assertEqual(calculate(0, 0, "-"), 0)
        self.assertEqual(calculate(0, 0, "*"), 0)
        self.assertEqual(calculate(0, 0, "/"), None)

    def test_calculate_floats(self):
        """Testing calculate function on operations with floats
        """

        self.assertEqual(calculate(0.1, 1, "+"), 1.1)
        self.assertEqual(calculate(2.5, 2, "-"), 0.5)
        self.assertEqual(calculate(0.5, 120, "*"), 60)
        self.assertEqual(calculate(0.8, 4, "/"), 0.2)

        self.assertEqual(calculate(5, 0.5, "+"), 5.5)
        self.assertEqual(calculate(5, 0.7, "-"), 4.3)
        self.assertEqual(calculate(5, 0.2, "*"), 1)
        self.assertEqual(calculate(120, 0.5, "/"), 240)

        self.assertEqual(calculate(-0.5, 120, "+"), 119.5)
        self.assertEqual(calculate(-10, -2.5, "-"), -7.5)
        self.assertEqual(calculate(-0.1, 5, "*"), -0.5)
        self.assertEqual(calculate(-10, -0.5, "/"), 20)

    def test_convert_type(self): 
        """Testing the return type of the convert function
        """
        self.assertIsInstance(convert("52+2"), list)

    def test_convert_negative_numbers(self): 
        """Testing the convert funtion with negative numbers
        """
        self.assertEqual(convert("5+-120"), [5.0, -120.0, "+"])
        self.assertEqual(convert("5--120"), [5.0, -120.0, "-"])
        self.assertEqual(convert("5*-120"), [5.0, -120.0, "*"])
        self.assertEqual(convert("120/-5"), [120.0, -5.0, "/"])

        self.assertEqual(convert("-5+120"), [-5.0, 120.0, "+"])
        self.assertEqual(convert("-5-120"), [-5.0, 120.0, "-"])
        self.assertEqual(convert("-5*120"), [-5.0, 120.0, "*"])
        self.assertEqual(convert("-120/5"), [-120.0, 5.0, "/"])

        self.assertEqual(convert("-5+-120"), [-5.0, -120.0, "+"])
        self.assertEqual(convert("-10--203"), [-10.0, -203.0, "-"])
        self.assertEqual(convert("-0.1*-5"), [-0.1, -5.0, "*"])
        self.assertEqual(convert("-10/-20"), [-10.0, -20.0, "/"])

    def test_convert_zero(self): 
        """Testing the convert function with 0 as input
        """

        self.assertEqual(convert("5+0"), [5.0, 0.0, "+"])
        self.assertEqual(convert("5-0"), [5.0, 0.0, "-"])
        self.assertEqual(convert("5*0"), [5.0, 0.0, "*"])
        self.assertEqual(convert("120/0"), [120.0, 0.0, "/"])

        self.assertEqual(convert("0+120"), [0.0, 120.0, "+"])
        self.assertEqual(convert("0-120"), [0.0, 120.0, "-"])
        self.assertEqual(convert("0*120"), [0.0, 120.0, "*"])
        self.assertEqual(convert("0/5"), [0.0, 5.0, "/"])

        self.assertEqual(convert("0+0"), [0.0, 0.0, "+"])
        self.assertEqual(convert("0-0"), [0.0, 0.0, "-"])
        self.assertEqual(convert("0*0"), [0.0, 0.0, "*"])
        self.assertEqual(convert("0/0"), [0.0, 0.0, "/"])

    def test_convert_floats(self): 
        """Testing the convert function with floats as input
        """

        self.assertEqual(convert("5+0.5"), [5.0, 0.5, "+"])
        self.assertEqual(convert("5-0.5"), [5.0, 0.5, "-"])
        self.assertEqual(convert("5*0.5"), [5.0, 0.5, "*"])
        self.assertEqual(convert("120/0.5"), [120.0, 0.5, "/"])

        self.assertEqual(convert("0.5+120"), [0.5, 120.0, "+"])
        self.assertEqual(convert("0.5-120"), [0.5, 120.0, "-"])
        self.assertEqual(convert("0.5*120"), [0.5, 120.0, "*"])
        self.assertEqual(convert("0.5/5"), [0.5, 5.0, "/"])

        self.assertEqual(convert("0.5+0.1"), [0.5, 0.1, "+"])
        self.assertEqual(convert("0.5-0.1"), [0.5, 0.1, "-"])
        self.assertEqual(convert("0.5*0.1"), [0.5, 0.1, "*"])
        self.assertEqual(convert("0.5/0.1"), [0.5, 0.1, "/"])

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