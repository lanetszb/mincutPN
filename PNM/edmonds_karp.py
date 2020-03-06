import matplotlib.pyplot as plt
import networkx as nx
from networkx.algorithms.flow import edmonds_karp


def calculate_edmonds_karp(pores, throats, viscosity):
    
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
    print('max_flow', R['in_a']['in_b']['flow'])  
        
    nx.draw_networkx(R)
    plt.show()
    
    return R
    

