class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
       
       #We are using the prefix suffix method

       #We will create 2 lists prefix and suffix
       #For the prefix we will traverse from left to right and store all the values on the left (Except for the current index). Default value for the first index will be 1
       #For the suffix we will traverse from right to left and store all the values on the right (Except for the current index). Default value for the last index will be 1

       prefix = []
       suffix = [1] * len(nums)

       for i in range (0, len(nums)):
        if(i==0):
            prefix.append(1)
        else:
            prefix.append(nums[i-1] * prefix[i-1])

       for i in range(len(nums) - 1, -1, -1):
            if i == len(nums) - 1:
                suffix[i] = 1
            else:
                suffix[i] = nums[i+1] * suffix[i+1]

       output = []
       for i in range(0, len(nums)):
            output.append(prefix[i] * suffix[i])

       return output

        