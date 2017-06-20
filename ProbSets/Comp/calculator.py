
# coding: utf-8

# In[8]:

#Creating the calculator module

def calcsum(A, B):
    finalsum = A + B
    return finalsum

def calcprod(A, B):
    finalprod = A * B
    return finalprod

def calcsqrt(A):
    from math import sqrt
    finalsqrt = sqrt(A)
    return finalsqrt

if __name__ =="__main__":
    print(calcsum(3,4))
    print(calcprod(5,6))
    print(calcsqrt(9))


# In[ ]:



