import sys
import os

current_path = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.join(current_path, '../../tmp/pmeal/OpenPNM/'))
sys.path.append(os.path.join(current_path, '../../tmp/pmeal/porespy/'))

import openpnm as op
from functions.calculate_perm import calculate_perm

flow_params, min_cut_edges_id = calculate_perm(op.io.Dict.load('out/pn_0.net'), 'out/pn_0')
