N, K = map(int, input().split())
p = [None]*N
for i in range(N):
    A, B = map(int, input().split())
    p[i] = ((A-1)/B, A, B)

def f(A, B, value):
    return A*value + B

dp = [0]*K
p.sort()
for i in range(N):
    A, B = p[i][1], p[i][2]
    for j in reversed(range(1, K)):
        dp[j] = max(dp[j], f(A, B, dp[j-1]))
    dp[0] = max(dp[0], f(A, B, 1))

print(dp[-1])