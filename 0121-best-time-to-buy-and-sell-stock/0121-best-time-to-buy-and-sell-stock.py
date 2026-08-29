class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        cheapest = prices[0]
        best = 0
        for i in range(len(prices)):
            cheapest = min(cheapest, prices[i])
            best = max(best, prices[i]-cheapest)
        return best

        