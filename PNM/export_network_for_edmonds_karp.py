import numpy as np
import pandas as pd
import os

def export_network_to_csv(pore_network, liq_model, save_to_csv=False):
    pores = pd.DataFrame(columns=['id', 'x', 'y', 'z','x_left','x_right','y_left','y_right','z_left','z_right'])         
    pores.id = pore_network['pore._id']
    pores.x = pore_network['pore.coords'][:,0]
    pores.y = pore_network['pore.coords'][:,1]
    pores.z = pore_network['pore.coords'][:,2]
    pores.x_left = pore_network['pore.left']
    pores.x_right = pore_network['pore.right']
    pores.y_left = pore_network['pore.front']
    pores.y_right = pore_network['pore.back']
    pores.z_left = pore_network['pore.top']
    pores.z_right = pore_network['pore.bottom']
    pores.index = pores.id
    if save_to_csv:
        pores.to_csv('pores.csv', index=False)    
    
    throats = pd.DataFrame(columns=['id', 'pore_a', 'pore_b', 'conductance', 'length'])
    throats.id = pore_network['throat._id']
    throats.pore_a = pore_network['throat.conns'][:,0]
    throats.pore_b = pore_network['throat.conns'][:,1]
    throats.conductance = liq_model['throat.hydraulic_conductance']
    throats.index = throats.id
    throats.length = pore_network['throat.total_length']
    if save_to_csv:
        throats.to_csv('throats.csv', index=False)
    
    return pores, throats



