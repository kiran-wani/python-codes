import matplotlib.pyplot as plt
import numpy as np
h = 6.626e-34
c = 3.0e+8
k = 1.38e-23

def planck(nu, T):
    a = 2.0*h*nu**3
    b = h*nu/(k*T)
    intensity = a/ ( (c**3) * (np.exp(b) - 1.0) )
    return intensity

# generate x-axis in increments from 1nm to 3 micrometer in 1 nm increments
# starting at 1 nm to avoid wav = 0, which would result in division by zero.
nu = np.arange(9,18.,0.5)
nu=10**nu 
intensity4000 = planck(nu, 1000.)

plt.style.use('classic')
fig,ax=plt.subplots()
ax.plot(nu, intensity4000, 'r-') 
ax.minorticks_on()
plt.legend.frameon=False
ax.tick_params(direction="in")
ax.tick_params(axis='both',which='minor',length=3,width=1,labelsize=14)
ax.tick_params(axis='both',which='major',length=6,width=2,labelsize=16)
ax.yaxis.set_ticks_position('both')
ax.xaxis.set_ticks_position('both')
plt.show()
# doesn't erase plots on subsequent calls of plt.plot()
#plt.plot(wavelengths*1e9, intensity4000, 'r-') 
# plot intensity4000 versus wavelength in nm as a red line
#plt.plot(wavelengths*1e9, intensity5000, 'g-') # 5000K green line
#plt.plot(wavelengths*1e9, intensity6000, 'b-') # 6000K blue line
#plt.plot(wavelengths*1e9, intensity7000, 'k-') # 7000K black line

