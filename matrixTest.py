from numpy import *
import numpy as np
windowWidth = 10                      # width of the window displaying the curve
#Xm = linspace(0,0,windowWidth)
Xm=np.array([1,2,3,4,5,6,7,8,9])
ptr=Xm[:-1]
ptr2=Xm[1:]
ptr3=Xm[-1]
print(ptr)
print(ptr2)
print(ptr3)