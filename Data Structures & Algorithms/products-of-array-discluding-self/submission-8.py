class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # Track total product of non-zero numbers and count of zeros
        nonzero_product = 1
        zero_count = 0
        
        for num in nums:
            if num == 0:
                zero_count += 1
            else:
                nonzero_product *= num
                
        # Case 1: More than one zero means everything becomes zero
        if zero_count > 1:
            return [0] * len(nums)
            
        # Case 2 & 3: One zero or no zeros
        output = []
        for num in nums:
            if zero_count == 1:
                # Only the zero position gets the product
                output.append(nonzero_product if num == 0 else 0)
            else:
                # No zeros, safe to use division
                output.append(nonzero_product // num)
                
        return output
