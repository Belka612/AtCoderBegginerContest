N = int(input())
A = list(map(int, input().split()))

ans = 0
for i in range(N):
    if A[i] >= i:
        ans += 1
print(ans)