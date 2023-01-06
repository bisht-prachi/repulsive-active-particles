from antialigners import *

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
    plt.savefig('antialigners2.png',dpi=80)
    

if __name__ == "__main__":
    main()
