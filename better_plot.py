
#def vivek_plot(a,b,c):
 import numpy as np
 import matplotlib.pyplot as plt
 plt.style.use('classic')
 a=np.arange(-6.28,6.28,0.1)
 b=np.sin(a)
 fig,ax=plt.subplots()
 ax.plot(a,b,c,lw=2)
 #ylim(-1.2,1.2)
 #xlim(-6.5,6.5)
 ax.legend()
 #ax.grid()
 ax.minorticks_on()
 plt.legend.frameon=False
 ax.tick_params(direction="in")
 ax.tick_params(axis='both',which='minor',length=3,width=1,labelsize=14)
 ax.tick_params(axis='both',which='major',length=6,width=2,labelsize=16)
 ax.yaxis.set_ticks_position('both')
 ax.xaxis.set_ticks_position('both')
 #return
