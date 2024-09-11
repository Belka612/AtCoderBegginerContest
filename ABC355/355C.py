N, T = map(int, input().split())
A = list(map(int, input().split()))
rows = [0]*N
cols = [0]*N
diag = [0]*2

for i in range(T):
    x, y = (A[i]-1)//N, (A[i]-1)%N
    rows[x] += 1
    cols[y] += 1
    if x==y:
        diag[0] += 1
    if N-1-x==y:
        diag[1] += 1
    if max(rows[x], cols[y], max(diag)) == N:
        print(i+1)
        exit()
print(-1)
    