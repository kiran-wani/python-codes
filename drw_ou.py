#Python code to demonstrate the Ornstein-Uhlenbeck process

import numpy as np
import matplotlib.pyplot as pl

class OU_process(object):

    def __init__(self,X_0, mu, theta, sigma, dt=0.01):
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


dt = 0.01
X_0 = -2
mu = 1.
theta = 1.
sigma = 1.

OU = OU_process(X_0, mu, theta, sigma, dt)






T = 10
ts = np.arange(0,T,dt)

mean = np.array([X_0*np.exp(-theta*t) + \
                 mu*(1-np.exp(-theta*t)) for t in ts])
var = np.array([sigma**2/(2*theta)* \
                  (1-np.exp(-2*theta*t)) for t in ts])

#fig = pl.figure()
#fig.set_size_inches(5,3)

for k in range(5):
    path = OU.path(T, reset=X_0)
    pl.plot(ts, path, 'blue')
pl.plot(ts, mean+2*np.sqrt(var), 'r', linestyle='dashed', 
        lw=1., label=r'$\mu \pm 2 \sigma$')
pl.plot(ts, mean-2*np.sqrt(var), 'r', linestyle='dashed', 
         lw=1.)
pl.ylim(-3,3)
pl.legend(loc='lower right', frameon=False, prop={'size':12})
pl.show()

