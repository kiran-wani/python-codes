#A simple code for multiple gaussian distribution generation and plotting and then writing it to a text file.
#Just for trial and error
#Writen by Vivek Jha
#18/04/2018
# JRF at ARIES Nainital.

import numpy as np
from matplotlib import pyplot as plt
import csv
sigma=[2.5,2,1.5,3,3.5,4,2,3,2.4,2,3,1,1.5,2.5,4,3.5,2.4,4]
mu=range(0,320,20)
x= np.linspace(0, 350, 10000)
y=0
def gauss(x, sigma,mu): 
    return 1.0/(sigma*np.sqrt(2*np.pi))*np.exp(-(x-mu)**2/(2*sigma**2))

for i in range(0,16):
	y1=gauss(x,sigma[i],mu[i])	
	y=y+y1
plt.plot(x,y)	
plt.show()


zip(x,y)
with open ("data.csv", "w") as f:
	writer= csv.writer(f, delimiter=" ")
	writer.writerows(zip(x,y))
	quit()




