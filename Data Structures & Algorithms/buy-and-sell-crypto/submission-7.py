class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        i = 0
        j = i+1

        while j<len(prices):
            
            if prices[i] > prices[j]:
                i = j
                j = i+1
            else:
                curr_profit = prices[j] - prices[i]
                max_profit = max(max_profit,curr_profit)
                j+=1
            
        if max_profit > 0:
            return max_profit
        else:
            return 0

            
           