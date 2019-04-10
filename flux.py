import sep,glob,os
from astropy.io.fits import getdata
from pylab import *
x=np.arange(2,10.8,0.2)
y=np.arange(0,44,1)
yerr=np.arange(0,44,1)
t=sorted(glob.glob('convolution*.fits'))
print(len(t))
for i in range(0,len(t)):
  print('reading image no%i'%i)
  data, header = getdata(t[i],0,header=True)
  data=np.around(data)
  bkg=sep.Background(data)
  back=bkg.back()
  data2=data-back
  thresh=0.5*bkg.globalrms
  objects=sep.extract(data2,thresh,err=bkg.globalrms)
  flux,fluxerr,flag=sep.sum_circle(data2,objects['x'],objects['y'], 150,err=bkg.globalrms,gain=1.4)
  y[i]=np.max(flux)
  yerr[i]=np.max(fluxerr)

fig,ax=subplots()
plot(x,y,'ro')
errorbar(x,y,yerr=yerr, capsize=3,fmt='--o')
ylim(17200,18300)

ylabel('flux  [counts]')
xlabel('seeing  [arcseconds]')
title('Flux vs seeing graph for 150 pixel aperture')
ax.tick_params(axis="y",direction="in", pad=10)
ax.tick_params(axis="x",direction="in", pad=10)
show()


#plt.savefig('box150.eps', format='eps', dpi=100)

