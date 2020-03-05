import matplotlib.pyplot as plt
import networkx as nx
from networkx.algorithms.flow import edmonds_karp


def calculate_edmonds_karp(pores, throats):
    
    edges = list()
    for id in throats.index:
        edges.append((throats.loc[id , 'pore_a'], throats.loc[id , 'pore_b'], {'capacity': throats.loc[id , 'conductance']*throats.loc[id , 'length']*10.e-4}))
        
    pores_in = pores.x_left
    pores_in = pores_in[pores_in]
    for id in pores_in.index:
        edges.append(('in', id))    
    
    pores_out = pores.x_right
    pores_out = pores_out[pores_out]
    for id in pores_out.index:
        edges.append(('out', id)) 
        
        
    G = nx.Graph()
        
    G.add_edges_from(edges)
        
    R = edmonds_karp(G, 'in', 'out')
    flow_value = nx.maximum_flow_value(G, 'in', 'out')
    print(flow_value)
    
    
    nx.draw_networkx(G)
    plt.show()
    

