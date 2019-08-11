'''
This will generate a time series based on damped random walk model/Ornstein Uhlenback Process which wll be the continuum light curve. The continuum LC is scaled, smoothed and shifted to form the emission line light curve.

Written by:
Vivek Kumar Jha
JRF @ ARIES, Nainital India

'''


import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mp
import csv,random,sys
from astropy.convolution import MexicanHat1DKernel,Trapezoid1DKernel,Box1DKernel,Gaussian1DKernel,convolve
from scipy.ndimage.interpolation import shift
#~~~~~~~~~~~~~~~~ For Plotting only~~~~~~~~~~#
mp.rcParams['font.family']='serif'
mp.rcParams['xtick.major.size']=10
mp.rcParams['xtick.major.width']=2
mp.rcParams['xtick.minor.size']=7
mp.rcParams['xtick.minor.width']=2
mp.rcParams['ytick.major.size']=10
mp.rcParams['ytick.major.width']=2
mp.rcParams['ytick.minor.size']=7
mp.rcParams['ytick.minor.width']=2
mp.rcParams['axes.linewidth']=1.5
mp.rcParams['xtick.labelsize']=16
mp.rcParams['ytick.labelsize']=16
    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#




def generate_drw(N,x0,mu,tau,sigma):
    '''
	The basic function to generate the DRW continuum Light curve. 
	
	inputs: 
	N: No. of total points over which sampling is done.
	x0: The initial value of the flux.
	mu: The mean value of the damped random walk.
	tau: The damping timescale.
	sigma: The deviation from the mean.
	
	outputs:
	The time series generated from the DRW model.   
    '''
    class OU_process:
        def __init__(self,X_0, mu, theta, sigma, dt=0.1):
            self.X = X_0
            self.dt = dt
            self.mu = mu
            self.theta = theta
            self.sigma = sigma
            self.setup()
        
        def setup(self):
            self.emdt = np.exp(-self.theta*self.dt)
            self.a = np.sqrt(self.sigma**2/(2*self.theta) *
                            (1 - np.exp(-2*self.theta*self.dt)))


        def step(self):
            X_dt = self.X*self.emdt+self.mu*(1 - self.emdt) + \
                    self.a*np.random.normal()
            self.X = X_dt


        def path(self, T, reset=None):

            if reset != None:
                self.X = reset

            path = []
            for t in np.arange(0,T,self.dt):
                path.append(self.X)
                self.step()
            return path



    dt = 1
    X_0 = x0 #3
    mu = mu #3
    theta = tau #0.5
    sigma = sigma #2



    ou= OU_process(X_0,mu,theta,sigma,dt)
    T=N
    ts=np.arange(0,T,dt)
    for k in range(1):
        path=ou.path(T)
        fig,ax=plt.subplots()
        #plot(ts,path,'k',markersize=10)
        #plot(ts,path,'ko',markersize=6)
        path1=[x-mu for x in path]
        #path=[abs(x) for x in path]
        #plt.hist(path,bins=50,edgecolor='white',linewidth=2.5,color='cyan')#,histtype='step',edgecolor='green',linewidth=2.5,color='orange',stacked=True,fill=True,alpha=0.4)
        print(np.max(path),np.max(path1))
        perr=[0.05*x for x in path]
        plt.plot(ts,path,'go',markersize=10)
        #ylim(-1,1)
        #plot(ts,path,color='green',linestyle='steps',lw=2)
        #plot(ts,path,color='darkorange',marker='o',lw=0,markersize=10)
    
        #err=0.1*path
    # errorbar(ts,path,yerr=perr,color='green',fmt=' ',capsize=4)
        #ax.set_ylim(0,2)
        #plot(ts,path,'k-',lw=1)
        plt.ylabel(" Flux (arbitrary units)",fontsize=36)
        plt.xlabel(" No. of days",fontsize=36)
        plt.title("DRW model for AGN variability",fontsize=36)
        ax.tick_params(axis="both",which='minor',direction="in")
        ax.tick_params(axis="both",which='major',direction="in")
        ax.yaxis.set_ticks_position('both')
        ax.xaxis.set_ticks_position('both')
        ax.minorticks_on()
       # ax.legend(fontsize=16)
        
        

        
    # plt.savefig('random_lc.eps',format='eps',dpi=200)
        plt.show()
    
    zip(ts,path,perr)
    with open ("test_con.csv", "w") as f:
        writer= csv.writer(f, delimiter=" ")
        writer.writerows(zip(ts,path,perr))
        quit()
    



def generate_emission(path):
    
    '''
    To generate the emission line light curve from the continuum light curve by shifting, scaling and smoothing it with a transfer function.
    
    inputs:
    
    The path to the continuum light curve (string)
    
    outputs:
    
    The generated emission light curve.
    '''
    
    date,con_flux,flerr=np.genfromtxt(path,unpack=True,usecols=(0,1,2))
    em_flux=shift(con_flux,5,cval=0)
    for i in range(0,5):
        em_flux[i]+=random.randint(-4,6)
    
    new_em=0.7*em_flux*np.log(2)


    #plot(b,d,drawstyle='steps')
    #show()

    '''
    gau=Gaussian1DKernel(2)
    new_c=convolve(c,gau)


    kk=Box1DKernel(5)
    new_cc=convolve(c,kk)
    '''
    tt=Trapezoid1DKernel(2,slope=1)
    emm=convolve(new_em,tt)
    # making the plots
    fig, ax =plt.subplots()
    ax.plot(date,con_flux,color='darkturquoise',marker='o',lw=1,label='Continuum line')
    #ax.plot(b,c,color='darkorange',lw=2,drawstyle='line',label='Gaussian Convolution')
    #ax.plot(b,emm,color='darkturquoise',lw=2,drawstyle='line',label='1D Box Convolution')
    ax.plot(date,emm,color='darkorange',marker='o',lw=1,label='Emission Line')
    #ax.set_xlim(0,40)
    ax.set_xlabel('Days', size=16)
    ax.set_ylabel('Flux (arbitrary units)', color='k', size=16)
    ax.tick_params(axis="both",which='minor',direction="in")
    ax.tick_params(axis="both",which='major',direction="in")
    ax.yaxis.set_ticks_position('both')
    ax.xaxis.set_ticks_position('both')
    ax.minorticks_on()
    ax.legend(fontsize=16)
    plt.show()

    #kk=zip(b,emm)
    #np.savetxt("jj.csv",kk)

    #zip(b,emm)
    
    with open ("test_em.csv", "w") as f:
        writer= csv.writer(f, delimiter=" ")
        writer.writerows(zip(date,emm,flerr))
        sys.exit()
    

