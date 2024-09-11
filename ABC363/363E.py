from heapq import heappop, heappush
H, W, Y = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(H)]

prim = []
visited = [[False for _ in range(W)] for _ in range(H)]
for i in range(H):
    for j in range(W):
        if i == 0 or i == H-1 or j == 0 or j == W-1:
            heappush(prim, (A[i][j], (i, j)))
            visited[i][j] = True

ans = H*W
for h in range(1, Y+1):
    while prim and prim[0][0] <= h:
        _, (x, y) = heappop(prim)
        ans -= 1
        for dx, dy in ((0, 1), (1, 0), (0, -1), (-1, 0)):
            nx, ny = x+dx, y+dy
            if 0 <= nx < H and 0 <= ny < W and not visited[nx][ny]:
                visited[nx][ny] = True
                heappush(prim, (A[nx][ny], (nx, ny)))
    print(ans)