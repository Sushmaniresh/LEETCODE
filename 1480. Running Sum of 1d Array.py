class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        for i in range(1,len(nums)):
            nums[i]=nums[i]+nums[i-1]
        return nums

class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        
        # Starting Point 
        s = 0 
        running_sum = []

        for num in nums: 

            # Add a New Element Linearly 
            s += num 
            
            # Add Element to Stack 
            running_sum.append(s)

        # Return Running Summ 
        return running_sum