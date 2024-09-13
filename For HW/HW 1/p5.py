# The input is an undirected graph G. We say that G is bipartite if there exists an array c
# such that c[u] ∈ {1, 2} for every u ∈ V , and for every {u, v} ∈ E, c[u]̸ = c[v]. (Intuitively, G is bipartite
# if we can color each vertex red or blue such that every edge has a red endpoint and a blue endpoint.)
# Describe an O(m + n)-time algorithm that either returns the array c (if G is bipartite) or nothing (if G is
# not bipartite), briefly explain why it’s correct, and analyze its running time.

from collections import deque

def ALG(G):
   n = len(G)
   c = [-1] * n

   def BFS(start):
      queue = deque([start])
      c[start] = 1

      while queue:
         u = queue.popleft()
         for v in G[u]:
            v -= 1
            if c[v] == -1:
               c[v] = 3 - c[u]
               queue.append(v)
            elif c[v] == c[u]:
               return False
      return True
   
   for i in range(n):
      if c[i] == -1:
         if not BFS(i):
            return None
         
   return c

G = [
    [3],
    [4, 5],
    [1, 4, 5],
    [2, 3],
    [2, 3]
]

result = ALG(G)
if result:
    print("Graph is bipartite. Color array:", result)
else:
    print("Graph is not bipartite.")