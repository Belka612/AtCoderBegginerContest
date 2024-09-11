from math import comb
from collections import Counter
N = int(input())
A = list(map(int, input().split())); A = [(element, count) for element, count in sorted(Counter(A).items())]

check = [0]*(A[-1][0]+1)
for element, count in A:
    check[element] += count

for i in reversed(range(A[-1][0])):
    check[i] += check[i+1]

ans = 0
for element, count in A:
    cnt = 0
    check[element] -= count
    while (cnt+1)*element <= A[-1][0]:
        cnt += 1
        ans += count*check[cnt*element]
    ans += comb(count, 2)
print(ans)