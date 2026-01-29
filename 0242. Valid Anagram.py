class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
         return Counter(s) == Counter(t)

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False
        
        for ch in set(s):
            if s.count(ch) != t.count(ch):
                return False
        return True  

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s1, s2 = {}, {}
        
        if len(s) != len(t):
            return False
        for i in s:
            s1[i] = s1.get(i,0)+1
        for j in t:
            s2[j] = s2.get(j,0)+1
        if s1 == s2:
            return True
        else: return False