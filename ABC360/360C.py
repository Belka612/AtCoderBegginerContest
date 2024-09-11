from heapq import heappop, heappush
from collections import defaultdict
N = int(input())
A = list(map(int, input().split()))
W = list(map(int, input().split()))

check = []
dic = defaultdict(int)
for i in range(N):
    heappush(check, (W[i], A[i]))
    dic[A[i]] += 1

ans = 0
for i in range(N):
    W, A = heappop(check)
    if dic[A] != 1:
        ans += W
        dic[A] -= 1
print(ans)