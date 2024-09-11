from bisect import bisect_right
N, T = map(int, input().split())
S = input()
X = list(map(int, input().split()))

PreLeft = []
AfLeft = []
PreRight = []
AfRight = []
for i in range(N):
    if S[i] == '1':
        PreRight.append(X[i])
        AfRight.append(X[i]+T)
    else:
        PreLeft.append(X[i])
        AfLeft.append(X[i]-T)
PreLeft.sort()
AfLeft.sort()
ans = 0
for i in range(len(PreRight)):
    ans += bisect_right(AfLeft, AfRight[i]) - bisect_right(PreLeft, PreRight[i]) 
print(ans)