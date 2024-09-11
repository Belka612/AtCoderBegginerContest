from collections import defaultdict
N = int(input())
A = list(map(int, input().split()))

dic = defaultdict(int)

for i in range(N):
    dic[A[i]] = i+1

A.sort()
print(dic[A[-2]])