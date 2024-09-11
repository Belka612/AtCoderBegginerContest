N = int(input())

ans, NG = 0, N+1
while NG-ans > 1:
    mid = (ans+NG)//2
    if mid**2 <= N:
        ans = mid
    else:
        NG = mid
s = set()
for i in range(3, 60):
    cnt = 2
    while cnt**i <= N:
        n = cnt**i
        if int(n**(1/2))**2 != n:
            s.add(n)
        cnt += 1

print(ans+len(s))