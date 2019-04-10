from astropy.io import fits
import matplotlib.pyplot as plt
from glob import glob
import numpy as np
x=np.array([2,2.2,2.4,2.5,2.6,2.8,3.0,3.2,3.4,3.5,3.6,3.8,4.0])
s=np.zeros(13)
t=sorted(glob('csig*.fits'))
for i in range(0,13):
 print(t[i])
 k=t[i]
 agn=fits.open(k)
 agn_data=agn[0].data
 plt.plot(agn_data[980:1080,980:1080])
 plt.ylim(1.3,6)
 plt.show()
