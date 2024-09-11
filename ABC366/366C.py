from collections import defaultdict
Q = int(input())
ans = 0
dic = defaultdict(int)
for _ in range(Q):
    query = list(map(int, input().split()))
    if query[0] == 1:
        x = query[1]
        if dic[x] == 0:
            ans += 1
        dic[x] += 1
    elif query[0] == 2:
        x = query[1]
        dic[x] -= 1
        if dic[x] == 0:
            ans -= 1
    else:
        print(ans)