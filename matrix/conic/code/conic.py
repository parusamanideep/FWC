import numpy as np
import matplotlib.pyplot as plt
from numpy import linalg as LA

import sys, os
script_dir = os.path.dirname(__file__)
lib_relative = '../../coord/conic'
sys.path.insert(0,os.path.join(script_dir, lib_relative))

#local imports
from funcon import *

# set center of the circle
C = np.array((2,2))
#circle pass through the point (4,5)
A = np.array((4,5))
#radius of the circle
r = LA.norm(A-C)

#generate circle
x_circ = circ_gen(C,r)

#plot circle
plt.plot(x_circ[0,:],x_circ[1,:],label= '$Circle$')

#label coordinates

cir_coords = np.vstack((A,C)).T
plt.scatter(cir_coords[0,:], cir_coords[1,:])
vert_labels = ['A','C']

for i, txt in enumerate(vert_labels):
    plt.annotate(txt, # this is the text
                 (cir_coords[0,i], cir_coords[1,i]), # this is the point to label
                 textcoords="offset points", # how to position the text
                 xytext=(5,10), # distance from text to points (x,y)
                 ha='center') # horizontal alignment can be left, right or center

plt.xlabel('$x$')
plt.ylabel('$y$')
plt.grid()
plt.axis('equal')

plt.savefig('../figs/plot_con.png')





