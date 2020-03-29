import sys
import os
import pickle

current_path = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.join(current_path, '/Users/bigelk/data/tmp/pmeal/OpenPNM/'))
sys.path.append(os.path.join(current_path, '/Users/bigelk/data/tmp/pmeal/porespy/'))

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

# This function allows exporting and processing segmenting image from .raw file

def read_raw_file(raw_file_name):
    dim_file_name = raw_file_name[0:-4] + '.txt'

    with open(dim_file_name, 'r') as dim_file:
        line = dim_file.readline()
        dims = list()
        for word in line.split():
            dims.append(int(word))
        dims.reverse()

    with open(raw_file_name, 'rb') as raw_file:
        data = list(raw_file.read())

    image = np.reshape(np.array(data, dtype=bool), (dims[0], dims[1], dims[2]))
    image = np.transpose(image)

    return image


# This function allows to flip void/rock phases if needed
def flip_values(data, val1, val2):
    data = np.where(data == val1, -999.25, data)
    data = np.where(data == val2, val1, data)
    data = np.where(data == -999.25, val2, data)
    return data


# im_dat = read_dat_file('Berea.dat')
im = read_raw_file('segmented_Gambier_512.raw')

# Plots one layer of the image in 2D
plt.imshow(im[0])
plt.show()

im = flip_values(im, 0, 1).astype(bool)

# Runs pore network extraction algorithm
net = ps.networks.snow(im, voxel_size=3.024e-6)

# Exporting network for openpnm
ps.io.to_openpnm(net, filename='gambier_limestone')

# Opportunity to graphically match segmented image and produced PN (does not seem to work properly)

# im = ps.tools.align_image_with_openpnm(im)
# imageio.mimsave('extracted_network.tif', sp.array(im, dtype=np.int32))
