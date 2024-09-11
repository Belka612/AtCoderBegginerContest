from sortedcontainers import SortedList

H, W, Q = map(int, input().split())

row = [SortedList([i for i in range(W)]) for _ in range(H)]
col = [SortedList([i for i in range(H)]) for _ in range(W)]
isWall = [[True for _ in range(W)] for _ in range(H)]
ans = H * W

for _ in range(Q):
    R, C = map(int, input().split())
    R -= 1; C -= 1
    lr_key = row[R].bisect_left(C)
    ud_key = col[C].bisect_left(R)
    if isWall[R][C]:
        isWall[R][C] = False
        row[R].pop(lr_key)
        col[C].pop(ud_key)
        ans -= 1
    else:
        cand = []
        if lr_key != 0:
            left = row[R][lr_key-1]
            if C > left:
                cand.append((R, left))
        if lr_key != len(row[R]):
            right = row[R][lr_key]
            if C < right:
                cand.append((R, right))
        if ud_key != 0:
            up = col[C][ud_key-1]
            if R > up:
                cand.append((up, C))
        if ud_key != len(col[C]):
            down = col[C][ud_key]
            if R < down:
                cand.append((down, C))
        for r, c in cand:
            ans -= 1
            isWall[r][c] = False
            row[r].discard(c)
            col[c].discard(r)

print(ans)