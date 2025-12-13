"""
Kosaraju's algorithm finds strongly connected components (SCCs) in a directed graph. It involves two DFS passes.
"""


def kosaraju_scc(graph):
    """
    Finds strongly connected components in a directed graph using Kosaraju's algorithm.

    Args:
        graph: A dictionary representing the adjacency list of the graph.

    Returns:
        A list of lists, where each inner list is a strongly connected component.
    """

    def dfs1(node, visited, stack):
        visited.add(node)
        for neighbor in graph.get(node, []):
            if neighbor not in visited:
                dfs1(neighbor, visited, stack)
        stack.append(node)

    def reverse_graph(graph):
        rev_graph = {node: [] for node in graph}
        for node, neighbors in graph.items():
            for neighbor in neighbors:
                rev_graph[neighbor].append(node)
        return rev_graph

    def dfs2(node, visited, component):
        visited.add(node)
        component.append(node)
        for neighbor in reversed_graph.get(node, []):
            if neighbor not in visited:
                dfs2(neighbor, visited, component)

    stack = []
    visited = set()
    for node in graph:
        if node not in visited:
            dfs1(node, visited, stack)

    reversed_graph = reverse_graph(graph)

    sccs = []
    visited.clear()
    while stack:
        node = stack.pop()
        if node not in visited:
            component = []
            dfs2(node, visited, component)
            sccs.append(component)
    return sccs


# Example Usage:
scc_graph = {0: [1], 1: [2], 2: [0, 3], 3: [4], 4: [5], 5: [3]}

print("Strongly Connected Components (Kosaraju's Algorithm):")
print(kosaraju_scc(scc_graph))
print("\n")
