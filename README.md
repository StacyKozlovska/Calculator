# Python Calculator Package

## This package allows you to perform basic mathematical operations by using the class Calculator and its methods.

The main package contains a class Calculator that is able to perform these actions:

- Addition 
- Subtraction
- Multiplication 
- Division
- Floor division
- Take (n) root of a number
- Reset memory (Calculator has its own memory, meaning it manipulates its starting number 0 until it is reset).
___________________________________________________________________
### Methods available in the package:

- Calculator.add(num)
- Calculator.subtract(num)
- Calculator.multiply(num)
- Calculator.divide(num)
- Calculator.floor_divide(num)
- Calculator.root(root, num)
- Calculator.reset()
___________________________________________________________________
## How to use the package
___________________________________________________________________
### Installation:
- Create a virtual environment and install the package from TestPyPI:
```
pip install -i https://test.pypi.org/simple/ mysimplepycalc==0.0.3
```
- Import the package:
```
from mysimplepycalc import Calculator
```
- Create the Calculator object:
```
my_calculator = Calculator()
```
or
```
my_calculator = Calculator(start_num = 1)
```
*start_num is zero by default, if you need to start counting from another number, specify it when 
creating the instance.

___________________________________________________________________


### Overview of the methods:
- **.add(num)** 
  - Function that performs addition. It takes the input number (integer or float) and 
     adds it to the active value (the one we're working with until the reset method is called). 
     Output is a float number.
- **.subtract(num)**
  - Function that performs subtraction. It takes
    the input number (integer or float) and subtracts it from the active value
    (the one we're working with until the reset method is called). 
     Output is a float number.
- **.multiply(num)**
  - Function that performs multiplication. It takes
    the input number (integer or float) and multiplies it by the active value
    (the one we're working with until the reset method is called).
     Output is a float number.
- **.divide(num)**
  - Function that performs division. It takes
    the input number (integer or float) and divides the active value
    (the one we're working with until the reset method is called)
     by that input number. Output is a float number. 
- **.floor_divide(num)**
  - Function that performs floor division. It takes
    the input number (integer or float) and divides the active value
    (the one we're working with until the reset method is called)
    by that input number and rounds down to the lower integer (still returned as float).
- **.root(root, num)**
  - Function that performs n-th root calculation of a number.
    Argument {num} is optional.
    It takes the input root number (integer or float) and, if no additional
    argument for num is specified (aka num is None), takes the root of
    the active_value (the one we're working with until the reset
    method is called). If additional argument for num (integer or float) is specified by
    the instance, then we take the root of that number and don't update
    the active_value, we just return the calculation with given arguments.
- **reset()**
  - Function that clears the output and resets the active_value to zero.
    It also prints out the active value after the reset (should be zero).
___________________________________________________________________
### Limitations:
- You need to create an instance(object) of the Calculator to use all the methods.

- The methods for with integer and floats. If you give other data types, the exception for the type error will be raised.

- If you try to divide by zero (Calculator.divide(0)), exception for ZeroDivisionError will be raised.

- In method .root(), if you get a result that will be too big to be represented,
   you will get the exception for OverflowError.

- If you provide more arguments than needed, the exception for the value error will be raised.

___________________________________________________________________
## Code examples (copy-pastable)

```python  
pip install -i https://test.pypi.org/simple/ mysimplepycalc==0.0.3

from mysimplepycalc import Calculator
```
```
my_calculator = Calculator()
my_calculator.add(15)
``` 
15.0
```
my_calculator.multiply(2)
``` 
30.0
``` 
my_calculator.divide(2)
``` 
15.0
```
my_calculator.subtract(3)
``` 
12.0
```
my_calculator.floor_divide(5)
``` 
2.0
```
my_calculator.root(8)
``` 
1.090507
```
#doesn't change the active value in the calculator memory:

my_calculator.root(5, 12)  
 ``` 
1.643751
```
my_calculator.reset()
``` 
You have reset the calculator, now the starting value is 0.0
```
my_calculator.active_value
``` 
0.0
```
#Example with specified start value:
 
my_calc_2 = Calculator(start_num=2) 
my_calc_2.add(15)
``` 
17.0

________________________________________________________________________________
# Links:

- Link to the package: https://test.pypi.org/project/mysimplepycalc/0.0.3/
