# This is a code snipet to extract flux form the objects by first identifying them. 
#Loading the necessary modules
def flux(path,aperture):

 import sep, numpy as np
 from astropy.io import fits


# Reading the fits image alongwith its header
 galaxy=fits.open(path)
 data=galaxy[0].data


# This step seems meaningless but it works. The issue is the change of byte order which will increase the computation time  so I had this workaround!
 data=data+0

# subtracting the background. It's a good idea to ckech the image of background!
 bkg=sep.Background(data)
 back=bkg.back()
 data2=data-back

# it will be really helpful if we see the image at this point. It is background subtracted so the difference should be noticable.

# printing the global background as well as the  rms of background.

 #print(bkg.globalback)
 #print(bkg.globalrms)

# defining the threshold, it is necessary for flux estimation.

 thresh=10*bkg.globalback
 #print(thresh)


# finding out the objects, it will store all the objects found out in the frame determined by the threshold.

 objects=sep.extract(data2,thresh,err=bkg.globalrms)

#The most important, flux and its error determination. This will take a given aperture and calculate the flux in that aperture around the centroid of the object.

 flux,fluxerr,flag=sep.sum_circle(data2,objects['x'],objects['y'],   aperture,err=bkg.globalrms,gain=1.4)


#printing the flux values.


 l=len(objects)
 flux=np.max(flux)
 fluxerr=np.max(fluxerr)
 return(l,flux,fluxerr)





def slice_fits(dpath):
 from astropy.io import fits,ascii
 block=fits.open(dpath)
 for i in range(0,4):
  data=block[i].data
  new=fits.PrimaryHDU(data)
  myfit=fits.HDUList([new])
  if i==0:
     myfit.writeto('blank.fits', overwrite=True)  
  elif i==1:
      myfit.writeto('observed.fits', overwrite=True)  
  elif i==2:  
      myfit.writeto('fitted_model.fits', overwrite=True)  
  elif i==3:
      myfit.writeto('residual_agn.fits', overwrite=True)  
 myfit.close()

 return









