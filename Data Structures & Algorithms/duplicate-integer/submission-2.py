class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        myDict = {}

        for i in range (len(nums)):
            if nums[i] not in myDict.keys():
                myDict[nums[i]] = 1
            elif nums[i] in myDict.keys():
                return True
        return False