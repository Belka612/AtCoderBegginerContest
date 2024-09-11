R, G, B = map(int, input().split())
C = input()
if C == "Red":
    print(min(G, B))
elif C == "Green":
    print(min(B, R))
else:
    print(min(R, G))