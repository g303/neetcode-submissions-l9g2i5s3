class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        for i in range(len(prices)):
            for j in range(i):
                if prices[i] - prices[j] > profit:
                    profit = prices[i] - prices[j]
        return profit