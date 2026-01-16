class Solution:
    def firstUniqChar(self, s: str) -> int:
        if len(s)==1: return 0
        for n in range(len(s)):
            print(s[n])
            print(s.count(s[n]))
            if s.count(s[n])==1:
                return n
        return -1

class Solution:
    def firstUniqChar(self, s: str) -> int:
        counter = Counter(s)
        for i, letter in enumerate(s):
            if counter[letter] == 1:
                return i 
        return -1