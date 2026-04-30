class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = defaultdict(int)

        for n in nums:
            freq[n] += 1

        top_k = list(sorted(freq,key=freq.get,reverse=True)[:k])

        return top_k
        