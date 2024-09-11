N = int(input())
S = input()

dp = [1, 0]

win = {
    "R":"P",
    "S":"R",
    "P":"S"
}

for i in range(1, N):
    ndp = [0, 0]
    if win[S[i-1]] != win[S[i]]:
        ndp[0] = dp[0] + 1
    if S[i-1] != win[S[i]]:
        ndp[0] = max(ndp[0], dp[1] + 1)
    if S[i-1] != S[i]:
        ndp[1] = dp[1]
    if win[S[i-1]] != S[i]:
        ndp[1] = max(ndp[1], dp[0])
    dp = ndp
print(max(dp))