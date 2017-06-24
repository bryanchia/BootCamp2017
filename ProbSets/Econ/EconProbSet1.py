#Solve for the steady state of 3 person OG model

#Exercise 5 

#Import libraries
import numpy as np
import scipy.optimize as opt

#Household parameters
'''
Sigma is a scalar >= 1, represents coefficient of relative risk aversion 
'''
nvec = np.array([1.0, 1.0, 0.2])
yrs_lived = 60
S = 3
beta_annual = 0.96
beta = beta_annual ** (yrs_lived / S)
#beta = 0.55
sigma = 3 

#Firm parameters
alpha = 0.35 #how much is allocated to capital owners in economy
A = 1
delta_annual = 0.05
delta = 1 - (1 - delta_annual) ** (yrs_lived / S) 
params = (A, alpha, delta)

#Solve eqn

#Define aobout 6 functions that the root finder will call 

#Market clearing conditions

L = np.sum(nvec)

#Firm's optimization problem

def getr(K, L, params):
    A, alpha, delta = params
    r = alpha * A * ((L / K) ** (1 - alpha)) - delta
    return r

def getw(K, L, params):
    A, alpha, delta = params
    w = (1 - alpha) * A * ((K / L) ** (alpha)) 
    return w

#Household's optimization problem

def getmuc1(b2b3vals, nvec, sigma, params, r, w):
    b2, b3 = b2b3vals
    K = sum(b2b3vals)
    ct1 = nvec[0] * w - b2 
    MUc1 = ct1 ** (-sigma)
    return MUc1

def getmuc2(b2b3vals, nvec, sigma, params, r, w):
    b2, b3 = b2b3vals
    K = np.sum(b2b3vals)
    ct2 = nvec[1] * w + (1 + r) * b2 - b3
    MUc2 = ct2 ** (-sigma)
    return MUc2

def getmuc3(b2b3vals, nvec, sigma, params, r, w):
    b2, b3 = b2b3vals
    K = np.sum(b2b3vals)
    ct3 = nvec[2] * w + (1 + r) * b3
    MUc3 = ct3 ** (-sigma)
    return MUc3

def errorcal(b2b3vals, args):
    beta, sigma, params, nvec = args
    b2, b3 = b2b3vals
    K = np.sum(b2b3vals)
    L = np.sum(nvec)
    r = getr(K, L, params)
    w = getw(K, L, params)
    MUc1 = getmuc1(b2b3vals, nvec, sigma, params, r, w)
    MUc2 = getmuc2(b2b3vals, nvec, sigma, params, r, w)
    MUc3 = getmuc3(b2b3vals, nvec, sigma, params, r, w)
    error1 = MUc1 - beta * (1 + r) * MUc2
    error2 = MUc2 - beta * (1 + r) * MUc3
    errors = np.array([error1, error2])
    return errors

b2_init = 0.02
b3_init = 0.02
b_init = np.array([b2_init, b3_init])
b_args = [beta, sigma, params, nvec]
b_result = opt.root(errorcal, b_init, args = b_args )

print(b_result)

#Calculations
K = sum(b_result.x)
r = getr(K, L, params)
w = getw(K, L, params)
b2 = b_result.x[0]
b3 = b_result.x[1]
ct1 = nvec[0] * w - b2
ct2 = nvec[1] * w + (1 + r) * b2 - b3
ct3 = nvec[2] * w + (1 + r) * b3
print("c1 = ",ct1)
print("c2 = ",ct2)
print("c3 = ",ct3)
print("r = ",r)
print("w = ",w)
print("b2 = ",b2)
print("b2 = ",b3)

'''
5a.

c1 =  0.182412558356
c2 =  0.209614907071
c3 =  0.240873817366
r =  2.43303025357
w =  0.201725293595
b2 =  0.0193127352389
b2 =  0.0584115908788

5b.

c1 =  0.195975352642
c2 =  0.228615593799
c3 =  0.266692158088
r =  1.88635999915
w =  0.22415231191
b2 =  0.028176959268
b2 =  0.0768655662396

If households become more patient, all the numbers would increase.
The numbers that have the greatest increase are the savings rates.
Saving rates would most evidently increase first when households are more patient.
As savings increase, this affects the capital, which in turn affects output.
An increase in output increases the steady state of consumption in the long run. 

TPI questions

print: distance: sum of squared errors, 
maximum of euler errors (shows that every person's equation is solved)

#TPI parameters


'''
