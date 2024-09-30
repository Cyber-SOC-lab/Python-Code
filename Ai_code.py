import random
import heapq

class NetworkGraph:
    def __init__(self, edge_servers, routers, connections):
        self.edge_servers = edge_servers
        self.routers = routers
        self.connections = connections
        self.latency_values = {}
        self.bandwidth_values = {}

    def values(self):
        for server in self.edge_servers:
            for router in self.routers:
                if server in self.connections.get(router, []):
                    self.latency_values[(server, router)] = round(random.uniform(0.1, 10), 2)  # Latency in milliseconds
                    self.bandwidth_values[(server, router)] = round(random.uniform(0.1, 10), 2)  # Bandwidth in gigabits

    def print_values(self):
        print("Latency in (ms):")
        for server in self.edge_servers:
            for router in self.routers:
                if (server, router) in self.latency_values:
                    print(f"{server} -> {router}: {self.latency_values[(server, router)]}", end=", ")
            print()

        print("\nBandwidth in (Gbps):")
        for server in self.edge_servers:
            for router in self.routers:
                if (server, router) in self.bandwidth_values:
                    print(f"{server} -> {router}: {self.bandwidth_values[(server, router)]}", end=", ")
            print()

    def dijkstra(self, start_node, end_node):
        if start_node == end_node:
            return [start_node]

        distance = {node: float('inf') for node in self.connections}
        distance[start_node] = 0
        visited = set()
        queue = [(0, start_node)]
        parent = {}

        while queue:
            _, item_name = heapq.heappop(queue)
            if item_name in visited:
                continue
            visited.add(item_name)
            if item_name == end_node:
                break

            for adj in self.connections.get(item_name, []):
                latency = self.latency_values.get((item_name, adj), float('inf'))
                adj_path_cost = distance[item_name] + latency
                if adj_path_cost < distance.get(adj, float('inf')):
                    distance[adj] = adj_path_cost
                    heapq.heappush(queue, (adj_path_cost, adj))
                    parent[adj] = item_name

        if end_node not in parent:
            return []  # No path found

        shortest_path = [end_node]
        temp = end_node
        while temp != start_node:
            temp = parent[temp]
            shortest_path.append(temp)
        shortest_path.reverse()

        return shortest_path

def main():
    Edge_server = ['Es1', 'Es2', 'Es3', 'Es4', 'Es5', 'R1', 'R2', 'R3', 'R4', 'R5', 'R6', 'R7']
    routers = ['R1', 'R2', 'R3', 'R4', 'R5', 'R6', 'R7', 'Es1', 'Es2', 'Es3', 'Es4', 'Es5']
    connections = {
        'Es1': ['R2','R4'],
        'Es2': ['R5'],
        'Es3': ['R1'],
        'Es4': ['R7'],
        'Es5': ['R8'],
        'R1': ['Es3','R2'],
        'R2': ['R1','R4','Es1'],
        'R3': ['R4','R5','R6'],
        'R4': ['R2','R3','R5','Es1'],
        'R5': ['R3','R4','Es2'],
        'R6': ['R3','R7','R8'],
        'R7': ['R6','Es4'],
        'R8': ['R6','Es5']
    }

    network = NetworkGraph(Edge_server, routers, connections)
    network.values()
    network.print_values()

    start_node = 'Es1'
    end_node = 'R7'
    shortest_path = network.dijkstra(start_node, end_node)
    if shortest_path:
        print(f"\nShortest path from {start_node} to {end_node} based on latency: {shortest_path}")
        total_latency = sum(network.latency_values.get((shortest_path[i], shortest_path[i + 1]), 0) for i in range(len(shortest_path) - 1))
        print(f"Total latency: {total_latency} ms")
    else:
        print(f"No path found from {start_node} to {end_node}")

if __name__ == "__main__":
    main()
