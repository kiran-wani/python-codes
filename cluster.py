from scipy.ndimage import gaussian_filter
import numpy
import random
from numpy import *
import numpy as np
import os
# Create empty image
nx, ny = 512, 512
x=np.array[512,512]
y=np.array(512,512)
image = np.zeros((ny, nx))

# Set number of stars
n = 10000

# Generate random positions
r = random.random() * nx
theta = random.random()

# Generate random fluxes
f = random.random() ** 2

# Compute position
x = nx / 2 + r * cos(theta)
y = ny / 2 + r * sin(theta)

# Add stars to image
# ==> First for loop and if statement <==
for i in range(n):
    if x[i] >= 0 and x[i] < nx and y[i] >= 0 and y[i] < ny:
        image[y[i], x[i]] += f[i]

# Convolve with a gaussian
image = gaussian_filter(image, 1)

# Add noise
image += random.normal(3., 0.01, image.shape)

# Write out to FITS image
new=fits.PrimaryHDU(image)
myfit=fits.HDUList([new])
myfit.writeto('cluster.fits', overwrite=True) 
myfit.close()
os.system("ds9 cluster.fits")
