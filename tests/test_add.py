"""
File with tests for add method
"""

from mysimplepycalc.calculator import Calculator
import random

test_cases = [1, -5, 0.003, -1000, 5230.0, -12839.9, -1.9, 1.0, 30.8, -3.14, 22, 69, 123.123]

def test_addition():
    """
    Function to test add method.
    """
    start_num = 3
    my_calc = Calculator(start_num=start_num)

    for i in range(20):
        num = random.choice(test_cases)
        start_num += float(num)
        assert my_calc.add(num) == start_num

    my_calc.reset()
    assert my_calc.add(1) == 1.0