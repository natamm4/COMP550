# The input is a connected, undirected graph G = (V, E). An edge e is a bridge if the graph
# (V, E \ {e}) is not connected. Describe an O(m2)-time algorithm that returns a list of the bridges in G,
# briefly explain why it’s correct, and analyze its running time.

def findBridges(G):
   bridges = []
   n = len(G)
   for u in range(n):
      for v in G[u][:]:
         if u < v - 1:
            G[u].remove(v)
            G[v-1].remove(u+1)
            if not is_connected(G, n):
               bridges.append((u+1, v))
            G[u].append(v)
            G[v-1].append(u+1)
   return bridges
      
def is_connected(G, n):
   visited = [False] * n
   start = 0
   DFS(G, start, visited)
   return all(visited)

def DFS(G, node, visited):
   visited[node] = True
   for neighbor in G[node]:
      if not visited[neighbor-1]:
         DFS(G, neighbor-1, visited)



G = [[3, 4],  # Vertex 1 is connected to vertices 2, 3, and 4
    [4],       # Vertex 2 is connected to vertices 1 and 4
    [1, 4],     # Vertex 3 is connected to vertices 1 and 4
    [1, 2, 3]]   # Vertex 4 is connected to vertices 1, 2, and 3
print(findBridges(G))