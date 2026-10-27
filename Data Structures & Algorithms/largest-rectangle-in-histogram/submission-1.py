class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:

        #For this problem we will be using a monotonic stack
        #One will be to find the leftmost smaller elelments from each index i 
        #One will be to find the rightmost smaller elements from each index i
        #We will keep the topmost element of the stack as the smallest one (we will add indices not the actual heights) and as soon as we find a smaller element than at the top of the stack we will pop all elements from the stack and add that smaller element
        #At the end we will calculate the area of the rectangle using (rightmost - leftmost + 1) * height
        #Runtime will be O(n) and space is also O(n)

        n = len(heights)
        stack = []
        leftmost = [-1] * n

        #We are finding the leftmost element for each index i
        for i in range(n):

            while stack and heights[i] <= heights[stack[-1]]:
                stack.pop()

            if stack:
                leftmost[i] = stack[-1]

            stack.append(i)

    
        stack = []
        rightmost = [n] * n

        for i in range(n-1, -1, -1):

            while stack and heights[i] <= heights[stack[-1]]:
                stack.pop()

            if stack:
                rightmost[i] = stack[-1]
            stack.append(i)

        #Calculating the area

        maxArea = 0

        #We added one to the leftmost and rightmost because they are the boundaries not from where we will calculate the area
        for i in range(n):
            leftmost[i] += 1
            rightmost[i] -= 1
            #To find the max area we need to iterate through the whole leftmost/rightmost and calculate each area and keep the max
            maxArea = max(maxArea, (rightmost[i] - leftmost[i] + 1) * heights[i])

        return maxArea

        

        