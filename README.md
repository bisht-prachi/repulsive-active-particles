# anti-aligners-spp
A model for anti-aligning self propelled particles. 
The orientation update rule is asynchronous as opposed to the synchronous update rule implemented in traditional Vicsek model. 
The particle orientation are **sequentially** updated in the first step. The average orientation of a particle's neighbourhood
is evaluated, the said particle assumes an orientation = (average + pi), thus effectuating a *repulsive* inter-particle interaction.
In the second step, all particles move simultaneously.

The steady state picture:
  Two alternating lanes consisting of particle clusters, moving in opposite directions respectively.
  

