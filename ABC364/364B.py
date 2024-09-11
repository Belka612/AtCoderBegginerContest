H, W = map(int, input().split())
Si, Sj = map(int, input().split()); Si, Sj = Si-1, Sj-1
C = [list(input()) for _ in range(H)]
X = input()

for x in X:
    if x == 'L':
        di, dj = 0, -1
    elif x == 'R':
        di, dj = 0, 1
    elif x == 'U':
        di, dj = -1, 0
    else:
        di, dj = 1, 0
    if 0 <= Si+di < H and 0 <= Sj+dj < W:
        if C[Si+di][Sj+dj] != '#':
            Si, Sj = Si+di, Sj+dj

print(Si+1, Sj+1)