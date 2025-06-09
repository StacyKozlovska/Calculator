"""
Module with the class called Calculator
"""
from typing import Union

class Calculator:
    """
    This class has internal memory for the value we are working with
    until the reset method is called.
    Methods of this class are include:
    - add
    - subtract
    - multiply
    - divide
    - n-th root
    - reset
    """
    # Class attribute, active value we're working
    # with until reset method is called
    active_value = 0.0

    def __init__(self, start_num: Union[int, float] = active_value):
        """
        Inputs: start_num - set a starting number for future operations,
                            zero by default.
        """
        try:
            self.active_value = float(start_num)
        except TypeError:
            print(f"Your input value should be one integer or one float.")

    def add(self, num: Union[int, float]) -> float:
        """
        Function that performs addition. It takes
        the input number and adds it to the active value
        (the one we're working with until the reset method is called).

        Inputs: num - integer or float number.
        Outputs: Calculator.active_value - updated active value (float).

        Examples:
        >>> my_calc = Calculator()
        >>> my_calc.add(5)
        5.0
        >>> my_calc.add(-2)
        3.0
        >>> my_calc.add("22")
        Your input values should be integers or floats.
        """

        try:
            self.active_value += float(num)
            # print(Calculator.active_value)
            return self.active_value
        except (TypeError, ValueError):
            print(f"Your input value should be one integer or one float.")

    def subtract(self, num: Union[int, float]) -> float:
        """
        Function that performs subtraction. It takes
        the input number and subtracts it from the active value
        (the one we're working with until the reset method is called).

        Inputs: num - integer or float number.
        Outputs: Calculator.active_value - updated active value (float).

        Examples:
        >>> my_calc = Calculator()
        >>> my_calc.subtract(10)
        -10.0
        >>> my_calc.subtract(-2)
        -8.0
        >>> my_calc.subtract("140")
        Your input values should be integers or floats.
        """
        try:
            self.active_value -= float(num)
            # print(Calculator.active_value)
            return self.active_value
        except (TypeError, ValueError):
            print(f"Your input value should be one integer or one float.")

    def multiply(self, num: Union[int, float]) -> float:
        """
        Function that performs multiplication. It takes
        the input number and multiplies it by the active value
        (the one we're working with until the reset method is called).

        Inputs: num - integer or float number.
        Outputs: Calculator.active_value - updated active value (float).

        Examples:
        >>> my_calc = Calculator(start_num=1)
        >>> my_calc.multiply(5)
        5.0
        >>> my_calc.multiply(-3)
        -15.0
        >>> my_calc.multiply("77")
        Your input values should be integers or floats.
        """
        try:
            self.active_value *= float(num)
            # print(Calculator.active_value)
            return self.active_value
        except (TypeError, ValueError):
            print(f"Your input value should be one integer or one float.")

    def divide(self, num: Union[int, float]) -> float:
        """
        Function that performs division. It takes
        the input number and divides the active value
        (the one we're working with until the reset method is called)
        by that input number.

        Inputs: num - integer or float number.
        Outputs: Calculator.active_value - updated active value (float).

        Examples:
        >>> my_calc = Calculator(start_num=1)
        >>> my_calc.divide(5)
        0.2
        >>> my_calc.divide(-3)
        -0.06666666666666667
        >>> my_calc.divide("79")
        Your input values should be integers or floats.
        >>> my_calc.divide(0)
        You can't divide by zero.
        """
        try:
            self.active_value /= float(num)
            # print(Calculator.active_value)
            return self.active_value
        except (TypeError, ValueError):
            print("Your input value should be one integer or one float.")
        except ZeroDivisionError:
            print("You can't divide by zero.")

    def floor_divide(self, num: Union[int, float]) -> float:
        """
        Function that performs floor division. It takes
        the input number and divides the active value
        (the one we're working with until the reset method is called)
        by that input number and rounds down to the lower integer (still returned as float).

        Inputs: num - integer or float number.
        Outputs: Calculator.active_value - updated active value (float).

        Examples:
        >>> my_calc = Calculator(start_num=100)
        >>> my_calc.floor_divide(5.5)
        18.0
        >>> my_calc.floor_divide(-7)
        -3.0
        >>> my_calc.floor_divide("12")
        Your input values should be integers or floats.
        >>> my_calc.floor_divide(0)
        You can't divide by zero.
        """
        try:
            self.active_value = float(self.active_value // num)
            # print(Calculator.active_value)
            return self.active_value
        except (TypeError, ValueError):
            print(f"Your input value should be one integer or one float.")
        except ZeroDivisionError:
            print("You can't divide by zero.")

    def root(self, root: Union[int, float], num: Union[int, float, None] = None) -> float:
        """
        Function that performs n-th root calculation.
        It takes the input root number and, if no additional
        argument for num is specified (aka num is None), takes the root of
        the active_value (the one we're working with until the reset
        method is called). If additional argument for num is specified by
        the instance, then we take the root of that number and don't update
        the active_value, we just return the calculation with given arguments.

        Inputs: num - integer or float number.
        Outputs: Calculator.active_value - updated active value (float)
                 or
                 result - root calculation with given arguments (doesn't change
                          the active_value in class internal memory) (float)
        Examples:
        >>> my_calc = Calculator(start_num=100)
        >>> my_calc.floor_divide(5.5)
        18.0
        >>> my_calc.floor_divide(-7)
        -3.0
        >>> my_calc.floor_divide("12")
        Your input values should be integers or floats.
        >>> my_calc.floor_divide(0)
        You can't divide by zero.
        """

        try:
            root = round(float(root), 5)

            if num is None:
                self.active_value = round(self.active_value, 5)
                self.active_value = self.active_value ** (1.0 / root)
                # print(Calculator.active_value)
                return self.active_value
            else:
                num = round(num, 5)
                result = (float(num)) ** (1.0 / root)
                # print(result)
                return result
        except (TypeError, ValueError):
            print(f"Your input values should be integers or floats that are greater or equal to zero.")
        except ZeroDivisionError:
            print("You can't divide by zero / zero cannot be raised to a negative power.")
        except OverflowError:
            print("The result is too big to be represented.")



    def reset(self) -> float:
        """
        Function that clears the output and resets the active_value to zero.
        It also prints out the active value after the reset (should be zero).

        Inputs: no additional inputs,
        Outputs: Calculator.active_value - active value that is 0.0

        Examples:
        >>> my_calc = Calculator()
        >>> my_calc.add(5)
        5.0
        >>> my_calc.reset()
        You have reset the calculator, now the starting value is 0.0
        """
        try:
            self.active_value = 0.0
            # print (f"You have reset the calculator, now the starting value is {Calculator.active_value}")
            # return Calculator.active_value
            return f"You have reset the calculator, now the starting value is {self.active_value}"
        except (TypeError, ValueError):
            print ("Sorry, there should be no arguments given.")

    def __repr__(self):
        """
        Function to represent the class description.
        """
        return f"Calculator's active value is {self.active_value}"


