from collections import deque
S = deque(input())
T = deque(input())

cnt = 1
while S and T:
    while S[0] != T[0]:
        T.popleft()
        cnt += 1
    print(cnt)
    S.popleft()
    T.popleft()
    cnt += 1