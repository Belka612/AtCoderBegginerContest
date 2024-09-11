N = int(input())
H = [float('inf')] + list(map(int, input().split()))
check = [(float('inf'), 0)]
ans = [1]*(N+1)

for i in range(1, N+1):
    while check[-1][0] < H[i]:
        check.pop()
    h, ind = check[-1]
    ans[i] = ans[ind] + (i-ind)*H[i]
    check.append((H[i], i))
    print(ans[i])