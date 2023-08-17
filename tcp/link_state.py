import queue

def dijkstra(graph, start):
    # Create a priority queue
    pq = queue.PriorityQueue()
    # Initialize the distance and visited arrays
    n = len(graph)
    dist = [float('inf')] * n
    path = [[] for _ in range(n)]
    visited = [False] * n
    # Set the distance of the starting node to 0
    dist[start] = 0
    # Add the starting node to the priority queue
    pq.put((0, start))
    while not pq.empty():
        # Get the node with the smallest distance
        (d, u) = pq.get()
        # Check if the node has already been visited
        if visited[u]:
            continue
        # Mark the node as visited
        visited[u] = True
        # Update the distance of all the neighbors
        for (v, w) in graph[u]:
            if dist[u] + w < dist[v]:
                dist[v] = dist[u] + w
                path[v] = path[u] + [u]
                pq.put((dist[v], v))
    # Return the distances and paths to all the nodes
    return dist, path

# Example usage
n = int(input("Enter the number of nodes: "))
m = int(input("Enter the number of edges: "))
graph = [[] for _ in range(n)]
for i in range(m):
    u, v, w = map(int, input("Enter the edges and their weights (u v w): ").split())
    graph[u].append((v, w))
start = int(input("Enter the start node: "))
dist, path = dijkstra(graph, start)
print("Distances from node", start, ":")
for i in range(n):
    print("Node", i, ":", dist[i], "Path:", start, end="")
    for j in path[i]:
        print(" ->", j, end="")
    print()