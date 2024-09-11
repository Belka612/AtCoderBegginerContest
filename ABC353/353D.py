from collections import defaultdict
N = int(input())
A = list(map(int, input().split()))
mod = 998244353
dic = defaultdict(int)
for i in range(N):
    dic[len(str(A[i]))] += 1

ans = 0
for i in range(N):
    ans += A[i]*i
    dic[len(str(A[i]))] -= 1
    for j in range(10):
        ans += dic[j+1]*A[i]*10**(j+1)
    ans %= mod
print(ans)