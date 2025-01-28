# Graph represented as an adjacency list
graph = {
    "A": [("B", 1), ("C", 4)],
    "B": [("C", 2), ("D", 5)],
    "C": [("D", 1)],
    "D": [],
}


def dijkstra(graph, start):
    # Initialize distances from start to all other vertices
    distances = {vertex: float("infinity") for vertex in graph}
    distances[start] = 0

    # Initialize the queue
    queue = [start]

    # Loop until the queue is empty
    while queue:
        # Get the vertex with the smallest distance
        vertex = queue.pop(0)

        # Loop through the neighbors of the vertex
        for neighbor, weight in graph[vertex]:
            # Calculate the new distance
            new_distance = distances[vertex] + weight

            # If the new distance is smaller than the current distance
            if new_distance < distances[neighbor]:
                # Update the distance
                distances[neighbor] = new_distance

                # Add the neighbor to the queue
                queue.append(neighbor)

    return distances


# Find shortest paths from vertex 'A'
shortest_paths = dijkstra(graph, "A")
print(shortest_paths)
