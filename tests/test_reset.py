"""
File with tests for the reset method.
"""

from mysimplepycalc.calculator import Calculator

def test_reset():
    """
    Function to test reset method.
    """
    my_calc = Calculator(start_num=5)
    my_calc.reset()
    assert my_calc.active_value == 0.0

    my_calc.add(8)
    my_calc.multiply(-12)
    my_calc.reset()
    my_calc.add(1)
    assert my_calc.active_value == 1.0