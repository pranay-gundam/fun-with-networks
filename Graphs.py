class Node:
    def __init__(self, val = None):
        self.val = val
    
    def get_val(self):
        return self.val
    
    def set_val(self, val):
        self.val = val


class Edge:
    def __init__(self, n1, n2):
        self.n1 = n1
        self.n2 = n2

    def get_nodes(self):
        return (self.n1, self.n2)
    
    def set_nodes(self, nodes):
        self.n1 = nodes[0]
        self.n2 = nodes[1]

class DirectedEdge(Edge):
    def __init__(self, n1, n2):
        super().__init__(n1, n2)

    def get_nodes(self):
        return super().get_nodes()
    
    def get_node1(self):
        return self.n1
    
    def get_node2(self):
        return self.n2

    def set_nodes(self, index, node):
        assert index == 1 or index == 2
        if index == 1:
            self.n1 = node
        else:
            self.n2 = node


class WeightedEdge(Edge):
    def __init__(self, n1, n2, weight = 0):
        super().__init__(n1, n2)
        self.weight = weight

    def get_nodes(self):
        return super().get_nodes()

    def set_nodes(self, nodes):
        super().set_nodes(nodes)

    def get_weight(self):
        return self.weight
    
    def set_weight(self, weight):
        self.weight = weight


class WeightedDirectedEdge(WeightedEdge):
    def __init__(self, n1, n2, weight=0):
        super().__init__(n1, n2, weight)

    def get_nodes(self):
        return super().get_nodes()
    
    def set_nodes(self, index, node):
        assert index == 1 or index == 2
        if index == 1:
            self.n1 = node
        else:
            self.n2 = node

    def get_weight(self):
        return super().get_weight()
    
    def set_weight(self, weight):
        super().set_weight(weight)

    def get_node1(self):
        return self.n1
    
    def get_node2(self):
        return self.n2

class Graph:
    def __init__(self, nodes, edges, name = ""):
        self.nodes = nodes
        self.edges = edges
        self.name = name

    def get_nodes(self):
        return self.nodes

    def has_nodes(self, nodes):
        for node in nodes:
            if node not in self.nodes:
                return False
        return True

    def add_node(self, node):
        self.nodes.append(node)

    def get_edges(self):
        return self.edges
    
    def add_edge(self, edge, safety = True):
        if safety and not self.has_nodes(edge.get_nodes()):
            raise ValueError("Nodes of the given edge do not exist in this graph")
        self.edges.append(edge)

    def remove_edge(self, edge):
        self.edges.remove(edge)

    # TBD, draw a graph using any open source, easy to download, visualization package
    def draw_graph(self):
        pass
