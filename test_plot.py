import numpy as np
import matplotlib.pyplot as plt
import matplotlib
import os

font = {'family'         : 'serif',
	'weight'         : 'bold',
	'size'	         : 16}
matplotlib.rc('font',**font)
matplotlib.rc('grid',linewidth=1)
matplotlib.rc('xtick.major',width=2)
matplotlib.rc('xtick.major',size=7)
matplotlib.rc('xtick.minor',width=2)
matplotlib.rc('xtick.minor',size=4)
matplotlib.rc('ytick.major',width=2)
matplotlib.rc('ytick.major',size=7)
matplotlib.rc('ytick.minor',width=2)
matplotlib.rc('ytick.minor',size=4)

plt.style.use('classic')
a=np.arange(-6.28,6.28,0.8)
b=np.sin(a)
c=np.cos(a)
d=np.exp(-a*a)
fig,ax=plt.subplots()
ax.plot(a,b,'ro',markersize=5,label='Cosine')
ax.errorbar(a,b,yerr=b*0.1,xerr=a*0.1,fmt=' ',color='red')
#ax.plot(a,c,'go--',markersize=5,label='Sine')
#ax.plot(a,d,'bo--',markersize=5,label='exponential')
plt.ylim(-1.2,1.2)
 #xlim(-6.5,6.5)
ax.legend()
ax.legend(loc='upper right')
 #ax.grid()
ax.minorticks_on()
#ax.legend.frameon=False
ax.tick_params(direction="in")
ax.tick_params(axis='both',which='minor',length=3,width=1,labelsize=14)
ax.tick_params(axis='both',which='major',length=6,width=2,labelsize=16)
ax.yaxis.set_ticks_position('both')
ax.xaxis.set_ticks_position('both')
plt.title("A simple way to demonstrate Matplotlib",color='Green')
plt.xlabel('Value of X')
plt.ylabel('Sine of X')
plt.savefig('test.eps',format='eps',dpi=200)
os.system("evince test.eps")
