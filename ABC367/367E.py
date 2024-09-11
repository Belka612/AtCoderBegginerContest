from collections import defaultdict
from atcoder.scc import SCCGraph

# 入力を受け取る
N, K = map(int, input().split())
X = list(map(int, input().split()))
A = list(map(int, input().split()))

# SCCグラフの作成
p = [X[i] - 1 for i in range(N)]
sccG = SCCGraph(N)
for i in range(N):
    sccG.add_edge(i, X[i] - 1)

# SCCで強連結成分を求める
scc = sccG.scc()

# 各成分が巡回かどうかを判定
iscycle = defaultdict(lambda: False)
cycle_length = {}
for c in scc:
    u, v = c[0], c[0]
    for _ in range(len(c)):
        v = p[v]
    if u == v:
        for q in c:
            iscycle[q] = True
            cycle_length[q] = len(c)
    else:
        for q in c:
            iscycle[q] = False

# Aの最終状態を計算
final_A = A[:]

for c in scc:
    if iscycle[c[0]]:
        # 巡回成分の場合、K回の操作を効率化して行う
        cycle_len = cycle_length[c[0]]
        steps = K % cycle_len
        for _ in range(steps):
            new_A = final_A[:]
            for u in c:
                new_A[u] = final_A[p[u]]
            final_A = new_A
    else:
        # 非巡回成分の処理
        for u in c:
            steps = K
            while steps > 0:
                next_u = p[u]
                final_A[u] = final_A[next_u]
                u = next_u
                steps -= 1
                if iscycle[u]:
                    # 巡回に入ったら残りのステップを巡回内で処理
                    cycle_len = cycle_length[u]
                    steps = steps % cycle_len
                    break  # ここで巡回に入るので、外のループで処理を続ける

            # 巡回に入った後の処理
            if steps > 0 and iscycle[u]:
                cycle = []
                while u not in cycle:
                    cycle.append(u)
                    u = p[u]
                cycle_len = len(cycle)
                for _ in range(steps):
                    new_A = final_A[:]
                    for u in cycle:
                        new_A[u] = final_A[p[u]]
                    final_A = new_A

# 結果を出力
print(' '.join(map(str, final_A)))
