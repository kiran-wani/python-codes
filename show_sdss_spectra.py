'''
This small code is written to display the sdss spectra for QSOs. It takes the input spectrum and displays the emission line profiles in wavelength as well as velocity dispersion scales.  Can be used to display hundreds/thousands of spectra at a go.

'''

from pylab import *
from astropy.io import fits
import glob
import matplotlib
import matplotlib.animation as animation
from scipy.ndimage.filters import gaussian_filter1d


#fig=matplotlib.pyplot.gcf()
path=input(" Enter the path of the spectra:\t")
files=sorted(glob.glob(path+'/spec*fits'))
c=3e5 # velocity of light in km/sec
ims = []
kk=np.zeros(len(files))
fig = plt.figure()
print(len(files))
for i in range (0,len(files)):
    data=fits.open(files[i])
    lam=10**data[1].data['loglam'] # OBS wavelength [A]
    flux=data[1].data['flux']             # OBS flux [erg/s/cm^2/A]
    err=1./np.sqrt(data[1].data['ivar'])  # 1 sigma error
    z=data[2].data['z'][0]   
    lam=lam/(1+z)
    ra=data[2].data['PLUG_RA'][0] 
    dec=data[2].data['PLUG_DEC'][0]
    plate=data[2].data['PLATEID'][0] 
    mjd=data[2].data['MJD'][0]
    fibre=data[2].data['FIBERID'][0] 
    snr=data[2].data['SN_MEDIAN_ALL'] [0]
    hbeta_lam=np.where((lam > 4600) & ( lam < 5100))
    
    # Unit conversion from angstrom to km/sec for the calculation of velocity dispersion
    cent_wav=4862.68 
    dl=lam[hbeta_lam]-cent_wav
    vel=(c*dl)/cent_wav
    ysmoothed = gaussian_filter1d(flux[hbeta_lam], sigma=1) # to smooth the spectra with a gaussian filter of order 1.
    im=plt.plot(vel,ysmoothed,'b',lw=1,label="Observed H beta flux. Spectra no.%i"%i) # in terms of velocity dispersion.

    #im=plt.plot(lam[hbeta_lam],ysmoothed,'b',lw=3,label="Observed H beta flux. Spectra no.%i"%i)  # in terms of wavelength.
    
    ims.append([im])
    plt.xlabel(' Velocity dispersion (km/sec)')
    plt.ylabel('Flux')
    plt.legend()
    plt.axvline(x=0,color='green',lw=0.5) # line centre
    #plt.xlim(4800,4920) # limits for H_beta line
    plt.xlim(-3000,3000) # limits for velocity dispersion of H_beta line
    plt.tight_layout()
    plt.pause(1)
    plt.clf()

plt.show()    
  




