import sys
sys.path.append('..')

from graph_traversal import Graph

graph = Graph()
graph.insert_edge(100, 1, 2)
graph.insert_edge(101, 1, 3)
graph.insert_edge(102, 1, 4)
graph.insert_edge(103, 3, 4)
# Should be [(100, 1, 2), (101, 1, 3), (102, 1, 4), (103, 3, 4)]
assert (graph.get_edge_list() == [(100, 1, 2), (101, 1, 3), (102, 1, 4), (103, 3, 4)]), "Failed in get_edge_list"
# Should be [None, [(2, 100), (3, 101), (4, 102)], None, [(4, 103)], None]
assert (graph.get_adjacency_list() == [None, [(2, 100), (3, 101), (4, 102)], None, [(4, 103)], None]), "Failed in get_adjacency_list"
# Should be [[0, 0, 0, 0, 0], [0, 0, 100, 101, 102], [0, 0, 0, 0, 0], [0, 0, 0, 0, 103], [0, 0, 0, 0, 0]]
assert (graph.get_adjacency_matrix() == [[0, 0, 0, 0, 0], [0, 0, 100, 101, 102], [0, 0, 0, 0, 0], [0, 0, 0, 0, 103], [0, 0, 0, 0, 0]]), "Failed in get_adjacency_matrix"

print ("ALL TEST PASSED")
