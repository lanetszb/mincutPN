import sys
import os

current_path = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.join(current_path, '../'))

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

min_cut_node_pairs = set()
for u, neighbors in ((n, G[n]) for n in reachable):
    min_cut_node_pairs.update((u, v) for v in neighbors if v in non_reachable)

all_edges = G.edges()
edge_color = list()
for edge in all_edges:
    if edge in min_cut_node_pairs:
        edge_color.append('r')
    else:
        edge_color.append('b')

node_color = list()
for node in G.nodes:
    if node == 'x' or node == 'y':
        node_color.append('tab:purple')
    else:
        node_color.append('tab:olive')

pos = nx.spring_layout(G)
nx.draw_networkx(G, pos=pos, edge_color=edge_color, node_color=node_color)

edge_labels = dict()
for edge in G.edges:
    edge_labels[edge] = G.edges[edge]['capacity']
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_color='black')

plt.axis('off')

plt.savefig('out/min_cut_max_flow_demo.pdf', format="pdf", bbox_inches='tight')

# plt.show()
