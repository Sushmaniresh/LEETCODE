class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        max_c = max(candies)
        return [True if (i+extraCandies)>=max_c else False for i in candies]
        