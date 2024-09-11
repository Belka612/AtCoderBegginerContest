S = set([1, 2, 3])
S -= set(map(int, input().split()))
if len(S) == 1:
    print(*S)
else:
    print(-1)
