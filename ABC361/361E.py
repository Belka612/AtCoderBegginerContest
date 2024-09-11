import sys; sys.setrecursionlimit(10**9)
# pypyで再帰を提出するためのおまじない
# import pypyjit
# pypyjit.set_param("max_unroll_recursion=-1")
N = int(input())
g = [[] for _ in range(N)]

total_cost = 0
for _ in range(N-1):
    A, B, C = map(int, input().split())
    A, B = A-1, B-1
    g[A].append((B, C))
    g[B].append((A, C))
    total_cost += C

def DFS(current, cost, visited):
    visited[current] = True
    max_cost = cost
    max_vertex = current
    for nx, c in g[current]:
        if not visited[nx]:
            new_cost, new_vertex = DFS(nx, cost + c, visited)
            if new_cost > max_cost:
                max_cost = new_cost
                max_vertex = new_vertex
    visited[current] = False
    return max_cost, max_vertex

visited = [False] * N
_, farthest_vertex = DFS(0, 0, visited)

visited = [False] * N
max_cost, _ = DFS(farthest_vertex, 0, visited)

min_distance = 2 * total_cost - max_cost

print(min_distance)
