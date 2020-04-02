import numpy as np
import pandas as pd


# Export PN and min-cut data

def total_pn_export(pore_network, key_left, key_right, save_to_csv=False, name='sample'):
    pores = pd.DataFrame(columns=['id', 'x', 'y', 'z', 'left', 'right'])
    pores.id = np.arange(len(pore_network['pore.coords']))
    pores.x = pore_network['pore.coords'][:, 0]
    pores.y = pore_network['pore.coords'][:, 1]
    pores.z = pore_network['pore.coords'][:, 2]
    pores.left = pore_network['pore.' + key_left]
    pores.right = pore_network['pore.' + key_right]
    pores.index = pores.id
    if save_to_csv:
        pores.to_csv(name + '_pores.csv', index=False)

    throats = pd.DataFrame(columns=['id', 'pore_a', 'pore_b', 'conductance',
                                    'length', 'radius', 'velocity', 'min_cuts_in_net'])
    throats.id = np.arange(len(pore_network['throat.conns']))
    throats.pore_a = pore_network['throat.conns'][:, 0]
    throats.pore_b = pore_network['throat.conns'][:, 1]
    throats.conductance = pore_network['throat.hydraulic_conductance']
    throats.index = throats.id
    throats.length = pore_network['throat.total_length']
    throats.radius = pore_network['throat.diameter'] / 2.
    throats.velocity = pore_network['throat.velocity']
    throats.min_cuts_in_net = pore_network['throat.min_cuts_in_net']
    if save_to_csv:
        throats.to_csv(name + '_throats.csv', index=False)

    return pores, throats
