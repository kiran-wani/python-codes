'''
A simple python code to demonstrate least square fitting. We fit the curve using a straight line, calculate the chisq, reduced chisq, probability of chisq, correlation coefficient, correlation probability etc.
Vivek Jha
JRF at ARIES, Nainital.
Friday 31 August 2018 11:53:24 PM IST 
''' 
import matplotlib.pyplot as plt
import numpy as np
from pylab import *
import math

k=np.loadtxt('ass_2.dat',unpack=True)
y=k[0]   			# log emission measure.
x=k[1]			# log temperature.
yerr=k[2]			# error in emissivity.

a1=y/yerr**2
a2=x/yerr**2
a3=x*y/yerr**2
a4=x**2/yerr**2
a5=1/yerr**2
A=np.array([[sum(a1) ,sum(a2)],[sum(a3),sum(a4)]])
B=np.array([[sum(a5),sum(a1)],[sum(a2),sum(a3)]])
E=np.array([[sum(a5),sum(a2)],[sum(a2),sum(a4)]])
p=np.linalg.det(A) 
q=np.linalg.det(B)
r=np.linalg.det(E)
a=p/r
b=q/r
# we have calculated  coefficients a and b
# Now, we need the errors in a and b
aerr=sum(a2)/r
berr=sum(a5)/r


y_new=a+b*x

#  chisq and chisq/dof are needed, dof will be 6 for 8 data points.
ds=((y_new-y)/yerr)**2
chisq=sum(ds)
redchisq=chisq/(len(y)-2)


# Now the probability of chisq

upper=chisq**(2)* exp(-chisq/2)
lower=8* math.gamma(3)
prob=upper/lower



# The correlation coefficients { b_corr and c_corr}

xiyi=sum(x*y)
xi=sum(x)
yi=sum(y)
xisq=sum(x*x)
yisq=sum(y*y)

num=8*xiyi-xi*yi
denomb=(8*xisq)-(xi*xi)

b_corr=num/denomb

denomc= (8*yisq)-(yi*yi)
c_corr=num/denomc

r=sqrt(b_corr*c_corr)

# the probability of no correlation
prob_r=1/sqrt(np.pi) * (math.gamma(7/2)/math.gamma(3))*(1-r*r)**2




#=============================================
# This is for  the plot only!!!!

plt.style.use('classic')
fig,ax=plt.subplots()
ax.plot(x,y,'ro',label='data') 
errorbar(x,y,yerr=yerr,capsize=2,marker='o',color='k',ecolor='k',markerfacecolor='r',linestyle='None')
ax.plot(x,y_new,linestyle='--',label='Fitted line')
ax.minorticks_on()
ax.set_xlabel(r'Log temperature (T)',size="x-large")
ax.set_ylabel(r'Log Emission measure',size="x-large")
plt.ticklabel_format(style="sci",axis="y")
plt.legend.frameon=False
ax.tick_params(direction="in")
ax.tick_params(axis='both',which='minor',length=3,width=1,labelsize=14)
ax.tick_params(axis='both',which='major',length=6,width=2,labelsize=16)
ax.yaxis.set_ticks_position('both')
ax.xaxis.set_ticks_position('both')
plt.title('Illustration of least square fitting process ')
legend(loc='upper left')
plt.xlim(7.35,7.95)
textstr = '\n'.join((  r'a=%.2f' % (a, ),
    r'b=%.2f' % (b, ),
    r'$\chi^2=%.2f$' % (chisq, ),
r'$\chi^2$-per-dof=%.2f' % (redchisq, ),
    r'$\chi^2$-probability=%.2f' % (prob*100, ),r'r=%.2f' % (r, ),
    r'No correlation probability=%.2f' % (prob_r*100, ),))
props = dict(boxstyle='round', facecolor='white', alpha=0.5)
ax.text(0.62,0.35,' The parameters',transform=ax.transAxes,fontsize=12,color='black',verticalalignment='top', bbox=props)
ax.text(0.60, 0.30, textstr, transform=ax.transAxes, fontsize=10,color='black',
        verticalalignment='top', bbox=props)

#============================================================================



plt.savefig('plot.eps',overwrite=True,format='eps',dpi=500)
plt.show()




