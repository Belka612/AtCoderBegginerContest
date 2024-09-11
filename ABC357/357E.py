from atcoder.scc import SCCGraph
from collections import defaultdict
N = int(input())
a = list(map(int, input().split()))
scc = SCCGraph(N)
dic = defaultdict(lambda: -1)

for i in range(N):
    a[i] -= 1
    scc.add_edge(i, a[i])

def DFS(u, v, cnt):
    if u == v:
        return cnt
    elif dic[v] != -1:
        return cnt + dic[v]
    else:
        return DFS(u, a[v], cnt+1)

ans = 0
for l in reversed(scc.scc()):
    u = l[-1]
    dic[u] = DFS(u, a[u], 1)
    ans += dic[u]
    for i in range(len(l)-1):
        v = l[i]
        dic[v] = dic[u]
        ans += dic[v]
print(ans)