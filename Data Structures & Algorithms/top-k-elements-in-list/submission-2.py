class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = Counter(nums)
        counts = sorted(counts.items(), key=lambda x: x[1], reverse=True)
        return [i for i, _ in counts][:k]