class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
       
       #This one this the optimal solution, before we stored the prefix and suffix in a different list but this time will store it in the output list itself. We will make 2 passes, the first one will get the prefixes in the ouput list and the second one we will multiply the suffixes with the prefixes

        res = [1] * (len(nums))

        prefix = 1
        for i in range(len(nums)):
            res[i] = prefix
            prefix *= nums[i]
        postfix = 1
        for i in range(len(nums) - 1, -1, -1):
            res[i] *= postfix
            postfix *= nums[i]
        return res