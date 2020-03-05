import numpy as np
import pandas as pd
import scipy as sp
import csv

import os


# Constracting output data for PNFlow toolbox

def savemhd(file_name, image, dims,
            voxel_sizes=(1., 1., 1.), offsets=(0., 0., 0.)):
    dim_size = str(dims[0]) + ' ' + str(
        dims[1]) + ' ' + str(dims[2])

    box_size_h_0 = offsets[0] + dims[0] * voxel_sizes[0]
    box_size_h_1 = offsets[1] + dims[1] * voxel_sizes[1]
    box_size_h_2 = offsets[2] + dims[2] * voxel_sizes[2]

    box_size = str(offsets[0]) + ' ' + str(box_size_h_0) + ' '
    box_size += str(offsets[1]) + ' ' + str(box_size_h_1) + ' '
    box_size += str(offsets[2]) + ' ' + str(box_size_h_2)

    image_arr = sp.array(image, dtype=np.int32)
    head = 'ascii\n3uc\n' + dim_size + '\n' + box_size

    np.savetxt(file_name + '.dat', image_arr, fmt='%1u',
               header=head, comments='')

    image_arr.astype('bool').tofile(file_name + '.raw')

    with open(file_name + '.mhd', 'w') as f:
        f.write('ObjectType = Image\n')
        f.write('ElementType = MET_UCHAR\n')
        f.write('NDims = 3\n\n')

        f.write('DimSize = ' + dim_size + '\n')

        element_spacing = str(voxel_sizes[0]) + ' ' + str(
            voxel_sizes[1]) + ' ' + str(voxel_sizes[2])
        f.write('ElementSpacing = ' + element_spacing + '\n')

        offset = str(offsets[0]) + ' ' + str(
            offsets[1]) + ' ' + str(offsets[2])
        f.write('Offset = ' + offset + '\n')

        f.write('ElementDataFile = ' + file_name + '.raw\n')
        f.write('threshold 1 1 ' + '\n')


# Path for PN data output
path = r'./out/'


# === Pore dictionary ===


def form_pore_data(pore_network):
    pore_dict = dict.fromkeys(['pore_list', 'conn_number', 'pore_diameter', 'x_coord', 'y_coord', 'y_coord'])

    # Adding pore indexes
    pore_list = np.arange(len(pore_network['pore.coords'])).tolist()
    pore_dict['pore_list'] = pore_list

    # Adding pore coords one by one

    x_coord = [item[0] for item in pore_network['pore.coords']]
    y_coord = [item[1] for item in pore_network['pore.coords']]
    z_coord = [item[2] for item in pore_network['pore.coords']]

    pore_dict['x_coord'] = x_coord
    pore_dict['y_coord'] = y_coord
    pore_dict['z_coord'] = z_coord

    # Adding pore diameter

    pore_dict['pore_diameter'] = pore_network['pore.diameter'].tolist()

    # Calculating pore connections

    pore_conns = [[] for i in range(len(pore_list))]

    for i in range(len(pore_list)):
        for j in range(len(pore_network['throat.conns'])):
            if i == pore_network['throat.conns'][j][0]:
                pore_conns[i].append(pore_network['throat.conns'][j][1])
            if i == pore_network['throat.conns'][j][1]:
                pore_conns[i].append(pore_network['throat.conns'][j][0])

    # Calculating connection number

    conn_number = []

    for i in range(len(pore_list)):
        conn_number.append(len(pore_conns[i]))

    # Adding connection number

    pore_dict['conn_number'] = conn_number

    pore_dict = pd.DataFrame.from_dict(pore_dict)

    # pore_dict['conn_indices'] = pore_dict['conn_indices'].astype(str) \
    #     .str.replace("[", "").str.replace("]", "")

    # Converting pores data to pandas and writing into csv file

    pore_dict.to_csv(path + 'pores_data.csv', index=False)


def form_throat_data(pore_network, liq_model):
    # === Throat dictionary ===
    throat_dict = dict.fromkeys(['throat_list', 'pore_i', 'pore_j',
                                 'throat_diameter', 'throat_length'])

    # Adding throat indexes
    throat_list = np.arange(len(pore_network['throat.conns'])).tolist()
    throat_dict['throat_list'] = throat_list

    # Adding connected pores
    pore_i = [item[0] for item in pore_network['throat.conns']]
    pore_j = [item[1] for item in pore_network['throat.conns']]

    throat_dict['pore_i'] = pore_i
    throat_dict['pore_j'] = pore_j

    # Adding throat diameter
    throat_dict['throat_diameter'] = pore_network['throat.diameter'].tolist()
    # throat_dict['throat_diameter'] = pore_network['throat.equivalent_diameter'].tolist()

    # Adding throat length
    throat_dict['throat_length'] = pore_network['throat.length'].tolist()

    # Adding throat hydraulic conductance
    throat_dict['hydr_cond'] = liq_model['throat.hydraulic_conductance'].tolist()

    # Converting throat data to pandas and writing into csv file
    throat_dict = pd.DataFrame.from_dict(throat_dict)

    throat_dict.to_csv(path + 'pore_throats.csv', index=False)


# === Boundary pores dictionary ===
def form_boudnary_pores(pore_network):
    pore_left_x = pore_network['pore.left']
    pore_right_x = pore_network['pore.right']

    pore_front_y = pore_network['pore.front']
    pore_back_y = pore_network['pore.back']

    pore_top_z = pore_network['pore.top']
    pore_bot_z = pore_network['pore.bottom']

    boundary_pores = {}

    boundary_pores['pore_left_x'] = pore_left_x.tolist()
    boundary_pores['pore_right_x'] = pore_right_x.tolist()

    boundary_pores['pore_front_y'] = pore_front_y.tolist()
    boundary_pores['pore_back_y'] = pore_back_y.tolist()

    boundary_pores['pore_top_z'] = pore_top_z
    boundary_pores['pore_bot_z'] = pore_bot_z

    boundary_pores = pd.DataFrame.from_dict(boundary_pores)

    boundary_pores.to_csv(path + 'boundary_pores.csv', index=False)


def form_thorat_hydraulic_conductance(liquid_model):
    # for i in range(len(liquid_model['throat.hydraulic_conductance'])):
    #     if liquid_model['throat.hydraulic_conductance'][i] < 0:
    #         liquid_model['throat.hydraulic_conductance'][i] * -1

    thorat_hydraulic_conductance = {}

    thorat_hydraulic_conductance['hydr_cond'] = liquid_model['throat.hydraulic_conductance'].tolist()
    thorat_hydraulic_conductance = pd.DataFrame.from_dict(thorat_hydraulic_conductance)

    thorat_hydraulic_conductance.to_csv(path + 'hydraulic_conductance.csv', index=False)
