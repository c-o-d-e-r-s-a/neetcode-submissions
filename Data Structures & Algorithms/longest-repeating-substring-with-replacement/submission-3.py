class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        # #Applying the brute force solution
        # #For this solution we'll need the following variables
        # #left, right, window_size, max_freq, max_length
        
        # max_length = 0

        # for i in range(0, len(s)):

        #     myDict = {}
        #     window_length = 0
        #     max_freq = 0

        #     for j in range(i, len(s)):

        #         #Assigning values in dictionary
        #         if s[j] in myDict:
        #             myDict[s[j]] += 1
        #         else:
        #             myDict[s[j]] = 1
                
        #         #Assigning max frequency of one letter
        #         max_freq = max(max_freq , myDict[s[j]])

        #         #Increasing window length 
        #         window_length += 1

        #         #Checking if the number of letters replaced is valid
        #         if window_length - max_freq <= k:
        #             max_length = max(max_length, window_length)

        # return max_length

        #Time: O(n^2), Space: O(1) = only 26 letters possible



        #Applying the optimal solution O(n)
        #Instead of using 2 for loops and going through each possible combination, we can use 2 pointers one starting at the left and one starting at the right. 

        max_freq = 0
        l = 0
        myDict = {}
        max_length = 0

        # Let r expand forward on every iteration
        for r in range(len(s)):
            # 1. Add current right character
            myDict[s[r]] = myDict.get(s[r], 0) + 1
            max_freq = max(max_freq, myDict[s[r]])

            # 2. If invalid, shrink from left UNTIL valid
            while (r - l + 1) - max_freq > k:
                myDict[s[l]] -= 1  # Decrement LEFT character
                l += 1             # Move left pointer

            # 3. Now window is guaranteed valid, update max_length
            max_length = max(max_length, r - l + 1)

        return max_length