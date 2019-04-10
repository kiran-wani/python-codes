#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
Tuesday 31 July 2018 12:41:36  IST 

Procedure to create a 2D Gaussian profile, with added noise and write it to a FITS file. Basically, this gaussian profile represents a AGN psf and it has to be introdced to the Galaxy center. Further, in order to study AGN variability, the amplitude of this gaussian profile needs to be variable.
written by: Vivek kumar Jha
JRF at ARIES, Nainital
'''
from pylab import *
from mpl_toolkits.mplot3d import Axes3D
from scipy.stats import genpareto, multivariate_normal
from astropy.io.fits import getdata
from astropy.io import fits
import random
import os
import numpy as np
x, y = np.mgrid[0.0:2047.0:2047j, 0.0:2047.0:2047j]  #x, y is a grid of 2048 pixels each so the resulting image models the one obtained from a 2K CCD.
xy = np.column_stack([x.flat, y.flat])

##for the AGN profile a 2 pixel wide gaussian 2D profile.
mu = np.array([1024,1024])
sigma = np.array([10, 10])
covariance = np.diag(sigma**2)*2
z = multivariate_normal.pdf(xy,mean=mu, cov=covariance)*10000

## these are the background_stars in the frame. Gaussian profiles with 1 pixel width.



#gaussian function added. choice of constants is arbitrary..have to get flux so will be modified with time

z = z.reshape(x.shape)
z+=np.random.poisson(z)
print(np.max(z))
#imshow(z,origin='lower',cmap='viridis')
#show()
#imshow(z,origin='lower',cmap='Accent')
#show()

#noisemap = np.random.poisson(z)
#noisy = z + np.random.poisson(noisemap)  

#plot(z)
'''
imshow(z,origin='lower')
plt.xlim(1010,1040)
plt.ylim(1010,1040)
show()
#writing the obtained distribution to a fits file.

z = z.reshape(x.shape)
new=fits.PrimaryHDU(z)
myfit=fits.HDUList([new])
myfit.writeto('background_stars.fits', overwrite=True)
myfit.close()
print('wrote gaussian profile no %i to fits!')
os.system("ds9 background_stars.fits")

#displaying the fits file
dat=fits.open('agn_poisson.fits')
data=dat[0].data
plt.imshow(data)
plt.show()
'''
#3d plot of the figure
fig = plt.figure()
ax = fig.add_subplot(111,projection='3d')
ax.plot_surface(x,y,z)
#ax.plot_wireframe(x,y,z)
plt.show()




