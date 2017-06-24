# solutions.py
"""Volume IB: Testing.
<Name>
<Date>
"""
import math
import os

# Problem 1 Write unit tests for addition().
# Be sure to install pytest-cov in order to see your code coverage change.


def addition(a, b):
    return a + b


def smallest_factor(n):
    """Finds the smallest prime factor of a number.
    Assume n is a positive integer.
    """
    if n == 1:
        return 1
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return i
    return n


# Problem 2 Write unit tests for operator().
def operator(a, b, oper):
    if type(oper) != str:
        raise ValueError("Oper should be a string")
    if len(oper) != 1:
        raise ValueError("Oper should be one character")
    if oper == "+":
        return a + b
    if oper == "/":
        if b == 0:
            raise ValueError("You can't divide by zero!")
        return a/float(b)
    if oper == "-":
        return a-b
    if oper == "*":
        return a*b
    else:
        raise ValueError("Oper can only be: '+', '/', '-', or '*'")

# Problem 3 Write unit test for this class.
class ComplexNumber(object):
    def __init__(self, real=0, imag=0):
        self.real = real
        self.imag = imag

    def conjugate(self):
        return ComplexNumber(self.real, -self.imag)

    def norm(self):
        return math.sqrt(self.real**2 + self.imag**2)

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

    def __eq__(self, other):
        return self.imag == other.imag and self.real == other.real

    def __str__(self):
        return "{}{}{}i".format(self.real, '+' if self.imag >= 0 else '-',
                                                                abs(self.imag))

# Problem 5: Write code for the Set game here

def set(filename):
    

    #read files
    #make sure that filename is valid 
    
    try:
        file = filename + ".txt"
        with open(file, "r") as infile:
            hand = infile.read().splitlines()
    except FileNotFoundError:
        pass
    #make sure that there are the right number of cards

    if len(hand) != 12:
        raise ValueError("There are not enough cards")

    #make sure that cards are valid

    for i in range (0,len(hand)):
        card = hand[i]
        if len(card) != 4:
            raise ValueError("There is an invalid card")

        for j in range (0,len(card)):
            card_int = int(card[j])
            if card_int > 2 :
                raise ValueError("There is an invalid number")           

    #make sure that there are no duplicate cards

    for k in range (0, len(hand)):
        card_check = hand[k]

        for l in range (k + 1, len(hand)):
            if card_check == hand[l]:
                raise ValueError("There are duplicate cards")
    
    #run program to check for number of sets 

    #myarray = []
    goodsets = 0

    for m in range (0, len(hand)):
        card1 = hand[m]

        for n in range (m + 1, len(hand)):
            card2 = hand[n]

            for o in range (n + 1, len(hand)):
                card3 = hand[o]

                goodlist = 0

                for p in range (0 , len(card1)):
                    digit1 = int(card1[p])
                    digit2 = int(card2[p])
                    digit3 = int(card3[p])

                    if (digit1 + digit2 + digit3) % 3 == 0:
                        goodlist += 1 

                    if goodlist == 4:
                        goodsets += 1

                #myarray.append([card1, card2, card3])
    
    print(goodsets)
    return goodsets

    
