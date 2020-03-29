import sys
import os

current_path = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.join(current_path, '../tmp/pmeal/OpenPNM/'))
sys.path.append(os.path.join(current_path, '../tmp/pmeal/porespy/'))

import porespy as ps
import matplotlib.pyplot as plt
import numpy as np
import re


# This demo project allows to create a pore network using PoreSPY
# and export it for later usage in OpenPNM

# This function allows to flip void/rock phases if needed
def flip_values(data, val1, val2):
    data = np.where(data == val1, -999.25, data)
    data = np.where(data == val2, val1, data)
    data = np.where(data == -999.25, val2, data)
    return data


# This function allows exporting and processing segmenting image from .raw file

def read_raw_file(base_path, mhd_file_name):
    dims = list()
    voxel_sizes = list()
    raw_file_name = str()
    with open(base_path + '/' + mhd_file_name, 'r') as file:
        while True:
            line = file.readline()
            if not line:
                break
            words = re.split(' = | |\n', line)
            words.pop(-1)
            key = words.pop(0)
            if key == 'DimSize':
                for word in words:
                    dims.append(int(word))
                dims.reverse()
            elif key == 'ElementSize':
                for word in words:
                    voxel_sizes.append(float(word))
                voxel_sizes.reverse()
            elif key == 'ElementDataFile':
                raw_file_name = str(words.pop(0))

    with open(base_path + '/' + raw_file_name, 'rb') as raw_file:
        data = list(raw_file.read())

    image = np.reshape(np.array(data, dtype=bool), (dims[0], dims[1], dims[2]))
    image = np.transpose(image)
    image = flip_values(image, 0, 1).astype(bool)

    case_name = os.path.splitext(os.path.basename(raw_file_name))[0]

    return image, voxel_sizes, case_name


def extract_pn(image, voxel_size, case_name):
    # Runs pore network extraction algorithm
    net = ps.networks.snow(image, voxel_size=voxel_size)
    # Exporting network for openpnm
    ps.io.to_openpnm(net, filename='out/' + case_name)

    return net


if __name__ == '__main__':
    im, voxel_sizes, case_name = read_raw_file('samples', 'gambier_512.mhd')

    voxel_size = voxel_sizes[0]

    # im = np.load('out/im_0.npy')
    # voxel_size = 1.e-6

    # Plots one layer of the image in 2D
    plt.imshow(im[0])
    plt.show()

    net = extract_pn(image=im, voxel_size=voxel_size, case_name=case_name)
