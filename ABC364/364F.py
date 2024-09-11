from atcoder.dsu import DSU
N, Q = map(int, input().split())
dsu = DSU(N)

krs = []
for _ in range(Q):
    L, R, C = map(int, input().split())
    krs.append((C, L-1, R-1))
krs.sort()

v = [i for i in range(N)]
ans = 0

for C, L, R in krs:
    p = L
    while p <= R:
        p = v[dsu.leader(p)]
        ans += C
        if p + 1 <= R:
            dsu.merge(p, p+1)
            v[dsu.leader(p)] = v[dsu.leader(p+1)]
        p += 1

if dsu.size(0) == N:
    print(ans)
else:
    print(-1)