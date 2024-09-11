N, L, R = map(int, input().split()); L -= 1
ans = [i+1 for i in range(N)]
ans[L:R] = ans[L:R][::-1]
print(*ans)