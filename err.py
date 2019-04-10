import numpy as np
import matplotlib.pyplot as plt
a =np.loadtxt('cont.dat')
b=a[:,0]
c=a[:,1]
d=a[:,2]
plt.plot(b,c)
plt.errorbar(x,y,yerr=d)
cerr=d
plt.errorbar(b,c,yerr=cerr)
plt.show()

