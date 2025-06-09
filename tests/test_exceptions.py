"""
File with tests for the exceptions and error raises.
"""

from mysimplepycalc.calculator import Calculator
import pytest

test_cases = [1, -5, 0.003, -1000, 5230.0, -12839.9, -1.9, 1.0, 30.8, -3.14, 22, 69, 123.123]


@pytest.mark.xfail(raises=Exception)
def test_exceptions_and_raises():
    my_calc = Calculator()

    my_calc.add("hello")

    my_calc.subtract("654")

    my_calc.multiply(Calculator())
    my_calc.multiply("90")

    my_calc.divide(0)
    my_calc.divide("123")

    my_calc.floor_divide("234")
    my_calc.floor_divide(0)

    my_calc.root("23", 23)
    my_calc.root(my_calc, 23.02)
    my_calc.root(-4)

    with pytest.raises(TypeError):
        my_calc.reset("239")
        my_calc.subtract(92, "ind")
        my_calc.add(24.9, 13)
        my_calc.divide(839, 239)
        my_calc.floor_divide("923", "hello")

