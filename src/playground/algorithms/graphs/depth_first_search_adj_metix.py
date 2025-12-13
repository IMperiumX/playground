"""
This implementation uses a 2D list to represent the adjacency matrix.
"""


def dfs_recursive_adj_matrix(graph, node_index, visited, num_nodes):
    """
    Performs a recursive Depth-First Search on a graph represented by an adjacency matrix.

    Args:
        graph: A 2D list representing the adjacency matrix.
        node_index: The index of the starting node for the DFS traversal.
        visited: A list or set to keep track of visited node indices.
        num_nodes: The total number of nodes in the graph.
    """
    print(node_index, end=" ")
    visited[node_index] = True

    for i in range(num_nodes):
        if graph[node_index][i] == 1 and not visited[i]:
            dfs_recursive_adj_matrix(graph, i, visited, num_nodes)


def dfs_iterative_adj_matrix(graph, start_node_index, num_nodes):
    """
    Performs an iterative Depth-First Search on a graph represented by an adjacency matrix.

    Args:
        graph: A 2D list representing the adjacency matrix.
        start_node_index: The index of the starting node for the DFS traversal.
        num_nodes: The total number of nodes in the graph.
    """
    visited = [False] * num_nodes
    stack = [start_node_index]

    while stack:
        node_index = stack.pop()
        if not visited[node_index]:
            print(node_index, end=" ")
            visited[node_index] = True

            # Add neighbors in reverse order to visit them in the correct order
            for i in range(num_nodes - 1, -1, -1):
                if graph[node_index][i] == 1 and not visited[i]:
                    stack.append(i)


# Example Usage:
# Adjacency matrix for a graph with 4 nodes (0, 1, 2, 3)
graph_adj_matrix = [
    [0, 1, 1, 0],
    [0, 0, 1, 0],
    [1, 0, 0, 1],
    [0, 0, 0, 1],
]
num_nodes_matrix = len(graph_adj_matrix)

if __name__ == "__main__":
    print("DFS with Adjacency Matrix (Recursive):")
    visited_matrix = [False] * num_nodes_matrix
    dfs_recursive_adj_matrix(graph_adj_matrix, 0, visited_matrix, num_nodes_matrix)
    print("\n")

    # Example Usage:
    print("DFS with Adjacency Matrix (Iterative with Stack):")
    dfs_iterative_adj_matrix(graph_adj_matrix, 0, num_nodes_matrix)
    print("\n")
