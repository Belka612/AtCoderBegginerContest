A, B = map(int, input().split())

if A == B:
    print(1)
elif A%2 != B%2:
    print(2)
else:
    print(3)