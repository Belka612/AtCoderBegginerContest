S, T = map(str, input().split())

if S == T:
    print("Yes")
    exit()
for i in range(len(S)-1):
    for j in range(1, i+1):
        ans = ""
        cnt = 0
        while cnt*i+j < len(S):
            ans += S[cnt*i+j]
            cnt += 1
        if ans == T:
            print("Yes")
            exit()
print("No")