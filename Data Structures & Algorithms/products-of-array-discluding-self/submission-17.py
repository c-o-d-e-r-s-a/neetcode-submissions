class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        myArr = [1] * n
        
        # 1. Pass: Compute left (prefix) products
        left_product = 1
        for i in range(n):
            myArr[i] = left_product
            left_product *= nums[i]
            
        # 2. Pass: Compute right (suffix) products and multiply in-place
        right_product = 1
        for i in range(n - 1, -1, -1):
            myArr[i] *= right_product
            right_product *= nums[i]
            
        return myArr