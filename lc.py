import numpy as np, matplotlib.pyplot as pl
a,b,c,=np.genfromtxt('continuum.txt',unpack=True)
pl.plot(a,b,'ro')
pl.errorbar(a,b,yerr=c,capsize=5)
pl.show()

d,e,f,=np.genfromtxt('hb.txt',unpack=True)
pl.plot(d,e,'ro')
pl.errorbar(d,e,yerr=f,capsize=5)
pl.show()

