class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # 1. Count frequencies in O(N) time
        counts = Counter(nums)
        
        # 2. Get the top K elements in O(N log k) time
        return [item[0] for item in counts.most_common(k)]