class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dictA = self.makeDictFromString(s)
        dictB = self.makeDictFromString(t)
 
        if not(len(dictA.keys()) == len(dictB.keys())):
            return False

        for key in dictA.keys():
            if key in dictB and dictA[key] == dictB[key]:
                continue
            else:
                return False

        return True

    def makeDictFromString(self, a: str) -> dict:
         myDict = {}
         for i in range(len(a)):
            if a[i] not in myDict.keys():
                myDict[a[i]] = 1
            else:
                myDict[a[i]] += 1
         return myDict

        


        