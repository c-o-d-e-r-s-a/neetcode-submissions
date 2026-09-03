class Solution:
    def trap(self, height: List[int]) -> int:

        #This is the optimal solution: Time O(n)
        # We will use 2 pointers, one will start on the left and one will start at the extreme right
        #We will store the max value of the left in the variable left and the max value of the right in the variable right

        left = 0
        right = len(height) - 1
        left_max = 0
        right_max = 0
        boxes = 0

        while left < right:

            if height[left] >= left_max:
                left_max = height[left]
            else:
                boxes += left_max - height[left]

            if height[right] >= right_max:
                right_max = height[right]
            else:
                boxes += right_max - height[right]

            if left_max < right_max:
                left += 1
            else:
                right -= 1

        return boxes
            
            
             

        