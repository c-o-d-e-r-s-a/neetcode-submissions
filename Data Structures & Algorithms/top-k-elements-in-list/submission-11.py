class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        #We will store unique numbers in a list of length k
        #Use a dictionary to store total counts of every number

        myDict = {}
        myList = []

        for number in nums:
            if number in myDict:
                myDict[number] += 1
            else:
                myDict[number] = 1
        
        #Keep comparing the max to the dictionary values once you get k elements return
        
        #Finding max in the dictionary values
        
        maximums = sorted(myDict.values(), reverse=True)

        if all(x == 1 for x in maximums):
            return nums

        for number in maximums:
            if not k == 0:
                for key in myDict:
                    if myDict[key] == number:
                     if key not in myList:
                        myList.append(key)
                        k -= 1
                        break
            else:
                return myList
        return myList

        
            
            

        
