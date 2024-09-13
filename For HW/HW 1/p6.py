# Suppose there is a cooking competition with n dishes and k judges. Each judge ranks
# exactly ℓ of the n dishes from tastiest to least tasty (in their opinion). Our goal is to return a ranking
# R of the n dishes such that every judge’s ranking is a subsequence of R. (Judges don’t care about dishes
# other than the ℓ they ranked.) If this task is not possible (due to disagreement among the judges), the
# algorithm should return 0.
# More formally, the input is an integer n and an array A of size k, where A[i] is a list containing the ℓ
# dishes ranked by Judge i from tastiest to least tasty. Each dish is represented by a number in {1, . . . , n}.
# The output should either be a list R of the n dishes (from tastiest to least tasty) that contains every
# judge’s list as a subsequence, or 0 (if no such ranking exists). Describe an O(kℓ + n)-time algorithm for
# this problem, briefly explain why it’s correct, and analyze its running time.
# Example: Suppose there are n = 4 dishes, k = 2 judges, and each judge ranks ℓ = 3 dishes. If
# A = [[4, 2, 1], [2, 3, 1]], then the algorithm can output R = [4, 2, 3, 1] because each A[i] is a subsequence of
# R. If A = [[4, 2, 1], [1, 2, 3]], then the algorithm must output 0, because Judge 1 thinks Dish 2 is tastier
# than Dish 1 but Judge 1 thinks otherwise.

from collections import deque

def ALG(A, n):
    adj_list = [[] for _ in range(n)] 
    in_deg = [0] * n  

    for judge in A:
        for i in range(len(judge) - 1):
            u = judge[i] - 1 
            v = judge[i + 1] - 1
            adj_list[u].append(v) 
            in_deg[v] += 1  

    def cycle():
        visited = [-1] * n  
        def DFS(u):
            if visited[u] == 0: 
                return True
            if visited[u] == 1: 
                return False

            visited[u] = 0
             
            for v in adj_list[u]:
                if visited[v] == -1:  
                    if DFS(v):
                        return True
                elif visited[v] == 0: 
                    return True
            visited[u] = 1 
            return False

        for u in range(n):
            if visited[u] == -1:
                if DFS(u):
                    return True
        return False

    if cycle():
        return 0

		queue = new Queue()
    for i from 0 to n - 1:
         if in_deg[i] == 0: queue.enqueue(i)
    R = []

    while queue is not empty:
        u = queue.popleft()
        R.append(u + 1) 

        for v in adj_list[u]:
            in_deg[v] -= 1
            if in_deg[v] == 0:
                queue.append(v)

    if len(R) == n:
        return R
    else:
        return 0

# Example usage:
n = 4  # Number of dishes
A = [
    [4, 2, 1],  # Judge 1's ranking
    [2, 3, 1]   # Judge 2's ranking
]

print(find_ranking(n, A))  # Expected output: [4, 2, 3, 1]

# Example usage:
n = 6  # Number of dishes
A = [
    [1, 2, 6],  # Judge 1's ranking
    [1, 5, 2]   # Judge 2's ranking
]

print(find_ranking(n, A))  # Expected output: [4, 2, 3, 1]