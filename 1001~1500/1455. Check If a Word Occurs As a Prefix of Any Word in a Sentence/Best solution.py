class Solution:
    def isPrefixOfWord(self, s: str, searchWord: str) -> int:
        a = s.split()
        for i in range(len(a)):
            if a[i].startswith(searchWord):
                return i+1
        return -1

Not write
