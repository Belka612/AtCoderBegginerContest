from collections import deque
N, M = map(int, input().split())
A = list(map(int, input().split()))
G = [[] for _ in range(N)]
for _ in range(M):
    U, V, B = map(int, input().split())
    U, V = U-1, V-1
    G[U].append((V, B))
    G[V].append((U, B))

min_w = [float("inf")]*N
min_w[0] = A[0]
BFS = deque([0])
while BFS:
    u = BFS.popleft()
    for v, b in G[u]:
        new_w = min_w[u] + A[v] + b
        if new_w < min_w[v]:
            min_w[v] = new_w
            BFS.append(v)
print(*min_w[1:])