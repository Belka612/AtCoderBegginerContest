A, B, C = map(int, input().split())

ans = 'Yes'
while C != A:
    C += 1
    C %= 24
    if C == B:
        ans = 'No'
        break
print(ans)