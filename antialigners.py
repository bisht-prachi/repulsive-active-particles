"""
Adapted from pmocz/activematter-python
Philip Mocz (2021) Princeton Univeristy, @PMocz

Anti-aligning self propelled particles

"""

import matplotlib.pyplot as plt
import numpy as np
import random, time

np.random.seed(seed=int(time.time()))      

#simulation parameters
v0       = 1
dt       = 1
eta      = 0
R        = 10       
L        = 200
Nt       = 5000
N        = 40000
T        = 5
binsize  = 0.1
plotRealTime = True

def simulate(coord):    
    # fig = plt.figure(figsize=(4,4), dpi=80)
    # ax = plt.gca()
    
    #run
     #get x,y,theta
     x = np.array([[item[0]] for item in coord])
     y = np.array([[item[1]] for item in coord])
     theta = np.array([[item[2]] for item in coord])    
     
     #update x,y coordinates 
     x = (x + v0 * dt * np.cos(theta)) % L
     y = (y + v0 * dt * np.sin(theta)) % L      
                     
     for i in range(N):
         #update orientation. 
         neighbors = (x-x[i])**2 + (y-y[i])**2 < R**2
         sx = np.sum(np.cos(theta[neighbors]))
         sy = np.sum(np.sin(theta[neighbors]))
         theta[i] = np.arctan2(-sy,-sx) + eta*(random.uniform(0,1)-0.5)             
     
     #update coordinates
     for i in range(len(coord)):
         coord[i][0] = x[i]
         coord[i][1] = y[i]
         coord[i][2]  = theta[i]            
         
     #shuffle the particle order        
     np.random.shuffle(coord)          
         
     # if plotRealTime or (t == Nt - 1):     
     #     plt.cla()
     #     plt.quiver(x, y, np.cos(theta), np.sin(theta), np.arctan2(np.sin(theta), np.cos(theta)), angles='xy', scale_units='xy', scale=0.5, pivot='mid', cmap='hsv_r')
     #     ax.set(xlim=(0, L), ylim=(0, L))
     #     ax.set_aspect('equal')	           
     
            
     return 0
 
def getthetaDist(coord, thetaDist):    
    theta = np.array([[item[2]] for item in coord])
    for i in range(len(theta)):
        a = (theta[i] + np.pi) % (2 * np.pi)
        a /= binsize
        thetaDist[int(a)] += 1
            
     
   
def getvelCorr(coord, velCorr,counter):
    x = np.array([[item[0]] for item in coord])
    y = np.array([[item[1]] for item in coord])
    theta = np.array([[item[2]] for item in coord])

   
    for i in range(len(theta)):
    # i = random.randint(0,N-1)
        for j in range(len(theta)):
            dx = abs(x[j] - x[i]) 
            dy = abs(y[j] - y[i])
            r = np.sqrt(dx**2 + dy**2)
            if r > np.sqrt(2)*0.5*L: r = np.sqrt(2)*L - r
            bin = int(r/binsize)
            counter[bin] += 1
            velCorr[bin] += (np.cos(theta[i]) * np.cos(theta[j]) + np.sin(theta[i]) * np.sin(theta[j]))
            

      
if __name__ == "__main__":
    coord = np.random.rand(N,3)
    for i in range(len(coord)):
        coord[i][0] *= L
        coord[i][1] *= L
        coord[i][2]  = 2 * np.pi * (coord[i][2] - 0.5)
        
    simulate(coord)
    x = np.array([[item[0]] for item in coord])
    y = np.array([[item[1]] for item in coord])
    theta = np.array([[item[2]] for item in coord])

    fig = plt.figure(figsize=(8,8), dpi=80)
    ax = plt.gca()
    plt.title(r'N = {} particles, R = {}, eta = {}. Initial State'.format(N,R,eta))      
    plt.quiver(x, y, np.cos(theta), np.sin(theta), np.arctan2(np.sin(theta), np.cos(theta)), angles='xy', scale_units='xy', scale=0.5, pivot='mid', cmap='hsv_r')
    plt.clim(-np.pi,np.pi)
    cbar = plt.colorbar()
    cbar.ax.set_ylabel(r'theta', rotation=0)  
    ax.set(xlim=(0, L), ylim=(0, L))
    ax.set_aspect('equal')	           
