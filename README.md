# anti-aligners-spp
A model for anti-aligning self propelled particles. 
- The orientation update rule is asynchronous as opposed to the synchronous update rule implemented in traditional Vicsek model. 
* The particle orientation are **sequentially** updated in the first step. The average orientation of a particle's neighbourhood - defined as a circle of radius R centered around the particle - is evaluated and the said particle assumes an orientation = (average + pi). The *pi* terms effectuates a *repulsive* inter-particle interaction.
+ In the second step, all particles move simultaneously.
+ Third step, the particle order is shuffled randomly

The steady state picture:
  Two alternating lanes consisting of particle clusters, moving in opposite directions respectively.
  
![antialignersI](https://user-images.githubusercontent.com/103419553/211536292-5a4184bd-49ff-4389-aa71-d00d3d203d9f.png)
![antialigners](https://user-images.githubusercontent.com/103419553/211529382-aad67015-0c1c-46af-ba1a-b7a62d930ba8.png)
![thetaDist](https://user-images.githubusercontent.com/103419553/211529409-d5d69e85-4f68-4f91-badb-c51089e6561d.png)
