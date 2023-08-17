vertices = int(input(f"Enter no of vertices : "))
edge = int(input(f"Enter no of edges : "))
edge_list = []
for i in range(0,vertices):
    temp_edge = [int(x) for x in input().split()]
    edge_list.append(temp_edge)

source_node = int(input("Enter source node : "))
dist = []
for i in range(0,vertices):
    dist.append(1e9)
dist[source_node]=0

for i in range(0,vertices-1):
    for it in edge_list:
        u = it[0]
        v = it[1]
        wt = it[2]
        if dist[u]!=1e9 and dist[u]+wt<dist[v]:
            dist[v]=dist[u]+wt


print("Shortest distance list : ")
for i in range(0,vertices-1):
    print(f'{source_node} --> {i} = {dist[i]}')