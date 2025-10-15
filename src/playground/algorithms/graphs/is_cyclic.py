"""
This function uses DFS and keeps track of the recursion stack to detect back edges.
"""


def is_cyclic_util(graph, node, visited, recursion_stack):
    visited[node] = True
    recursion_stack[node] = True

    for neighbor in graph.get(node, []):
        if not visited[neighbor]:
            if is_cyclic_util(graph, neighbor, visited, recursion_stack):
                return True
        elif recursion_stack[neighbor]:
            return True

    recursion_stack[node] = False
    return False


def is_cyclic(graph):
    """
    Checks if a directed graph contains a cycle.

    Args:
        graph: A dictionary representing the adjacency list of the graph.

    Returns:
        True if the graph has a cycle, False otherwise.
    """
    nodes = list(graph.keys())
    visited = {node: False for node in nodes}
    recursion_stack = {node: False for node in nodes}

    for node in nodes:
        if not visited[node]:
            if is_cyclic_util(graph, node, visited, recursion_stack):
                return True
    return False


# Example Usage:
cyclic_graph = {"A": ["B"], "B": ["C"], "C": ["A"]}
acyclic_graph = {"A": ["B"], "B": ["C"]}

print("Check for Cycle:")
print("Cyclic Graph:", is_cyclic(cyclic_graph))
print("Acyclic Graph:", is_cyclic(acyclic_graph))
print("\n")
