class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        size = len(nums)
        freq = {}
        res = []

        for n in nums:
            freq[n] = freq.get(n,0) + 1

        for n in freq.keys():
            if freq[n] > size/3:
                res.append(n)
        return res   