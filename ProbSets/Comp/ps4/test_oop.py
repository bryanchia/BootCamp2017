#Problem 1

def test_backpack():

	from oop import Backpack 
	testpack = Backpack("Barry", "black")

	if testpack.max_size != 5:
		print("Wrong default max_size!")

	for item in ["pencil", "pen", "paper", "computer"]:
		testpack.put(item)
	print(testpack.name, testpack.contents)

	badpack = Backpack("Fred", "green")

	for item in ["pencil", "pen", "paper", "computer","eraser","bottle"]:
		badpack.put(item)
	print(badpack.name, badpack.contents)

	testpack.dump()
	print(testpack.contents)

	return

test_backpack()

#Problem 2

def test_jetpack():

	from oop import Jetpack 
	testpack2 = Jetpack("Lance", "white")
	print(testpack2.name, testpack2.fuel_size)
	print(testpack2.color)

	testpack2.fly(12)

	testpack3 = Jetpack("Willis", "white")
	testpack3.fly(6)
	print(testpack3.name, testpack3.fuel_size)

	testpack4 = Jetpack("Bryan", "white")
	testpack4.dump()
	print(testpack4.name, testpack4.fuel_size)

test_jetpack()

#Problem 3 

def test_prob3():

	from oop import Backpack

	testpack5 = Backpack("Barry", "black")
	for item in ["pencil", "pen"]:
		testpack5.put(item)

	testpack6 = Backpack("Barry", "black")
	for item in ["pencil", "pen"]:
		testpack6.put(item)

	print(testpack5 == testpack6)

	testpack7 = Backpack("Barry", "black")
	for item in ["pencil", "pen", "bottle"]:
		testpack7.put(item)

	print(testpack5 == testpack7)

	testpack8 = Backpack("Bryan", "black")
	for item in ["pencil", "pen"]:
		testpack8.put(item)

	print(testpack5 == testpack8)

	testpack9 = Backpack("Bryan", "white")
	for item in ["pencil", "pen"]:
		testpack9.put(item)

	print(testpack8 == testpack9)

	print(testpack8)

test_prob3()

#Problem 4
import oop as soln
import pytest
import math

@pytest.fixture
def set_up_complex_nums():
	number_1 = soln.ComplexNumber(1, 2)
	number_2 = soln.ComplexNumber(5, 5)
	number_3 = soln.ComplexNumber(2, 9)
	number_4 = soln.ComplexNumber(0, 0)
	number_5 = soln.ComplexNumber(1, 2)
	return number_1, number_2, number_3, number_4, number_5

def test_complex_conjugate(set_up_complex_nums):
	number_1, number_2, number_3, number_4, number_5 = set_up_complex_nums
	assert abs(number_1) == math.sqrt(1**2 + 2**2)

def test_complex_addition(set_up_complex_nums):
	number_1, number_2, number_3, number_4, number_5 = set_up_complex_nums 
	assert number_1 + number_3 == soln.ComplexNumber(3, 11)

def test_complex_multiplication(set_up_complex_nums):
	number_1, number_2, number_3, number_4, number_5 = set_up_complex_nums
	assert number_1 * number_2 == soln.ComplexNumber(-5, 15)
	assert number_1 * number_3 == soln.ComplexNumber(-16, 13)

def test_complex_subtraction(set_up_complex_nums):
	number_1, number_2, number_3, number_4, number_5 = set_up_complex_nums
	assert number_1 - number_2 == soln.ComplexNumber(-4, -3)
	assert number_1 - number_3 == soln.ComplexNumber(-1, -7)

def test_complex_division(set_up_complex_nums):
	number_1, number_2, number_3, number_4, number_5 = set_up_complex_nums
	assert number_1 / number_2 == soln.ComplexNumber(3/10, 1/10)
	assert number_1 / number_3 == soln.ComplexNumber(4/17, -1/17)

#Part (a) test norms

print (abs(soln.ComplexNumber(1, 2)))

#Part (b) test leq and geq

print(soln.ComplexNumber(1, 2) < soln.ComplexNumber(5, 5))
print(soln.ComplexNumber(6, 6) < soln.ComplexNumber(5, 5))

print(soln.ComplexNumber(1, 2) > soln.ComplexNumber(5, 5))
print(soln.ComplexNumber(6, 6) > soln.ComplexNumber(5, 5))

#Part (c) test eq and neq

print(soln.ComplexNumber(1, 2) == soln.ComplexNumber(1, 2))
print(soln.ComplexNumber(6, 6) == soln.ComplexNumber(5, 5))

print(soln.ComplexNumber(1, 2) != soln.ComplexNumber(5, 5))
print(soln.ComplexNumber(5, 5) != soln.ComplexNumber(5, 5))

#Part (d) test add, multiply, subtract, divide above!
