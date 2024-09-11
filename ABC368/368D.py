import sys
sys.setrecursionlimit(10**9)
# import pypyjit
# pypyjit.set_param("max_unroll_recursion=-1")

N, K = map(int, input().split())
edges = [[] for _ in range(N + 1)]
for _ in range(N - 1):
    A, B = map(int, input().split())
    edges[A].append(B)
    edges[B].append(A)

V = list(map(int, input().split()))
need = [False] * (N + 1)
for v in V:
    need[v] = True

ans = 0

def dfs(u, parent):
    global ans
    is_needed = need[u]
    
    for v in edges[u]:
        if v == parent:
            continue
        child_needed = dfs(v, u)
        if child_needed:
            is_needed = True
    
    if is_needed:
        ans += 1
    
    return is_needed

dfs(V[0], -1)

print(ans)
