H, W, K = map(int, input().split())
si, sj = map(int, input().split());si, sj = si-1, sj-1
A = [list(map(int, input().split())) for _ in range(H)]
dp = [[[-1 for _ in range(W)] for _ in range(H)] for _ in range(min(K, H*W)+1)]
dp[0][si][sj] = 0
ans = 0
for i in range(min(K, H*W)):
    for x in range(H):
        for y in range(W):
            if dp[i][x][y] >= 0:
                ans = max(ans, dp[i][x][y] + (K-i)*A[x][y])
                for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                    if 0 <= x+dx < H and 0 <= y+dy < W:
                        dp[i+1][x+dx][y+dy] = max(dp[i+1][x+dx][y+dy], dp[i][x][y] + A[x+dx][y+dy])

print(ans)