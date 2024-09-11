N = int(input())
A = [[list(map(int, input().split())) for _ in range(N)] for _ in range(N)]

S = [[[0 for _ in range(N+1)] for _ in range(N+1)] for _ in range(N+1)]

for x in range(1, N + 1):
    for y in range(1, N + 1):
        for z in range(1, N + 1):
            S[x][y][z] = A[x-1][y-1][z-1] \
                        + S[x-1][y][z] + S[x][y-1][z] + S[x][y][z-1] \
                        - S[x-1][y-1][z] - S[x-1][y][z-1] - S[x][y-1][z-1] \
                        + S[x-1][y-1][z-1]

def ans(S, Lx, Rx, Ly, Ry, Lz, Rz):
    res = S[Rx][Ry][Rz] \
            - S[Lx-1][Ry][Rz] - S[Rx][Ly-1][Rz] - S[Rx][Ry][Lz-1] \
            + S[Lx-1][Ly-1][Rz] + S[Lx-1][Ry][Lz-1] + S[Rx][Ly-1][Lz-1] \
            - S[Lx-1][Ly-1][Lz-1]
    return res

Q = int(input())
for _ in range(Q):
    Lx, Rx, Ly, Ry, Lz, Rz = map(int, input().split())
    print(ans(S, Lx, Rx, Ly, Ry, Lz, Rz))
