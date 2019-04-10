import matplotlib.pyplot as plt
import numpy as np
from astropy.io.fits import getdata
data,header=getdata('noise.fits',0,header=True)
plt.imshow(data,cmap='gray')
plt.show()
