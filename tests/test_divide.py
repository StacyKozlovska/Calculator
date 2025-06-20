"""
File with tests for the divide method.
"""

from mysimplepycalc.calculator import Calculator
import random

test_cases = [1, -5, 0.003, -1000, 5230.0, -12839.9, -1.9, 1.0, 30.8, -3.14, 22, 69, 123.123]

def test_division():
    """
    Function to test divide method.
    """
    start_num = 0
    my_calc = Calculator(start_num=start_num)
    for i in range(20):
        num = random.choice(test_cases)
        start_num /= float(num)
        assert my_calc.divide(num) == start_num

    start_num_2 = 5
    my_calc_2 = Calculator(start_num=start_num_2)
    for i in range(20):
        num = random.choice(test_cases)
        start_num_2 /= float(num)
        assert my_calc_2.divide(num) == start_num_2

    my_calc.reset()
    my_calc_2.reset()
    assert my_calc.divide(1) == 0.0
    assert  my_calc_2.divide(4) == 0.0