
import numpy as np
import matplotlib.pyplot as plt
from numpy import linalg as LA

import sys, os
script_dir = os.path.dirname(__file__)
lib_relative = '../../coord'
sys.path.insert(0,os.path.join(script_dir, lib_relative))

#local imports 
from square.funsq import *

##set length of square
a= 10 

#get vertices
[O,A,B,C,M] = sq_vert(a)

##gen lines
X_OA = line_gen(O,A)
X_BA = line_gen(A,B)
X_BC = line_gen(B,C)
X_CO = line_gen(C,O)
X_D1 = line_gen(O,B)
X_D2 = line_gen(C,A)

#ploting lines
plt.plot(X_OA[0,:], X_OA[1,:])
plt.plot(X_BA[0,:], X_BA[1,:])
plt.plot(X_BC[0,:], X_BC[1,:])
plt.plot(X_CO[0,:], X_CO[1,:])
plt.plot(X_D1[0,:], X_D1[1,:])
plt.plot(X_D2[0,:], X_D2[1,:])

sq_coords = np.vstack((A,B,C,O,M)).T
plt.scatter(sq_coords[0,:], sq_coords[1,:])
vert_labels = ['A','B','C','O','M']
for i, txt in enumerate(vert_labels):
    plt.annotate(txt, # this is the text
                 (sq_coords[0,i], sq_coords[1,i]), # this is the point to label
                 textcoords="offset points", # how to position the text
                 xytext=(5,10), # distance from text to points (x,y)
                 ha='center') # horizontal alignment can be left, right or center

plt.xlabel('$x$')
plt.ylabel('$y$')
#plt.legend(loc='best')
plt.grid()
plt.axis('equal')
plt.savefig('../figs/sq_plot.png')
plt.show()

