import matplotlib.pyplot as plt
import networkx as nx
from networkx.algorithms.flow import edmonds_karp


def calculate_edmonds_karp(pores, throats, viscosity, A, dP, L):
    
    edges = list()
    for id in throats.index:
        edges.append((throats.loc[id , 'pore_a'], throats.loc[id , 'pore_b'], {'capacity': throats.loc[id , 'conductance']*throats.loc[id , 'length']*viscosity}))
        
    pores_in = pores.left
    pores_in = pores_in[pores_in]
    for id in pores_in.index:
        edges.append(('in_b', id))
    edges.append(('in_a', 'in_b'))  
    
    pores_out = pores.right
    pores_out = pores_out[pores_out]
    for id in pores_out.index:
        edges.append(('out_a', id))
    edges.append(('out_a','out_b'))
        
        
    G = nx.Graph()    
    G.add_edges_from(edges)
        
    R = edmonds_karp(G, 'in_a', 'out_b')
    print()    
    print('K_fulk', R['in_a']['in_b']['flow'] / A)
    print('Q_fulk', R['in_a']['in_b']['flow'] / A * dP / L)
    
    
    cut_value, partition = nx.minimum_cut(G, 'in_a', 'out_b')
    reachable, non_reachable = partition

    print()
    print('K_cut', cut_value / A)
    print('Q_cut', cut_value / A * dP / L)    

    reachable, non_reachable = partition
    cutset = set()
    for u, nbrs in ((n, G[n]) for n in reachable):
        cutset.update((u, v) for v in nbrs if v in non_reachable)
    
    print()    
    print('edges_n', len(edges))
    print('min_cut_edges_n', len(cutset))
    # print()
    # print('min_cut_edges', sorted(cutset))      
        
    # nx.draw_networkx(R)
    # plt.show()
    
    return R
    

