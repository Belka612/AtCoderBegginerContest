H = int(input())
h = 0
ans = 0
while h <= H:
    h += 2**ans
    ans += 1
print(ans)