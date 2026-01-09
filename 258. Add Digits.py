class Solution:
    def addDigits(self, num: int) -> int:
        res = num
        while res>9:
            temp = 0
            for n in str(res):
                temp += int(n)
                print(temp)
                res = temp
        return res 

class Solution:
    def addDigits(self, num: int) -> int:
        if num ==0: return 0
        elif num%9 == 0: return 9
        else: return num % 9 