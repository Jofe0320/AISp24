from environment import UndirectedGraph, WeightedUndirectedGraph
from agentsclass import ReachableAgent

#Build graph
G2 = UndirectedGraph()
G2.add_node("A")
G2.add_node("B")
G2.add_node("C")
G2.add_node("D")
G2.add_edge("A", "B")
G2.add_edge("A", "C")
G2.add_edge("A", "D")
G2.add_edge("B", "C")
G2.add_edge("D", "C")
G2.print()

#test
agent = ReachableAgent(G2)
t1 = agent.is_reachable("D","B")
print("Test 1 -> Reachable: ", t1)

G2.add_node("F")
G2.add_node("G")
G2.add_edge("F", "G")
t1 = agent.is_reachable("D","F")
print("Test 2-> Reachable: ", t1)

G2.add_edge("D", "F")
t1 = agent.is_reachable("A","G")
print("Test 3-> Reachable: ", t1)

agent = ReachableAgent(G2)
path, cost = agent.find_path("D","B")
print("Test 4 -> Path: ", path)
print("Test 4 -> cost: ", cost)

agent = ReachableAgent(G2)
path, cost = agent.find_path("A","G")
print("Test 4 -> Path: ", path)
print("Test 4 -> cost: ", cost)

G3 = WeightedUndirectedGraph()
G3.add_node("A")
G3.add_node("B")
G3.add_node("C")
G3.add_node("D")
G3.add_edge_weight("A", "B", 1)
G3.add_edge_weight("A", "C", 5)
G3.add_edge_weight("A", "D", 7)
G3.add_edge_weight("B", "C", 3)
G3.add_edge_weight("D", "C", 2)
G3.print()
print("Done Weighted Undirected Test.")

from agents import RecheablePathAgentWithCost
agent = RecheablePathAgentWithCost(G3)
path, cost = agent.find_path("A","C")
print("Reachable: ", path, "cost: ", cost)

path, cost = agent.find_path("A","D")
print("Reachable: ", path, "cost: ", cost)
