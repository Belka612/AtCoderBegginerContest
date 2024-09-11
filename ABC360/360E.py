N, K = map(int, input().split())
mod = 998244353

denominator = pow(pow(N**2, K, mod), -1, mod)
ans = 1
p = 2*(N-1)*pow(N**2, -1, mod) % mod
q = pow(N**2, -1, mod)*2 % mod
for i in range(K):
    ans = (1-p)*ans + q*(1-ans); ans %= mod

ans += (2 + N)*pow(2, -1, mod)*(1-ans)%mod
print(ans%mod)