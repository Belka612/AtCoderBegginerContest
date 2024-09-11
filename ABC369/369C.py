from math import comb
N = int(input())
A = list(map(int, input().split()))
B = [None]*(N-1)

for i in range(N-1):
    B[i] = A[i+1] - A[i]

def run_length_encoding(arr):
    if not arr:
        return []
    
    encoded = []
    current_element = arr[0]
    count = 1
    
    for i in range(1, len(arr)):
        if arr[i] == current_element:
            count += 1
        else:
            encoded.append((current_element, count))
            current_element = arr[i]
            count = 1
    
    # 最後の要素を追加
    encoded.append((current_element, count))
    
    return encoded


ans = N + N-1

for num, cnt in run_length_encoding(B):
    if cnt >= 2:
        ans += comb(cnt, 2)
print(ans)
