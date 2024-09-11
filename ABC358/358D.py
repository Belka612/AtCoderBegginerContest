from sortedcontainers import SortedList
N, M = map(int, input().split())
A = SortedList(map(int, input().split()))
B = list(map(int, input().split()))
B.sort()

ans = 0
while B:
    b = B.pop()
    k = A.bisect_left(b)
    if k == len(A):
        print(-1)
        quit()
    ans += A[k]
    A.pop(k)
print(ans)