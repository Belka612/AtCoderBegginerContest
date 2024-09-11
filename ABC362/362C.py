N = int(input())
ans = [None]*N
D = [None]*N
s = 0
for i in range(N):
    L, R = map(int, input().split())
    ans[i] = L
    D[i] = R-L
    s -= L

for i in range(N):
    if s > 0:
        ans[i] += min(s, D[i])
        s -= min(s, D[i])
if s == 0:
    print("Yes")
    print(*ans)
else:
    print("No")