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

# This codel allows generating artificial PN model
n = 2
i = int(0)

while True:

    # Random generator of porosity and blobiness based on gaussian distribution
    poro = random.gauss(0.2, 0.3)
    blob = random.gauss(0.8, 1.5)

    if 0.18 <= poro <= 0.35 and 1.5 <= blob <= 2.5:

        i += 1
        if i == n:
            break

        dims = [300, 300, 300]
        im = ps.generators.blobs(shape=dims, porosity=poro, blobiness=blob)
        plt.imshow(im[:, :, 99])
        plt.axis('off')
        plt.show()

        # exporing generated image to VTK format
        ps.io.to_vtk(im, path=f'im_{i}', divide=False, downsample=False, voxel_size=1E-6, vox=False)

        net = ps.networks.snow(im, voxel_size=1.E-6)

        # exporting pore network from generated image
        ps.io.to_openpnm(net, filename=f'PNTest_{i}')
