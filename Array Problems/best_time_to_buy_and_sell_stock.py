class Solution(object):
    def maxProfit(self, prices):
        min_index = 0
        max_profit = 0
        N = len(prices)
        for i in range(1, N):
            if prices[i]-prices[min_index] < 0:
                min_index = i
            else:
                current_profit = prices[i] - prices[min_index]
                if current_profit > max_profit:
                    max_profit = current_profit

        return max_profit


solution = Solution()
print(solution.maxProfit([2, 9, 5, 4, 1, 10]))
