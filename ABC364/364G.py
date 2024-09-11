def H(n, k):
    if k == 0:
        return 1
    if n == 0:
        return  1
    res = 0
    for i in range(k+1):
        res += H(n-1, i)
    return res
print(H(10, 1))