from atcoder.segtree import SegTree
N, K = map(int, input().split())
P = list(map(int, input().split()))
for i in range(N):
    P[i] = (P[i], i)
P.sort()
P = [ind for p, ind in P]
def op_max(a, b):
    return max(a, b)
def op_min(a, b):
    return min(a, b)
st_max = SegTree(op_max, -float("inf"), P)
st_min = SegTree(op_min, float("inf"), P)

ans = float("inf")
for i in range(N-K+1):
    ans = min(ans, st_max.prod(i, i+K)-st_min.prod(i, i+K))
print(ans)