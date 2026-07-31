class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        output = []

        for i in range(0, len(nums)):

            if i == 0:
                output.append(self.product(nums[i+1:]))
            elif i > 0 and i < len(nums) - 1:
                output.append(self.product(nums[0:i]) * self.product(nums[i+1:]))
            else:
                output.append(self.product(nums[0:i]))

        return output

    def product(self, nums: List[int]) -> int:

        multi = 1

        for num in nums:
            multi *= num

        return multi
