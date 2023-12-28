"""Dijkstra algorithm

Only for positive edges


Time complexity: O(E + V * log(V)) V - num of vertexes, E - num of edges
"""

from math import inf

type Graph = dict[str, dict[str, int]]
type Costs = dict[str, int | float]
type Parents = dict[str, str | None]


def dijkstra_algoritm(graph: Graph, parents: Parents, costs: Costs):
    processed = set()

    def find_lowest_cost(costs: Costs):
        lowest_cost = inf
        lowest_cost_node = None

        for node in costs:
            cost = costs[node]
            if cost < lowest_cost and node not in processed:
                lowest_cost = cost
                lowest_cost_node = node
        return lowest_cost_node

    node = find_lowest_cost(costs)
    while node is not None:
        cost = costs[node]
        neighbors = graph[node]
        for n in neighbors.keys():
            new_cost = cost + neighbors[n]
            if costs[n] > new_cost:
                costs[n] = new_cost
                parents[n] = node
        processed.add(node)
        node = find_lowest_cost(costs)


graph: Graph = {}

graph["start"] = {}
graph["start"]["a"] = 6
graph["start"]["b"] = 2

graph["a"] = {}
graph["a"]["fin"] = 1

graph["b"] = {}
graph["b"]["a"] = 3
graph["b"]["fin"] = 5

graph["fin"] = {}


costs: Costs = {}
costs["a"] = 6
costs["b"] = 2
costs["fin"] = inf


parents: Parents = {}
parents["a"] = "start"
parents["b"] = "start"
parents["fin"] = None


dijkstra_algoritm(graph, parents, costs)
print(costs)
print(parents)
