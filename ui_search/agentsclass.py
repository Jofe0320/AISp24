from environment import UndirectedGraph, WeightedUndirectedGraph
from queue import Queue, PriorityQueue

class ReachableAgent:
    def __init__(self, G:UndirectedGraph):
        self.G = G

    def is_reachable(self, node1, node2)-> bool:
        #Queue with frontier nodes
        Q = Queue()
        #dictionary with visited nodes
        visited = dict()
        Q.put(node1)
        #visited[node1] = True
        while not Q.empty():
            current_node = Q.get()
            if (current_node == node2):
                return True
            if not visited.get(current_node, False):
                visited[current_node] = True
                neighbors  = self.G.get_adjacent(current_node)
                for item in neighbors:
                    Q.put(item)
        return False

    def find_path(self, node1, node2) -> list:
        Q = Queue()
        visited = dict()
        current_node = (node1, None, "visit", [node1], 0)
        Q.put(current_node)
        visited[node1] = True
        while(not Q.empty()):
            current_node = Q.get()
            current_state = current_node[0]
            if current_state == node2:
                return current_node[3], current_node[4]
            else:
                neighbors = self.expand(current_node)
                for node in neighbors:
                    state = node[0]
                    if not (state in visited.keys()):
                        visited[state] = True
                        Q.put(node)
        return []

    def expand(self, current_node):
        result = []
        current_state = current_node[0]
        for state in self.G.get_adjacent(current_state):
            path = current_node[3] + [state]
            cost = current_node[4] + 1
            new_node = (state, current_state, "visit", path, cost)
            result.append(new_node)
        return result


class WeighedReachableAgent:
    def __init__(self, G:WeightedUndirectedGraph):
        self.G = G

    def find_path(self, start, end):
        Q = PriorityQueue() # (priority, value)
        visited = dict()
        path_cost = dict()
        current_node = (start, None, "visit", [start], 0)
        Q.put((0, current_node))
        visited[start] = True
        path_cost[start] = 0
        while (not Q.empty()):
            _,current_node = Q.get()
            current_state = current_node[0]
            if current_state == end:
                return current_node[3], current_node[4]
            else :
                neighboors = self.expand(current_node)
                for node in neighboors:
                    state = node[0]
                    new_cost = node[4]
                    if (state not in visited.keys()) or (self.less_cost(state, path_cost, new_cost)):
                        visited[state] = True
                        path_cost[state] = new_cost
                        Q.put((new_cost, node))
        return []

    def expand(self, current_node):
        result = []
        current_state = current_node[0]
        for state in self.G.get_adjacent(current_state):
            path = current_node[3] + [state]
            cost = current_node[4] + self.G.get_weight(current_state, state)
            new_node = (state, current_state, "visit", path, cost)
            result.append(new_node)
        return result


    def less_cost(self, state, path_cost, new_cost):
        old_cost = path_cost.get(path_cost, -1)
        if old_cost == -1:
            return True
        else:
            return new_cost < old_cost

