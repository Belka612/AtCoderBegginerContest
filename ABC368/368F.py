def factorization(n):
    arr = []
    temp = n
    for i in range(2, int(-(-n**0.5//1))+1):
        if temp%i==0:
            cnt=0
            while temp%i==0:
                cnt+=1
                temp //= i
            arr.append([i, cnt])

    if temp!=1:
        arr.append([temp, 1])

    if arr==[]:
        arr.append([n, 1])

    return arr

N = int(input())
A = list(map(int, input().split()))

ans = 0
for a in A:
    grundy = 0
    for p, cnt in factorization(a):
        grundy += cnt
    ans ^= grundy

print('Bruno' if ans == 0 else 'Anna') 