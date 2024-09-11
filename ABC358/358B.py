N, A = map(int, input().split())
T = list(map(int, input().split()))

ans = 0
for i in range(N):
    ans = max(ans, T[i]) + A
    print(ans)