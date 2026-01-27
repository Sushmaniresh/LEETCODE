class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        count = {}
        for x in nums:
            count[x] = count.get(x,0)+1

        for key in count:
            if count[key] == 1:
                return key