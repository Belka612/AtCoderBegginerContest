Sx, Sy = map(int, input().split()); Sx -= (Sx%2 != Sy%2)
Tx, Ty = map(int, input().split()); Tx -= (Tx%2 != Ty%2)
Sx = abs(Sx-Tx); Sy = abs(Sy-Ty)
print(Sy + max(0, Sx - Sy)//2)