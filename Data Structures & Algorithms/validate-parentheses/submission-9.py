class Solution:
    def isValid(self, s: str) -> bool:

        #To check if a opening bracket is also closing we will use a stack
        #We can keep adding to the stack and then as soon as we get a closing element like ] or ) we can check if the top most element is our stack is matching if it is we will pop the top element of the stack or else we will just return False

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

        return not stack

            