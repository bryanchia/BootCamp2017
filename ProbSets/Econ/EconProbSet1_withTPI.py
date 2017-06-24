#Solve for the steady state of 3 person OG model

#Exercise 5 a, b

#Import libraries
import numpy as np
import scipy.optimize as opt
import matplotlib.pyplot as plt

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
Kbar = sum(b_result.x)
rbar = getr(Kbar, L, params)
wbar = getw(Kbar, L, params)
b2bar = b_result.x[0]
b3bar = b_result.x[1]
ct1bar = nvec[0] * wbar - b2bar
ct2bar = nvec[1] * wbar + (1 + rbar) * b2bar - b3bar
ct3bar = nvec[2] * wbar + (1 + rbar) * b3bar
print("c1 = ",ct1bar)
print("c2 = ",ct2bar)
print("c3 = ",ct3bar)
print("r = ",rbar)
print("w = ",wbar)
print("b2 = ",b2bar)
print("b2 = ",b3bar)

'''
#5.1

c1 =  0.182412558356
c2 =  0.209614907071
c3 =  0.240873817366
r =  2.43303025357
w =  0.201725293595
b2 =  0.0193127352389
b2 =  0.0584115908788

#5.2

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
'''
#5.3 

#TPI Paramters
T = 20
b_t1 = np.array([0.8 * b2bar, 1.1 * b3bar])
epsilon = 1e-9
K1_1 = np.sum(b_t1)
epscheck = False
xi = 0.5
counter = 1

#Function: Calculate linear function in between K1 and Kbar

def getline(T, K1_1, Kbar):
    points = [(1,K1_1),(T,Kbar)]
    T_coords, K_coords = zip(*points)
    A = np.vstack([T_coords,np.ones(len(T_coords))]).T
    m, c = np.linalg.lstsq(A, K_coords)[0]
    linevec = (m, c)
    return linevec

#Function that gives us the first Kvec_1 by a linear function

def getKvec_1(linevec, T):
    m, c = linevec
    Kvec_1 = np.zeros((T, 1))
    for i in range (0, T):
        Kvec_1[i] = (m * (i+1)) + c 
    return Kvec_1

def getrvec(Kvec, T, L, params):
    rvec = np.zeros((T, 1))
    for j in range (0, T):
        rvec[j] = getr(Kvec[j], L, params)
    return rvec

def getwvec(Kvec, T, L, params):
    wvec = np.zeros((T, 1))
    for k in range (0, T):
        wvec[k] = getw(Kvec[k], L, params)
    return wvec

def getmuc1_tpi(b2b3vals, nvec, sigma, params, w1):
    b2, b3 = b2b3vals
    ct1 = nvec[0] * w1 - b2 
    MUc1 = ct1 ** (-sigma)
    return MUc1

def getmuc2_tpi(b2b3vals, nvec, sigma, params, r2, w2):
    b2, b3 = b2b3vals
    ct2 = nvec[1] * w2 + (1 + r2) * b2 - b3
    MUc2 = ct2 ** (-sigma)
    return MUc2

def getmuc3_tpi(b2b3vals, nvec, sigma, params, r3, w3):
    b2, b3 = b2b3vals
    ct3 = nvec[2] * w3 + (1 + r3) * b3
    MUc3 = ct3 ** (-sigma)
    return MUc3

def tpi_uni_errorcal(b32, args):
    beta, sigma, params, nvec, b21, rvec, wvec = args
    r1 = rvec[0]
    r2 = rvec[1]
    w1 = wvec[0]
    w2 = wvec[1]
    b2b3vals = (b21, b32)
    MUc2 = getmuc2_tpi(b2b3vals, nvec, sigma, params, r1, w1)
    MUc3 = getmuc3_tpi(b2b3vals, nvec, sigma, params, r2, w2)
    error = MUc2 - beta * (1 + r2) * MUc3
    return error

