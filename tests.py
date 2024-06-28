from Graphs import *

# Tests to create and modify nodes
node1 = Node(1)
assert node1.get_val() == 1

node1.set_val(2)
assert node1.get_val() == 2

node2 = Node()
assert node2.get_val() == None

node2.set_val("Hello World!")
assert node2.get_val() == "Hello World!"

# Tests to create and modify edges
edge1 = Edge(node1, node2)
assert edge1.get_nodes() == (node1, node2)

node3 = Node(5)
edge1.set_nodes((node2, node3))
assert edge1.get_nodes() == (node2, node3)


# Tests to create and modify weighted edges


# Tests to create and modify directed edges


# Tests to create and modify weighted, directed edges


# Tests to create and modify graphs

## Test case 1: Creating an empty graph
graph1 = Graph([], [])
assert graph1.get_nodes() == []
assert graph1.get_edges() == []

## Test case 2: Adding nodes to the graph
node1 = Node(1)
node2 = Node(2)
graph2 = Graph([node1, node2], [])
assert graph2.get_nodes() == [node1, node2]

## Test case 3: Adding edges to the graph
edge1 = Edge(node1, node2)
graph3 = Graph([node1, node2], [edge1])
assert graph3.get_edges() == [edge1]

## Test case 4: Removing an edge from the graph
graph3.remove_edge(edge1)
assert graph3.get_edges() == []

## Test case 5: Adding an edge with safety check
node3 = Node(3)
edge2 = Edge(node1, node3)
graph4 = Graph([node1, node2], [])
try:
    graph4.add_edge(edge2)
except Exception as e:
    assert str(e) == "Nodes of the given edge do not exist in this graph"

## Test case 6: Adding an edge without safety check
graph4.add_edge(edge2, safety=False)
assert graph4.get_edges() == [edge2]

# Tests to draw graphs





print("All tests passed!")