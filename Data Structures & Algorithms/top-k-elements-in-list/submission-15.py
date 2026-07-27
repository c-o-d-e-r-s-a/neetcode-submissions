class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        #key:index, value: frequency
        myDict = {}
        for num in nums:
            if num in myDict:
                myDict[num] += 1
            else:
                myDict[num] = 1
        
        # Create buckets where the index is the frequency
        # Example: bucket[3] will hold a list of all numbers that appeared exactly 3 times
        buckets = [[] for _ in range(len(nums) + 1)]
        for num, freq in myDict.items():
            buckets[freq].append(num)
            
        # Iterate backwards from the highest frequency bucket to collect top K elements
        result = []
        for i in range(len(buckets) - 1, 0, -1):
            for num in buckets[i]:
                result.append(num)
                if len(result) == k:
                    return result