class Solution:
    def maxArea(self, heights: List[int]) -> int:

        #Start with 2 pointers one at the left and one at the right
        #Lets choose the first and the last bar to form a container
        #Index 0 and Index n-1. 
        #Width = n-1, height = min(heights[0],heights[n-1])

        i,j,area = 0, len(heights)-1, 0
        area = (j - i) * min(heights[i], heights[j])

        while i < j:

            temp = heights[i]
            
            if heights[i] < heights[j]:
                while not heights[i] > temp and i < j:
                    i += 1

                area = max(area,(j - i) * min(heights[i], heights[j]))

            elif heights[j] < heights[i]:

                temp = heights[j]
                
                while not heights[j] > temp and j > i:
                    j -= 1
                
                area = max(area,(j - i) * min(heights[i], heights[j]))

            else:
                i += 1

        return area

            