import operator

class Solution:

    def evalRPN(self, tokens: List[str]) -> int:

        #We will use a stack for this question, we will only need to elements ever in the stack, as we go forward we just need to add elements to the stack until we get an operator, as soon as we get an operator we will perform the calculation between the 2 digits that is stack[0] and stack[-1] and then replace stack[0] with that number and stack[-1] with whatever number will come next, we will do this until we reach the end of the string. 

        #We will need to convert every string that is a number to a digit and perform a string equivalency test for the operators

        stack = []
        result = 0

        #Using a dictionary with operators
        myDict = {
            "+": operator.add,
            "-": operator.sub,
            "*": operator.mul,
            "/": operator.truediv,
        }

        for token in tokens:

            #We cannot use .isdigit() because it does not accoutn for negative numbers
            if token not in myDict:
                stack.append(int(token))
            
            else:
                b = stack.pop()
                a = stack.pop()

                #Syntax to use the value from the dictionary
                result = myDict[token](a,b)

                #Preventing our result to go into decimal we need to convert it to an integer because if it remains a floating point number our rest of the calculations in the future will also be floating point
                if token == "/":
                    result = int(result)

                stack.append(result)

        #Returning the first element because only that will be left at the end of the complete program (look at the line stack.append(result)) which will be our result
        return stack[0]

        