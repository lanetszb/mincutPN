import sys
import os

current_path = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.join(current_path, '../max_radius'))
sys.path.append(os.path.join(current_path, '../tmp/pmeal/OpenPNM/'))
sys.path.append(os.path.join(current_path, '../tmp/pmeal/porespy/'))

import porespy as ps
import matplotlib.pyplot as plt
import numpy as np

from extract_pn import read_raw_file
from extract_pn import extract_pn
from functions.calculate_perm import calculate_perm
from calculate_max_radius import calculate_max_radius

hdm_file_names = ['bead_pack_512.mhd', 'castle_512.mhd',
                  'gambier_512.mhd', 'lrc32_512.mhd']

base_path_in = 'samples'
base_path_out = 'out'

for hdm_file_name in hdm_file_names:
    im, dims, voxel_sizes, case_name = read_raw_file(base_path_in, hdm_file_name)
    voxel_size = voxel_sizes[0]
    net = extract_pn(im, voxel_size, case_name)
    flow_params, min_cut_edges_id, min_cut_radii = calculate_perm(net,
                                                                  base_path_out + '/' + case_name)
    np.savetxt(base_path_out + '/' + case_name + '_min_cut_radii.txt', min_cut_radii)
    input_output_im = np.zeros_like(im, dtype=int)
    input_output_im[0, :, :] = im[0, :, :]
    input_output_im[dims[0] - 1, :, :] = im[dims[0] - 1, :, :] * 2
    result = calculate_max_radius(im, voxel_size, input_output_im,
                                  base_path_out + '/' + case_name + '_max_radius.txt')
