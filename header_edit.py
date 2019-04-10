from astropy.io import fits
data,header=fits.getdata('galaxy.fits',header=True)


'''
for modifying the header parameters:
header['OBJECT']="This contains the object to be detected!"
header['SIGMA']="This contains the sigma image to be inserted"
header['PSF']=" This includes the PSF"

for renaming the keywords
header.rename_keyword('NEWPAR','NEXTPAR')

for removing the header keyword:
header.remove('NEWPAR')

for adding the comments to the headers:
header.comments['SIGMA']=" "

for inserting a new header keyord:
header.insert('SIGMA', ("NEWPAR","let us check the append as well"))

finally to write the operations to the fits file

'''

fits.writeto('galaxy.fits', data,header,overwrite=True)

# for multiple files
import glob,os
from astropy.io import fits
file=glob.glob("/media/vivek/data/PRM/flux_study/*fits")
a=file[7]
print(a)
k=fits.getheader(a,0)
print(k)
