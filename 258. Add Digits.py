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

