N, X, Y = map(int, input().split())
A = list(map(int, input().split())); A.sort()
B = list(map(int, input().split())); B.sort()

sweet, salty = 0, 0
for i in range(N):
    sweet += A.pop()
    salty += B.pop()
    if sweet > X or salty > Y:
        print(i+1)
        exit()
print(N)