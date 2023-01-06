"""
Adapted from pmocz/activematter-python
Philip Mocz (2021) Princeton Univeristy, @PMocz

Anti-aligning self propelled particles

"""

import matplotlib.pyplot as plt
import numpy as np
import random, time

#comment this out if latex is not installed
#plt.rcParams['text.usetex'] = True
plt.rcParams['font.size'] = '12'


np.random.seed(seed=int(time.time()))      

#simulation parameters
v0       = 1
dt       = 1
eta      = 0.5
R        = 10       
L        = 100
Nt       = 2000
N        = 10000
plotRealTime = True

def simulate(coord):      
       
       #run
       for t in range(Nt):
           #get x,y,theta
           x = np.array([[item[0]] for item in coord])
           y = np.array([[item[1]] for item in coord])
           theta = np.array([[item[2]] for item in coord])
           
           #update x,y coordinates
           x = (x + v0 * dt * np.cos(theta)) % L
           y = (y + v0 * dt * np.sin(theta)) % L                      
                 
           #update orientation. 
           #sequential update of orientation
           for i in range(N):           
               neighbors = (x-x[i])**2 + (y-y[i])**2 < R**2
               sx = np.sum(np.cos(theta[neighbors]))
               sy = np.sum(np.sin(theta[neighbors]))
               theta[i] = np.arctan2(-sy,-sx)             
               
           theta = theta + eta*(np.random.rand(N,1)-0.5)
           
           for i in range(len(coord)):
               coord[i][0] = x[i]
               coord[i][1] = y[i]
               coord[i][2]  = theta[i]            
                   
           np.random.shuffle(coord)          
               
           # if plotRealTime or (t == Nt - 1):     
           #     plt.cla()
           #     plt.quiver(x, y, np.cos(theta), np.sin(theta), np.arctan2(np.sin(theta), np.cos(theta)), angles='xy', scale_units='xy', scale=0.5, pivot='mid', cmap='hsv_r')
           #     ax.set(xlim=(0, L), ylim=(0, L))
           #     ax.set_aspect('equal')	           
           
               
       return 0
       

def main():
    #initialize, x, y, theta
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
    plt.title('N = {} particles, Steady State'.format(N))
       
    
    plt.quiver(x, y, np.cos(theta), np.sin(theta), np.arctan2(np.sin(theta), np.cos(theta)), angles='xy', scale_units='xy', scale=0.5, pivot='mid', cmap='hsv_r')
    plt.clim(-np.pi,np.pi)
    cbar = plt.colorbar()
    cbar.ax.set_ylabel('orientation', rotation=270)
    
    ax.set(xlim=(0, L), ylim=(0, L))
    ax.set_xlabel(r'x')
    ax.set_ylabel(r'y')
    ax.set_aspect('equal')	
    plt.show()     
    plt.savefig('antialigners1.png',dpi=80)
    

if __name__ == "__main__":
    main()