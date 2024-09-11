from collections import deque
N = int(input())
S = [input() for _ in range(N)]
M = max([len(s) for s in S])

ans = [deque() for _ in range(M)]
for i in range(N):
    for j in range(M):
        if j < len(S[i]):
            ans[j].appendleft(S[i][j])
        else:
            ans[j].appendleft('*')

for i in range(M):
    while ans[i][-1] == '*':
        ans[i].pop()
    print(*ans[i], sep="")