xa, ya = map(int, input().split())
xb, yb = map(int, input().split())
xc, yc = map(int, input().split())

edges = [(xa-xb)**2 + (ya-yb)**2, (xb-xc)**2 + (yb-yc)**2, (xc-xa)**2 + (yc-ya)**2]
edges.sort()
if edges[0]+edges[1] == edges[2]:
    print("Yes")
else:
    print("No")