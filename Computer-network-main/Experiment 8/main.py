from math import inf

names = ["A", "B", "C", "D"]
links = [[0, 1, 4, inf], [1, 0, 2, 6], [4, 2, 0, 3], [inf, 6, 3, 0]]


def distance_vector(graph):
    count = len(graph)
    costs = [row[:] for row in graph]
    hops = [[j if graph[i][j] < inf else None for j in range(count)] for i in range(count)]
    changed = True
    while changed:
        previous = [row[:] for row in costs]
        changed = False
        for router in range(count):
            for neighbor in range(count):
                if neighbor == router or graph[router][neighbor] == inf:
                    continue
                for destination in range(count):
                    candidate = graph[router][neighbor] + previous[neighbor][destination]
                    if candidate < costs[router][destination]:
                        costs[router][destination] = candidate
                        hops[router][destination] = neighbor
                        changed = True
    return costs, hops


def dijkstra(graph, source):
    count = len(graph)
    costs = [inf] * count
    parents = [None] * count
    visited = set()
    costs[source] = 0
    for _ in range(count):
        choices = [i for i in range(count) if i not in visited]
        router = min(choices, key=lambda i: costs[i])
        if costs[router] == inf:
            break
        visited.add(router)
        for destination in range(count):
            candidate = costs[router] + graph[router][destination]
            if destination not in visited and candidate < costs[destination]:
                costs[destination] = candidate
                parents[destination] = router
    return costs, parents


def main():
    costs, hops = distance_vector(links)
    print("Distance Vector: source destination next-hop cost")
    for source in range(len(names)):
        for destination in range(len(names)):
            hop = hops[source][destination]
            next_name = names[hop] if hop is not None else "unreachable"
            print(names[source], names[destination], next_name, costs[source][destination])
    print("Link State: source destination path cost")
    for source in range(len(names)):
        distances, parents = dijkstra(links, source)
        for destination in range(len(names)):
            path = []
            current = destination
            while current is not None:
                path.append(names[current])
                current = parents[current]
            route = "->".join(reversed(path)) if distances[destination] < inf else "unreachable"
            print(names[source], names[destination], route, distances[destination])


if __name__ == "__main__":
    main()
