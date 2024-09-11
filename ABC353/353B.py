N, K = map(int, input().split())
A = list(map(int, input().split()))
ans = 1
cnt = 0
for a in A:
    if cnt+a > K:
        cnt = a
        ans += 1
    else:
        cnt += a
print(ans)