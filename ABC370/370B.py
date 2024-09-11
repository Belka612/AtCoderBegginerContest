N = int(input())
A = [list(map(int, input().split())) for _ in range(N)]

ans = 1
for i in range(N):
    if ans-1 > i:
        ans = A[ans-1][i]
    else:
        ans = A[i][ans-1]

print(ans)