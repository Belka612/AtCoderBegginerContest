N = int(input())
A = list(map(int, input().split()))[::-1]

ans = []
while A:
    ans.append(A.pop())
    while len(ans) > 1 and ans[-2] == ans[-1]:
        ans.pop()
        ans.append(ans.pop()+1)
print(len(ans))