N, T, P = map(int, input().split())
L = list(map(int, input().split()))

NG, OK = -1, 100
while OK - NG > 1:
    mid = (OK + NG)//2
    cnt = 0
    for i in range(N):
        if L[i] + mid >= T:
            cnt += 1
    if cnt >= P:
        OK = mid
    else:
        NG = mid
print(OK)