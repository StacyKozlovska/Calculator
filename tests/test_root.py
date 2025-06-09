"""
File with tests for the root method.
"""

from mysimplepycalc.calculator import Calculator
import random
import cmath

test_cases = [1, -5, 0.003, -1000, 5230.0, -12839.9, -1.9, 1.0, 30.8, -3.14, 22, 69, 123.123, 0]

def test_root():
    """
    Function to test root method.
    """
    try:
        start_num = 2
        my_calc = Calculator(start_num=start_num)
        for i in range(10):
            root = round(random.choice(test_cases), 5)
            assert cmath.isclose(my_calc.root(root), start_num**(1.0/root), abs_tol=0.0001)
            start_num = start_num**(1.0/root)

        my_calc_2 = Calculator()
        for i in range(10):
            num = round(random.choice(test_cases), 5)
            root = round(random.choice(test_cases), 5)
            assert cmath.isclose(my_calc_2.root(root=root, num=num), (float(num))**(1.0/root), abs_tol=0.0001)

        my_calc.reset()
        my_calc_2.reset()
        assert my_calc.root(1, 5) == 5.0
        assert my_calc_2.root(4) == 0.0

    # needed for the result calculated inside tests out of random numbers (without using any methods)
    except ZeroDivisionError:
        print("You can't divide by zero / zero cannot be raised to a negative power.")