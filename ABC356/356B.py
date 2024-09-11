import numpy as np
N, M = map(int, input().split())
A = np.array(list(map(int, input().split())))
X = np.array([0]*M)
for _ in range(N):
    X += np.array(list(map(int, input().split())))
print('Yes' if (X >= A).all() else 'No')
