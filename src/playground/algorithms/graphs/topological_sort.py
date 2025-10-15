"""
Topological sort is a linear ordering of vertices such that for every directed edge from vertex `u` to vertex `v`, `u` comes before `v` in the ordering. It is only applicable to Directed Acyclic Graphs (DAGs).

"""

from .is_cyclic import is_cyclic


def topological_sort_util(graph, node, visited, stack):
    visited.add(node)
    for neighbor in graph.get(node, []):
        if neighbor not in visited:
            topological_sort_util(graph, neighbor, visited, stack)
    stack.append(node)


def topological_sort(graph):
    """
    Performs a topological sort on a Directed Acyclic Graph.

    Args:
        graph: A dictionary representing the adjacency list of the graph.

    Returns:
        A list of nodes in topological order.
    """
    if is_cyclic(graph):
        print("Graph has a cycle, topological sort not possible.")
        return []

    visited = set()
    stack = []
    for node in graph:
        if node not in visited:
            topological_sort_util(graph, node, visited, stack)
    return stack[::-1]


# Example Usage:
dag = {"A": ["C"], "B": ["C", "D"], "C": ["E"], "D": ["F"], "E": ["F"], "F": []}

print("Topological Sort:")
print(topological_sort(dag))
print("\n")
