class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid          # target found
            elif nums[mid] < target:
                left = mid + 1      # search right half
            else:
                right = mid - 1     # search left half
        
        # target not found, left is the insert position
        return left

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        for p in range(len(nums)):
            if(nums[p]==target):
               return p
            elif(target<nums[p]):
               return p
        else:
            return len(nums) 