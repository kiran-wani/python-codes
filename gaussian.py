#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
from scipy.stats import genpareto, multivariate_normal
from astropy.io.fits import getdata
from astropy.io import fits
import random




x, y = np.mgrid[0.0:2047.0:2047j, 0.0:2047.0:2047j]  #x, y is a grid of 2048 pixels each so the resulting image models the one obtained from a 2K CCD.
xy = np.column_stack([x.flat, y.flat])
mu = np.array([1024,1024])
sigma = np.array([2, 2])
covariance = np.diag(sigma**2)

z = multivariate_normal.pdf(xy,mean=mu, cov=covariance)*100
#gaussian function added. choice of constants is arbitrary..have to get flux so will be modified with time
z = z.reshape(x.shape)+np.random.rand(2047,2047)

plt.imshow(z,origin='lower')
plt.xlim(1000,1040)
plt.ylim(1000,1040)
plt.colorbar()
plt.show()

#writing the obtained distribution to a fits file.

'''
new=fits.PrimaryHDU(z)
myfit=fits.HDUList([new])
myfit.writeto('agn.fits', overwrite=True)
myfit.close()
print('wrote gaussian profile no %i to fits!')

#displaying the fits file
dat=fits.open('agn_noise.fits')
data=dat[0].data
plt.imshow(data)
plt.show()



#3d plot of the figure
fig = plt.figure()
ax = fig.add_subplot(111,projection='3d')
ax.plot_surface(x,y,z)
#ax.plot_wireframe(x,y,z)
plt.show()
'''
