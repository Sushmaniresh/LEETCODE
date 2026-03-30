class Solution:
    def checkStrings(self, s: str, t: str) -> bool:
        return sorted(s[::2]) == sorted(t[::2]) and sorted(s[1::2]) == sorted(t[1::2])
