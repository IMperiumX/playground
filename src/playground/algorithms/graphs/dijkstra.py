"""
Dijkstra's algorithm finds the shortest path from a single source node to all other nodes in a weighted graph. It's a greedy algorithm that maintains a set of visited vertices and repeatedly selects the unvisited vertex with the smallest known distance from the source.
"""

import heapq


def dijkstra(graph, start_node):
    """
    Finds the shortest paths from a starting node to all other nodes in a weighted graph.

    Args:
        graph: A dictionary representing the weighted graph.
               The keys are nodes, and the values are dictionaries of neighbors and their weights.
        start_node: The starting node for finding the shortest paths.

    Returns:
        A dictionary mapping each node to its shortest distance from the start_node.
    """
    distances = {node: float("infinity") for node in graph}
    distances[start_node] = 0
    priority_queue = [(0, start_node)]

    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)

        if current_distance > distances[current_node]:
            continue

        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))

    return distances


# Example Usage:
weighted_graph = {
    "A": {"B": 1, "C": 4},
    "B": {"A": 1, "C": 2, "D": 5},
    "C": {"A": 4, "B": 2, "D": 1},
    "D": {"B": 5, "C": 1},
}

print("Dijkstra's Algorithm:")
shortest_paths = dijkstra(weighted_graph, "A")
print(shortest_paths)
print("\n")
