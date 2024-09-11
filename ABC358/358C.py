import numpy as np
N, M = map(int, input().split())
S = [input() for _ in range(N)]
INF = 10**20
ans = INF
for i in range(2**N):
    check = [False]*M
    cnt = 0
    for j in range(N):
        if i & 1<<j:
            cnt += 1
            for k in range(M):
                if S[j][k] == 'o':
                    check[k] = True
    if sum(check) == M:
        ans = min(ans, cnt)
print(ans)