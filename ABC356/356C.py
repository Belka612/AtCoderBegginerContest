def linput():
    L = list(map(str, input().split()))
    res = 0
    for i in L[1:len(L)-1]:
        res += 1<<(int(i)-1)
    return int(L[0]), res, L[-1]

N, M, K = map(int, input().split())
C, A, R = [None]*M, [None]*M, [None]*M
for i in range(M):
    C[i], A[i], R[i] = linput()

ans = 0
for i in range(1<<N):
    flag = True
    for j in range(M):
        if R[j] == 'o' and bin(i & A[j]).count('1') < K:
            flag = False
            break
        elif R[j] == 'x' and bin(i & A[j]).count('1') >= K:
            flag = False
            break
    ans += flag
print(ans)