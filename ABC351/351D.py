from collections import deque
H, W = map(int, input().split())
S = [list(input()) for _ in range(H)]

check = []
for i in range(H):
    for j in range(W):
        if S[i][j] == "#":
            check.append((i, j))

while check:
    x, y = check.pop()
    for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
        if 0 <= x+dx < H and 0 <= y+dy < W:
            S[x+dx][y+dy] = "@"

ans = 0
for i in range(H):
    for j in range(W):
        res = set()
        if S[i][j] == ".":
            BFS = deque([(i, j)])
            while BFS:
                x, y = BFS.popleft()
                if S[x][y] != "#":
                    S[x][y] = "#"
                    res.add((x, y))
                    for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                        if 0 <= x+dx < H and 0 <= y+dy < W:
                            if S[x+dx][y+dy] == ".":
                                BFS.append((x+dx, y+dy))
                            elif S[x+dx][y+dy] == "@":
                                res.add((x+dx, y+dy))
        elif S[i][j] == "@":
            res.add((i, j))
        ans = max(ans, len(res))
print(ans)