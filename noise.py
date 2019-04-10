import matplotlib.pyplot as plt
import numpy as np
from astropy.io.fits import getdata
from astropy.io import fits
import random
data,header=getdata('combined.fits',0,header=True)

com=data+random.randint(0,13)
new=fits.PrimaryHDU(com)
myfit=fits.HDUList([new])
myfit.writeto('noise.fits', overwrite=True) 
myfit.close()

