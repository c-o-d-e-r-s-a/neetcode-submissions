class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        
        myDict = {}
            
        for i in range(len(strs)):

            if "".join(sorted(strs[i])) in myDict:
                myDict["".join(sorted(strs[i]))].append(i)
            else:
                myDict["".join(sorted(strs[i]))] = [i]

        myList = []

        for key in myDict:
            tempList = []
            for number in myDict[key]:
                tempList.append(strs[number])
            myList.append(tempList)

        return myList

            
            
        