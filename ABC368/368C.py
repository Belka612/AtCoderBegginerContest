N = int(input())
H = list(map(int, input().split()))

ans = 0

for i in range(N):
    ans += (H[i] // 5) * 3
    H[i] %= 5
    while H[i] > 0:
        if ans%3 == 2:
            H[i] -= 3
        else:
            H[i] -= 1
        ans += 1

print(ans)