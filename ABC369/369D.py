N = int(input())
A = list(map(int, input().split()))

dp = [0]*2
dp[0] = A[0]
for i in range(1, N):
    dp[0], dp[1] = max(dp[0], dp[1] + A[i]), max(dp[1], dp[0] + 2*A[i])

print(max(dp))