def dfs_recursive_adj_list(graph, node, visited):
    """
    Performs a recursive Depth-First Search on a graph represented by an adjacency list.

    Args:
        graph: A dictionary representing the adjacency list of the graph.
        node: The starting node for the DFS traversal.
        visited: A set to keep track of visited nodes.
    """
    if node not in visited:
        print(node, end=" => ")
        visited.add(node)
        for neighbor in graph.get(node, []):
            dfs_recursive_adj_list(graph, neighbor, visited)


def dfs_iterative_adj_list(graph, start_node):
    """
    Performs an iterative Depth-First Search on a graph represented by an adjacency list.

    Args:
        graph: A dictionary representing the adjacency list of the graph.
        start_node: The starting node for the DFS traversal.
    """
    visited = set()
    stack = [start_node]

    while stack:
        node = stack.pop()
        if node not in visited:
            print(node, end=" => ")
            visited.add(node)
            # Add neighbors in reverse order to visit them in the correct order
            for neighbor in reversed(graph.get(node, [])):
                if neighbor not in visited:
                    stack.append(neighbor)


graph_adj_list = {
    "A": ["B", "G"],
    "B": ["C", "D", "E"],
    "D": [],
    "E": ["F"],
    "F": [],
    "G": ["H"],
    "H": ["I"],
    "I": [],
}
if __name__ == "__main__":
    print("DFS with Adjacency List (Recursive):")
    visited_nodes = set()
    dfs_recursive_adj_list(graph_adj_list, "A", visited_nodes)
    print("\n")

    print("DFS with Adjacency List (Iterative with Stack):")
    dfs_iterative_adj_list(graph_adj_list, "A")
    print("\n")
