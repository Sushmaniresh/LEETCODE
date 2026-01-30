class Solution:
    def canAliceWin(self, nums: List[int]) -> bool:
        suma, sumb = 0, 0 
        for i in nums:
            if len(str(i))==1:
                suma += i
            else: sumb += i 
        return suma > sumb or sumb > suma

class Solution:
    def canAliceWin(self, nums: List[int]) -> bool:
        diff = 0
        for num in nums:
            if num > 9:
                diff += num
            else:
                diff -= num
        
        return diff != 0