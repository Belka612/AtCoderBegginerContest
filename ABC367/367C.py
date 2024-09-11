N, K = map(int, input().split())
R = list(map(int, input().split()))

ans = []
s = []
def DFS(depth):
    if depth == N:
        if sum(s)%K == 0:
            ans.append(s.copy())
    else:
        for i in range(1, R[depth]+1):
            s.append(i)
            DFS(depth+1)
            s.pop()
DFS(0)
ans.sort()
for v in ans:
    print(*v)
