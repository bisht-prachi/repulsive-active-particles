from antialigners import *

plt.rcParams['text.usetex'] = True
plt.rcParams['font.size'] = '28'
plt.rcParams['text.latex.preamble'] = [r"\usepackage{amsmath}"]

def main():
    #initialize, x, y, theta
    coord = np.random.rand(N,3)
    for i in range(len(coord)):
        coord[i][0] *= L
        coord[i][1] *= L
        coord[i][2]  = 2 * np.pi * (coord[i][2] - 0.5)
        
    #plot particle distribution in 2D space: initial state
    x = np.array([item[0] for item in coord])
    y = np.array([item[1] for item in coord])
    theta = np.array([item[2] for item in coord])
    fig = plt.figure(figsize=(10,8))
    ax = fig.gca()
    ax.set(xlim=(0, L), ylim=(0, L))
    ax.set_xlabel(r'x')
    ax.set_ylabel(r'y')
    ax.set_aspect('equal')	    
    plt.title(r'N = {} particles, R = {}, $\eta$ = {}. Initial State'.format(N,R,eta))      
    plt.quiver(x, y, np.cos(theta), np.sin(theta), np.arctan2(np.sin(theta), np.cos(theta)), angles='xy', scale_units='xy', scale=0.5, pivot='mid', cmap='hsv_r')
    plt.clim(-np.pi,np.pi)
    cbar = plt.colorbar()
    cbar.ax.set_ylabel(r'\textbf{$\theta$}', rotation=0)      
    plt.savefig('antialigners_initial_state.eps', format='eps',bbox_inches='tight',dpi=100)
    plt.show() 
    plt.close()
    
    #simulate till steady state
    for _ in range(Nt): 
        simulate(coord)
    
    #declare empty array to store frequency of data
    thetaDist = np.zeros(int(7/binsize), dtype=float)
    
    for _ in range(T):
        simulate(coord)
        getthetaDist(coord, thetaDist)
        
    # plot particle distribution in 2D space: steady state
    x = np.array([item[0] for item in coord])
    y = np.array([item[1] for item in coord])
    theta = np.array([item[2] for item in coord])
    fig = plt.figure(figsize=(8,8))
    ax = fig.gca()
    ax.set(xlim=(0, L), ylim=(0, L))
    ax.set_xlabel(r'x')
    ax.set_ylabel(r'y')
    ax.set_xlabel(r'\textbf{x}')
    ax.set_ylabel(r'\textbf{y}')
    ax.set_aspect('equal')	    
    plt.title(r'N = {} particles, R = {}, $\eta$ = {}. Steady State'.format(N,R,eta))      
    plt.quiver(x, y, np.cos(theta), np.sin(theta), np.arctan2(np.sin(theta), np.cos(theta)), angles='xy', scale_units='xy', scale=0.5, pivot='mid', cmap='hsv_r')
    plt.clim(-np.pi,np.pi)
    cbar = plt.colorbar()
    cbar.ax.set_ylabel(r'\textbf{$\theta$}', rotation=0)       
    plt.savefig('antialigners_steady_stateL50eta0.eps', format = 'eps', bbox_inches='tight',dpi=100)
    plt.show()  
    
    with open('thetaDistL100eta0.csv', 'w') as f:
        for a in range(len(thetaDist)):
            f.write(f"{a*binsize - np.pi},{thetaDist[a]/(N*T)}\n")
            
    #plot theta frequency plot
    fig1 = plt.figure(figsize=(8,6))
    ax1 = fig1.gca()
    ax1.set(xlim=(-3.5, 3.5))
    ax1.set_xlabel(r'\textbf{$\theta$ (rad)}')
    ax1.set_ylabel(r'\textbf{P($\theta$) }')
    plt.plot(np.arange(len(thetaDist))*binsize - np.pi, thetaDist/(N*T), marker = '.')
    plt.grid()
    plt.savefig('thetaDist.png', bbox_inches='tight',dpi=100)
    plt.show()  
    
   

if __name__ == "__main__":
    main()
