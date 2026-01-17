class Solution:
    def differenceOfSum(self, nums: List[int]) -> int:
        elementsum = 0
        digitsum = 0
        for i in nums:
            elementsum+=i
        for i in nums:
            while i>0:
                digitsum+=(i%10)
                i=i//10
        return abs(elementsum - digitsum)

