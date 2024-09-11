from bisect import bisect_left
from atcoder.segtree import SegTree
N = int(input())
A = list(map(int, input().split()))
B = sorted(A)
def op(x, y):
    return x+y
st_sum = SegTree(op, 0, [0]*N)
st_cnt = SegTree(op, 0, [0]*N)
ans = 0
for i in reversed(range(N)):
    k = bisect_left(B, A[i])
    ans += st_sum.prod(k, N) - st_cnt.prod(k, N)*A[i]
    st_sum.set(k, st_sum.get(k)+A[i])
    st_cnt.set(k, st_cnt.get(k)+1)
print(ans)
