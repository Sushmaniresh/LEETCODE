class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        ans = ""

        while columnNumber > 0:
            columnNumber -= 1
            rem = columnNumber % 26
            ch = chr(ord('A') + rem)
            ans = ch + ans
            columnNumber //= 26

        return ans
