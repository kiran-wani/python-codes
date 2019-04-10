import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import quad
z=np.arange(0,5.1,0.1)
h=0.7
omega0=[1,0.05,0.2]
omegal=[0.0,0.0,0.8]
omegak=[0.0,0.95,0.0]
dce=dcdhe=dmdhe=dadhe=np.zeros(51)
dcl=dcdhl=dmdhl=dadhl=dcdhl=np.zeros(51)
dch=dcdhh=dmdhh=dadhh=np.zeros(51)
#np.zeros(51)

#the epeeble function.
def epeebles(k,c):
    return quad(lambda k:1/(np.sqrt((omega0[c]*(1+k)**3)+(omegak[c]*(1+k)**2)+omegal[c])),0,k)

for i in range(0,len(z)):
    einstein=epeebles(z[i],0)
    low=epeebles(z[i],1)
    high=epeebles(z[i],2)
    dcdhe[i]=einstein[0]
    dcdhl[i]=low[0]
    dcdhh[i]=high[0]
    dce[i]=(dcdhe[i])/h
    #dcl[i]=(dcdhl[i])/h
    dch[i]=(dcdhh[i])/h
    t=np.sqrt(omegak[1])
    dmdhl[i]=(1/t)*np.sinh(t*dcdhl[i])
plt.plot(z,dce,'g')
plt.plot(z,dch,'r')
plt.plot(z,dmdhl,'k')
plt.ylim(0,3)
plt.show()
