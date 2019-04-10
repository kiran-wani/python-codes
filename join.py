from astropy.io.fits import getdata
from astropy.io import fits
from pylab import *
galaxy,header=getdata('sp_gal16.fits',0,header=True)
bkg,header=getdata('vineet.fits',0,header=True)
agn,header=getdata('agn_noise.fits',0,header=True)
com=galaxy+agn+bkg
new=fits.PrimaryHDU(com)
myfit=fits.HDUList([new])
myfit.writeto('vcom.fits', overwrite=True)  
myfit.close()
print('galaxy+agn combined image written')
imshow('vcom.fits',cmap='invgrey')
show()
'''

for i in range(0,len(a)):
 iraf.gauss('combined16.fits','convolution_%i.fits'%i,a[i])
 print('convolution no.%i performed'%i)
os.system("mv convolution* convolved")
'''
