from astropy.io import fits,ascii
import matplotlib.pyplot as pl
import os
import sys
import numpy as np

print('please enter the path to the fits file to be sliced')
dpath=input()
block=fits.open(dpath)
for i in range(0,4):
 data=block[i].data
 new=fits.PrimaryHDU(data)
 myfit=fits.HDUList([new])
 myfit.writeto('%iseeing4.fits'%i, overwrite=True)  
 myfit.close()


