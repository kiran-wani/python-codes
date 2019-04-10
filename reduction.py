from aperphot import *
import numpy as np
from pyraf import iraf
import os
from readcol import *
import glob
import matplotlib.pyplot as plt
#os.system(!ds9 &)
#filename='./20151414/mcg09_v1.fits'
datadir='./20151228/'
print("Reducing data in directory:", datadir)
band=['b', 'v', 's']
i=2
print("Band:", band[i])
os.chdir(datadir)
datafiles=glob.glob(strcompress('*_'+band[i]+'*'))
os.system("rm mbias.fits")
os.system("rm *.in*")
os.system("rm *flatr*")
os.system("rm *subBias*")
os.system("rm *divFlat*")
os.system("rm *cosmic*")
# combine bias files:
os.system("ls *bias* > bias.in")
iraf.imcombine('@bias.in', 'mbias.fits', combine='median')
iraf.imstat('mbias.fits')
#================================
# now make bias substracted image:
#================================
if i==0:
    os.system("ls *_b* >subBias.in")
    os.system("ls *flat_b* >flatr.in")
if i==1:
    os.system("ls *_v* >subBias.in")
    os.system("ls *flat_v* >flatr.in")
if i==2:
    os.system("ls *_s* >subBias.in")
    os.system("ls *flat_s* >flatr.in")

os.system("sed s/.fits/B.fits/g subBias.in> subBias.out")


iraf.imarith('@subBias.in', '-', 'mbias.fits', '@subBias.out')
iraf.imcombine('@flatr.in', 'mflatr.fits', combine='median')

# to get normalise flat:
iraf.imstat('mflatr.fits')
iraf.imarith('mflatr.fits', '/', 'mflatr.fits', 'nflatr.fits')

if i==0:
    os.system("ls mcg*_b*B.fits* gd*_b*B.fits* pg*_b*B.fits* bd*_b*B.fits* > divFlat.in")

if i==1:
    os.system("ls mcg*_v*B.fits* gd*_v*B.fits* pg*_v*B.fits* bd*_v*B.fits* > divFlat.in")

if i==2:
    os.system("ls mcg*_s*B.fits* gd*_s*B.fits* pg*_s*B.fits* bd*_s*B.fits* > divFlat.in")

os.system("sed s/B.fits/BF.fits/g divFlat.in> divFlat.out")

iraf.imarith('@divFlat.in', '/',  'nflatr.fits',  '@divFlat.out')

#cosmic ray removal :
os.system("cp divFlat.out rm_cosmic.in")
os.system("sed s/BF.fits/BFC.fits/g rm_cosmic.in> rm_cosmic.out")

iraf.imred(_doprint=0)
iraf.crutil(_doprint=0)

# if ERROR: PLIO: reference out of bounds on mask error happen then use image[*,*,1] in input image as ur image may be more then 2 dim or [*,*,1]
# if ERROR: segmentation violation in xgterm use terminal or use linux machine
os.system("sed s/F.fits/F.fits[*,*,1]/g rm_cosmic.in> rm_cosmic_ind.in")

crmasks='0, 0, 0, 0, 0'  # total 5 frames: 2 AGN frame and 3 standard frames.
iraf.crutil.cosmicrays("@rm_cosmic_ind.in", "@rm_cosmic.out", interactive='no', crmasks=crmasks)

#os.system("sed s/bfc.fits/bfc.fits[10:507,10:507]/g rm_cosmic.out> trim.in")
# Note: Check the limits. This is for 512 times 512 image size
#os.system("sed s/bfc.fits/bfct.fits/g rm_cosmic.out > trim.out")

filenames=readcol('rm_cosmic.out')

photometry(filenames)

os.chdir('..')

