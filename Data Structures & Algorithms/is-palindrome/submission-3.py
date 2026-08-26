class Solution:
    def isPalindrome(self, s: str) -> bool:

        #We are using two pointers to solve this problem
        #First pointer starts at the left and keeps going until it finds an alphanumeric character
        #Second pointer starts at the right and keeps going left until it finds an alphanumeric character
        #We compare the lowercase characters with each other
        #The moment those don't match we return false
        #Else we will return true

        i = 0
        j = len(s) - 1
        
        while i < j:

            while i < j and not s[i].isalnum():
                i += 1
            
            while j > i and not s[j].isalnum():
                j -= 1

            if s[i].lower() != s[j].lower():
                return False

            i += 1
            j -= 1

        return True