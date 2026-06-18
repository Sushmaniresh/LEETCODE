class Solution:
    def maxArea(self, height: List[int]) -> int:
        best = 0
        n = len(height)
        for i in range(n):
            for j in range(i + 1, n):
                area = min(height[i], height[j]) * (j - i)
                best = max(best, area)
        return best

  def maxArea(height):
    left, right = 0, len(height) - 1
    best = 0

    while left < right:
        area = min(height[left], height[right]) * (right - left)
        best = max(best, area)
        if height[left] < height[right]:
            left += 1
        else:
            right -= 1
    return best

class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_area = 0
        l, r = 0, len(height)-1

        while l != r:
            area = min(height[l],height[r]) * (r - l)
            max_area = max(max_area, area)
            if height[r] > height[l]:
                l += 1
            else:
                r -= 1
