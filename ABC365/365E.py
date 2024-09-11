import numpy as np
from collections import defaultdict
N = int(input())
A = list(map(int, input().split()))
B = [0]*(N+1)

for i in range(N):
    B[i+1] = B[i] ^ A[i]

dic = defaultdict(int)
for i in range(N+1):
    S = np.base_repr(B[i])
    for j, s in enumerate(S[::-1]):
        if s == '1':
            dic[j] += 1

ans = 0
for key in dic.keys():
    ans += pow(2, key)*dic[key]*(N+1-dic[key])

print(ans - sum(A))