class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maxAmount = 0
        l = 0 
        r = len(heights) -1

        while(l<r):
            newWater = (r-l) * min(heights[l],heights[r])

            maxAmount = max(maxAmount,newWater)

            if heights[l] < heights[r]:
                l = l + 1
            else:
                r = r-1
        return maxAmount

        