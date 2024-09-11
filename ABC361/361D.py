from collections import deque
N = int(input())
S = input() + ".."
T = input() + ".."

que = deque([(S, 0)])
visited = set()
visited.add(S)

while que:
    current, moves = que.popleft()
    if current == T:
        print(moves)
        exit()
    for i in range(N+1):
        if current[i:i+2] != '..':
            for j in range(N+1):
                if current[j:j+2] == '..':
                    nx = list(current)
                    nx[i:i+2], nx[j:j+2] = nx[j:j+2], nx[i:i+2]
                    nx = ''.join(nx)
                    if nx not in visited:
                        visited.add(nx)
                        que.append((nx, moves + 1))
print(-1)