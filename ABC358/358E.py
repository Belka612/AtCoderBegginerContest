K = int(input())
C = list(map(int, input().split()))
mod = 998244353

def combslist(n, mod):
    combs = [[0] * (n+1) for _ in range(n+1)]
    for i in range(n+1):
        combs[i][0] = 1
        for j in range(1, i+1):
            combs[i][j] = (combs[i-1][j-1] + combs[i-1][j]) % mod
    return combs

combs = combslist(K, mod)
dp = [0] * (K + 1)
dp[0] = 1

for i in range(26):
    for j in reversed(range(K+1)):
        if dp[j] >= 1 and C[i] > 0:
            for k in range(1, min(C[i], K-j)+1):
                dp[j+k] = (dp[j+k] + dp[j] * combs[j+k][k]) % mod

ans = sum(dp[1:K+1]) % mod
print(ans)