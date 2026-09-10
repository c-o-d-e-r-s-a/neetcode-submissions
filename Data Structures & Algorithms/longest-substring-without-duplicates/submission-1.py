class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        #We are given a String
        #We need to find the longest sequence of continuous characters that are not repeating
        #We can use 2 pointers, 1 at i = 0 and one at r = 0
        #The left pointer stays in its original place and the right pointer moves
        #The moment it encounters a duplicate, we need to update the l pointer, the r pointer can keep going
        #To update the l pointer we will use a dictionary to store the characters and its previous indices, if the previous index + 1 > current l then we will move l to that point
        #We can keep r moving, it does not need to change
        #We will repeat this process till the end
        #Use a max variable to keep the highest sequence so far

        l,r = 0,0
        length = 0
        myDict = {}

        while r < len(s):

            if s[r] in myDict:
                l = max(l,myDict[s[r]] + 1)
                myDict[s[r]] = r
            else:
                myDict[s[r]] = r

            length = max(length, (r+1) - l)

            r += 1

        return length
            

            
        

        