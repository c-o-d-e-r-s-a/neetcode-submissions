class Solution:
    def isPalindrome(self, s: str) -> bool:

        temp = s.lower()
        temp = temp.replace(" ", "")
        temp = "".join(char for char in temp if char.isalnum())

        return temp == temp[::-1]
        