N = int(input())

if N <= 10:
    print(N-1)
    exit()
    
def palindrome_num(n):
    if n == 1:
        return 10
    if n%2 == 0:
        return 9*10**(n//2 - 1)
    else:
        return 9*10**(n//2)

cnt = 1
while N > palindrome_num(cnt):
    N -= palindrome_num(cnt)
    cnt += 1
N -= 1
N += pow(10, (cnt+1)//2 - 1)

if cnt%2 == 1:
    ans = str(N)[:-1] + str(N)[::-1]
else:
    ans = str(N) + str(N)[::-1]
print(ans)