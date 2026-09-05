class Solution:
    def maxArea(self, height: List[int]) -> int:
        best = 0
        l,r = 0,len(height)-1
        while l<r:
            area = min(height[r],height[l])*(r-l)
            best = max(best,area)
            if height[l]<height[r]:
                l+=1
            else:
                r-=1
        return best
        