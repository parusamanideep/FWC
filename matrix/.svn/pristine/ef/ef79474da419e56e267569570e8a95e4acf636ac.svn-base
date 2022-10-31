 #code by Manideep Parusha
 #September 17, 2022
 #functions related to square
import numpy as np
 


#Square vertices
def sq_vert(a):
    p = a
    O = np.array([0,0])
    A = np.array([p,0])
    C = np.array([p,p])
    B = np.array([0,p])
    M = np.array([p/2,p/2])
    return O,A,B,C,M

#line gen
def line_gen(K,L):
    len = 10
    dim = K.shape[0]
    x_KL = np.zeros((dim,len))
    lam_1 = np.linspace(0,1,len)
    for i in range(len):
        temp1 = K + lam_1[i]*(L-K)
        x_KL[:,i] = temp1.T
    return x_KL



