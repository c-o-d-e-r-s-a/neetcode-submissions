class Solution:

  def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
    myList = []
    myDict = {}
    
    for i in range(len(strs)):
        # Create a count array of 26 zeros for letters 'a' through 'z'
        count = [0] * 26
        for char in strs[i]:
            count[ord(char) - ord('a')] += 1
            
        # Convert list to a tuple so it can be used as a dictionary key
        myKey = tuple(count)
        
        # Store the actual string directly instead of its index
        if myKey in myDict:
            myDict[myKey].append(strs[i])
        else:
            myDict[myKey] = [strs[i]]
            
    # Directly extract the grouped anagram lists from the dictionary values
    for key in myDict:
        myList.append(myDict[key])
        
    return myList