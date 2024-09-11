N, M = map(int, input().split())
A = list(map(int, input().split()))

if sum(A) <= M:
    print('infinite')
    exit()
OK, NG = 0, M+1
while NG - OK > 1:
    mid = (OK + NG)//2
    total = 0
    for i in range(N):
        total += min(mid, A[i])
    if total <= M:
        OK = mid
    else:
        NG = mid
print(OK)