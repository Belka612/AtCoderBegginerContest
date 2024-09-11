from itertools import permutations
N, K = map(int, input().split())
S = input()

ans = 0
P = ["".join(p) for p in permutations(S)]
P.sort()
def is_palindrome(s):
    for i in range(len(s) // 2):
        if s[i] != s[-i - 1]:
            return False
    return True

for i in range(len(P)):
    if i > 0 and P[i] == P[i-1]:
        continue
    flag = True
    for j in range(N-K+1):
        if is_palindrome(P[i][j:j+K]):
            flag = False
            break
    ans += flag
print(ans)