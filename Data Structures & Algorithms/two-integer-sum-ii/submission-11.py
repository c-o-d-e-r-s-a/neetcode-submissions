class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        #Using dictionary

        myDict = {}

        for i in range(0, len(numbers)):

            if target - numbers[i] in myDict:
                return[myDict[target - numbers[i]], i+1]

            if numbers[i] not in myDict:
                myDict[numbers[i]] = i + 1
            
        return []

        

        
        

        

        