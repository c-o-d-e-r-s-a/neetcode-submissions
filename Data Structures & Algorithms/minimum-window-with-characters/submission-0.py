class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not s or not t:
            return ""

        dict1 = {}
        have = 0
        need = 0

        # Build frequency map for t
        for letter in t:
            if letter in dict1:
                dict1[letter] += 1
            else:
                dict1[letter] = 1
                need += 1

        left = 0
        dict2 = {}
        min_len = float("inf")
        myString = ""

        for right in range(len(s)):
            char = s[right]
            dict2[char] = dict2.get(char, 0) + 1

            # Check if this char satisfies a requirement in dict1
            if char in dict1 and dict2[char] == dict1[char]:
                have += 1

            # Shrink window while valid
            while have == need:
                # Update minimum length string
                if (right - left + 1) < min_len:
                    min_len = right - left + 1
                    myString = s[left : right + 1]

                # Pop left character out of the window
                left_char = s[left]
                dict2[left_char] -= 1

                # Check if removing left_char invalidates our window
                if left_char in dict1 and dict2[left_char] < dict1[left_char]:
                    have -= 1

                left += 1  # Move left pointer forward

        return myString