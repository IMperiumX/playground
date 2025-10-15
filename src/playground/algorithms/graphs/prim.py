"""
Prim's algorithm is a greedy algorithm that finds a minimum spanning tree for a weighted undirected graph. It starts from an arbitrary vertex and grows the spanning tree by adding the cheapest edge that connects a vertex in the tree to a vertex outside the tree.
"""

import heapq


def prim(graph):
    """
    Finds the Minimum Spanning Tree of a connected, undirected, weighted graph.

    Args:
        graph: A dictionary representing the weighted graph.

    Returns:
        A list of edges in the Minimum Spanning Tree.
    """
    start_node = list(graph.keys())[0]
    mst = []
    visited = {start_node}
    edges = [(cost, start_node, to) for to, cost in graph[start_node].items()]
    heapq.heapify(edges)  # priority queue (heapify a list[Tuple[cost, from, to]])

    while edges and len(visited) < len(graph):
        cost, frm, to = heapq.heappop(edges)
        if to not in visited:
            visited.add(to)
            mst.append((frm, to, cost))
            for to_next, cost_next in graph[to].items():
                if to_next not in visited:
                    heapq.heappush(edges, (cost_next, to, to_next))
    return mst


# Example Usage:
mst_graph = {
    "A": {"B": 2, "D": 3},
    "B": {"A": 2, "C": 4, "D": 1},
    "C": {"B": 4, "E": 5},
    "D": {"A": 3, "B": 1, "E": 6},
    "E": {"C": 5, "D": 6},
}

print("Minimum Spanning Tree (Prim's Algorithm):")
minimum_spanning_tree = prim(mst_graph)
print(minimum_spanning_tree)
print("\n")
