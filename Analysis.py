from Graphs import *

# TBD: Returns the number of neighbors a given node has in a given graph.
def degree_centrality(graph, node):
    #return type is Int
    
    pass

# TBD: Returns the sum of connections an individual has where a direct connection is given weight x^0, a second degree connection
# is given weight x^1, a nth degree connection is given weight x^(n-1). 
def nth_degree_centrality(graph, node, weight):
    pass

# TBD: Same as above but the weighting is an arbitrary function f(degree) -> weight.
def nth_degree_centrality_custom(graph, node, weightfunc):
    pass

# TBD: Returns the proportion of a given node's centrality to sum of friends' centralities. 
def eigenvector_centrality(graph, node):
    pass

# TBD: Returns a measure of the how many nodes a node can quickly reach.
def diffusion_centrality(graph, node):
    pass

# TBD: Returns a measure of if a node is a key broker/connection between multiple sets of nodes.
def betweeness_centrality(graph, node):
    pass

# TBD: Returns a boolean that indicates if the graph is acyclic.
def is_acyclic(graph):
    pass



# Future potential stuff includes, stochastically evolving graphs, so nodes are likely to form edges based on how connected they are 
# to eachother.