CHAR_SIZE = 26

class Trie:
    def __init__(self):
        self.isLeaf = False
        self.children = [None] * CHAR_SIZE
        self.count = 0
    
    def insert(self, key):
        curr = self
        for char in key:
            index = ord(char) - ord('a')
            if curr.children[index] is None:
                curr.children[index] = Trie()
            curr = curr.children[index]
            curr.count += 1
        curr.isLeaf = True
    
    def query(self, key):
        curr = self
        length = 0
        for i in range(len(key)):
            index = ord(key[i]) - ord('a')
            curr = curr.children[index]
            if curr.count == 1:
                break
            length += curr.count - 1
        return length

N = int(input())
S = list(map(str, input().split()))

trie = Trie()
for s in S:
    trie.insert(s)

ans = 0
for s in S:
    ans += trie.query(s)

print(ans//2)
