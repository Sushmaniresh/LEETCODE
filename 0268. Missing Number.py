class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        expected = n * (n + 1) // 2
        actual = sum(nums)
        
        return expected - actual

def missingNumber(nums):
    for i in range(len(nums) + 1):
        if i not in nums:
            return i
