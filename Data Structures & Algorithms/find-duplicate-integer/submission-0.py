class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        countMap = {}

        for n in nums:
            if n in countMap:
                return n
            countMap[n] = 1
        return -1
        