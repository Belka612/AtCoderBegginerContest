N = int(input())
check = []
for i in range(N):
    A, C = map(int, input().split())
    check.append((A, -C, i+1))
check.sort()
ans = [check.pop()]
while check:
    if ans[-1][0] > check[-1][0] and ans[-1][1] > check[-1][1]:
        check.pop()
    else:
        ans.append(check.pop())
print(len(ans))
print(*sorted(ans[i][2] for i in range(len(ans))))