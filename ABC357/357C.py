N = int(input())

def DFS(N):
    if N == 0:
        return [['#']]
    pattern = DFS(N-1)
    size = 3**(N-1)
    res = [['.' for _ in range(3*size)] for _ in range(3*size)]
    for i, j in [(0, 0), (0, size), (0, 2*size), (size, 0), (size, 2*size), (2*size, 0), (2*size, size), (2*size, 2*size)]:
        for di in range(size):
            for dj in range(size):
                res[i+di][j+dj] = pattern[di][dj]
    return res
ans = DFS(N)
for i in range(3**N):
    print(*ans[i], sep='')