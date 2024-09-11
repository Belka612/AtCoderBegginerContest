N, T = map(int, input().split())
A = list(map(int, input().split()))

def check(M):
    S = [False for _ in range(N*N)]
    for i in range(M):
        S[A[i]-1] = True
    res = False
    for i in range(N):
        flag = True
        if not S[i*N+i]:
            flag = False
            break
    res = res or flag
    for i in range(N):
        flag = True
        if not S[N*i+N-1-i]:
            flag = False
            break
    res = res or flag
    for i in range(N):
        flag = True
        for j in range(N):
            if not S[i*N+j]:
                flag = False
                break
        res = res or flag
    for j in range(N):
        flag = True
        for i in range(N):
            if not S[i*N+j]:
                flag = False
                break
        res = res or flag
    return res
NG, OK = -1, T
while OK-NG > 1:
    mid = (OK+NG)//2
    if check(mid):
        OK = mid
    else:
        NG = mid
print(OK if check(OK) else -1)