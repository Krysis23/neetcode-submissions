class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # maxProfit = 0

        # for i in range(len(prices)-1):
        #     currPrice = i

        #     j = i +1
        #     while(j < len(prices)):
        #         currProfit = prices[j] - prices[i]
        #         maxProfit = max(currProfit,maxProfit)
        #         j = j + 1

        # return maxProfit

        l,r = 0, 1
        maxP = 0
        while r < len(prices):
            if prices[l] < prices[r]:
                profit = prices[r] - prices[l]
                maxP = max(maxP, profit)
            else:
                l = r
            r += 1
        return maxP

        