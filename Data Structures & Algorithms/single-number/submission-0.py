class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        count = {}
        for num in nums:
            count[num] = 1 + count.get(num,0)
        for key,value in count.items():
            if value == 1:
                return key
        