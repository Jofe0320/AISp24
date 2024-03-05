from environment import UndirectedGraph, WeightedUndirectedGraph
from queue import Queue, PriorityQueue

class ReachableAgent:
    def __init__(self, G: UndirectedGraph):
        self.G = G

    def is_reachable(self, start, end):
        if self.G.has_node(start) and self.G.has_node(end):
            Q = Queue()
            visited = dict() #visited
            #action 1 - add node to queue
            Q.put(start)
            while not Q.empty():
                #action 2 - remote node from queue
                current_state = Q.get()
                visited[current_state] = True
                if current_state == end:
                    return True #is rechable
                else:
                    next_states = self.G.get_adjacent(current_state)
                    for s in next_states:
                        if not s in visited:
                            Q.put(s)
            #not recheable
            return False
        else:
            #not recheable
            return False

class RecheablePathAgent:
    def __init__(self, G: UndirectedGraph):
        self.G = G

    def find_path(self, start, end):
        if self.G.has_node(start) and self.G.has_node(end):
            Q = Queue()
            visited = dict() #visited
            #action 1 - add node to queue
            node = (start, None, "visit", [start], 0)
            Q.put(node)
            while not Q.empty():
                #action 2 - remote node from queue
                current_node = Q.get()
                current_state = current_node[0]
                visited[current_state] = True
                if current_state == end:
                    return current_node[3]
                else:
                    for node in self.expand(current_state, current_node, self.G):
                        s = node[0]
                        if not s in visited:
                            Q.put(node)
            #not recheable
            return []
        else:
            #not recheable
            return []

    def expand(self, current_state, current_node, G):
        result = []
        next_states = self.G.get_adjacent(current_state)
        for s in next_states:
            new_path = current_node[3] + [s]
            node = (s, current_state, "visit", new_path, 0)
            result.append(node)
        return result


class RecheablePathAgentWithCost:
    def __init__(self, G: WeightedUndirectedGraph):
        self.G = G

    def find_path(self, start, end):
        Q = PriorityQueue()
        visited = dict()
        path_cost = dict()
        current_node = (start, None, "visit", [start], 0)
        Q.put((0, current_node))
        visited[start] = True
        path_cost[start] = 0
        while (not Q.empty()):
            current_node = Q.get()[1]
            current_state = current_node[0]
            if current_state == end:
                return current_node[3], current_node[4]
            else:
                neighbors = self.expand(current_node)
                for node in neighbors:
                    state = node[0]
                    new_cost = node[4]
                    if (state not in visited.keys()) or self.less_cost(state, path_cost, new_cost):
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
        old_cost = path_cost.get(state, -1)
        if (old_cost == -1):
            return True #not found so new cost is less
        else:
            return new_cost < old_cost
