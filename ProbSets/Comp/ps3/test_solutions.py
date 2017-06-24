# test_solutions.py
"""Volume 1B: Testing.
<Name>
<Class>
<Date>
"""

import solutions as soln
import pytest
import math

# Problem 1: Test the addition and fibonacci functions from solutions.py
def test_addition():
    assert soln.addition(1,3) == 4, "Addition failed on positive integers"
    assert soln.addition(-5,-7) == -12, "Addition failed on negative integers"
    assert soln.addition(-6,14) == 8, "Addition failed on a negative and positive integer"

def test_smallest_factor():
    assert soln.smallest_factor(1) == 1, "Failed on 1"
    assert soln.smallest_factor(8) == 2, "Failed on number with smallest prime factor neq to itself"
    assert soln.smallest_factor(17) == 17, "Failed on number where smallest prime factor is eq to itself"

# Problem 2: Test the operator function from solutions.py
def test_operator():

    with pytest.raises(Exception) as excinfo:
        soln.operator(1, 1, 1)
    assert excinfo.typename == 'ValueError'
    assert excinfo.value.args[0] == "Oper should be a string"

    with pytest.raises(Exception) as excinfo:
        soln.operator(1, 1, "+-")
    assert excinfo.typename == 'ValueError'
    assert excinfo.value.args[0] == "Oper should be one character"

    assert soln.operator(1, 1, "+") == 2, "Failed on addition"
    assert soln.operator(4, 2, "/") == 2, "Failed on division"

    with pytest.raises(Exception) as excinfo:
        soln.operator(5, 0, "/")
    assert excinfo.typename == 'ValueError'
    assert excinfo.value.args[0] == "You can't divide by zero!"   

    assert soln.operator(1, 1, "-") == 0, "Failed on subtraction"
    assert soln.operator(4, 2, "*") == 8, "Failed on multiplication"

    with pytest.raises(Exception) as excinfo:
        soln.operator(1, 1, "$")
    assert excinfo.typename == 'ValueError'
    assert excinfo.value.args[0] == "Oper can only be: '+', '/', '-', or '*'"     
    
# Problem 3: Finish testing the complex number class
@pytest.fixture
def set_up_complex_nums():
    number_1 = soln.ComplexNumber(1, 2)
    number_2 = soln.ComplexNumber(5, 5)
    number_3 = soln.ComplexNumber(2, 9)
    number_4 = soln.ComplexNumber(0, 0)
    number_5 = soln.ComplexNumber(1, 2)
    return number_1, number_2, number_3, number_4, number_5

def test_complex_addition(set_up_complex_nums):
    number_1, number_2, number_3, number_4, number_5 = set_up_complex_nums #What the heck is this line doing?
    assert number_1 + number_2 == soln.ComplexNumber(6, 7)
    assert number_1 + number_3 == soln.ComplexNumber(3, 11)
    assert number_2 + number_3 == soln.ComplexNumber(7, 14)
    assert number_3 + number_3 == soln.ComplexNumber(4, 18)

def test_complex_multiplication(set_up_complex_nums):
    number_1, number_2, number_3, number_4, number_5 = set_up_complex_nums
    assert number_1 * number_2 == soln.ComplexNumber(-5, 15)
    assert number_1 * number_3 == soln.ComplexNumber(-16, 13)
    assert number_2 * number_3 == soln.ComplexNumber(-35, 55)
    assert number_3 * number_3 == soln.ComplexNumber(-77, 36)

def test_complex_subtraction(set_up_complex_nums):
    number_1, number_2, number_3, number_4, number_5 = set_up_complex_nums
    assert number_1 - number_2 == soln.ComplexNumber(-4, -3)
    assert number_1 - number_3 == soln.ComplexNumber(-1, -7)
    #assert number_2 - number_3 == soln.ComplexNumber(-35, 55)
    #assert number_3 - number_3 == soln.ComplexNumber(-77, 36)

def test_complex_division(set_up_complex_nums):
    number_1, number_2, number_3, number_4, number_5 = set_up_complex_nums
    assert number_1 / number_2 == soln.ComplexNumber(3/10, 1/10)
    assert number_1 / number_3 == soln.ComplexNumber(4/17, -1/17)
    #assert number_2 - number_3 == soln.ComplexNumber(-35, 55)
    #assert number_3 - number_3 == soln.ComplexNumber(-77, 36)

    with pytest.raises(Exception) as excinfo:
        number_1 / number_4
    assert excinfo.typename == 'ValueError'
    assert excinfo.value.args[0] == "Cannot divide by zero"

def test_complex_equal(set_up_complex_nums):
    number_1, number_2, number_3, number_4, number_5 = set_up_complex_nums
    assert number_1 == number_5
    assert number_1 != number_2

def test_complex_string(set_up_complex_nums):
    number_1, number_2, number_3, number_4, number_5 = set_up_complex_nums
    assert str(number_1) == "1+2i"

def test_complex_conjugate(set_up_complex_nums):
    number_1, number_2, number_3, number_4, number_5 = set_up_complex_nums
    assert soln.ComplexNumber.conjugate(number_1) == soln.ComplexNumber(1, -2)

def test_complex_(set_up_complex_nums):
    number_1, number_2, number_3, number_4, number_5 = set_up_complex_nums
    assert soln.ComplexNumber.norm(number_1) == math.sqrt(5)

# Problem 4: Write test cases for the Set game.

def test_file():

    with pytest.raises(Exception) as excinfo:
        soln.set("randomfile")
    assert excinfo.typename == 'UnboundLocalError'

def test_enoughcards():
   
    with pytest.raises(Exception) as excinfo:
        soln.set("fewcards")
    assert excinfo.typename == 'ValueError'
    assert excinfo.value.args[0] == "There are not enough cards" 

def test_invalid():

    with pytest.raises(Exception) as excinfo:
        soln.set("invalidcards")
    assert excinfo.typename == 'ValueError'
    assert excinfo.value.args[0] == "There is an invalid card"

    with pytest.raises(Exception) as excinfo:
        soln.set("invalidnumbers")
    assert excinfo.typename == 'ValueError'
    assert excinfo.value.args[0] == "There is an invalid number"       

def test_duplicate():

    with pytest.raises(Exception) as excinfo:
        soln.set("duplicatecards")
    assert excinfo.typename == 'ValueError'
    assert excinfo.value.args[0] == "There are duplicate cards"   

def test_function():
    assert soln.set("case1") == 6
