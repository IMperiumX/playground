"""
A graph is bipartite if its vertices can be divided into two disjoint and independent sets, U and V, such that every edge connects a vertex in U to one in V. This can be checked using graph coloring (with two colors).
"""


def is_bipartite(graph):
    """
    Checks if a graph is bipartite using DFS.

    Args:
        graph: A dictionary representing the adjacency list of the graph.

    Returns:
        True if the graph is bipartite, False otherwise.
    """
    colors = {}

    def dfs_bipartite(node, color):
        colors[node] = color
        for neighbor in graph.get(node, []):
            if neighbor not in colors:
                if not dfs_bipartite(neighbor, 1 - color):
                    return False
            elif colors[neighbor] == colors[node]:
                return False
        return True

    for node in graph:
        if node not in colors:
            if not dfs_bipartite(node, 0):
                return False
    return True


# Example Usage:
bipartite_graph = {0: [1, 3], 1: [0, 2], 2: [1, 3], 3: [0, 2]}
non_bipartite_graph = {0: [1, 2], 1: [0, 2], 2: [0, 1]}

print("Check for Bipartite Graph:")
print("Bipartite Graph:", is_bipartite(bipartite_graph))
print("Non-Bipartite Graph:", is_bipartite(non_bipartite_graph))
