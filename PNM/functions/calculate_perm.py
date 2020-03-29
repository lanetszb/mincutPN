import sys
import os

current_path = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.join(current_path, '../../tmp/pmeal/OpenPNM/'))
sys.path.append(os.path.join(current_path, '../../tmp/pmeal/porespy/'))

import openpnm as op

from functions.edmonds_karp_export import edmonds_karp_export
from functions.edmonds_karp import calculate_edmonds_karp

import numpy as np


def calculate_perm(net, pn_name='pn'):
    # net can be loaded as op.io.Dict.load(net_name)

    # Creating network dictionary which stores the required properties
    pn = op.network.GenericNetwork()
    pn.update(net)

    # Double-check isolating pores
    h = pn.check_network_health()
    op.topotools.trim(network=pn, pores=h['trim_pores'])

    # Adding required fluid props and calculate hydraulic conductance
    water = op.phases.Water(network=pn)
    water.add_model(propname='throat.hydraulic_conductance',
                    model=op.models.physics.hydraulic_conductance.hagen_poiseuille)

    # Set in/out pressures
    Pout = 101325
    Pin = 2 * Pout
    dP = Pin - Pout

    # Set viscosity
    viscosity = 10e-4
    water['pore.viscosity'] = viscosity
    water['throat.viscosity'] = viscosity

    water['throat.hydraulic_conductance'] = np.pi * pn['throat.diameter'] ** 4 / (
            128 * viscosity * pn['throat.total_length'])

    # Option to calculate hydraulic conductance manually
    # water['throat.hydraulic_conductance'] = np.pi * R ** 4 / (8 * mu_w * L)

    # Specifying boundary conditions and run the solver
    flow = op.algorithms.StokesFlow(network=pn, phase=water)
    key_left = 'left'
    key_right = 'right'
    flow.set_value_BC(pores=pn.pores(key_left), values=Pin)
    flow.set_value_BC(pores=pn.pores(key_right), values=Pout)
    flow.run()

    # Calculate flow length
    Lx = np.amax(pn['pore.coords'][:, 0]) - np.amin(pn['pore.coords'][:, 0])
    L = Lx
    # since the network is cubic Lx = Ly = Lz
    A = Lx * Lx

    # Add pore pressure to output csv file
    pn['pore.pressure'] = flow['pore.pressure']

    # Add hydraulic conductance to output csv filr
    pn['throat.hydraulic_conductance'] = water['throat.hydraulic_conductance']

    # Calc total flow rate
    Q_pnm = flow.rate(pores=pn.pores('left'))[0]

    # Calc permeability and output permeability and flow rate using PNM
    K_pnm = flow.calc_effective_permeability(domain_area=A, domain_length=Lx)[0]
    print("K_pnm", K_pnm)
    print("Q_pnm", Q_pnm)

    # Save PN data into VTK file
    # prj = pn.project
    # prj.export_data(filename=pn_name, filetype='vtk')
    # Save PN data into CSV file
    # op.io.CSV.save(pn, filename=pn_name)

    # Find coeffs for paraview draw and output it to file
    throat_radius_min = min(pn['throat.diameter'] / 2)
    max_min_ratio = max(pn['throat.diameter']) / min(pn['throat.diameter'])

    with open('visualization/paraview_params.txt', 'w') as file:
        file.write(str(throat_radius_min) + '\n')
        file.write(str(max_min_ratio) + '\n')

    pores, throats = edmonds_karp_export(pn, water, key_left, key_right, save_to_csv=False)

    R, min_cut_edges_id = calculate_edmonds_karp(pores, throats, viscosity, A, dP, L)

    K_edm = R['in_a']['in_b']['flow'] / A
    Q_edm = R['in_a']['in_b']['flow'] * dP / L / viscosity

    flow_params = np.array([K_pnm, Q_pnm, K_edm, Q_edm])

    return flow_params
