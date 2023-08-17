class Router:
    def __init__(self, id, neighbors, costs):
        self.id = id
        self.neighbors = neighbors
        self.costs = costs
        self.routing_table = {n: {'cost': costs[n], 'next_hop': n} for n in neighbors}
        self.routing_table[id] = {'cost': 0, 'next_hop': id}

    def update_routing_table(self):
        for n in self.neighbors:
            for dest, dest_table in routers[n].routing_table.items():
                cost = self.costs[n] + dest_table['cost']
                if dest not in self.routing_table or cost < self.routing_table[dest]['cost']:
                    self.routing_table[dest] = {'cost': cost, 'next_hop': n}

    def print_routing_table(self):
        print(f"Routing table for Router {self.id}:")
        print("{:<10} {:<10} {:<10}".format('Destination', 'Cost', 'Next Hop'))
        for dest, dest_table in sorted(self.routing_table.items()):
            print("{:<10} {:<10} {:<10}".format(dest, dest_table['cost'], dest_table['next_hop']))

routers = {
    'A': Router('A', ['B', 'C'], {'B': 1, 'C': 5}),
    'B': Router('B', ['A', 'C', 'D'], {'A': 1, 'C': 3, 'D': 2}),
    'C': Router('C', ['A', 'B', 'D'], {'A': 5, 'B': 3, 'D': 3}),
    'D': Router('D', ['B', 'C'], {'B': 2, 'C': 3})
}

for r in routers.values():
    r.update_routing_table()

for r in routers.values():
    r.print_routing_table()