class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        s1Dict = {}
        s2Dict = {}

        # 1. Map character frequencies for s1
        for char in s1:
            s1Dict[char] = s1Dict.get(char, 0) + 1

        l = 0
        for r in range(len(s2)):
            # 2. Expand window by adding s2[r]
            s2Dict[s2[r]] = s2Dict.get(s2[r], 0) + 1

            # 3. Shrink window if it exceeds len(s1)
            if r - l + 1 > len(s1):
                s2Dict[s2[l]] -= 1
                if s2Dict[s2[l]] == 0:
                    del s2Dict[s2[l]]  # Key cleanup for map equality
                l += 1

            # 4. Check if current window matches s1 frequency
            if s1Dict == s2Dict:
                return True

        return False