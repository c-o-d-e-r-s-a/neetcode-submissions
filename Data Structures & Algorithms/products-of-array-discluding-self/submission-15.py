class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        leftArr = [1] * len(nums)
        rightArr = [1] * len(nums)
        myArr = [1] * len(nums)

        j = len(nums) - 1
        arrLength = len(nums)

        for i in range(0, len(nums)):

            if self.left(i):
                leftArr[i] = leftArr[i-1] * nums[i]
            else:
                leftArr[i] = nums[i]

            if self.right(j,arrLength):
                rightArr[j] = rightArr[j+1] * nums[j]
            else:
                rightArr[j] = nums[j]

            j -= 1


        for i in range(0, len(nums)):

            product = 1

            if self.left(i):
                product *= leftArr[i-1]

            if self.right(i,arrLength):
                product *= rightArr[i+1]

            myArr[i] = product

        return myArr
     

    def left(self, number: int) -> bool:
        if number > 0:
            return True
    
    def right(self, number: int, length: int) -> bool:
        if number < length - 1:
            return True