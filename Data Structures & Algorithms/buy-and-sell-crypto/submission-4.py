class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        #The index of max needs to be > than index of min
        #We can go through the list and find the min
        #When we find the max it's index should be greater than min's index
        if len(prices) == 1:
            return 0

        minimum = 101
        max_profit = 0

        for i in range(0, len(prices)):

            if prices[i] < minimum:
                minimum = prices[i]

            if prices[i] - minimum > 0:
                max_profit = max(max_profit, prices[i] - minimum)

        if max_profit > 0:
            return max_profit
        else:
            return 0
