'''
This is a python procedure to read the galaxy file, add AGN to it (multiple times) ,the Agn being variable means
the variability can be simulated using this model.
'''


from astropy.io import fits
import matplotlib.pyplot as plt
from glob import glob
import numpy as np

s=np.zeros(15)
x=np.arange(0,15)

#To open the galaxy.fits file and introduce a gaussian psf (the AGN ) inside it.
# 15 night continuous observations.

galaxy=fits.open('gal_moffat.fits')
gal_data=galaxy[0].data

#15 night continuous AGN observations with small variability in the amplitude.

t=glob('agn*.fits')
for i in range(0,15):
 k=t[i]
 agn=fits.open(k)
 agn_data=agn[0].data
 com=gal_data+agn_data
 print('%i th image being processed'%i)
 new=fits.PrimaryHDU(com)
 myfit=fits.HDUList([new])
 myfit.writeto('com%i.fits' %i, overwrite=True) 
 myfit.close()

# the AGN have been introduced into the galaxies and the  combined image is obtained for 15 continuous nights.

# For reading/ displaying the variabilty in the obtained Light curves.
t=glob('com*.fits')
for i in range(0,15):
 k=t[i]
 agn=fits.open(k)
 agn_data=agn[0].data
 g=np.max(agn_data)
 s[i]=g
 print('Displaying image no.%i---'%i) 
 plt.imshow(agn_data)
 plt.xlim(950,1100)
 plt.ylim(950,1100)
 plt.show()

plt.plot(x,s,'ro')
plt.ylim(850,1350)
plt.show()
 


