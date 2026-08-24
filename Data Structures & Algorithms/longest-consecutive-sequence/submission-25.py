class Solution:

    def longestConsecutive(self, nums: List[int]) -> int:

        #Keep going through the list until you find an element which is not one extra from the previous one
        #If no such element occurs we'll return the max count
        #If an element like that occurs we will save the count which we had and then start all over again
        if len(nums) == 0:
            return 0

        myList = sorted(nums)
        myList = list(dict.fromkeys(myList))
        count = 1
        temp = myList[0]
        myNum = 0
        
        for i in range(1, len(myList)):

            if myList[i] == temp + 1:
                count += 1
            
            else:
                myNum = max(count,myNum)
                count = 1

            temp = myList[i]


        if myNum > count:
            return myNum
        else:
            return count
            
            