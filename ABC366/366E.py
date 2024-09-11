N, D = map(int, input().split())
xs, ys = [None]*N, [None]*N
xm, ym = 0, 0
for i in range(N):
    x, y = map(int, input().split())
    xs[i], ys[i] = x, y
    xm += x; ym += y

xm //= N; ym //= N

for i in range()