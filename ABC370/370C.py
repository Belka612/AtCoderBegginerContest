S = list(input())
T = list(input())

ans = []

while S != T:
    next_step = []
    
    for i in range(len(S)):
        if S[i] != T[i]:
            next_S = S.copy()
            next_S[i] = T[i] 
            next_step.append("".join(next_S))
    next_step.sort()
    S = list(next_step[0])
    ans.append(next_step[0])

print(len(ans))
for step in ans:
    print(step)
