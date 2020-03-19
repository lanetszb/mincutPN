import sys
import os
import random
import imageio
import numpy as np

current_path = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.join(current_path, '../../tmp/pmeal/OpenPNM/'))
sys.path.append(os.path.join(current_path, '../../tmp/pmeal/porespy/'))

import porespy as ps
import matplotlib.pyplot as plt
import scipy as sp
import scipy.ndimage as spim
import openpnm as op
from porespy.filters import find_peaks, trim_saddle_points, trim_nearby_peaks
from skimage.morphology import watershed

from porespy.tools import randomize_colors

from calc_abs_perm_func import calculate_abs_perm

# This codel allows generating artificial PN model

with open('perm_comparison.csv', 'w') as file:
    file.write('Porosity,' + 'K_pnm,' + 'Q_pnm,' + 'K_fulk,' + 'Q_fulk' + '\n')

    n = 10
    i = int(-1)

    while True:

        # Random generator of porosity and blobiness based on gaussian distribution
        poro = random.gauss(0.15, 0.45)
        blob = random.gauss(0.6, 2.2)

        if 0.15 <= poro <= 0.35 and 0.6 <= blob <= 2.2:

            i += 1
            if i == n:
                break

            dims = [200, 200, 200]
            im = ps.generators.blobs(shape=dims, porosity=poro, blobiness=blob)
            # plt.imshow(im[:, :, int(dims[0] / 2)])
            # plt.axis('off')
            # plt.show()

            # exporing generated image to VTK format
            # ps.io.to_vtk(im, path=f'im_{i}', divide=False, downsample=False, voxel_size=1E-6, vox=False)

            net = ps.networks.snow(im, voxel_size=1.E-5)

            # exporting pore network from generated image
            # ps.io.to_openpnm(net, filename=f'PNTest_{i}')

            pn = op.network.GenericNetwork()
            pn.update(net)

            flow = calculate_abs_perm(net)

            file.write(str(poro) + ',' + str(flow[0]) + ',' + str(flow[1]) + ','
                       + str(flow[2]) + ',' + str(flow[3]) + '\n')

            print('\n')
            print('i= ', i)
