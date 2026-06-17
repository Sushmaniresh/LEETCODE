# Brute Force --> o(n2), o(1)

for i in range(len(nums)):
    for j in range(i + 1, len(nums)):
        if nums[i] + nums[j] == target:
            return [i, j]

# Hash Map (Dictionary) --> o(n), o(n)
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for i, x in enumerate(nums):
            need = target - x
            if need in seen:
                return seen[need], i
            seen[x] = i
