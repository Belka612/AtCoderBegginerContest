from sortedcontainers import SortedList
N = int(input())
T = 0
users = SortedList()
for _ in range(N):
    S, C = map(str, input().split())
    users.add(S)
    T += int(C)
print(users[T%N])