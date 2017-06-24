#Problem 1

class Backpack(object):

	def __init__ (self, name, color, max_size = 5):

		self.name = name
		self.contents = []
		self.color = color
		self.max_size = max_size

	def put(self, item):

		self.contents.append(item)

		if len(self.contents) > 5:
			self.contents = []
			print ("No Room!")

	def take(self, item):
		self.contents.remove(item)

	def dump(self):
		self.contents = []

####

#Problem 3

	def __eq__(self, other):

		return len(self.contents) == len (other.contents)\
		 and self.name == other.name \
		 and self.color == other.color

	def __str__(self):


		return "Owner:\t\t" + self.name + "\nColor:\t\t" + self.color + "\nSize:\t\t" + str(len(self.contents)) + "\nMax Size:\t" + str(self.max_size) + "\nContents:\t" + str(self.contents)

###
		
#Problem 2

class Jetpack(Backpack):

	def __init__(self, name, color, max_size = 2, fuel_size = 10):

	    Backpack.__init__(self, name, color, max_size)
	    self.fuel_size = fuel_size
	    self.fuel = 0

	def fly(self, fuel):

		self.fuel = fuel

		if self.fuel > self.fuel_size:
			print ("Not enough fuel!")

		else:
			self.fuel_size = self.fuel_size - self.fuel

	def dump(self):
		self.contents = []
		self.fuel_size = 0

###

##Problem 4

import math

class ComplexNumber(object):


	def __init__(self, real=0, imag=0):
		self.real = real
		self.imag = imag

	def conjugate(self):
		return ComplexNumber(self.real, -self.imag)

	def __abs__(self):
		return math.sqrt(self.real**2 + self.imag**2)

	def __lt__(self, other):
		selfmag = math.sqrt(self.real**2 + self.imag**2)
		othermag = math.sqrt(other.real**2 + other.imag**2)
		return selfmag < othermag

	def __gt__(self, other):
		selfmag = math.sqrt(self.real**2 + self.imag**2)
		othermag = math.sqrt(other.real**2 + other.imag**2)
		return selfmag > othermag

	def __eq__(self, other):
		return self.imag == other.imag and self.real == other.real

	def __ne__(self, other):
		return self.imag != other.imag or self.real != other.real

	def __add__(self, other):
		real = self.real + other.real
		imag = self.imag + other.imag
		return ComplexNumber(real, imag)

	def __sub__(self, other):
		real = self.real - other.real
		imag = self.imag - other.imag
		return ComplexNumber(real, imag)

	def __mul__(self, other):
		real = self.real*other.real - self.imag*other.imag
		imag = self.imag*other.real + other.imag*self.real
		return ComplexNumber(real, imag)

	def __truediv__(self, other):
		if other.real == 0 and other.imag == 0:
			raise ValueError("Cannot divide by zero")
		bottom = (other.conjugate()*other*1.).real
		top = self*other.conjugate()
		return ComplexNumber(top.real / bottom, top.imag / bottom)

	def __str__(self):
		return "{}{}{}i".format(self.real, '+' if self.imag >= 0 else '-', abs(self.imag))