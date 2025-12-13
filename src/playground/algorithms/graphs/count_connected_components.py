"""
This can be achieved by running DFS from every unvisited node and incrementing a counter.
"""

from .depth_first_search_adj_list import dfs_recursive_adj_list


def count_connected_components(graph):
    """
    Counts the number of connected components in an undirected graph.

    Args:
        graph: A dictionary representing the adjacency list of the graph.

    Returns:
        The number of connected components.
    """
    visited = set()
    count = 0
    for node in graph:
        if node not in visited:
            dfs_recursive_adj_list(graph, node, visited)
            count += 1
    return count


# Example Usage:
connected_graph = {0: [1, 2], 1: [0, 2], 2: [0, 1], 3: [4], 4: [3]}

print("Count Connected Components:")
# To avoid printing the DFS traversal, we'll just call the counting logic directly
visited_count = set()
component_count = 0
for node in connected_graph:
    if node not in visited_count:
        # A simple DFS traversal to mark all nodes in a component as visited
        stack = [node]
        visited_count.add(node)
        while stack:
            curr = stack.pop()
            for neighbor in connected_graph.get(curr, []):
                if neighbor not in visited_count:
                    visited_count.add(neighbor)
                    stack.append(neighbor)
        component_count += 1
print("Number of connected components:", component_count)
print("\n")
