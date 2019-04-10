from astropy.io import fits
import matplotlib.pyplot as plt
a=fits.open('imgblock.fits')
for i in range (0,4):
 dat=a[i].data
 plt.imshow(dat)
 plt.show()

