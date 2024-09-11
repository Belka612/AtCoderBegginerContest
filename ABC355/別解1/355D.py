from sortedcontainers import SortedList
N = int(input())
check = SortedList()
for i in range(N):
    l, r = map(int, input().split())
    check.add(l)
    check.add(r+0.5)

ans = 0
cnt = 0
while check:
    judge = check.pop(0)
    if judge%1 == 0:
        cnt += 1
    else:
        cnt -= 1
        ans += cnt
print(ans)