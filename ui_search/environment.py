class Graph:
    def __init__(self):
        self.nodes = list()
        self.adjacency_list = dict()

    def add_node(self, new_node):
        if new_node and (not new_node in self.nodes):
            self.nodes.append(new_node)

    def node_count(self):
        return len(self.nodes)

    def edge_count(self):
        count = 0
        for item in self.adjacency_list:
            count = count + len(item[1])
        return count

    def add_edge(self, node1, node2):
        if not self.has_edge(node1, node2):
            if node1 not in self.adjacency_list:
                self.adjacency_list[node1] = [node2]
            else:
                self.adjacency_list[node1] = self.adjacency_list[node1] + [node2]

    def has_node(self, node):
        return node in self.nodes

    def has_edge(self, node1, node2):
        return self.has_node(node1) and self.has_node(node2) and (node1 in self.adjacency_list) \
            and (node2 in self.adjacency_list[node1])

    def get_adjacent(self, node1):
        if self.has_node(node1):
            return self.adjacency_list[node1]
        else:
            return None

    def print(self):
        print("Nodes: ", self.nodes)
        print("Edges: ")
        for item in self.adjacency_list.items():
            print(item)


class UndirectedGraph(Graph):
    # def add_edge(self, node1, node2):
    #     super(UndirectedGraph, self).add_edge(node1, node2)
    #     super(UndirectedGraph, self).add_edge(node2, node1)
    def add_edge(self, node1, node2):
        super().add_edge(node1, node2)
        super().add_edge(node2, node1)

class WeightedUndirectedGraph(UndirectedGraph):
    def __init__(self):
        super().__init__()
        self.weights = dict()

    def __local_add_edge__(self, node1, node2, weight):
        super().add_edge(node1, node2)
        key = (node1, node2)
        self.weights[key] = weight
        key = (node2, node1)
        self.weights[key] = weight

    def add_edge(self, node1, node2):
        self.__local_add_edge__(node1, node2, 0)

    def add_edge_weight(self, node1, node2, weight):
        self.__local_add_edge__(node1, node2, weight)

    def get_weight(self, node1, node2):
        return self.weights.get((node1, node2), float("-inf"))

    def print(self):
        print("Nodes: ", self.nodes)
        print("Edges: ")
        for item in self.adjacency_list.items():
            key, value = item
            L = []
            for v in value:
                L.append((v, self.get_weight(key, v)))
            print(key,": ", L)
