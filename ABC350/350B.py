N, Q = map(int, input().split())
T = list(map(int, input().split()))

ans = [True]*N
for t in T:
    ans[t-1] = not ans[t-1]
print(sum(ans))