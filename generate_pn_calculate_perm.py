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

with open('out/perm_comparison.csv', 'w') as file:
    file.write('Porosity,' + 'K_pnm,' + 'Q_pnm,' + 'K_edm,' + 'Q_edm' + '\n')

    im_n = 1
    i = 0

    dims = [200, 200, 200]
    voxel_list = [1.E-5, 4.E-5]

    while True:

        # Random generator of porosity and blobiness based on gauss
        poro = random.gauss(0.15, 0.45)
        blob = random.gauss(0.6, 2.2)
        voxel_size = random.choice(voxel_list)

        if 0.15 <= poro <= 0.35 and 0.6 <= blob <= 2.2:

            if i > im_n - 1:
                break

            im = ps.generators.blobs(shape=dims, porosity=poro, blobiness=blob)
            np.save(f'out/im_{i}', im)
            # plt.imshow(im[:, :, int(dims[0] / 2)])
            # plt.axis('off')
            # plt.show()

            # exporting generated image to VTK format
            ps.io.to_vtk(im, path=f'out/im_{i}', divide=False,
                         downsample=False, voxel_size=1E-6, vox=False)

            # extract pore network using snow algorithm
            net = ps.networks.snow(im, voxel_size=voxel_size)

            # exporting pore network from generated image
            ps.io.to_openpnm(net, filename=f'out/pn_{i}')

            # calculate permeability
            flow_params, min_cut = calculate_perm(net, pn_name=f'out/pn_{i}')

            file.write(str(poro) + ',' + str(flow_params[0]) + ',' + str(
                flow_params[1]) + ','
                       + str(flow_params[2]) + ',' + str(flow_params[3]) + '\n')
            print()
            print('i', i)

            i += 1
