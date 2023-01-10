from antialigners import *
from scipy.stats import gaussian_kde

plt.rcParams['text.usetex'] = True
plt.rcParams['font.size'] = '12'

def main():
    #initialize, x, y, theta
    coord = np.random.rand(N,3)
    for i in range(len(coord)):
        coord[i][0] *= L
        coord[i][1] *= L
        coord[i][2]  = 2 * np.pi * (coord[i][2] - 0.5)
        
    x = np.array([item[0] for item in coord])
    y = np.array([item[1] for item in coord])
    theta = np.array([item[2] for item in coord])
        
    #plot particle distribution in 2D space: initial state
    fig1 = plt.figure(figsize=(8,8), dpi=80)
    ax = fig1.gca()
    ax.set(xlim=(0, L), ylim=(0, L))
    # ax.set_xlabel(r'x')
    # ax.set_ylabel(r'y')
    ax.set_xlabel(r'\textbf{x}')
    ax.set_ylabel(r'\textbf{y}')
    ax.set_aspect('equal')	
    plt.title(r'N = {} particles, R = {}, $\eta$ = {}. Initial State'.format(N,R,eta))      
    plt.quiver(x, y, np.cos(theta), np.sin(theta), np.arctan2(np.sin(theta), np.cos(theta)), angles='xy', scale_units='xy', scale=0.5, pivot='mid', cmap='hsv_r')
    plt.clim(-np.pi,np.pi)
    cbar = plt.colorbar()
    cbar.ax.set_ylabel('orientation', rotation=270)  
    plt.show()     
    plt.savefig('antialignersI.png',bbox_inches='tight',dpi=100)
        
    #simulate
    simulate(coord)
    
    x = np.array([item[0] for item in coord])
    y = np.array([item[1] for item in coord])
    theta = np.array([item[2] for item in coord])
    
    
    #plot particle distribution in 2D space: steady state
    fig1 = plt.figure(figsize=(8,8), dpi=80)
    ax = fig1.gca()
    ax.set(xlim=(0, L), ylim=(0, L))
    # ax.set_xlabel(r'x')
    # ax.set_ylabel(r'y')
    ax.set_xlabel(r'\textbf{x}')
    ax.set_ylabel(r'\textbf{y}')
    ax.set_aspect('equal')	    
    plt.title(r'N = {} particles, R = {}, $\eta$ = {}. Steady State'.format(N,R,eta))      
    plt.quiver(x, y, np.cos(theta), np.sin(theta), np.arctan2(np.sin(theta), np.cos(theta)), angles='xy', scale_units='xy', scale=0.5, pivot='mid', cmap='hsv_r')
    plt.clim(-np.pi,np.pi)
    cbar = plt.colorbar()
    cbar.ax.set_ylabel('orientation', rotation=270)  
    plt.show()     
    plt.savefig('antialignersS.png',bbox_inches='tight',dpi=100)
    
    
    #plot histogram for theta distribution
    fig2 = plt.figure()
    ax2 = fig2.gca()        
    ax2.set_xlabel(r'${\bf{\theta}}$')
    ax2.set_ylabel(r'\textbf{frequency}')    
    density = gaussian_kde(theta)
    t = np.linspace(-4, 4, 1000)
    density.covariance_factor = lambda : 0.1 #Smoothing parameter
    density._compute_covariance()
    plt.title('Histogram for orientation distribution \n N = {} particles, R = {}, $\eta$ = {}'.format(N,R,eta))
    plt.plot(t, density(t))
    plt.show()
    plt.savefig('thetaDist.png',dpi=100)
    
    # fig3 = plt.figure()
    # ax3 = fig3.gca()
    # counts, bins = np.histogram(theta)
    # plt.hist(bins[:-1], bins, weights=counts)
    # ax3.set_xlabel(r'$\theta$')
    # ax3.set_ylabel(r'frequency')   
    # plt.title('Histogram for orientation distribution \n N = {} particles, R = {}, $\eta$ = {}'.format(N,R,eta))
    # plt.show()
    # plt.savefig('thetaHist.png',dpi=100)
    
    

if __name__ == "__main__":
    main()
