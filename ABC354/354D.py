M = 10**9
A, B, C, D = map(lambda x:int(x)+M, input().split())

def f(x, y):
    s = [[0, 0, 0, 0, 0], [0, 2, 3, 3, 4], [0, 3, 6, 7, 8]]
    res = (x//4)*(y//2)*8
    res += (x//4)*s[y%2][4]
    res += (y//2)*s[2][x%4]
    res += s[y%2][x%4]
    return res
print(f(C, D)+f(A, B)-f(A, D)-f(C, B))
