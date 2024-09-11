N = int(input())
L = []
R = []

for i in range(N):
    A, S = map(str, input().split())
    if S == 'L':
        L.append(int(A))
    else:
        R.append(int(A))

print(sum([abs(L[i+1] - L[i]) for i in range(len(L)-1)]) + sum([abs(R[i+1] - R[i]) for i in range(len(R)-1)]))