#	Build Kinetic energy Graph; 

#	V    = (4/3)*pi*((r)**3)
#	m    = density * volume
#   E(v) = (1/2)*m*(v)**2 


import numpy as np 
import scipy.constants as CONST 
import matplotlib.pyplot as plt 


particle_radius  = 0.0005
particle_density = 1000.0


v = (4.0/3.0)*((particle_radius)**3)*np.pi
m = particle_density*v
vc = np.linspace(0, 0.1, 20)
particle_energy = 0.5*m*(vc*CONST.c)**2.0


print('\n', 'Mass: \t\t', m)
print('\n', 'Speed: \t', v)
print('\n', 'Energy: \t', particle_energy)

E_ton_TNT = particle_energy/CONST.ton_TNT 
E_kg_TNT  = 1000.0*E_ton_TNT

print('\n', 'LINSPACE: \t', vc)
print('\n', 'E_ton_TNT: \t', E_ton_TNT)
print('\n', 'E_kg_TNT: \t', E_kg_TNT)

plt.figure(num = None, figsize = (8, 2.5), dpi = 150)
plt.plot(vc, E_kg_TNT, 'r-')
plt.xlabel('Velocity of particle, v/c')
plt.ylabel('Energy of particle, kg_TNT')
plt.legend(['m={:3.2f} mg'.format(m*1e6)], loc = 'best')
plt.grid(linestyle = ':')