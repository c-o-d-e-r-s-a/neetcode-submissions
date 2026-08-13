class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        myList = [[] for i in range (len(nums) + 1)]

        myDict = {}
        myArr = []

        for num in nums:
            if num in myDict:
                myDict[num] += 1
            else:
                myDict[num] = 1

        for (key,value) in myDict.items():
            myList[value].append(key)

        for i in range(len(myList) - 1, -1, -1):
            for num in myList[i]:
                myArr.append(num)
                k -= 1
                if k==0:
                    return myArr

                    