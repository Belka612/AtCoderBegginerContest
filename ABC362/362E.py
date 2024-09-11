from collections import defaultdict
from functools import lru_cache
import sys; sys.setrecursionlimit(10**9)
N = int(input())
A = list(map(int, input().split()))
mod = 998244353

G = defaultdict(lambda: defaultdict(list))
for i in range(N-1):
    for j in range(i+1, N):
        G[A[j]-A[i]][i].append(j)

@lru_cache(maxsize = None)
def DFS(u, k):
    res = defaultdict(int); res[0] = 1
    for v in G[k][u]:
        for key in DFS(v, k).keys():
            res[key+1] += DFS(v, k)[key]
    return res
        
ans = [0]*N
for key in G.keys():
    for i in range(N):
        for ind in DFS(i, key).keys():
            ans[ind] += DFS(i, key)[ind]
ans[0] = N
print(*[x%mod for x in ans])