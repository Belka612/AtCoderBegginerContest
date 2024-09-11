N = int(input())
mod = 998244353
base = pow(10, len(str(N)), mod)
print((N*(pow(base, N, mod) - 1) * pow(base-1, -1, mod) % mod)) #等比数列の和の公式