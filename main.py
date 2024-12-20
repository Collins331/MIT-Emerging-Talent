import unittest


def add(num1: float, num2: float) -> float:
    """
    This function adds two numbers together.
    args:
        num1, num2
    returns:
        sum of num1 and num2
    """
    return num1 + num2


def sub(num1: float, num2: float) -> float:
    """
    This function subtracts num2 from num1.
    args:
        num1, num2
    returns:
        difference of num1 and num2
    """
    return num1 - num2


def mul(num1: float, num2: float) -> float:
    """
    This function multiplies two numbers together.
    args:
        num1, num2
    returns:
        product of num1 and num2
    """
    return num1 * num2


def div(num1: float, num2: float) -> float:
    """
    This function divides num1 by num2.
    args:
        num1, num2
    returns:
        quotient of num1 and num2
    """
    if num2 == 0:
        raise ValueError("Cannot divide by zero")
    return num1 / num2



class TestCalculator(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(5, 3), 8)
        self.assertEqual(add(-5, 3), -2)
        self.assertEqual(add(5, -3), 2)
        
    def test_sub(self):
        self.assertEqual(sub(5, 3), 2)
        self.assertEqual(sub(-5, 3), -8)
        self.assertEqual(sub(5, -3), 8)
        
    def test_mul(self):
        self.assertEqual(mul(5, 3), 15)
        self.assertEqual(mul(-5, 3), -15)
        self.assertEqual(mul(5, -3), -15)
        
    def test_div(self):
        self.assertEqual(div(5, 3), 1.6666666666666667)
        self.assertEqual(div(-5, 3), -1.6666666666666667)
        self.assertEqual(div(5, -3), -1.6666666666666667)
        
        
        
if __name__ == "__main__":
    unittest.main()  # pragma: no cover