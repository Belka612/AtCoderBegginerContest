from heapq import heappop, heappush
N = int(input())
check = []
for i in range(N):
    l, r = map(int, input().split())
    heappush(check, l); heappush(check, r+0.5)

ans = 0
cnt = 0
while check:
    judge = heappop(check)
    if judge%1 == 0:
        cnt += 1
    else:
        cnt -= 1
        ans += cnt
print(ans)