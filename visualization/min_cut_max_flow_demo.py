import sys
import os

current_path = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.join(current_path, '../../'))

import matplotlib.pyplot as plt
import networkx as nx

G = nx.Graph()
G.add_edge('x', 'a', capacity=3)
G.add_edge('x', 'b', capacity=1)
G.add_edge('a', 'c', capacity=3)
G.add_edge('b', 'c', capacity=5)
G.add_edge('b', 'd', capacity=4)
G.add_edge('d', 'e', capacity=1)
G.add_edge('c', 'y', capacity=2)
G.add_edge('e', 'y', capacity=3)

min_cut_value, partition = nx.minimum_cut(G, 'x', 'y')
reachable, non_reachable = partition
print('min_cut_value', min_cut_value)

max_flow_value = nx.maximum_flow_value(G, 'x', 'y')
print('max_flow_value', max_flow_value)

mincut_node_pairs = set()
for u, neighbors in ((n, G[n]) for n in reachable):
    mincut_node_pairs.update((u, v) for v in neighbors if v in non_reachable)

edges_mincut = list()
edges_residual = list()
for edge in G.edges():
    if edge in mincut_node_pairs:
        edges_mincut.append(edge)
    else:
        edges_residual.append(edge)

nodes_external = list()
nodes_internal = list()
for node in G.nodes:
    if node == 'x' or node == 'y':
        nodes_external.append(node)
    else:
        nodes_internal.append(node)

edges_labels = dict()
edges_widths = list()
for edge in G.edges:
    edges_labels[edge] = G.edges[edge]['capacity']
    edges_widths.append(float(G.edges[edge]['capacity']))

pos = nx.spring_layout(G)
nx.draw_networkx(G, pos=pos)
nx.draw_networkx_nodes(G, pos=pos, nodelist=nodes_external, node_color='tab:purple', label='external nodes')
nx.draw_networkx_nodes(G, pos=pos, nodelist=nodes_internal, node_color='tab:olive', label='internal nodes')
nx.draw_networkx_edge_labels(G, pos, edge_labels=edges_labels, font_color='black')
nx.draw_networkx_edges(G, pos=pos, edgelist=edges_mincut, edge_color='tab:orange', width=edges_widths,
                       label='mincut edges')
nx.draw_networkx_edges(G, pos=pos, edgelist=edges_residual, edge_color='tab:blue', width=edges_widths,
                       label='residual edges')
plt.legend()
plt.axis('off')

plt.savefig('out/min_cut_max_flow_demo.pdf', format="pdf", bbox_inches='tight')

# plt.show()
