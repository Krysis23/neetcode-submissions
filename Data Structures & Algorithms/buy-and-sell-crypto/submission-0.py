class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit = 0

        for i in range(len(prices)-1):
            currPrice = i

            j = i +1
            while(j < len(prices)):
                currProfit = prices[j] - prices[i]
                maxProfit = max(currProfit,maxProfit)
                j = j + 1

        return maxProfit

        