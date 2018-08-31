

'''
This is a python code which I have put here for the sole purpose of improving my plots. The example is a plot of Black body distibution
and the elements will keep on being added in the future so as to make it the best plot I can generate using matplotlib tools.
Vivek Jha
21/08/2018
'''
#!/usr/bin/env python
import matplotlib.pyplot as plt
import numpy as np
from pylab import *

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



h = 6.626e-34
c = 3.0e+8
k = 1.38e-23

def planck(wav, T):
    a = 2.0*h*c**2
    b = h*c/(wav*k*T)
    intensity = a/ ( (wav**5) * (np.exp(b) - 1.0) )
    return intensity

# generate x-axis in increments from 1nm to 3 micrometer in 1 nm increments
# starting at 1 nm to avoid wav = 0, which would result in division by zero.
wavelengths = np.arange(1e-9, 3e-6, 1e-9) 
intensity4000 = planck(wavelengths, 4000.)
intensity5000 = planck(wavelengths, 5000.)
intensity6000 = planck(wavelengths, 6000.)
intensity7000 = planck(wavelengths, 7000.)

plt.style.use('classic')
fig,ax=plt.subplots()
ax.plot(wavelengths*1e9, intensity4000, 'r-',lw=2,label='4000K') 
ax.plot(wavelengths*1e9, intensity5000,'g-',lw=2,label='5000K') 
ax.plot(wavelengths*1e9, intensity6000, 'b-',lw=2,label='6000K') 
ax.plot(wavelengths*1e9, intensity7000, 'k-',lw=2,label='7000K') 
ax.minorticks_on()

ax.set_xlabel(r'$\lambda \, [nm]$',size="x-large")
ax.set_ylabel(r'$B_{\lambda} \, [\mathrm{W \, m^{-2} \, nm^{-1} \, ster^{-1}}]$',size="x-large")

plt.ticklabel_format(style="sci",axis="y")
plt.legend.frameon=False
ax.tick_params(direction="in")
ax.tick_params(axis='both',which='minor',length=3,width=1,labelsize=14)
ax.tick_params(axis='both',which='major',length=6,width=2,labelsize=16)
ax.yaxis.set_ticks_position('both')
ax.xaxis.set_ticks_position('both')
plt.title('Black body spectrum obtained using Planck law')
legend(loc='upper right')

plt.show()
