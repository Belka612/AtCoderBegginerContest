N = int(input())
body, head = 0, 0
for _ in range(N):
    A, B = map(int, input().split())
    body += A
    head = max(head, B-A)
print(body + head)