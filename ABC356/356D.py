N, M = map(int, input().split())
ans = 0
mod = 998244353
for i in range(60):
    if M & (1<<i):
        ans += (N//(2**(i+1))) * 2**i + max(0, N%2**(i+1) + 1 - 2**i)
        ans %= mod
print(ans)