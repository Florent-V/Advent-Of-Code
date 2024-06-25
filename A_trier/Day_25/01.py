from itertools import combinations
import networkx as nx

g = nx.Graph()

for line in open("input.txt", "r").readlines():
    source, raw_targets = line.rstrip().split(": ")
    targets = raw_targets.split(" ")
    for target in targets:
        g.add_edge(source, target, capacity=1)


# I don't know which minimum_cut will require 3 nodes to remove,
# so I try all combinations of nodes
for s, t in combinations(list(g.nodes), 2):
    n, graphs = nx.minimum_cut(g, s, t)
    if n == 3:
        print(f"Solution: {len(graphs[0]) * len(graphs[1])}")
        break