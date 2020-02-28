import sys
import os
import pickle

current_path = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.join(current_path, '/Users/z5087785/data/projects/tmp/pmeal/OpenPNM/'))
sys.path.append(os.path.join(current_path, '/Users/z5087785/data/projects/tmp/pmeal/porespy/'))

import porespy as ps
import matplotlib.pyplot as plt
import imageio
import scipy as sp
import scipy.ndimage as spim
import openpnm as op
from porespy.filters import find_peaks, trim_saddle_points, trim_nearby_peaks
from skimage.morphology import watershed
from porespy.tools import randomize_colors

import numpy as np

# This demo project allows to create a pore network using PoreSPY and export it for later usage in OpenPNM

# Load net file produced by PoreSpy into OpenPNM
net = op.io.Dict.load(f'PNTest_1.net')

# Creating network dictionary which stores the required properties
pn = op.network.GenericNetwork()
pn.update(net)

# Double-check isolating pores

h = pn.check_network_health()
op.topotools.trim(network=pn, pores=h['trim_pores'])

prj = pn.project

# permeability calc

# Adding required fluid props and calculate hydraulic conductance
water = op.phases.Water(network=pn)
water.add_model(propname='throat.hydraulic_conductance',
                model=op.models.physics.hydraulic_conductance.hagen_poiseuille)

water['pore.viscosity'] = 10e-4
water['throat.viscosity'] = 10e-4

# Option to calculate hydraulic conductance manually
# water['throat.hydraulic_conductance'] = np.pi * R ** 4 / (8 * mu_w * L)

# In/out pressures
Pout = 101325
Pin = 2 * Pout

# Specifying boundary conditions and run the solver
flow = op.algorithms.StokesFlow(network=pn, phase=water)
flow.set_value_BC(pores=pn.pores('left'), values=Pin)
flow.set_value_BC(pores=pn.pores('right'), values=Pout)
flow.run()

# Calculate flow length and are
Lx = sp.amax(pn['pore.coords'][:, 0]) - sp.amin(pn['pore.coords'][:, 0])
A = Lx * Lx  # Since the network is cubic Lx = Ly = Lz

# Add pore pressure to output file
pn['pore.pressure'] = flow['pore.pressure']

# Calc total flow rate
Q = flow.rate(pores=pn.pores('left'))

# Calc permeability and output permeability and flow rate
K_w = flow.calc_effective_permeability(domain_area=A, domain_length=Lx)
print("K_w = ", K_w)
print('\n')
print("Q=", Q)

# Save PN data into VTK file
prj.export_data(filename='PNTest_1', filetype='vtk')
# Save PN data into CSV file
op.io.CSV.save(pn, filename='PNTest_1')

# Find coeffs for paraview draw and output it to file
throat_radius_min = min(pn['throat.diameter'] / 2)
max_min_ratio = max(pn['throat.diameter']) / min(pn['throat.diameter'])

with open('paraview_params.txt', 'w') as file:
    file.write(str(throat_radius_min) + '\n')
    file.write(str(max_min_ratio) + '\n')
