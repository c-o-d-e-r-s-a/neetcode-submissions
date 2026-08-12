class Solution:

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        myList = []
        myDict = {}

        for i in range(len(strs)):

            myString = "".join(sorted(strs[i]))

            if myString in myDict:
                myDict[myString].add(i)
            else:
                myDict[myString] = {i}

        for key in myDict:
            #We are trying to get the elements from the original list strs
            anagram = []
            for value in myDict[key]:
                anagram.append(strs[value])
            myList.append(anagram)

        return myList
            
