
 #code by Manideep Parusha
 #September 17, 2022
 #functions related to circle
import numpy as np


#Generating points on a circle
def circ_gen(O,r):
	len = 50
	theta = np.linspace(0,2*np.pi,len)
	x_circ = np.zeros((2,len))
	x_circ[0,:] = r*np.cos(theta)
	x_circ[1,:] = r*np.sin(theta)
	x_circ = (x_circ.T + O).T
	return x_circ


#Generating points on a parabola
def parab_gen(y):
    a = 4
    x = (y**2)/a
    return x
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


#line gen dir
def line_dir_pt(m,A,k1,k2):
  len = 10
  dim = A.shape[0]
  x_AB = np.zeros((dim,len))
  lam_1 = np.linspace(k1,k2,len)
  for i in range(len):
    temp1 = A + lam_1[i]*m
    x_AB[:,i]= temp1.T
  return x_AB
