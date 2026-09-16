class Solution:
    def canAliceWin(self, nums: List[int]) -> bool:
        single = sum(i for i in nums if i<10)
        double = sum(i for i in nums if i>9)
        return single != double
        