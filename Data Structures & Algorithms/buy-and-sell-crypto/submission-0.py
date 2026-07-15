class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        i = 0
        j = i+1

        while i <= len(prices)-2:         
            if prices[j] > prices[i]:
                profit = prices[j] - prices[i]
                max_profit = max(max_profit,profit)

            if j == len(prices)-1:
                i+=1
                j = i+1
            else:
                j+=1        

        if max_profit > 0:
            return max_profit
        else:
            return 0