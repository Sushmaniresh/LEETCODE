def maxProfit(prices):
    best = 0
    for i in range(len(prices)):
        for j in range(i + 1, len(prices)):
            best = max(best, prices[j] - prices[i])
    return best

def maxProfit(prices):
    min_price = prices[0]
    best = 0

    for price in prices:
        min_price = min(min_price, price)
        best = max(best, price - min_price)

    return best
