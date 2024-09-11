from collections import defaultdict

N, M = map(int, input().split())
A = list(map(int, input().split()))

B = [0] * (2 * N)
B[0] = 0

for i in range(1, 2 * N):
    B[i] = A[(i - 1) % N] + B[i - 1]

dic = defaultdict(set)
ans = 0

for i in range(N):
    dic[B[i] % M].add(i)

for i in range(N):
    k = len(dic[B[i] % M])
    ans += k-1

    dic[B[i] % M].discard(i)

    dic[B[i + N] % M].add(i)

print(ans)
