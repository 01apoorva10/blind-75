from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        left , right = 0 ,1
        maxProfit = 0

        while right < len(prices):
            # for profitability
            print(f"Left: {left}, Right: {right}")
            if prices[left] <  prices[right]:
                profit = prices[right] - prices[left]
                print(f"Prices[left]: {prices[left]}, Prices[right]: {prices[right]}, Profit: {profit}")
                maxProfit = max(maxProfit , profit)
            else:
                left = right
                print(f"Resetting left to {left}")
            right +=1
            print(f"Updated right: {right}\n")
        return maxProfit

solution = Solution()
prices = [7, 1, 5, 3, 6, 4]
print("Maximum Profit:", solution.maxProfit(prices))