def tpi_errorcal(b2b3vals, args):
    beta, sigma, params, nvec, rvec_trio, wvec_trio  = args
    b2, b3 = b2b3vals
    w1 = wvec_trio[0]
    w2 = wvec_trio[1]
    w3 = wvec_trio[2]
    r2 = rvec_trio[1]
    r3 = rvec_trio[2]
    MUc1 = getmuc1_tpi(b2b3vals, nvec, sigma, params, w1)
    MUc2 = getmuc2_tpi(b2b3vals, nvec, sigma, params, r2, w2)
    MUc3 = getmuc3_tpi(b2b3vals, nvec, sigma, params, r3, w3)
    error1 = MUc1 - beta * (1 + r2) * MUc2
    error2 = MUc2 - beta * (1 + r3) * MUc3
    errors = np.array([error1, error2])
    return errors

#Calculate linear function in between K1 and Kbar
linevec = getline(T, K1_1, Kbar)

#Get K_1 vector
Kvec = getKvec_1(linevec, T) 

while (epscheck == False):

    #Get r and w vectors given our assumed transition path
    rvec = getrvec(Kvec, T, L, params)
    wvec = getwvec(Kvec, T, L, params)

    #Solve for first period middle aged guy's old savings in 2nd period
    b32_init = 0.02
    b21 = b_t1[0]
    b_args_tpi_uni = [beta, sigma, params, nvec, b21, rvec, wvec]
    b_result_tpi_uni = opt.root(tpi_uni_errorcal, b32_init, args = b_args_tpi_uni )

    b32 = b_result_tpi_uni.x[0]

    #Iterate to solve for each individual's savings decisions

    rvec0 = np.append(rvec,np.array([rvec[T-1]]))
    rvec1 = np.append(rvec0,np.array([rvec[T-1]]))
    wvec0 = np.append(wvec,np.array([wvec[T-1]]))
    wvec1 = np.append(wvec0,np.array([wvec[T-1]]))
    
    K_prime = np.zeros((T, 1))
    b2t = np.zeros((T, 1))
    b3t = np.zeros((T, 1))

    b2t[0] = b21

    b3t[0] = b_t1[1]
    b3t[1] = b32
    
    for t in range(0, T): 
        rvec_trio = np.array([rvec1[t], rvec1[t+1],rvec1[t+2]])
        wvec_trio = np.array([wvec1[t], wvec1[t+1],wvec1[t+2]])
        b2init_tpi = 0.02
        b3init_tpi = 0.02
        b_init_tpi = np.array([b2init_tpi, b3init_tpi])
        b_args_tpi = [beta, sigma, params, nvec, rvec_trio, wvec_trio]
        b_result_tpi = opt.root(tpi_errorcal, b_init, args = b_args_tpi )
    
        #Create for our K_prime vector given each savings vector
        if t < (T - 1):
            b2t[t+1] = b_result_tpi.x[0]

        if t < (T - 2):
            b3t[t+2] = b_result_tpi.x[1]

        K_prime = b2t + b3t

    #Calculate the norm of K_prime - Kvec 

    norm = np.linalg.norm(K_prime - Kvec)

    print("Iteration No. " + str(counter) + ": "\
     + "Difference = " + str(norm))

    counter += 1

    #Check to see if the norm is less than the tolerance level
    #Return true if so 

    if norm < epsilon:
        print (b_result_tpi)
        epscheck = True 

    else:

        #Else, get a new K vector if necessary
        #Passing in xi, this gives a new K that is a convex combination K_prime and K_1 

        Kvec = xi * K_prime + (1 - xi) * Kvec

# 5.4 Plot K values 

timevec = np.arange(1, T+6).reshape(T+5,1)

Kvec_stable = np.zeros(((5, 1)))

for k in range(0, 5):
    Kvec_stable [k] = np.array([Kvec[T-1]])

Kvec_final = np.vstack((Kvec, Kvec_stable))
plot = np.hstack((timevec, Kvec_final))

t, k = plot.T
plt.scatter(t,k)
plt.title('Time path of aggregate K', fontsize=15)
plt.xlabel(r't')
plt.ylabel(r'K')
plt.ylim([0.075, 0.08]) 
plt.show()

for e in range (1, T):
    if abs(Kvec[e] - Kvec_stable [0]) >= 0.0001:
        e+=1
    else:
        print (e)

#It took 6 periods. 
