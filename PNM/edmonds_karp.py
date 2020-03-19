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
    print('Q_fulk', R['in_a']['in_b']['flow'] * dP / L / viscosity)
    
    
    # cut_value, partition = nx.minimum_cut(G, 'in_a', 'out_b',flow_func=edmonds_karp)
    cut_value, partition = nx.minimum_cut(G, 'in_a', 'out_b')
    reachable, non_reachable = partition

    print()
    print('K_cut', cut_value / A)
    print('Q_cut', cut_value * dP / L / viscosity)    

    reachable, non_reachable = partition
    
    cut_set_edges = set()
    for u, nbrs in ((n, G[n]) for n in reachable):
        cut_set_edges.update((u, v) for v in nbrs if v in non_reachable)    
    
    all_edges = G.edges()
    
    print()    
    print('edges_n', len(all_edges))
    print('min_cut_edges_n', len(cut_set_edges))
   
    # print()
    # print('all_edges', all_edges)
    # 
    # print()
    # print('min_cut_edges', sorted(cut_set_edges))
    
    color_edges = list()
    for edge in all_edges:        
        if edge in cut_set_edges:
            color_edges.append('r')
        else:
            color_edges.append('b')   
          
        
    # nx.draw_networkx(G,pos=nx.spring_layout(G),edge_color=color_edges)
 #    plt.show()
    
    edges_n = len(all_edges)
    min_cut_edges_n = len(cut_set_edges)
    
    file_perm = open('min_cut_max_flow.txt', 'w')

    with file_perm as file:
        file.write('edges_n' + 'min_cut_edges_n' + '\n')
        file.write(str(edges_n) + ',' + str(min_cut_edges_n) + '\n')
    
    return R
    
    Hagen-Poissels

