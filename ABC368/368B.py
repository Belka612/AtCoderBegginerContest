N = int(input())
A = list(map(int, input().split()))

ans = 0
while True:
    A.sort(reverse=True)
    if A[1] == 0:
        break
    A[0] -= 1
    A[1] -= 1
    ans += 1

print(ans)