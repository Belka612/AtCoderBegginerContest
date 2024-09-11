N, X, Y = map(int, input().split())
dp  = [[float('inf') for _ in range(X+2)]  for  _  in range(N+1)]; dp[0][0]  = 0

for _ in range(N):
    A, B  = map(int, input().split())
    for i in reversed(range(N+1)):
        for j in reversed(range(X+1)):
            if dp[i][j] != float('inf'):
                dp[i+1][min(j+A, X+1)] = min(dp[i+1][min(j+A, X+1)], dp[i][j] + B)

ans  =  0
for i in range(N):
    for j in range(X+1):
        if dp[i][j] <= Y:
            ans = max(ans, i+1)
print(ans)
