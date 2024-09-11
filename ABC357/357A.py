N, M = map(int, input().split())
H = list(map(int, input().split()))

for i in range(N):
    if M-H[i] < 0:
        print(i)
        quit()
    M -= H[i]
print(N)