from bisect import bisect_left, bisect_right
N, Q = map(int, input().split())
a = list(map(int, input().split()))
a.sort()

for _ in range(Q):
    b, k = map(int, input().split())
    NG, OK = -1, 10**10
    while OK - NG > 1:
        mid = (OK + NG) // 2
        L = bisect_left(a, b-mid)
        R = bisect_right(a, b+mid)
        if R-L >= k:
            OK = mid
        else:
            NG = mid
    print(OK)