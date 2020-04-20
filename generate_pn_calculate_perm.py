import sys
import os
import random
import numpy as np
import matplotlib.pyplot as plt

current_path = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.join(current_path, '../tmp/pmeal/OpenPNM/'))
sys.path.append(os.path.join(current_path, '../tmp/pmeal/porespy/'))

import porespy as ps
from functions.calculate_perm import calculate_perm

# This codel allows generating artificial PN model and calculate permeability

with open('out/plotting_data.csv', 'w') as file:
    file.write('porosity,' + 'k_pnm,' + 'q_pnm,' + 'k_edm,' +
               'q_edm,' + 'radius_pore_avg,' + 'radius_pore_std,' + 'radius_throat_avg,' +
               'radius_throat_std,' + 'length_throat_avg,' + 'length_throat_std,' +
               'connection_n_avg,' + 'connection_n_std,' + '\n')

    im_n = 1000
    i = 0

    dims = [200, 200, 200]

    while True:

        # Random generator of porosity and blobiness based on gauss
        poro = random.uniform(0.15, 0.45)
        blob = random.uniform(0.6, 2.2)
        voxel_size = random.uniform(1.E-6, 2.E-5)

        if 0.15 <= poro <= 0.35 and 0.6 <= blob <= 2.2:

            if i > im_n - 1:
                break

            im = ps.generators.blobs(shape=dims, porosity=poro, blobiness=blob)
            # np.save(f'out/im_{i}', im)
            # plt.imshow(im[:, :, int(dims[0] / 2)])
            # plt.axis('off')
            # plt.show()

            # exporting generated image to VTK format
            # ps.io.to_vtk(im, path=f'out/im_{i}', divide=False,
            #              downsample=False, voxel_size=1E-6, vox=False)

            # extract pore network using snow algorithm
            net = ps.networks.snow(im, voxel_size=voxel_size)

            # exporting pore network from generated image
            # ps.io.to_openpnm(net, filename=f'out/pn_{i}')

            # calculate permeability
            Dict, min_cut = calculate_perm(net, pn_name=f'out/pn_{i}')

            file.write(str(poro) + ',' + str(Dict['K_pnm']) +
                       ',' + str(Dict['Q_pnm']) + ',' + str(Dict['K_edm']) +
                       ',' + str(Dict['Q_edm']) + ',' + str(Dict['por_rad_avg']) +
                       ',' + str(Dict['por_rad_std']) + ',' + str(Dict['thr_rad_avg']) +
                       ',' + str(Dict['thr_rad_std']) + ',' + str(Dict['thr_len_avg']) +
                       ',' + str(Dict['thr_len_std']) + ',' + str(Dict['conn_num_avg']) +
                       ',' + str(Dict['conn_num_std']) + '\n')
            print()
            print('i', i)

            i += 1
