S = input()
R, M = 0, 0
for i in range(3):
    if S[i] == "R":
        R = i
    elif S[i] == "M":
        M = i
print("Yes" if R < M else "No")