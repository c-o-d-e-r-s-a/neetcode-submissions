class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
   
        #O(n) solution we only start a sequence if there is no element that is less than 1 in the dictionary
       
        myDict = {}
        seq = 1
        temp = 0


        for num in nums:
            if num in myDict:
                myDict[num] += 1
            else:
                myDict[num] = 1

        myArr = list(myDict.keys())

        i = 0

        while i < len(myArr):
            if myArr[i] - 1 not in myDict:
                count = myArr[i]
                while count + 1 in myDict:
                    seq += 1
                    count += 1
                if(seq > temp):
                    temp = seq
            i += 1
            seq = 1
            

        return temp

                
            
        