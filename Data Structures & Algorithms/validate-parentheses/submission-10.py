class Solution:
    def isValid(self, s: str) -> bool:

        #To check if a opening bracket is also closing we will use a stack
        #We can keep adding to the stack and then as soon as we get a closing element like ] or ) we can check if the top most element is our stack is matching if it is we will pop the top element of the stack or else we will just return False

        #We will use a hash map with the closing brackets as a key and opening brackets as the value, as we go through the string we can check if we have a opening bracket, if yes we will add it to the stack, if not then we will check if the top element of the stack matches the value of the closing bracket in the dictionary, if yes then we will pop the top element from the stack

        stack = []
        myDict = {"]":"[" , "}":"{", ")":"("}

        if not s:
            return True

        for char in s:
            
            if char in myDict:

                if stack and stack[-1] == myDict[char]:
                    stack.pop()

                else:
                    return False
            
            else:
                stack.append(char)

        #If the stack is full, we will return false because every bracket only matches when the stack is empty because we popped all the closing brackets with the opening brackets
        
        return not stack

            