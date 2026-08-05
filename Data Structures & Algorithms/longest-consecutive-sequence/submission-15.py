class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        temp = 1
        seq = 1
        myDict = {}

        if len(nums) == 0:
            return 0

        if len(set(nums)) <= 1:
            return 1

        for num in nums:
            if num in myDict:
                myDict[num] += 1
            else:
                myDict[num] = 1

        myArr = sorted(myDict.keys())

        for i in range(0, len(myArr) - 1):
            if myArr[i] + 1 == myArr[i+1]:
                seq += 1
                if(seq > temp):
                 temp = seq
            else:
                seq = 1

        return temp