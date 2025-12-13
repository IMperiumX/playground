from collections import deque


def bfs_adj_list(graph, start_node):
    """
    Performs a Breadth-First Search on a graph represented by an adjacency list.

    Args:
        graph: A dictionary representing the adjacency list of the graph.
        start_node: The starting node for the BFS traversal.
    """
    visited = set()
    queue = deque([start_node])
    visited.add(start_node)

    while queue:
        node = queue.popleft()
        print(node, end=" ")

        for neighbor in graph.get(node, []):
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)


def bfs_adj_matrix(graph, start_node_index, num_nodes):
    """
    Performs a Breadth-First Search on a graph represented by an adjacency matrix.

    Args:
        graph: A 2D list representing the adjacency matrix.
        start_node_index: The index of the starting node for the BFS traversal.
        num_nodes: The total number of nodes in the graph.
    """
    visited = [False] * num_nodes
    queue = deque([start_node_index])
    visited[start_node_index] = True

    while queue:
        node_index = queue.popleft()
        print(node_index, end=" ")

        for i in range(num_nodes):
            if graph[node_index][i] == 1 and not visited[i]:
                visited[i] = True
                queue.append(i)


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

graph_adj_matrix = [
    [0, 1, 1, 0],
    [0, 0, 1, 0],
    [1, 0, 0, 1],
    [0, 0, 0, 1],
]
num_nodes_matrix = len(graph_adj_matrix)

if __name__ == "__main__":
    print("BFS with Adjacency List:")
    bfs_adj_list(graph_adj_list, "A")
    print("\n")

    print("BFS with Adjacency Matrix:")
    bfs_adj_matrix(graph_adj_matrix, 0, num_nodes_matrix)
    print("\n")
