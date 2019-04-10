import numpy as np
import pylab as pl
from scipy import integrate

t=np.arange(0,10.01,0.01)

fx=[]
intfx=[]

counter=0
for i in t:
    counter+=1
    fx.append(np.sin(i))
    intfx.append(fx[0]+integrate.trapz(fx[-2:], dx=0.1))
pl.plot(t,fx)
pl.plot(t,intfx)
pl.show()

#
