class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        #profit = 0
        #for i in range(len(prices)):
        #    for j in range(i):
        #        if prices[i] - prices[j] > profit:
        #            profit = prices[i] - prices[j] 
        #return profit
        min_price = prices[1]
        max_profit = 0

        for price in prices:
            min_price = min(min_price, price)

            profit = price - min_price
            max_profit = max(max_profit, profit)

        return max_profit


