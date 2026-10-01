class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:

        #For this question we will use a monotonically decreasing stack. As we go ahead we will check if the current element is greater than the element at the top of the stack, if it is then we will pop the top and calculate the difference between the top index and the current index

        result = [0] * len(temperatures)
        stack = [] #This is a pair of (temp, index) a list of tuples

        for i, t in enumerate(temperatures):
            while stack and t > stack[-1][0]:
                stackT, stackInd = stack.pop()
                result[stackInd] = i - stackInd
            stack.append((t,i))
        
        return result

        