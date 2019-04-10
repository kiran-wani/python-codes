'''
To get all the distance using the hogg's paper

'''

import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import quad

z=np.arange(0,5.1,0.1)
h=0.7
omega0=[1,0.05,0.2]
omegal=[0.0,0.0,0.8]
omegak=[0.0,0.95,0.0]


# defining the E(z); the peebles function for a given z and cosmology..
e1=np.sqrt((omega0[1]*(1+z)**3)+(omegak[1]*(1+z)**2)+omegal[1])
e0=np.sqrt((omega0[0]*(1+z)**3)+(omegak[0]*(1+z)**2)+omegal[0])
e2=np.sqrt((omega0[2]*(1+z)**3)+(omegak[2]*(1+z)**2)+omegal[2])
#fquad(lambda e:1/e,min(z),max(z))






dcdh0=z/e0
dcdh1=z/e1
dcdh2=z/e2

k=np.sqrt(omegak[1])
dmdh1=(1/k)*np.sinh(k*dcdh1)
dmdh2=h*dcdh2
dmdh0=h*dcdh0

dadh1=dmdh1/(1+z)
dadh2=dmdh2/(1+z)
dadh0=dmdh0/(1+z)

dldh1=dmdh1*(1+z)
dldh2=dmdh2*(1+z)
dldh0=dmdh0*(1+z)

plt.style.use('classic')
fig,ax=plt.subplots()
ax.plot(z,dldh0,lw=2,label='Einstein de-sitter')
ax.plot(z,dldh1,lw=2,label='Low density')
ax.plot(z,dldh2,lw=2,label='High Lambda') 
ax.legend()
#ax.grid()
ax.minorticks_on()
plt.legend.frameon=True
ax.tick_params(direction="in")
ax.tick_params(axis='both',which='minor',length=3,width=1,labelsize=14)
ax.tick_params(axis='both',which='major',length=6,width=2,labelsize=16)
ax.yaxis.set_ticks_position('both') 
ax.xaxis.set_ticks_position('both')
#plt.savefig('first.eps',format='eps',dpi=500)
plt.show()
'''
plt.plot(z,dadh1,'g')
plt.plot(z,dadh2,'r--')
plt.plot(z,dadh3,'b')
plt.show()


plt.plot(z,dmdh3,'g')
plt.plot(z,dmdh2,'r')
plt.plot(z,dmdh1,'k')
plt.show()
'''
