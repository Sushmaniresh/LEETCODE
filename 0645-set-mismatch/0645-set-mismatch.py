class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        res = []
        seen = set()
        for n in nums:
            if n in seen:
                res.append(n)
            seen.add(n)
        for i in range(1,len(nums)+1):
            if i not in seen:
                res.append(i)
        return res

        