from heapq import heappop, heappush
from atcoder.dsu import DSU
N, M = map(int, input().split())

check = []
G = DSU(N)
for _ in range(M):
    K, C = map(int, input().split())
    A = list(map(int, input().split()))
    for i in range(1, K):
        heappush(check, (C, A[0]-1, A[i]-1))

ans = 0
while check:
    C, u, v = heappop(check)
    if not G.same(u, v):
        ans += C
        G.merge(u, v)

print(ans if len(G.groups()) == 1 else -1)