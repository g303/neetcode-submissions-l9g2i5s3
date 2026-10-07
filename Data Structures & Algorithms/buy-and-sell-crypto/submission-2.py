class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        for i in range(len(prices)):
            for j in range(i):
                profit = prices[j] - prices[i]
        return profit