'''
dirlist=glob.glob('*2015*')
file1=open('mag.out', 'w')
day=np.array([1, 2, 3, 4, 5, 6, 8, 9, 10, 14])
for i in range(len(dirlist)):
    Bmagfile=glob.glob(strcompress(dirlist[i]+'/'+'mcg*_b1*phot*'))
    print("Bmagfile:", Bmagfile[0])
    ap=readcol(Bmagfile[0], skipline=107)
    Bmag  = float(ap[0, 4])
    Bemag = float(ap[0, 5])
    Vmagfile=glob.glob(strcompress(dirlist[i]+'/'+'mcg*_v1*phot*'))
    print("Vmagfile:", Vmagfile[0])
    ap=readcol(Vmagfile[0], skipline=107)
    Vmag  = float(ap[0, 4])
    Vemag = float(ap[0, 5])
    SIImagfile=glob.glob(strcompress(dirlist[i]+'/'+'mcg*_s*_1*phot*'))
    print("SIImagfile:", SIImagfile[0])
    ap=readcol(SIImagfile[0], skipline=107)
    SIImag  = float(ap[0, 4])
    SIIemag = float(ap[0, 5])
    file1.write('{0}\t {1}\t {2} \t {3}\t {4}\t {5}\t {6}\n'.format(day[i], Bmag, Bemag, Vmag, Vemag, SIImag, SIIemag))

file1.close()
'''
file1=open('Standards_mag.out', 'w')
day=np.array([1, 2, 3, 4, 5, 6, 8, 9, 10, 14])
standards=['gd', 'pg', 'bd']
for j in range(3):
    for i in range(len(dirlist)):
        Bmagfile=glob.glob(strcompress(dirlist[i]+'/'+standards[j]+'*_b*phot*'))
        Vmagfile=glob.glob(strcompress(dirlist[i]+'/'+standards[j]+'*_v*phot*'))
        SIImagfile=glob.glob(strcompress(dirlist[i]+'/'+standards[j]+'*_s*phot*'))
        print("i and j:", i, j)
        print("Bmagfile:", Bmagfile[0])
        ap=readcol(Bmagfile[0], skipline=92)
        Bmag  = float(ap[0, 4])
        Bemag = float(ap[0, 5])
        print("Vmagfile:", Vmagfile[0])
        ap=readcol(Vmagfile[0], skipline=92)
        Vmag  = float(ap[0, 4])
        Vemag = float(ap[0, 5])
        #SIImagfile=glob.glob(strcompress(dirlist[i]+'/'+'mcg*_s*_1*phot*'))
        print("SIImagfile:", SIImagfile[0])
        ap=readcol(SIImagfile[0], skipline=92)
        SIImag  = float(ap[0, 4])
        SIIemag = float(ap[0, 5])
        file1.write('{0}\t {1}\t {2:0.3f} \t {3}\t {4}\t {5}\t {6}\t {7}\n'.format(day[i], j, Bmag, Bemag, Vmag, Vemag, SIImag, SIIemag))

file1.close()

'''
#day, mag, emag=np.loadtxt('Bmag.out', unpack=True)
day, Bmag, eBmag, Vmag, eVmag, SIImag, eSIImag=np.loadtxt('mag.out', unpack=True)
day, objno, Bmag, eBmag, Vmag, eVmag, SIImag, eSIImag=np.loadtxt('Standards_mag.out', unpack=True)
plt.figure(); 
plt.errorbar(day, Bmag, yerr=eBmag, fmt='or', label="B");
#plt.errorbar(day, Vmag, yerr=eVmag, fmt='ob');
plt.errorbar(day, SIImag, yerr=eSIImag, fmt='og', label="SII");
plt.xlim([0, 16]); 
plt.legend()
#plt.ylim([15.8, 16.5]);
plt.xlabel("time (days)")
plt.ylabel("mag")
plt.show(block=False)
lag=np.linspace(day[0], day[-1], 10*np.max(day))
Hb=SIImag-0.5*Vmag
BMAG=np.interp(lag, day, Bmag)
VMAG=np.interp(lag, day, Vmag)
SIIMAG=np.interp(lag, day, SIImag)
HBMAG=np.interp(lag, day, Hb)
corr=cross_corr(SIIMAG, BMAG)[-50+len(BMAG):120+len(BMAG)]
DELAY=np.arange(-50, 120)

plt.figure(); plt.plot(DELAY/10.,corr/len(BMAG), label='B vs SII');
plt.legend()
plt.xlabel("delay(days)"); plt.ylabel("CCF"); 
plt.show(block=False)


plate_scale=24 *40/1000.0 #arcsec/pixel
apersize_pixel=15*plate_scale
'''



'''
from astropy.time import Time
times=['1999-01-01T00:00:00.12']
t=Time(times, scale='utc')
jd=t.jd
'''
