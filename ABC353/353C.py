from sortedcontainers import SortedList
N = int(input())
A = list(map(int, input().split()))
B = SortedList(A)
ans = 0
for i in range(N):
    ans += A[i]*(N-1)
    B.discard(A[i])
    k = len(B) - B.bisect_left(10**8 - A[i])
    ans -= k*10**8
print(ans)
