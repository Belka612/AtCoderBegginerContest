from atcoder.lazysegtree import LazySegTree
N, Q = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
mod = 998244353

lst = LazySegTree(op, e, mapping, composition, _id, [[A[i], B[i]] for i in range(N)])
for _ in range(Q):
    query = list(map(int, input().split()))
    if query[0] == 1:
        l, r, x = query[1:]
        lst.apply(l-1, r, [x, 0])
    elif query[0] == 2:
        l, r, x = query[1:]
        lst.apply(l-1, r, [0, x])
    else:
        l, r = query[1:]
        x, y = lst.prod(l-1, r)
        print(x, y)
    tmp = []
    for i in range(N):
        tmp.append(lst.get(i))
    print(tmp)