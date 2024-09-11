from heapq import heappop, heapify
N, M = map(int, input().split())
A = list(map(int, input().split())); heapify(A)
B = list(map(int, input().split())); heapify(B)
ans = 0
while A and B:
    a, b = heappop(A), heappop(B)
    while a < b and A:
        a = heappop(A)
    if a < b:
        ans = -1
        break
    ans += a
print(-1 if B else ans)