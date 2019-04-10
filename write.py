from astropy.io.fits import getdata
from astropy.io import fits
import matplotlib.pyplot as pl ,numpy as np, os
#from pyraf import iraf
'''
a=np.array([1.57,1.7301,1.8874,2.0446,2.202,2.36,2.516,2.674,2.8311,2.988,3.1456,3.14 ,  3.4602, 3.7748, 4.0892, 4.404,  4.72,   5.032,  5.348,  5.6622, 5.976,
 6.2912,4.71,   5.1903, 5.6622, 6.1338, 6.606 , 7.08,   7.548 , 8.022 , 8.4933 ,8.964,
 9.4368, 6.28,    6.9204,  7.5496,  8.1784 , 8.808 ,  9.44   ,10.064 , 10.696,  11.3244,
 11.952,  12.5824])
'''
galaxy,header=getdata('galaxy.fits',0,header=True)
agn,header=getdata('agn_poisson.fits',0,header=True)
com=galaxy+agn
new=fits.PrimaryHDU(com)
myfit=fits.HDUList([new])
myfit.writeto('galagn_poisson.fits', overwrite=True)  
myfit.close()
print('galaxy+agn combined image written')
'''

for i in range(0,len(a)):
 iraf.gauss('combined16.fits','convolution_%i.fits'%i,a[i])
 print('convolution no.%i performed'%i)
os.system("mv convolution* convolved")
'''
