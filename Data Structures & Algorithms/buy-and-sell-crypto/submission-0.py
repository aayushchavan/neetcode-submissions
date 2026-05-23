class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        hold = -prices[0]
        sell = 0
        
        for i in range(1, len(prices)):
            hold_old = hold  # Save the old value
            hold = max(hold, -prices[i])
            sell = max(sell, hold_old + prices[i])  # Use the old hold
        
        return sell