def my_plot(a,b):
 import matplotlib.pyplot as plt
 import numpy as np



 plt.style.use('classic')
 fig,ax=plt.subplots()
 
 ax.plot(a,b, 'k-',lw=2,label='7000K') 
 ax.minorticks_on()

 ax.set_xlabel(r'$\lambda \, [nm]$',size="x-large")
 ax.set_ylabel(r'$B_{\lambda} \, [\mathrm{W \, m^{-2} \, nm^{-1} \, ster^{-1}}] $',size="x-large")

 plt.ticklabel_format(style="sci",axis="y")
 plt.legend.frameon=False
 ax.tick_params(direction="in")
 ax.tick_params(axis='both',which='minor',length=3,width=1,labelsize=14)
 ax.tick_params(axis='both',which='major',length=6,width=2,labelsize=16)
 ax.yaxis.set_ticks_position('both')
 ax.xaxis.set_ticks_position('both')
 plt.title('Black body spectrum obtained using Planck law')
 plt.legend(loc='upper right')

 plt.show()


'''
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

'''


